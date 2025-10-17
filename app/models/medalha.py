"""
Gerador de Certificados de Medalha (layout alinhado ao Agradecimento/Moeda)

Campos esperados em 'dados':
    - subtipo       : Tipo da medalha (ex.: Tempo de Serviço, Amigo, etc.)
    - subsubtipo    : Detalhe (ex.: 10 ANOS, 20 ANOS…)
    - nome_agraciado: Nome do contemplado (mantendo sua convenção atual)
    - decreto       : Decreto / base legal
    - local         : Local de expedição/entrega
    - data          : Data (YYYY-MM-DD ou texto)
    - comandante    : Nome do Comandante-Geral
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .utils import find_model_image


def gerar_certificado_medalha(dados: dict) -> str:
    """
    Gera o Certificado de Medalha com layout harmonizado ao Agradecimento.
    """

    # ===================== FONTES =============================================
    def registrar_fontes_customizadas():
        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
        fontes = {
            'Arial-Regular': 'arial.ttf',
            'Corsiva': 'Monotype Corsiva Itálico.TTF',
            'Arial-Negrito': 'Arial Negrito.ttf',
            'Arial-Unicode': 'Arial Unicode Regular.TTF',
            'Freestyle-Script': 'Freestyle Script Regular.TTF'
        }
        for nome, arquivo in fontes.items():
            caminho = os.path.join(fonts_dir, arquivo)
            if os.path.exists(caminho):
                try:
                    pdfmetrics.registerFont(TTFont(nome, caminho))
                except Exception as e:
                    print(f"[ERRO] Fonte {nome}: {e}")
            else:
                print(f"[AVISO] Fonte ausente: {arquivo}")

    registrar_fontes_customizadas()
    # ==========================================================================

    # ===================== TEMPLATE ===========================================
    subtipo = (dados.get('subtipo') or '').strip()
    subsub = (dados.get('subsubtipo') or '').strip()

    if subtipo and subsub:
        imagem = find_model_image('Medalhas', subtipo, subsub)
    elif subtipo:
        imagem = find_model_image('Medalhas', subtipo)
    else:
        imagem = find_model_image('Medalhas')

    if imagem is None:
        raise FileNotFoundError('Modelo de Medalha não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Medalha.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)
    # ==========================================================================

    # ===================== LAYOUT =============================================
    pw, ph = iw, ih

    MARGEM_ESQ = 170 * mm
    MARGEM_DIR = 50 * mm
    MARGEM_SUP = 125 * mm
    ALTURA_BLOCO = 400 * mm

    FONTE_CORPO_NOME = "Corsiva"
    FONTE_ASS_NOME = "Freestyle-Script"

    FONTE_CORPO = 40
    FONTE_LOCALDATA = 40
    FONTE_ASS = 44
    FONTE_CARGO = 32
    LEADING = 50
    ESPACO_APOS_CORPO = 110

    # ===================== DADOS/VALIDAÇÃO ====================================
    nome = (dados.get("nome_agraciado") or "").strip()  # mantém sua convenção atual
    decreto = (dados.get("decreto") or "").strip()
    local = (dados.get("local") or "").strip()
    data_bruta = (dados.get("data") or "").strip()
    comandante = (dados.get("comandante") or "").strip()

    faltando = [k for k, v in {
        "Nome do Agraciado": nome, "Decreto": decreto, "Local": local,
        "Data": data_bruta, "Comandante": comandante
    }.items() if not v]
    if faltando:
        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(faltando)}")

    def formatar_data_brasileira(s: str) -> str:
        try:
            from datetime import datetime
            meses = {
                1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
                5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
                9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
            }
            if len(s) == 10 and s.count('-') == 2:
                d = datetime.strptime(s, '%Y-%m-%d')
                return f'{d.day} de {meses[d.month]} de {d.year}'
            return s
        except Exception:
            return s

    DATA_LOCAL = f"{local}, {formatar_data_brasileira(data_bruta)}."
    # ==========================================================================

    # ===================== TEXTO ==============================================
    nome_medalha = (subsub or subtipo or "Medalha")
    texto = (
        "O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, "
        f"usando das atribuições que lhe compete por meio do Decreto N° <font color='red'>{decreto}</font>, "
        f"confere a <font name='Corsiva' color='red'>{nome}</font> a "
        f"<font name='Corsiva' color='red'>Medalha {nome_medalha}</font>, do Corpo de Bombeiros Militar do Estado do Acre, "
        "pelos relevantes serviços prestados ao Estado do Acre e ao Corpo de Bombeiros Militar."
    )

    estilo_principal = ParagraphStyle(
        "principal_medalha",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        textColor=colors.black,
        firstLineIndent=70
    )
    estilo_data = ParagraphStyle(
        "data_medalha",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_LOCALDATA,
        leading=LEADING,
        alignment=2,
        textColor=colors.black
    )
    style_cargo = ParagraphStyle(
        "cargo_assinatura",
        fontName=FONTE_ASS_NOME if FONTE_ASS_NOME in pdfmetrics.getRegisteredFontNames() else "Helvetica",
        fontSize=FONTE_CARGO,
        leading=FONTE_CARGO + 6,
        alignment=TA_CENTER,
    )

    x = MARGEM_ESQ
    w = pw - MARGEM_ESQ - MARGEM_DIR
    y = ph - MARGEM_SUP - 20 * mm - ALTURA_BLOCO
    frame = Frame(x, y, w, ALTURA_BLOCO, showBoundary=0)

    story = [
        Paragraph(texto, estilo_principal),
        Spacer(1, ESPACO_APOS_CORPO),
        Paragraph(DATA_LOCAL, estilo_data),
        Spacer(1, ESPACO_APOS_CORPO)
    ]
    frame.addFromList(story, c)

    # Assinatura central
    c.setFillColor(colors.black)
    c.setFont(FONTE_ASS_NOME if FONTE_ASS_NOME in pdfmetrics.getRegisteredFontNames() else "Helvetica", FONTE_ASS)
    c.drawCentredString(450 * mm, 150 + 40, comandante)
    c.setFont(FONTE_ASS_NOME if FONTE_ASS_NOME in pdfmetrics.getRegisteredFontNames() else "Helvetica", FONTE_CARGO)
    cargo_html = f"Comandante-Geral e Chanceler do Conselho da {subtipo}"
    frame_w = 140 * mm  # mais estreito para forçar a quebra automática
    frame_h = 30 * mm   # altura suficiente para 2 linhas
    frame_x = 385 * mm
    frame_y = 65  # ajuste fino vertical (mesma região onde estava o seu texto)

    p = Paragraph(cargo_html, style_cargo)
    w, h = p.wrap(frame_w, frame_h)  # calcula quebra
    p.drawOn(c, frame_x, frame_y)    # desenha centralizado dentro da área
    
    c.showPage()
    c.save()
    return out_path
