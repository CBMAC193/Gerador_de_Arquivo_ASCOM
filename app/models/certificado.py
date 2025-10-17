"""
Gerador de Certificado (layout alinhado ao Agradecimento/Moeda)

Campos esperados em 'dados':
    - nome        : Nome do contemplado
    - decreto     : Número do decreto / base legal
    - local       : Local de expedição/entrega
    - data        : Data (YYYY-MM-DD ou texto)
    - comandante  : Nome do Comandante-Geral
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


def gerar_certificado_certificado(dados: dict) -> str:
    """
    Gera o Certificado (ex.: Amigo dos Veteranos) com layout harmonizado ao Agradecimento.
    """

    # ===================== REGISTRO DE FONTES CUSTOMIZADAS =====================
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

    # ===================== TEMPLATE DE FUNDO (MODELO) ==========================
    # Mantém a mesma chave dos seus arquivos atuais
    imagem = find_model_image('Certificado Amigo dos Veteranos')
    if imagem is None:
        raise FileNotFoundError('Modelo de Certificado Amigo dos Veteranos não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Certificado.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)
    # ==========================================================================

    # ===================== PARÂMETROS DE LAYOUT (HARMONIZADOS) ================
    pw, ph = iw, ih

    MARGEM_ESQ = 170 * mm
    MARGEM_DIR = 50 * mm
    MARGEM_SUP = 125 * mm
    ALTURA_BLOCO_CORPO = 400 * mm

    FONTE_CORPO_NOME = "Corsiva"
    FONTE_ASS_NOME = "Freestyle-Script"

    FONTE_CORPO = 40
    FONTE_LOCALDATA = 40
    FONTE_ASS = 44
    FONTE_CARGO = 32

    LEADING = 50
    ESPACO_APOS_CORPO = 110

    COR_TEXTO = colors.black
    COR_DATA = colors.black
    # ==========================================================================

    # ===================== CAMPOS / VALIDAÇÃO =================================
    nome = (dados.get("nome") or "").strip()
    decreto = (dados.get("decreto") or "").strip()
    local = (dados.get("local") or "").strip()
    data_bruta = (dados.get("data") or "").strip()
    comandante = (dados.get("comandante") or "").strip()

    faltando = [k for k, v in {
        "Nome": nome, "Decreto": decreto, "Local": local, "Data": data_bruta, "Comandante": comandante
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

    # ===================== TEXTO / ESTILOS ====================================
    texto = (
        "O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, "
        f"usando das atribuições que lhe compete com base no Decreto N° <font color='red'>{decreto}</font>, "
        f"confere a <font name='Corsiva' color='red'>{nome}</font> o Certificado "
        "Amigo dos Veteranos do Corpo de Bombeiros Militar do Estado do Acre, "
        "pelos relevantes serviços prestados ao Estado do Acre e ao Corpo de Bombeiros."
    )

    estilo_principal = ParagraphStyle(
        "principal_cert",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        textColor=COR_TEXTO,
        firstLineIndent=70
    )
    estilo_data = ParagraphStyle(
        "data_cert",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_LOCALDATA,
        leading=LEADING,
        alignment=2,
        textColor=COR_DATA
    )
    
    x_frame = MARGEM_ESQ
    largura_frame = pw - MARGEM_ESQ - MARGEM_DIR
    y_base_frame = ph - MARGEM_SUP - 20 * mm - ALTURA_BLOCO_CORPO
    frame_corpo = Frame(x_frame, y_base_frame, largura_frame, ALTURA_BLOCO_CORPO, showBoundary=0)

    story = [
        Paragraph(texto, estilo_principal),
        Spacer(1, ESPACO_APOS_CORPO),
        Paragraph(DATA_LOCAL, estilo_data),
        Spacer(1, ESPACO_APOS_CORPO)
    ]
    frame_corpo.addFromList(story, c)

    # ------ 1) Desenha o NOME da assinatura e guarda o y ------
    x_centro = 450 * mm
    y_nome = 150 + 40
    fonte_nome = FONTE_ASS_NOME if FONTE_ASS_NOME in pdfmetrics.getRegisteredFontNames() else "Helvetica"

    c.setFont(fonte_nome, FONTE_ASS)
    c.drawCentredString(x_centro, y_nome, comandante)

    # Altura "real" de uma linha dessa fonte, em pontos
    ascent  = pdfmetrics.getAscent(fonte_nome)    * (FONTE_ASS / 1000.0)
    descent = abs(pdfmetrics.getDescent(fonte_nome)) * (FONTE_ASS / 1000.0)
    altura_linha_nome = ascent + descent

    # Espaço desejado entre o nome e o cargo
    gap = -5 * mm  # ajuste fino aqui (aumente/diminua para colar mais/menos)

    # ------ 2) Monta o PARÁGRAFO do cargo (quebra automática ou com <br/>) ------
    style_cargo = ParagraphStyle(
        "cargo_assinatura",
        fontName=fonte_nome,
        fontSize=FONTE_CARGO,
        leading=FONTE_CARGO + 6,
        alignment=TA_CENTER,
    )

    cargo_html = f"Comandante-Geral e Chanceler do Conselho da"  # ou com <br/>

    # largura que força a quebra; ajuste se quiser 1/2/3 linhas
    frame_w = 160 * mm

    p = Paragraph(cargo_html, style_cargo)
    w, h = p.wrap(frame_w, 100 * mm)  # calcula a altura necessária para o cargo

    # y do CARGO: imediatamente abaixo do nome (linha do nome + gap), 
    # lembrando que Paragraph.drawOn usa a base inferior do box
    y_cargo = y_nome - altura_linha_nome - gap - h

    # x para centralizar o parágrafo no mesmo centro do nome
    x_cargo = x_centro - (frame_w / 2.0)

    p.drawOn(c, x_cargo, y_cargo)
    
    c.showPage()
    c.save()
    return out_path
