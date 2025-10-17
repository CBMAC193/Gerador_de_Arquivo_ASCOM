"""
Gerador de Certificados de Medalhas - CBMAC
===========================================

Este módulo é responsável por gerar certificados de medalhas do CBMAC.
Utiliza templates de imagem específicos para cada tipo de medalha e
sobrepõe as informações fornecidas pelo usuário.

Tipos de medalhas suportadas:
- Medalhas simples (uma imagem por tipo)
- Medalhas de tempo de serviço (10, 20, 30 anos)

Dependências:
- reportlab: Para geração do PDF
- PIL/Pillow: Para manipulação de imagens
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .utils import find_model_image


def gerar_certificado_medalha(dados: dict) -> str:
    """
    Gera um certificado de medalha em PDF
    
    Args:
        dados (dict): Dicionário contendo os dados do formulário
            - subtipo: Tipo específico da medalha
            - subsubtipo: Sub-categoria (ex: anos de serviço)
            - nome, decreto, local, data, comandante: Dados para preenchimento
    
    Returns:
        str: Caminho para o arquivo PDF gerado
    
    Raises:
        FileNotFoundError: Se o template da medalha não for encontrado
    """
    import logging
    logger = logging.getLogger(__name__)
    
    # Extrair tipo e subtipo para localizar o template correto
    subtipo = dados.get('subtipo')
    sub_subtipo = dados.get('subsubtipo')
    
    # Log detalhado para auditoria e debugging
    logger.info(f"Debug medalha - subtipo: '{subtipo}', sub_subtipo: '{sub_subtipo}'")
    logger.info(f"Debug medalha - dados: {dados}")
    
    # Estratégia de busca hierárquica por template:
    # 1º: Buscar com subtipo + sub-subtipo (ex: Tempo de Serviço + 10 ANOS)
    # 2º: Buscar apenas com subtipo (ex: Amigo, Bombeiro Durão)
    # 3º: Buscar template genérico de medalhas
    if subtipo and sub_subtipo:
        imagem = find_model_image('Medalhas', subtipo, sub_subtipo)
        logger.info(f"Debug: Procurando com subtipo e sub_subtipo: {imagem}")
    elif subtipo:
        imagem = find_model_image('Medalhas', subtipo)
        logger.info(f"Debug: Procurando só com subtipo: {imagem}")
    else:
        imagem = find_model_image('Medalhas')
        logger.info(f"Debug: Procurando só Medalhas: {imagem}")
    
    # Validar se template foi encontrado
    if imagem is None:
        logger.error("Modelo de medalha não encontrado")
        raise FileNotFoundError('Modelo de Medalha não encontrado')

    # Carregar template e obter dimensões para o PDF
    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    # Preparar diretório de saída
    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Medalha.pdf')

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
        f'confere ao Senhor {dados.get("nome_agraciado","")}, a Medalha {dados.get("tipo_documento","")}, '
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

    c.showPage()
    c.save()

    return out_path
