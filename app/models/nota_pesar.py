"""
Gerador de Notas de Pesar Oficiais CBMAC
========================================

Responsável pela geração de notas de pesar oficiais do Corpo de Bombeiros
Militar do Acre para expressar condolências pelo falecimento de pessoas
ligadas à corporação ou à comunidade.

As notas seguem protocolo oficial e incluem:
- Expressão de lamento institucional
- Informações sobre o falecido e parentesco
- Condolências aos familiares
- Dados oficiais (local, data, comandante)
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .utils import find_model_image



def gerar_certificado_nota_pesar(dados: dict) -> str:
    """
    Gera uma nota de pesar oficial em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - falecido_nota_pesar: Nome da pessoa falecida
            - parentesco_nota_pesar: Relação com o bombeiro/servidor
            - pessoa_enlutada_nota_pesar: Nome do enlutado (bombeiro/servidor)
            - local_nota_pesar: Local de expedição da nota
            - data_nota_pesar: Data de expedição
            - comandante_nota_pesar: Nome do comandante geral
    
    Returns:
        str: Caminho absoluto para o arquivo PDF gerado
        
    Raises:
        FileNotFoundError: Se o template não for encontrado
    """
    # ===================== REGISTRO DE FONTES CUSTOMIZADAS =====================
    def registrar_fontes_customizadas():
        """Registra as fontes TTF customizadas para uso no ReportLab"""
        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
        
        # Dicionário com as fontes disponíveis
        fontes_disponiveis = {
            'Arial-Regular': 'arial.ttf',
            'Arial-Bold': 'Arial Negrito.ttf',
            'Arial-Unicode': 'Arial Unicode Regular.TTF',
            'Freestyle-Script': 'Freestyle Script Regular.TTF',
            'Corsiva': 'Monotype Corsiva Itálico.TTF'
        }
        
        # Registrar cada fonte se o arquivo existir
        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():
            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)
            if os.path.exists(caminho_fonte):
                try:
                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))
                    print(f"✅ Fonte registrada: {nome_fonte}")
                except Exception as e:
                    print(f"❌ Erro ao registrar fonte {nome_fonte}: {e}")
            else:
                print(f"⚠️  Fonte não encontrada: {arquivo_fonte}")
    
    # Registrar as fontes customizadas
    registrar_fontes_customizadas()
    
    # ============================================================================
    
    # Localizar template padrão de nota de pesar
    imagem = find_model_image('Nota de Pesar')
    if imagem is None:
        raise FileNotFoundError('Modelo de Nota de Pesar não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'NotaDePesar.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)

    # ===================== PARÂMETROS AJUSTÁVEIS =====================
    PAGE_SIZE = (iw, ih)  # Usar tamanho da imagem de fundo
    MARGEM_ESQ   = 40 * mm
    MARGEM_DIR   = 40 * mm
    MARGEM_SUP   = 350 * mm
    MARGEM_INF   = 25 * mm

    # =============== CONFIGURAÇÃO DE FONTES CUSTOMIZADAS ===============
    # Você pode escolher entre as fontes padrão do ReportLab ou as customizadas
    
    # OPÇÃO 1: Fontes Padrão ReportLab
    # FONTE_CORPO_NOME = "Times-Roman"
    # FONTE_TITULO_NOME = "Times-Bold" 
    # FONTE_ASSINATURA_NOME = "Times-Bold"
    
    # OPÇÃO 2: Fontes Customizadas (descomente para usar)
    FONTE_CORPO_NOME = "Arial-Regular"        # Arial normal
    FONTE_TITULO_NOME = "Arial-Regular"          # Arial negrito
    FONTE_ASSINATURA_NOME = "Arial-Regular"      # Arial negrito
    FONTE_DECORATIVA_NOME = "Arial-Regular" # Para elementos decorativos
    FONTE_ELEGANTE_NOME = "Arial-Regular"           # Monotype Corsiva para assinaturas elegantes
    
    # Tamanhos de fonte
    FONTE_CORPO     = 150
    FONTE_LOCALDATA = 150
    FONTE_ASSINAT   = 150
    FONTE_CARGO     = 150

    # Espaçamentos (leading = espaçamento entre linhas)
    LEADING_CORPO     = 200   # ajuste para mais/menos espaço entre linhas do parágrafo
    ESPACO_APOS_CORPO = 40   # espaço em pontos após o corpo até a data/local
    ESPACO_ENTRE_LINHAS_ASSINAT = 20

    # Altura reservada para o bloco do corpo do texto
    ALTURA_BLOCO_CORPO = 1000 * mm  # aumente/diminua conforme o texto
    # ================================================================
    
    pw, ph = PAGE_SIZE
    centro_x = pw / 2
    
    # Cores
    from reportlab.lib.colors import white
    
    # Função para formatar data no padrão brasileiro
    def formatar_data_brasileira(data_str):
        """Converte data do formato YYYY-MM-DD para DD/MM/YYYY"""
        if not data_str:
            return ""
        try:
            from datetime import datetime
            # Se a data estiver no formato YYYY-MM-DD (vem do input date)
            if len(data_str) == 10 and data_str.count('-') == 2:
                data_obj = datetime.strptime(data_str, '%Y-%m-%d')
                return data_obj.strftime('%d/%m/%Y')
            # Se já estiver em outro formato, retorna como está
            return data_str
        except:
            return data_str
    
    # Conteúdo (montado com as variáveis dos dados)
    TEXTO = (
        f'O Corpo de Bombeiros Militar do Estado do Acre, através do Comandante-Geral, '
        f'lamenta o falecimento de {dados.get("falecido","")}, {dados.get("parentesco","")} '
        f'do {dados.get("pessoa_enlutada","")}. A corporação presta suas sinceras '
        f'condolências aos familiares e amigos por tão grande perda.'
    )
    LOCAL_DATA = f'{dados.get("local","Rio Branco")}, Acre {formatar_data_brasileira(dados.get("data",""))}'
    NOME_ASSINAT = dados.get('comandante', '')
    CARGO = "Comandante-Geral"
    # ================================================================
    
    # Utilitários
    def draw_centered_text(canv, txt, y, size=12, font=None):
        """Desenha texto centralizado com fonte especificada ou padrão"""
        if font is None:
            font = FONTE_CORPO_NOME
        canv.setFont(font, size)
        canv.drawCentredString(pw/2, y, txt)

    # 2) Corpo do texto dentro de um Frame (para controlar largura e leading)
    #    - Posição do frame: (x, y_base). Atenção: o y no Frame é a BASE (e não o topo).
    x_frame = MARGEM_ESQ
    largura_frame = pw - MARGEM_ESQ - MARGEM_DIR
    y_base_frame = ph - MARGEM_SUP - 1*mm - ALTURA_BLOCO_CORPO  # 20mm abaixo do título
    frame_corpo = Frame(x_frame, y_base_frame, largura_frame, ALTURA_BLOCO_CORPO, showBoundary=0)

    estilo_corpo = ParagraphStyle(
        "corpo",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,   # << espaçamento entre linhas
        alignment=1,             # 0=esq,1=centro,2=dir,4=justify
        textColor=white,
    )

    story = [
        Paragraph(TEXTO, estilo_corpo),
        Spacer(1, ESPACO_APOS_CORPO)
    ]

    # Desenha o corpo no canvas
    frame_corpo.addFromList(story, c)
    c.setFillColor(white)


    # 3) Local e data (centralizado logo abaixo do bloco do corpo)
    #    Pegamos a altura do topo do frame para calcular uma posição aproximada:
    y_apos_corpo = 1100*mm  # ajuste fino
    c.setFillColor(white)
    draw_centered_text(c, LOCAL_DATA, y_apos_corpo, FONTE_LOCALDATA, FONTE_CORPO_NOME)

    # 4) Assinatura (nome + cargo), centralizado mais abaixo
    y_assin = 900*mm
    c.setFillColor(white)
    
    # Nome do comandante com fonte de assinatura elegante (pode usar Corsiva para mais elegância)
    draw_centered_text(c, NOME_ASSINAT, y_assin, FONTE_ASSINAT, FONTE_ELEGANTE_NOME)
    
    # Cargo com fonte normal
    draw_centered_text(c, CARGO, y_assin - (FONTE_ASSINAT + ESPACO_ENTRE_LINHAS_ASSINAT), FONTE_CARGO, FONTE_CORPO_NOME)


    c.showPage()
    c.save()

    return out_path
