"""
Gerador de Certificados de Moeda CBMAC (layout alinhado ao Agradecimento)

- Estrutura baseada no modelo de Agradecimento:
  * Registro de fontes TTF customizadas (se presentes em app/static)
  * Composição via Frame/Paragraph (ReportLab Platypus) para texto principal
  * Espaçamentos e alinhamentos consistentes
  * Data formatada em pt-BR
  * Assinatura centralizada com cargo do Comandante-Geral

Campos esperados em 'dados':
    - nome_agraciado : Nome do contemplado
    - decreto        : Decreto que autoriza a emissão
    - local          : Local da expedição/entrega
    - data           : Data da expedição/entrega (YYYY-MM-DD ou texto)
    - comandante     : Nome do comandante geral
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .utils import find_model_image


def gerar_certificado_moeda(dados: dict) -> str:
    """
    Gera o certificado de Moeda CBMAC em PDF, com layout harmonizado ao Agradecimento.
    """

    # ===================== REGISTRO DE FONTES CUSTOMIZADAS =====================
    def registrar_fontes_customizadas():
        """Registra as fontes TTF customizadas, se existirem em app/static."""
        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

        fontes_disponiveis = {
            'Arial-Regular': 'arial.ttf',
            'Corsiva': 'Monotype Corsiva Itálico.TTF',        # mesma usada no Agradecimento
            'Arial-Negrito': 'Arial Negrito.ttf',
            'Arial-Unicode': 'Arial Unicode Regular.TTF',
            'Freestyle-Script': 'Freestyle Script Regular.TTF'
        }

        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():
            caminho = os.path.join(fonts_dir, arquivo_fonte)
            if os.path.exists(caminho):
                try:
                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho))
                    print(f"[OK] Fonte registrada: {nome_fonte}")
                except Exception as e:
                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")
            else:
                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")

    registrar_fontes_customizadas()
    # ==========================================================================

    # ===================== TEMPLATE DE FUNDO (MODELO) ==========================
    imagem = find_model_image('Moeda CBMAC')
    if imagem is None:
        raise FileNotFoundError('Modelo de Moeda CBMAC não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'MoedaCBMAC.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)
    # ==========================================================================

    # ===================== PARÂMETROS AJUSTÁVEIS (HARMONIZADOS) ===============
    PAGE_SIZE = (iw, ih)   # tamanho do próprio template
    pw, ph = PAGE_SIZE

    # Margens e bloco principal (coerentes com o Agradecimento)
    MARGEM_ESQ   = 170 * mm
    MARGEM_DIR   = 50  * mm
    MARGEM_SUP   = 125 * mm
    MARGEM_INF   = 25  * mm

    # Fontes/cores (iguais/compatíveis com Agradecimento)
    FONTE_CORPO_NOME        = "Corsiva"
    FONTE_ASSINATURA_NOME   = "Freestyle-Script"
    FONTE_ELEGANTE_NOME     = "Corsiva"

    FONTE_CORPO       = 40
    FONTE_LOCALDATA   = 40
    FONTE_ASSINAT     = 44
    FONTE_CARGO       = 32

    LEADING_CORPO           = 50
    ESPACO_APOS_CORPO       = 110
    ESPACO_ENTRE_LINHAS_ASS = 30

    ALTURA_BLOCO_CORPO = 400 * mm

    COR_TEXTO_PRINCIPAL = colors.black
    COR_DATA            = colors.HexColor("#000000")
    COR_ASSINATURA      = colors.HexColor("#000000")
    COR_DESTAQUE        = colors.red  # para nome e/ou elementos da moeda
    # ==========================================================================

    # ===================== CAPTURA E VALIDAÇÃO DE CAMPOS ======================
    nome_agraciado = (dados.get("nome_agraciado") or "").strip()
    decreto        = (dados.get("decreto") or "").strip()
    local          = (dados.get("local") or "").strip()
    data_evento    = (dados.get("data") or "").strip()
    comandante     = (dados.get("comandante") or "").strip()

    print("[DEBUG][Moeda] dados recebidos:", dados)

    obrigatorios = {
        "Nome do Agraciado": nome_agraciado,
        "Decreto": decreto,
        "Local": local,
        "Data": data_evento,
        "Nome do Comandante": comandante
    }
    faltando = [k for k, v in obrigatorios.items() if not v]
    if faltando:
        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(faltando)}")

    # ===================== FORMATAÇÃO DE DATA ================================
    def formatar_data_brasileira(data_str: str) -> str:
        """Converte YYYY-MM-DD para 'DD de Mês de AAAA' (com DD/Mês/Ano em vermelho)."""
        if not data_str:
            return ""
        try:
            from datetime import datetime
            meses = {
                1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
                5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
                9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
            }
            if len(data_str) == 10 and data_str.count('-') == 2:
                d = datetime.strptime(data_str, '%Y-%m-%d')
                dia, mes, ano = d.day, meses[d.month], d.year
                return f'<font color="black">{dia}</font> de <font color="black">{mes}</font> de <font color="black">{ano}</font>'
            return data_str
        except Exception:
            return data_str

    DATA_FORMATADA = formatar_data_brasileira(data_evento)
    DATA_LOCAL     = f"{local}, {DATA_FORMATADA}."
    # ========================================================================

    # ===================== TEXTO PRINCIPAL (PARÁGRAFO) =======================
    # Texto institucional com destaques semelhantes ao Agradecimento:
    texto_partes = [
        "O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre,",
        f"usando das atribuições que lhe compete por meio do Decreto N° <font color='red'>{decreto}</font>,",
        "confere a"
    ]

    # nome do agraciado em destaque (vermelho + fonte cursiva)
    texto_partes.append(f' <font name="Corsiva" color="red">{nome_agraciado}</font>,')
    texto_partes.append(
        'o Diploma da Moeda Comemorativa do Corpo de Bombeiros Militar do Estado do Acre, '
        'pelos relevantes serviços prestados ao Estado do Acre e ao Corpo de Bombeiros Militar.'
    )

    TEXTO_PRINCIPAL = " ".join(texto_partes)

    estilo_principal = ParagraphStyle(
        "principal_moeda",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,
        alignment=4,  # justificado
        textColor=COR_TEXTO_PRINCIPAL,
        firstLineIndent=70  # recuo inicial, como no Agradecimento
    )

    estilo_data = ParagraphStyle(
        "data_moeda",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_LOCALDATA,
        leading=LEADING_CORPO,
        alignment=2,  # centralizado
        textColor=COR_DATA
    )

    # Frame do corpo do texto (mesmas margens/altura)
    x_frame = MARGEM_ESQ
    largura_frame = pw - MARGEM_ESQ - MARGEM_DIR
    y_base_frame = ph - MARGEM_SUP - 20 * mm - ALTURA_BLOCO_CORPO
    frame_corpo = Frame(x_frame, y_base_frame, largura_frame, ALTURA_BLOCO_CORPO, showBoundary=0)

    story = [
        Paragraph(TEXTO_PRINCIPAL, estilo_principal),
        Spacer(1, ESPACO_APOS_CORPO),
        Paragraph(DATA_LOCAL, estilo_data),
        Spacer(1, ESPACO_APOS_CORPO * 2)
    ]

    frame_corpo.addFromList(story, c)

    # ===================== ASSINATURA CENTRALIZADA ===========================
    y_linha_assinatura = 150  # ajuste fino conforme o seu template
    c.setFillColor(COR_ASSINATURA)
    c.setFont(FONTE_ASSINATURA_NOME, FONTE_ASSINAT)

    # Nome do Comandante
    c.drawCentredString(450 * mm, y_linha_assinatura + 40, comandante)

    # Cargo do Comandante
    c.setFillColor(colors.black)
    c.setFont(FONTE_ASSINATURA_NOME, FONTE_CARGO)
    c.drawCentredString(450 * mm, y_linha_assinatura - 10, "Comandante-Geral")
    # ========================================================================

    c.showPage()
    c.save()
    return out_path
