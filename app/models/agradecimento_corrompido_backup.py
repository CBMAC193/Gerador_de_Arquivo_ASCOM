"""""""""""""""

Gerador de Certificados de Agradecimento CBMAC

Estrutura facilmente editável similar ao conviteGerador de Certificados de Agradecimento CBMAC

"""

Estrutura similar ao convite para facilitar ediçõesGerador de Certificados de Agradecimento CBMAC

import os

from reportlab.pdfgen import canvas"""

from reportlab.lib.pagesizes import A4

from reportlab.lib.units import mm==============================================Gerador de Certificados de Agradecimento CBMACGerador de Certificados de Agradecimento CBMAC

from reportlab.platypus import Frame, Paragraph

from reportlab.lib.styles import ParagraphStyleimport os

from reportlab.lib.enums import TA_CENTER

from reportlab.lib import colorsfrom reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFontfrom reportlab.lib.pagesizes import A4



from reportlab.lib.units import mmGerador moderno e facilmente editável de certificados de agradecimento.============================================================================================

def gerar_certificado_agradecimento(dados: dict) -> str:

    """Gera PDF de agradecimento com estrutura fácil de editar"""from reportlab.platypus import Frame, Paragraph

    

    # =========================from reportlab.lib.styles import ParagraphStyleEstrutura similar ao convite para facilitar edições de posicionamento, 

    # CONFIGURAÇÕES EDITÁVEIS

    # =========================from reportlab.lib.enums import TA_CENTER

    

    # Tamanho da páginafrom reportlab.lib import colorsfontes e tamanhos.

    PAGE_SIZE = A4

    MARGEM_ESQ = 25 * mmfrom reportlab.pdfbase import pdfmetrics

    MARGEM_DIR = 25 * mm

    from reportlab.pdfbase.ttfonts import TTFont

    # Fontes e tamanhos

    FONTE_TEXTO_PRINCIPAL = "Times-Roman"

    TAMANHO_TEXTO_PRINCIPAL = 16

    FONTE_DATA = "Times-Roman"CONFIGURAÇÕES FÁCEIS DE EDITAR:Gerador moderno e facilmente editável de certificados de agradecimento.Gerador moderno e facilmente editável de certificados de agradecimento.

    TAMANHO_DATA = 12

    FONTE_ASSINATURA_NOME = "Times-Bold"def gerar_certificado_agradecimento(dados: dict) -> str:

    TAMANHO_ASSINATURA_NOME = 14

    FONTE_ASSINATURA_CARGO = "Times-Roman"    """Gera PDF de agradecimento com estrutura fácil de editar"""- Posicionamento de elementos (coordenadas Y)

    TAMANHO_ASSINATURA_CARGO = 11

    ESPACAMENTO_LINHAS = 22    

    

    # Cores    # CONFIGURAÇÕES EDITÁVEIS- Tamanhos e tipos de fonteEstrutura similar ao convite para facilitar edições de posicionamento, Estrutura similar ao convite para facilitar edições de posicionamento,

    COR_TEXTO_PRINCIPAL = colors.black

    COR_DATA = colors.gray    PAGE_SIZE = A4

    COR_ASSINATURA = colors.HexColor("#002B5B")

    COR_LINHA_ASSINATURA = colors.HexColor("#777777")    MARGEM_ESQ = 25 * mm- Cores e estilos

    

    # Posicionamento (valores de 0 a 1 = % da altura)    MARGEM_DIR = 25 * mm

    Y_TEXTO_PRINCIPAL = 0.5

    Y_DATA_LOCAL = 0.35    - Espaçamento entre elementosfontes e tamanhos.fontes e tamanhos.

    Y_LINHA_ASSINATURA = 0.20

    Y_NOME_COMANDANTE = 0.17    # FONTES E TAMANHOS

    Y_CARGO_COMANDANTE = 0.14

        FONTE_TEXTO_PRINCIPAL = "Times-Roman""""

    # Dimensões

    ALTURA_BLOCO_TEXTO = 70 * mm    TAMANHO_TEXTO_PRINCIPAL = 16

    LARGURA_LINHA_ASSINATURA = 90 * mm

        FONTE_DATA = "Times-Roman"

    # =========================

    # FIM DAS CONFIGURAÇÕES    TAMANHO_DATA = 12

    # =========================

        FONTE_ASSINATURA_NOME = "Times-Bold"import os

    def registrar_fontes_customizadas():

        """Registra fontes customizadas disponíveis no sistema"""    TAMANHO_ASSINATURA_NOME = 14

        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

        fontes_disponiveis = {    FONTE_ASSINATURA_CARGO = "Times-Roman"from reportlab.pdfgen import canvasCONFIGURAÇÕES FÁCEIS DE EDITAR:CONFIGURAÇÕES FÁCEIS DE EDITAR:

            'Arial-Regular': 'arial.ttf',

            'Arial-Bold': 'Arial Negrito.ttf',    TAMANHO_ASSINATURA_CARGO = 11

            'Arial-Unicode': 'Arial Unicode Regular.TTF',

            'Freestyle-Script': 'Freestyle Script Regular.TTF',    ESPACAMENTO_LINHAS = 22from reportlab.lib.pagesizes import A4

            'Corsiva': 'Monotype Corsiva Itálico.TTF'

        }    

        

        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():    # CORESfrom reportlab.lib.units import mm- Posicionamento de elementos (coordenadas Y)- Posicionamento de elementos (coordenadas Y)

            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)

            if os.path.exists(caminho_fonte):    COR_TEXTO_PRINCIPAL = colors.black

                try:

                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))    COR_DATA = colors.grayfrom reportlab.platypus import Frame, Paragraph

                    print(f"[OK] Fonte registrada: {nome_fonte}")

                except Exception as e:    COR_ASSINATURA = colors.HexColor("#002B5B")

                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")

        COR_LINHA_ASSINATURA = colors.HexColor("#777777")from reportlab.lib.styles import ParagraphStyle- Tamanhos e tipos de fonte- Tamanhos e tipos de fonte

    # Registrar fontes

    registrar_fontes_customizadas()    

    

    # Preparar diretórios e arquivos    # POSICIONAMENTO (valores de 0 a 1 = % da altura)from reportlab.lib.enums import TA_CENTER

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    uploads_dir = os.path.abspath(os.path.join(base_dir, '..', 'uploads'))    Y_TEXTO_PRINCIPAL = 0.5

    os.makedirs(uploads_dir, exist_ok=True)

    caminho_certificado = os.path.join(uploads_dir, 'Agradecimento.pdf')    Y_DATA_LOCAL = 0.35from reportlab.lib import colors- Cores e estilos- Cores e estilos

    

    # Extrair dados do formulário    Y_LINHA_ASSINATURA = 0.20

    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()

    funcao = (dados.get("funcao_agradecimento") or "").strip()    Y_NOME_COMANDANTE = 0.17from reportlab.pdfbase import pdfmetrics

    local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()

    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()    Y_CARGO_COMANDANTE = 0.14

    tema = (dados.get("tema_agradecimento") or "").strip()

    local = (dados.get("local_agradecimento") or "").strip()    from reportlab.pdfbase.ttfonts import TTFont- Espaçamento entre elementos- Espaçamento entre elementos

    data_evento = (dados.get("data_agradecimento") or "").strip()

    comandante = (dados.get("comandante_agradecimento") or "").strip()    # DIMENSÕES

    

    # Validação de campos obrigatórios    ALTURA_BLOCO_TEXTO = 70 * mm

    campos_obrigatorios = {

        'Nome do Agradecido': nome_agradecido,    LARGURA_LINHA_ASSINATURA = 90 * mm

        'Função': funcao,

        'Pelo que': pelo_que,    """"""

        'Local': local,

        'Data': data_evento,    # REGISTRO DE FONTES

        'Nome do Comandante': comandante

    }    def registrar_fontes_customizadas():def gerar_certificado_agradecimento(dados: dict) -> str:

    

    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

    if campos_vazios:

        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")        fontes_disponiveis = {    """

    

    # Criar canvas PDF            'Arial-Regular': 'arial.ttf',

    pw, ph = PAGE_SIZE

    c = canvas.Canvas(caminho_certificado, pagesize=PAGE_SIZE)            'Arial-Bold': 'Arial Negrito.ttf',    Gera PDF de agradecimento com estrutura fácil de editar

    

    def draw_centered(canv, txt, y, size, cor=colors.black, font="Times-Roman"):            'Arial-Unicode': 'Arial Unicode Regular.TTF',

        """Função auxiliar para desenhar texto centralizado"""

        canv.setFillColor(cor)            'Freestyle-Script': 'Freestyle Script Regular.TTF',    """import osimport os

        canv.setFont(font, size)

        canv.drawCentredString(pw / 2, y, txt)            'Corsiva': 'Monotype Corsiva Itálico.TTF'

    

    # Construir texto principal        }    

    texto_partes = ["Agradecemos"]

            

    if nome_agradecido and funcao:

        if local_funcao:        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():    # =============================================================================from reportlab.pdfgen import canvasfrom reportlab.pdfgen import canvas

            texto_partes.append(f"à {nome_agradecido} - {funcao}, {local_funcao},")

        else:            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)

            texto_partes.append(f"à {nome_agradecido} - {funcao},")

    elif nome_agradecido:            if os.path.exists(caminho_fonte):    # 🎛️ CONFIGURAÇÕES FÁCEIS DE EDITAR - AJUSTE AQUI CONFORME NECESSÁRIO

        texto_partes.append(f"à {nome_agradecido},")

                    try:

    if pelo_que:

        if tema:                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))    # =============================================================================from reportlab.lib.pagesizes import A4from reportlab.lib.pagesizes import A4

            texto_partes.append(f"pela {pelo_que} com o tema \"{tema}\".")

        else:                    print(f"[OK] Fonte registrada: {nome_fonte}")

            texto_partes.append(f"pela {pelo_que}.")

                    except Exception as e:    

    TEXTO_PRINCIPAL = " ".join(texto_partes)

                        print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")

    # Desenhar texto principal usando Frame para quebra de linha

    estilo_corpo = ParagraphStyle(        # 📐 DIMENSÕES E MARGENSfrom reportlab.lib.units import mmfrom reportlab.lib.units import mm

        "corpo",

        fontName=FONTE_TEXTO_PRINCIPAL,    registrar_fontes_customizadas()

        fontSize=TAMANHO_TEXTO_PRINCIPAL,

        textColor=COR_TEXTO_PRINCIPAL,        PAGE_SIZE = A4

        leading=ESPACAMENTO_LINHAS,

        alignment=TA_CENTER,    # PREPARAR ARQUIVOS

    )

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))    MARGEM_ESQ = 25 * mmfrom reportlab.platypus import Frame, Paragraph, Spacerfrom reportlab.platypus import Frame, Paragraph, Spacer

    x_frame = MARGEM_ESQ

    w_frame = pw - (MARGEM_ESQ + MARGEM_DIR)    uploads_dir = os.path.abspath(os.path.join(base_dir, '..', 'uploads'))

    y_base_frame = ph * Y_TEXTO_PRINCIPAL - (ALTURA_BLOCO_TEXTO / 2)

        os.makedirs(uploads_dir, exist_ok=True)    MARGEM_DIR = 25 * mm

    frame = Frame(x_frame, y_base_frame, w_frame, ALTURA_BLOCO_TEXTO, showBoundary=0)

    story = [Paragraph(TEXTO_PRINCIPAL, estilo_corpo)]    caminho_certificado = os.path.join(uploads_dir, 'Agradecimento.pdf')

    frame.addFromList(story, c)

            MARGEM_SUP = 25 * mmfrom reportlab.lib.styles import ParagraphStylefrom reportlab.lib.styles import ParagraphStyle

    # Desenhar data e local

    DATA_LOCAL = f"{local}, {data_evento}."    # VALIDAÇÃO

    y_data = ph * Y_DATA_LOCAL

    draw_centered(c, DATA_LOCAL, y_data, TAMANHO_DATA, COR_DATA, FONTE_DATA)    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()    MARGEM_INF = 25 * mm

    

    # Desenhar assinatura    funcao = (dados.get("funcao_agradecimento") or "").strip()

    NOME_ASSINATURA = f"{comandante} - Cel QOBMEC"

    CARGO_ASSINATURA = "Comandante-Geral"    local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()    from reportlab.lib.enums import TA_CENTERfrom reportlab.lib.enums import TA_CENTER

    

    # Linha da assinatura    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()

    y_linha = ph * Y_LINHA_ASSINATURA

    c.setStrokeColor(COR_LINHA_ASSINATURA)    tema = (dados.get("tema_agradecimento") or "").strip()    # 🔤 FONTES E TAMANHOS (fácil de ajustar)

    c.setLineWidth(1)

    c.line(pw / 2 - LARGURA_LINHA_ASSINATURA/2, y_linha, pw / 2 + LARGURA_LINHA_ASSINATURA/2, y_linha)    local = (dados.get("local_agradecimento") or "").strip()

    

    # Nome do comandante    data_evento = (dados.get("data_agradecimento") or "").strip()    FONTE_TEXTO_PRINCIPAL = "Times-Roman"from reportlab.lib import colorsfrom reportlab.lib import colors

    y_nome = ph * Y_NOME_COMANDANTE

    draw_centered(c, NOME_ASSINATURA, y_nome, TAMANHO_ASSINATURA_NOME, COR_ASSINATURA, FONTE_ASSINATURA_NOME)    comandante = (dados.get("comandante_agradecimento") or "").strip()

    

    # Cargo do comandante        TAMANHO_TEXTO_PRINCIPAL = 16

    y_cargo = ph * Y_CARGO_COMANDANTE

    draw_centered(c, CARGO_ASSINATURA, y_cargo, TAMANHO_ASSINATURA_CARGO, colors.black, FONTE_ASSINATURA_CARGO)    campos_obrigatorios = {

    

    # Finalizar PDF        'Nome do Agradecido': nome_agradecido,    from reportlab.pdfbase import pdfmetricsfrom reportlab.pdfbase import pdfmetrics

    c.showPage()

    c.save()        'Função': funcao,

    

    return caminho_certificado        'Pelo que': pelo_que,    FONTE_DATA = "Times-Roman"

        'Local': local,

        'Data': data_evento,    TAMANHO_DATA = 12from reportlab.pdfbase.ttfonts import TTFontfrom reportlab.pdfbase.ttfonts import TTFont

        'Nome do Comandante': comandante

    }    

    

    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]    FONTE_ASSINATURA_NOME = "Times-Bold"

    if campos_vazios:

        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")    TAMANHO_ASSINATURA_NOME = 14

    

    # CRIAR PDF    

    pw, ph = PAGE_SIZE

    c = canvas.Canvas(caminho_certificado, pagesize=PAGE_SIZE)    FONTE_ASSINATURA_CARGO = "Times-Roman"

    

    def draw_centered(canv, txt, y, size, cor=colors.black, font="Times-Roman"):    TAMANHO_ASSINATURA_CARGO = 11def gerar_certificado_agradecimento(dados: dict) -> str:def gerar_certificado_agradecimento(dados: dict) -> str:

        canv.setFillColor(cor)

        canv.setFont(font, size)    

        canv.drawCentredString(pw / 2, y, txt)

        # 📏 ESPAÇAMENTO ENTRE LINHAS    """    """

    # CONSTRUIR TEXTO

    texto_partes = ["Agradecemos"]    ESPACAMENTO_LINHAS = 22

    

    if nome_agradecido and funcao:        Gera PDF de agradecimento com estrutura fácil de editar    Gera PDF de agradecimento com estrutura fácil de editar

        if local_funcao:

            texto_partes.append(f"à {nome_agradecido} - {funcao}, {local_funcao},")    # 🎨 CORES (fácil de personalizar)

        else:

            texto_partes.append(f"à {nome_agradecido} - {funcao},")    COR_TEXTO_PRINCIPAL = colors.black    """    """

    elif nome_agradecido:

        texto_partes.append(f"à {nome_agradecido},")    COR_DATA = colors.gray

    

    if pelo_que:    COR_ASSINATURA = colors.HexColor("#002B5B")  # Azul institucional    

        if tema:

            texto_partes.append(f"pela {pelo_que} com o tema \"{tema}\".")    COR_LINHA_ASSINATURA = colors.HexColor("#777777")  # Cinza claro

        else:

            texto_partes.append(f"pela {pelo_que}.")        # =============================================================================    # =============================================================================

    

    TEXTO_PRINCIPAL = " ".join(texto_partes)    # 📍 POSICIONAMENTO VERTICAL (coordenadas Y - fácil de mover elementos)

    

    # TEXTO PRINCIPAL    # Valores de 0 a 1 representam porcentagem da altura da página    # 🎛️ CONFIGURAÇÕES FÁCEIS DE EDITAR - AJUSTE AQUI CONFORME NECESSÁRIO    # 🎛️ CONFIGURAÇÕES FÁCEIS DE EDITAR - AJUSTE AQUI CONFORME NECESSÁRIO

    estilo_corpo = ParagraphStyle(

        "corpo",    Y_TEXTO_PRINCIPAL = 0.5        # 50% da altura - centro da página

        fontName=FONTE_TEXTO_PRINCIPAL,

        fontSize=TAMANHO_TEXTO_PRINCIPAL,    Y_DATA_LOCAL = 0.35            # 35% da altura - abaixo do texto    # =============================================================================    # =============================================================================

        textColor=COR_TEXTO_PRINCIPAL,

        leading=ESPACAMENTO_LINHAS,    Y_LINHA_ASSINATURA = 0.20      # 20% da altura - linha da assinatura

        alignment=TA_CENTER,

    )    Y_NOME_COMANDANTE = 0.17       # 17% da altura - nome do comandante    

    

    x_frame = MARGEM_ESQ    Y_CARGO_COMANDANTE = 0.14      # 14% da altura - cargo do comandante

    w_frame = pw - (MARGEM_ESQ + MARGEM_DIR)

    y_base_frame = ph * Y_TEXTO_PRINCIPAL - (ALTURA_BLOCO_TEXTO / 2)        # 📐 DIMENSÕES E MARGENS    # 📐 DIMENSÕES E MARGENS

    

    frame = Frame(x_frame, y_base_frame, w_frame, ALTURA_BLOCO_TEXTO, showBoundary=0)    # 📐 DIMENSÕES DO BLOCO DE TEXTO

    story = [Paragraph(TEXTO_PRINCIPAL, estilo_corpo)]

    frame.addFromList(story, c)    ALTURA_BLOCO_TEXTO = 70 * mm   # Altura da área de texto    PAGE_SIZE = A4    PAGE_SIZE = A4

    

    # DATA E LOCAL    LARGURA_LINHA_ASSINATURA = 90 * mm  # Largura da linha de assinatura

    DATA_LOCAL = f"{local}, {data_evento}."

    y_data = ph * Y_DATA_LOCAL        MARGEM_ESQ = 25 * mm    MARGEM_ESQ = 25 * mm

    draw_centered(c, DATA_LOCAL, y_data, TAMANHO_DATA, COR_DATA, FONTE_DATA)

        # =============================================================================

    # ASSINATURA

    NOME_ASSINATURA = f"{comandante} - Cel QOBMEC"    # 🔧 REGISTRO DE FONTES CUSTOMIZADAS    MARGEM_DIR = 25 * mm    MARGEM_DIR = 25 * mm

    CARGO_ASSINATURA = "Comandante-Geral"

        # =============================================================================

    y_linha = ph * Y_LINHA_ASSINATURA

    c.setStrokeColor(COR_LINHA_ASSINATURA)    def registrar_fontes_customizadas():    MARGEM_SUP = 25 * mm    MARGEM_SUP = 25 * mm

    c.setLineWidth(1)

    c.line(pw / 2 - LARGURA_LINHA_ASSINATURA/2, y_linha, pw / 2 + LARGURA_LINHA_ASSINATURA/2, y_linha)        """Registra fontes TTF customizadas disponíveis"""

    

    y_nome = ph * Y_NOME_COMANDANTE        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))    MARGEM_INF = 25 * mm    MARGEM_INF = 25 * mm

    draw_centered(c, NOME_ASSINATURA, y_nome, TAMANHO_ASSINATURA_NOME, COR_ASSINATURA, FONTE_ASSINATURA_NOME)

            

    y_cargo = ph * Y_CARGO_COMANDANTE

    draw_centered(c, CARGO_ASSINATURA, y_cargo, TAMANHO_ASSINATURA_CARGO, colors.black, FONTE_ASSINATURA_CARGO)        fontes_disponiveis = {    

    

    c.showPage()            'Arial-Regular': 'arial.ttf',

    c.save()

                'Arial-Bold': 'Arial Negrito.ttf',    # 🔤 FONTES E TAMANHOS (fácil de ajustar)    # 🔤 FONTES E TAMANHOS (fácil de ajustar)

    return caminho_certificado
            'Arial-Unicode': 'Arial Unicode Regular.TTF',

            'Freestyle-Script': 'Freestyle Script Regular.TTF',    FONTE_TEXTO_PRINCIPAL = "Times-Roman"    FONTE_TEXTO_PRINCIPAL = "Times-Roman"

            'Corsiva': 'Monotype Corsiva Itálico.TTF'

        }    TAMANHO_TEXTO_PRINCIPAL = 16    TAMANHO_TEXTO_PRINCIPAL = 16

        

        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():    

            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)

            if os.path.exists(caminho_fonte):    FONTE_DATA = "Times-Roman"    FONTE_DATA = "Times-Roman"

                try:

                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))    TAMANHO_DATA = 12    TAMANHO_DATA = 12

                    print(f"[OK] Fonte registrada: {nome_fonte}")

                except Exception as e:    

                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")

            else:    FONTE_ASSINATURA_NOME = "Times-Bold"    FONTE_ASSINATURA_NOME = "Times-Bold"

                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")

        TAMANHO_ASSINATURA_NOME = 14    TAMANHO_ASSINATURA_NOME = 14

    # Registrar fontes customizadas

    registrar_fontes_customizadas()    

    

    # 📁 PREPARAR DIRETÓRIOS E ARQUIVOS    FONTE_ASSINATURA_CARGO = "Times-Roman"    FONTE_ASSINATURA_CARGO = "Times-Roman"

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    uploads_dir = os.path.abspath(os.path.join(base_dir, '..', 'uploads'))    TAMANHO_ASSINATURA_CARGO = 11    TAMANHO_ASSINATURA_CARGO = 11

    os.makedirs(uploads_dir, exist_ok=True)

    caminho_certificado = os.path.join(uploads_dir, 'Agradecimento.pdf')    

    

    # =============================================================================    # 📏 ESPAÇAMENTO ENTRE LINHAS    # 📏 ESPAÇAMENTO ENTRE LINHAS

    # ✅ VALIDAÇÃO DE CAMPOS OBRIGATÓRIOS

    # =============================================================================    ESPACAMENTO_LINHAS = 22    ESPACAMENTO_LINHAS = 22

    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()

    funcao = (dados.get("funcao_agradecimento") or "").strip()    

    local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()

    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()    # 🎨 CORES (fácil de personalizar)    # 🎨 CORES (fácil de personalizar)

    tema = (dados.get("tema_agradecimento") or "").strip()

    local = (dados.get("local_agradecimento") or "").strip()    COR_TEXTO_PRINCIPAL = colors.black    COR_TEXTO_PRINCIPAL = colors.black

    data_evento = (dados.get("data_agradecimento") or "").strip()

    comandante = (dados.get("comandante_agradecimento") or "").strip()    COR_DATA = colors.gray    COR_DATA = colors.gray

    

    # Validar campos obrigatórios - falhar se estiver vazio    COR_ASSINATURA = colors.HexColor("#002B5B")  # Azul institucional    COR_ASSINATURA = colors.HexColor("#002B5B")  # Azul institucional

    campos_obrigatorios = {

        'Nome do Agradecido': nome_agradecido,    COR_LINHA_ASSINATURA = colors.HexColor("#777777")  # Cinza claro    COR_LINHA_ASSINATURA = colors.HexColor("#777777")  # Cinza claro

        'Função': funcao,

        'Pelo que': pelo_que,    

        'Local': local,

        'Data': data_evento,    # 📍 POSICIONAMENTO VERTICAL (coordenadas Y - fácil de mover elementos)    # 📍 POSICIONAMENTO VERTICAL (coordenadas Y - fácil de mover elementos)

        'Nome do Comandante': comandante

    }    # Valores de 0 a 1 representam porcentagem da altura da página    # Valores de 0 a 1 representam porcentagem da altura da página

    

    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]    Y_TEXTO_PRINCIPAL = 0.5        # 50% da altura - centro da página    Y_TEXTO_PRINCIPAL = 0.5  # 50% da altura - centro da página

    if campos_vazios:

        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")    Y_DATA_LOCAL = 0.35            # 35% da altura - abaixo do texto    Y_DATA_LOCAL = 0.35  # 35% da altura - abaixo do texto

    

    # =============================================================================    Y_LINHA_ASSINATURA = 0.20      # 20% da altura - linha da assinatura    Y_LINHA_ASSINATURA = 0.20  # 20% da altura - linha da assinatura

    # 🎨 CRIAR DOCUMENTO PDF

    # =============================================================================    Y_NOME_COMANDANTE = 0.17       # 17% da altura - nome do comandante    Y_NOME_COMANDANTE = 0.17  # 17% da altura - nome do comandante

    pw, ph = PAGE_SIZE

    c = canvas.Canvas(caminho_certificado, pagesize=PAGE_SIZE)    Y_CARGO_COMANDANTE = 0.14      # 14% da altura - cargo do comandante    Y_CARGO_COMANDANTE = 0.14  # 14% da altura - cargo do comandante

    

    # 🎯 FUNÇÃO AUXILIAR PARA DESENHAR TEXTO CENTRALIZADO    

    def draw_centered(canv, txt, y, size, cor=colors.black, font="Times-Roman"):

        """Desenha texto centralizado na página"""    # 📐 DIMENSÕES DO BLOCO DE TEXTO    # 📐 DIMENSÕES DO BLOCO DE TEXTO

        canv.setFillColor(cor)

        canv.setFont(font, size)    ALTURA_BLOCO_TEXTO = 70 * mm   # Altura da área de texto    ALTURA_BLOCO_TEXTO = 70 * mm  # Altura da área de texto

        canv.drawCentredString(pw / 2, y, txt)

        LARGURA_LINHA_ASSINATURA = 90 * mm  # Largura da linha de assinatura    LARGURA_LINHA_ASSINATURA = 90 * mm  # Largura da linha de assinatura

    # =============================================================================

    # 📝 CONSTRUIR TEXTO PRINCIPAL DINÂMICO    

    # =============================================================================

    texto_partes = ["Agradecemos"]    # =============================================================================    # =============================================================================

    

    # Adicionar nome e função    # 🔧 REGISTRO DE FONTES CUSTOMIZADAS    # 🔧 REGISTRO DE FONTES CUSTOMIZADAS

    if nome_agradecido and funcao:

        if local_funcao:    # =============================================================================    # =============================================================================

            texto_partes.append(f"à {nome_agradecido} - {funcao}, {local_funcao},")

        else:    def registrar_fontes_customizadas():    def registrar_fontes_customizadas():

            texto_partes.append(f"à {nome_agradecido} - {funcao},")

    elif nome_agradecido:        """Registra fontes TTF customizadas disponíveis"""        """Registra fontes TTF customizadas disponíveis"""

        texto_partes.append(f"à {nome_agradecido},")

            fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))        fonts_dir = os.path.abspath(

    # Adicionar motivo

    if pelo_que:                    os.path.join(os.path.dirname(__file__), "..", "static")

        if tema:

            texto_partes.append(f"pela {pelo_que} com o tema \"{tema}\".")        fontes_disponiveis = {        )

        else:

            texto_partes.append(f"pela {pelo_que}.")            'Arial-Regular': 'arial.ttf',

    

    TEXTO_PRINCIPAL = " ".join(texto_partes)            'Arial-Bold': 'Arial Negrito.ttf',        fontes_disponiveis = {

    

    # =============================================================================            'Arial-Unicode': 'Arial Unicode Regular.TTF',            "Arial-Regular": "arial.ttf",

    # 🎨 1️⃣ BLOCO DE TEXTO PRINCIPAL (CENTRALIZADO)

    # =============================================================================            'Freestyle-Script': 'Freestyle Script Regular.TTF',            "Arial-Bold": "Arial Negrito.ttf",

    estilo_corpo = ParagraphStyle(

        "corpo",            'Corsiva': 'Monotype Corsiva Itálico.TTF'            "Arial-Unicode": "Arial Unicode Regular.TTF",

        fontName=FONTE_TEXTO_PRINCIPAL,

        fontSize=TAMANHO_TEXTO_PRINCIPAL,        }            "Freestyle-Script": "Freestyle Script Regular.TTF",

        textColor=COR_TEXTO_PRINCIPAL,

        leading=ESPACAMENTO_LINHAS,                    "Corsiva": "Monotype Corsiva Itálico.TTF",

        alignment=TA_CENTER,  # Centralizado

    )        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():        }

    

    # Calcular posição do bloco de texto            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)

    x_frame = MARGEM_ESQ

    w_frame = pw - (MARGEM_ESQ + MARGEM_DIR)            if os.path.exists(caminho_fonte):        for nome_fonte, arquivo_fonte in fontes_disponiveis.items():

    y_base_frame = ph * Y_TEXTO_PRINCIPAL - (ALTURA_BLOCO_TEXTO / 2)  # Posição baseada na configuração

                    try:            caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)

    frame = Frame(x_frame, y_base_frame, w_frame, ALTURA_BLOCO_TEXTO, showBoundary=0)

    story = [Paragraph(TEXTO_PRINCIPAL, estilo_corpo)]                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))            if os.path.exists(caminho_fonte):

    frame.addFromList(story, c)

                        print(f"[OK] Fonte registrada: {nome_fonte}")                try:

    # =============================================================================

    # 🎨 2️⃣ DATA E LOCAL                except Exception as e:                    pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))

    # =============================================================================

    DATA_LOCAL = f"{local}, {data_evento}."                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")                    print(f"[OK] Fonte registrada: {nome_fonte}")

    y_data = ph * Y_DATA_LOCAL  # Posição baseada na configuração

    draw_centered(c, DATA_LOCAL, y_data, TAMANHO_DATA, COR_DATA, FONTE_DATA)            else:                except Exception as e:

    

    # =============================================================================                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")

    # 🎨 3️⃣ ASSINATURA COM LINHA DECORATIVA

    # =============================================================================                else:

    NOME_ASSINATURA = f"{comandante} - Cel QOBMEC"

    CARGO_ASSINATURA = "Comandante-Geral"    # Registrar fontes customizadas                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")

    

    # Desenhar linha de assinatura    registrar_fontes_customizadas()

    y_linha = ph * Y_LINHA_ASSINATURA

    c.setStrokeColor(COR_LINHA_ASSINATURA)        # Registrar fontes customizadas

    c.setLineWidth(1)

    c.line(pw / 2 - LARGURA_LINHA_ASSINATURA/2, y_linha, pw / 2 + LARGURA_LINHA_ASSINATURA/2, y_linha)    # 📁 PREPARAR DIRETÓRIOS E ARQUIVOS    registrar_fontes_customizadas()

    

    # Nome do comandante    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    y_nome = ph * Y_NOME_COMANDANTE

    draw_centered(c, NOME_ASSINATURA, y_nome, TAMANHO_ASSINATURA_NOME, COR_ASSINATURA, FONTE_ASSINATURA_NOME)    uploads_dir = os.path.abspath(os.path.join(base_dir, '..', 'uploads'))    # 📁 PREPARAR DIRETÓRIOS E ARQUIVOS

    

    # Cargo do comandante    os.makedirs(uploads_dir, exist_ok=True)    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    y_cargo = ph * Y_CARGO_COMANDANTE

    draw_centered(c, CARGO_ASSINATURA, y_cargo, TAMANHO_ASSINATURA_CARGO, colors.black, FONTE_ASSINATURA_CARGO)    caminho_certificado = os.path.join(uploads_dir, 'Agradecimento.pdf')    uploads_dir = os.path.abspath(os.path.join(base_dir, "..", "uploads"))

    

    # =============================================================================        os.makedirs(uploads_dir, exist_ok=True)

    # 💾 FINALIZAR E SALVAR PDF

    # =============================================================================    # =============================================================================    caminho_certificado = os.path.join(uploads_dir, "Agradecimento.pdf")

    c.showPage()

    c.save()    # ✅ VALIDAÇÃO DE CAMPOS OBRIGATÓRIOS

    

    return caminho_certificado    # =============================================================================    # =============================================================================

    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()    # ✅ VALIDAÇÃO DE CAMPOS OBRIGATÓRIOS

    funcao = (dados.get("funcao_agradecimento") or "").strip()    # =============================================================================

    local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()    # use RELATIVOS pra “colar” no modelo

    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()    MARGEM_ESQ = 0.30 * iw  # ~30% da largura

    tema = (dados.get("tema_agradecimento") or "").strip()    MARGEM_DIR = 0.30 * iw

    local = (dados.get("local_agradecimento") or "").strip()    MARGEM_SUP = 0.16 * ih  # topo da área útil

    data_evento = (dados.get("data_agradecimento") or "").strip()    MARGEM_INF = 0.12 * ih  # rodapé da área útil

    comandante = (dados.get("comandante_agradecimento") or "").strip()

        # Tipografia

    # Validar campos obrigatórios - falhar se estiver vazio    F_TEXTO = max(12, int(0.023 * ih))  # escala com a altura

    campos_obrigatorios = {    F_DATA = max(12, int(0.018 * ih))

        'Nome do Agradecido': nome_agradecido,    F_NOME = max(14, int(0.02 * ih))

        'Função': funcao,    F_CARGO = max(11, int(0.017 * ih))

        'Pelo que': pelo_que,    LEAD = int(F_TEXTO * 1.35)

        'Local': local,

        'Data': data_evento,    COR_TEXTO = colors.black

        'Nome do Comandante': comandante    COR_DATA = colors.gray

    }    COR_ASSIN = colors.HexColor("#002B5B")

    

    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]    # =================== VALIDAÇÃO ===================

    if campos_vazios:    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()

        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")    funcao = (dados.get("funcao_agradecimento") or "").strip()

        local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()

    # =============================================================================    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()

    # 🎨 CRIAR DOCUMENTO PDF    tema = (dados.get("tema_agradecimento") or "").strip()

    # =============================================================================    cidade = (dados.get("local_agradecimento") or "").strip()  # “Rio Branco - Acre”

    pw, ph = PAGE_SIZE    data_str = (dados.get("data_agradecimento") or "").strip()

    c = canvas.Canvas(caminho_certificado, pagesize=PAGE_SIZE)    comandante = (dados.get("comandante_agradecimento") or "").strip()

    

    # 🎯 FUNÇÃO AUXILIAR PARA DESENHAR TEXTO CENTRALIZADO    obrig = {

    def draw_centered(canv, txt, y, size, cor=colors.black, font="Times-Roman"):        "Nome do Agradecido": nome_agradecido,

        """Desenha texto centralizado na página"""        "Função": funcao,

        canv.setFillColor(cor)        "Pelo que": pelo_que,

        canv.setFont(font, size)        "Local": cidade,

        canv.drawCentredString(pw / 2, y, txt)        "Data": data_str,

            "Nome do Comandante": comandante,

    # =============================================================================    }

    # 📝 CONSTRUIR TEXTO PRINCIPAL DINÂMICO    faltando = [k for k, v in obrig.items() if not v]

    # =============================================================================    if faltando:

    texto_partes = ["Agradecemos"]        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(faltando)}")

    

    # Adicionar nome e função    # =================== TEXTO PRINCIPAL ===================

    if nome_agradecido and funcao:    nome_fmt = f'<font color="red">{nome_agradecido}</font>' if nome_agradecido else ""

        if local_funcao:    tema_fmt = f'<font color="red">{tema}</font>' if tema else ""

            texto_partes.append(f"à {nome_agradecido} - {funcao}, {local_funcao},")

        else:    partes = ["Agradecemos"]

            texto_partes.append(f"à {nome_agradecido} - {funcao},")    if nome_agradecido and funcao:

    elif nome_agradecido:        if local_funcao:

        texto_partes.append(f"à {nome_agradecido},")            partes.append(f"à {nome_fmt} - {funcao}, {local_funcao},")

            else:

    # Adicionar motivo            partes.append(f"à {nome_fmt} - {funcao},")

    if pelo_que:    elif nome_agradecido:

        if tema:        partes.append(f"à {nome_fmt},")

            texto_partes.append(f"pela {pelo_que} com o tema \"{tema}\".")

        else:    if pelo_que:

            texto_partes.append(f"pela {pelo_que}.")        if tema:

                partes.append(f'pela {pelo_que} com o tema "{tema_fmt}".')

    TEXTO_PRINCIPAL = " ".join(texto_partes)        else:

                partes.append(f"pela {pelo_que}.")

    # =============================================================================

    # 🎨 1️⃣ BLOCO DE TEXTO PRINCIPAL (CENTRALIZADO)    TEXTO = " ".join(partes)

    # =============================================================================

    estilo_corpo = ParagraphStyle(    # estilo parágrafo

        "corpo",

        fontName=FONTE_TEXTO_PRINCIPAL,    estilo_corpo = ParagraphStyle(

        fontSize=TAMANHO_TEXTO_PRINCIPAL,        "corpo",

        textColor=COR_TEXTO_PRINCIPAL,        fontName="Corsiva",

        leading=ESPACAMENTO_LINHAS,        fontSize=F_TEXTO,

        alignment=TA_CENTER,  # Centralizado        leading=LEAD,

    )        textColor=COR_TEXTO,

            alignment=TA_CENTER,

    # Calcular posição do bloco de texto    )

    x_frame = MARGEM_ESQ

    w_frame = pw - (MARGEM_ESQ + MARGEM_DIR)    # ✅ área do corpo: centrada um pouco ACIMA do meio (como no modelo)

    y_base_frame = ph * Y_TEXTO_PRINCIPAL - (ALTURA_BLOCO_TEXTO / 2)  # Posição baseada na configuração    ALTURA_BLOCO = 0.20 * ih

        w_frame = 197.4 * mm  # 19,74 cm

    frame = Frame(x_frame, y_base_frame, w_frame, ALTURA_BLOCO_TEXTO, showBoundary=0)    x_frame = (iw - w_frame) / 2  # centraliza horizontalmente

    story = [Paragraph(TEXTO_PRINCIPAL, estilo_corpo)]    y_centro = ih * 0.56

    frame.addFromList(story, c)    y_frame = y_centro - ALTURA_BLOCO / 2

    

    # =============================================================================    Frame(x_frame, y_frame, w_frame, ALTURA_BLOCO, showBoundary=0).addFromList(

    # 🎨 2️⃣ DATA E LOCAL        [Paragraph(TEXTO, estilo_corpo)], c

    # =============================================================================    )

    DATA_LOCAL = f"{local}, {data_evento}."

    y_data = ph * Y_DATA_LOCAL  # Posição baseada na configuração    # =================== DATA E LOCAL ===================

    draw_centered(c, DATA_LOCAL, y_data, TAMANHO_DATA, COR_DATA, FONTE_DATA)    def data_extenso_pt(data_iso: str) -> str:

            from datetime import datetime

    # =============================================================================

    # 🎨 3️⃣ ASSINATURA COM LINHA DECORATIVA        meses = [

    # =============================================================================            "Janeiro",

    NOME_ASSINATURA = f"{comandante} - Cel QOBMEC"            "Fevereiro",

    CARGO_ASSINATURA = "Comandante-Geral"            "Março",

                "Abril",

    # Desenhar linha de assinatura            "Maio",

    y_linha = ph * Y_LINHA_ASSINATURA            "Junho",

    c.setStrokeColor(COR_LINHA_ASSINATURA)            "Julho",

    c.setLineWidth(1)            "Agosto",

    c.line(pw / 2 - LARGURA_LINHA_ASSINATURA/2, y_linha, pw / 2 + LARGURA_LINHA_ASSINATURA/2, y_linha)            "Setembro",

                "Outubro",

    # Nome do comandante            "Novembro",

    y_nome = ph * Y_NOME_COMANDANTE            "Dezembro",

    draw_centered(c, NOME_ASSINATURA, y_nome, TAMANHO_ASSINATURA_NOME, COR_ASSINATURA, FONTE_ASSINATURA_NOME)        ]

            try:

    # Cargo do comandante            d = datetime.strptime(data_iso, "%Y-%m-%d")

    y_cargo = ph * Y_CARGO_COMANDANTE            return f"{d.day} de {meses[d.month-1]} de {d.year}"

    draw_centered(c, CARGO_ASSINATURA, y_cargo, TAMANHO_ASSINATURA_CARGO, colors.black, FONTE_ASSINATURA_CARGO)        except Exception:

                return data_iso

    # =============================================================================

    # 💾 FINALIZAR E SALVAR PDF    data_fmt = f'<font color="red">{data_extenso_pt(data_str)}</font>'

    # =============================================================================    LOCAL_DATA = f"{cidade}, {data_fmt}."

    c.showPage()    # ✅ no modelo fica bem abaixo do corpo, mas não encostado no rodapé

    c.save()    y_data = ih * 0.37

    

    return caminho_certificado    def draw_centered(canv, txt, y, size, cor=colors.black, font="Times-Roman"):
        canv.setFillColor(cor)
        canv.setFont(font, size)
        canv.drawCentredString(iw / 2, y, txt)

    draw_centered(c, LOCAL_DATA, y_data, F_DATA, COR_DATA, "Times-Roman")

    # =================== ASSINATURA ===================
    NOME_ASSIN = f"{comandante} - Cel QOBMEC"
    CARGO = "Comandante Geral"  # <- sem hífen como no modelo

    # linha e textos de assinatura mais para baixo, centralizados
    y_assin_base = ih * 0.22
    c.setStrokeColor(colors.HexColor("#777777"))
    c.setLineWidth(1)
    c.line(iw / 2 - 0.18 * iw, y_assin_base + 6, iw / 2 + 0.18 * iw, y_assin_base + 6)

    draw_centered(c, NOME_ASSIN, y_assin_base, F_NOME, COR_ASSIN, "Times-Bold")
    draw_centered(
        c, CARGO, y_assin_base - (F_NOME + 3), F_CARGO, colors.black, "Times-Roman"
    )

    c.showPage()
    c.save()
    return caminho_certificado
