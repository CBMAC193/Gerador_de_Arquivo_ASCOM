"""
Gerador de Certificados de Moedas Comemorativas CBMAC
====================================================

Responsável pela geração de certificados para moedas comemorativas
do Corpo de Bombeiros Militar do Acre.

As moedas comemorativas são emitidas em ocasiões especiais como:
- Aniversários da corporação
- Eventos históricos importantes
- Homenagens especiais
- Datas comemorativas institucionais

O certificado acompanha a moeda física e atesta sua autenticidade
e significado histórico-institucional.
"""

import os
import logging
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .utils import find_model_image

# Logger específico para rastreamento de operações
logger = logging.getLogger('app')


def gerar_certificado_moeda(dados: dict) -> str:
    """
    Gera certificado para moeda comemorativa CBMAC em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - nome_moeda: Nome do contemplado com a moeda
            - decreto_moeda: Decreto que autoriza a emissão
            - local_moeda: Local de expedição
            - data_moeda: Data de expedição/entrega
            - comandante_moeda: Nome do comandante geral
    
    Returns:
        str: Caminho absoluto para o arquivo PDF gerado
        
    Raises:
        FileNotFoundError: Se o template da moeda não for encontrado
    """
    # Localizar template específico da moeda CBMAC
    imagem = find_model_image('Moeda CBMAC')
    if imagem is None:
        logger.error('find_model_image não encontrou modelo para Moeda CBMAC (procurado em app/static/Certificado/Moeda CBMAC)')
        raise FileNotFoundError('Modelo de Moeda CBMAC não encontrado')
    else:
        logger.info(f'Moeda: usando imagem de modelo em: {imagem}')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'MoedaCBMAC.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)

    # =================================================================
    # CONFIGURAÇÕES PERSONALIZÁVEIS DE TEXTO
    # =================================================================
    
    # 1. CONFIGURAÇÕES DE FONTE E COR
    fonte_titulo = 'Helvetica-Bold'
    tamanho_titulo = 30
    fonte_corpo = 'Helvetica'
    tamanho_corpo = 30
    fonte_assinatura = 'Helvetica'
    tamanho_assinatura = 30
    
    # Cores (valores RGB de 0 a 1)
    from reportlab.lib.colors import Color, black
    cor_titulo = Color(0.8, 0, 0, 1)    # Vermelho institucional
    cor_corpo = black                    # Preto
    cor_assinatura = Color(0.3, 0.3, 0.3, 1)  # Cinza escuro
    
    # 2. CONFIGURAÇÕES DE POSICIONAMENTO
    margem_esquerda = int(iw * 0.25)     # 25% da largura como margem esquerda
    margem_direita = int(iw * 0.08)      # 8% da largura como margem direita
    largura_texto = iw - margem_esquerda - margem_direita  # Largura útil para texto
    
    # Posições Y (de cima para baixo)
    y_titulo = int(ih * 0.75)            # 75% da altura - posição do título
    y_corpo = int(ih * 0.60)             # 60% da altura - corpo principal
    y_local_data = int(ih * 0.30)        # 30% da altura - local e data  
    y_comandante = int(ih * 0.25)        # 25% da altura - nome do comandante
    y_cargo = int(ih * 0.22)             # 22% da altura - cargo do comandante
    
    # 3. CONFIGURAÇÃO DE ESPAÇAMENTO ENTRE LINHAS
    espacamento_linha = 25               # Espaçamento entre linhas de texto
    
    # 4. FUNÇÃO PARA QUEBRA DE TEXTO
    def quebrar_texto(canvas, texto, x, y, largura_max, altura_linha=espacamento_linha):
        """Quebra texto em múltiplas linhas se necessário"""
        palavras = texto.split()
        linha_atual = ""
        y_atual = y
        
        for palavra in palavras:
            linha_teste = linha_atual + " " + palavra if linha_atual else palavra
            largura_linha = canvas.stringWidth(linha_teste, canvas._fontname, canvas._fontsize)
            
            if largura_linha <= largura_max:
                linha_atual = linha_teste
            else:
                if linha_atual:
                    canvas.drawString(x, y_atual, linha_atual)
                    y_atual -= altura_linha
                linha_atual = palavra
        
        if linha_atual:
            canvas.drawString(x, y_atual, linha_atual)
        return y_atual
    
    # 5. CORPO PRINCIPAL DO TEXTO
    c.setFont(fonte_corpo, tamanho_corpo)
    c.setFillColor(cor_corpo)
    
    texto_principal = (
        f'O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
        f'usando das atribuições que lhe compete por meio do Decreto N° {dados.get("decreto","")}, '
        f'confere ao Senhor {dados.get("nome_agraciado","")}, a Moeda CBMAC, '
        f'do Corpo de Bombeiros Militar do Estado do Acre, pelos relevantes serviços '
        f'prestados ao Estado do Acre e ao Corpo de Bombeiros Militar.'
    )
    
    # Desenhar texto com quebra automática
    y_final = quebrar_texto(c, texto_principal, margem_esquerda, y_corpo, largura_texto)
    
    # 6. LOCAL E DATA
    c.setFont(fonte_assinatura, tamanho_assinatura - 2)
    c.setFillColor(cor_assinatura)
    
    local_data = f'{dados.get("local","Rio Branco")} - Acre, {dados.get("data","")}'
    # Posicionar à direita
    largura_local_data = c.stringWidth(local_data, fonte_assinatura, tamanho_assinatura - 2)
    x_local_data = iw - margem_direita - largura_local_data
    c.drawString(x_local_data, y_local_data, local_data)
    
    # 7. ASSINATURA DO COMANDANTE
    c.setFont(fonte_assinatura, tamanho_assinatura)
    
    comandante = dados.get('comandante', '')
    largura_comandante = c.stringWidth(comandante, fonte_assinatura, tamanho_assinatura)
    x_comandante = iw - margem_direita - largura_comandante
    c.drawString(x_comandante, y_comandante, comandante)
    
    # Linha de assinatura (opcional)
    linha_inicio = x_comandante - 20
    linha_fim = x_comandante + largura_comandante + 20
    c.line(linha_inicio, y_comandante - 3, linha_fim, y_comandante - 3)
    
    # 8. CARGO DO COMANDANTE
    c.setFont(fonte_assinatura, tamanho_assinatura - 2)
    cargo = "Comandante Geral do CBMAC"
    largura_cargo = c.stringWidth(cargo, fonte_assinatura, tamanho_assinatura - 2)
    x_cargo = iw - margem_direita - largura_cargo
    c.drawString(x_cargo, y_cargo, cargo)

    try:
        c.showPage()
        c.save()
        logger.info(f'Moeda gerada: {out_path}')
        return out_path
    except Exception:
        logger.exception('Erro ao salvar PDF da Moeda')
        raise
