"""
Gerador de Diplomas CBMAC
=========================

Responsável pela geração de diplomas oficiais do Corpo de Bombeiros
Militar do Acre, incluindo diferentes tipos de condecorações.

Tipos de diplomas suportados:
- Bravura Bombeiro Militar
- Ordem do Mérito Dom Pedro II (Cavaleiro, Comendador, Grã-Oficial)

O sistema localiza automaticamente o template correto baseado no subtipo
selecionado e sobrepõe as informações fornecidas pelo usuário.
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .utils import find_model_image


def gerar_certificado_diploma(dados: dict) -> str:
    """
    Gera um diploma oficial em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - subtipo: Tipo específico do diploma 
            - nome: Nome do agraciado
            - decreto: Número do decreto
            - local: Local de expedição
            - data: Data de expedição  
            - comandante: Nome do comandante
    
    Returns:
        str: Caminho absoluto para o arquivo PDF gerado
        
    Raises:
        FileNotFoundError: Se o template do diploma não for encontrado
    """
    # Extrair subtipo para localizar o template específico
    subtipo = dados.get('subtipo')
    
    # Buscar template: primeiro específico, depois genérico
    if subtipo:
        imagem = find_model_image('Diplomas', subtipo)
    else:
        imagem = find_model_image('Diplomas')
    
    if imagem is None:
        raise FileNotFoundError('Modelo de Diploma não encontrado')

    # Carregar imagem de fundo e obter dimensões
    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    # Preparar diretório de saída para PDFs gerados
    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Diploma.pdf')

    # Criar PDF com as mesmas dimensões da imagem de fundo
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
    margem_esquerda = int(iw * 0.25)     # 8% da largura como margem esquerda
    margem_direita = int(iw * 0.08)      # 8% da largura como margem direita
    largura_texto = iw - margem_esquerda - margem_direita  # Largura útil para texto
    
    # Posições Y (de cima para baixo)
    y_titulo = int(ih * 0.75)            # 75% da altura - posição do título
    y_corpo = int(ih * 0.60)             # 55% da altura - corpo principal
    y_local_data = int(ih * 0.30)        # 30% da altura - local e data  
    y_comandante = int(ih * 0.25)        # 25% da altura - nome do comandante
    y_cargo = int(ih * 0.22)             # 22% da altura - cargo do comandante
    
    # 3. FUNÇÃO PARA QUEBRA DE TEXTO
    def quebrar_texto(canvas, texto, x, y, largura_max, altura_linha=25):
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
    
    # 4. APLICAR CONFIGURAÇÕES - TÍTULO (OPCIONAL - só se quiser sobrepor)
    # c.setFont(fonte_titulo, tamanho_titulo)
    # c.setFillColor(cor_titulo)
    # titulo = "DIPLOMA DE HONRA AO MÉRITO"
    # largura_titulo = c.stringWidth(titulo, fonte_titulo, tamanho_titulo)
    # x_titulo = (iw - largura_titulo) / 2  # Centralizado
    # c.drawString(x_titulo, y_titulo, titulo)
    
    # 5. CORPO PRINCIPAL DO TEXTO
    c.setFont(fonte_corpo, tamanho_corpo)
    c.setFillColor(cor_corpo)
    
    texto_principal = (
        f'O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
        f'usando das atribuições que lhe compete por meio do Decreto N° {dados.get("decreto", "")}, '
        f'confere ao(à) Senhor(a) {dados.get("nome", "")}, o presente Diploma '
        f'{dados.get("subtipo", "")}, do Corpo de Bombeiros Militar do Estado do Acre, '
        f'pelos relevantes serviços prestados à comunidade acreana.'
    )
    
    # Desenhar texto com quebra automática
    y_final = quebrar_texto(c, texto_principal, margem_esquerda, y_corpo, largura_texto)
    
    # 6. LOCAL E DATA
    c.setFont(fonte_assinatura, tamanho_assinatura + 2)
    c.setFillColor(cor_assinatura)
    
    local_data = f'{dados.get("local", "Rio Branco")} - Acre, {dados.get("data", "")}'
    # Posicionar à direita
    largura_local_data = c.stringWidth(local_data, fonte_assinatura, tamanho_assinatura + 2)
    x_local_data = iw - margem_direita - largura_local_data
    c.drawString(x_local_data, y_local_data, local_data)
    
    # 7. ASSINATURA DO COMANDANTE
    c.setFont(fonte_assinatura, tamanho_assinatura + 1)
    
    comandante = dados.get('comandante', '')
    largura_comandante = c.stringWidth(comandante, fonte_assinatura, tamanho_assinatura + 1)
    x_comandante = iw - margem_direita - largura_comandante
    c.drawString(x_comandante, y_comandante, comandante)
    
    # Linha de assinatura (opcional)
    linha_inicio = x_comandante - 20
    linha_fim = x_comandante + largura_comandante + 20
    c.line(linha_inicio, y_comandante - 3, linha_fim, y_comandante - 3)
    
    # 8. CARGO DO COMANDANTE
    c.setFont(fonte_assinatura, tamanho_assinatura)
    cargo = "Comandante Geral do CBMAC"
    largura_cargo = c.stringWidth(cargo, fonte_assinatura, tamanho_assinatura)
    x_cargo = iw - margem_direita - largura_cargo
    c.drawString(x_cargo, y_cargo, cargo)

    c.showPage()
    c.save()

    return out_path
