"""
Gerador de Certificados de Agradecimento CBMAC
==============================================

Responsável pela geração de certificados de agradecimento oficiais
do Corpo de Bombeiros Militar do Acre.

Os certificados seguem o protocolo oficial e incluem informações sobre:
- Pessoa/instituição agradecida
- Motivo do agradecimento
- Data, local do evento
- Assinatura da autoridade competente
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .utils import find_model_image


def gerar_certificado_agradecimento(dados: dict) -> str:
    """
    Gera um certificado de agradecimento oficial em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - nome_agradecido_agradecimento: Nome da pessoa agradecida
            - funcao_agradecimento: Função/cargo da pessoa
            - local_funcao_agradecimento: Local onde exerce a função
            - pelo_que_agradecimento: Motivo do agradecimento
            - tema_agradecimento: Tema específico (opcional)
            - local_agradecimento: Local do evento
            - data_agradecimento: Data do evento
            - comandante_agradecimento: Nome do comandante
    
    Returns:
        str: Caminho absoluto para o arquivo PDF gerado
        
    Raises:
        FileNotFoundError: Se o template não for encontrado
        ValueError: Se campos obrigatórios não forem preenchidos
    """
    
    # ===================== REGISTRO DE FONTES CUSTOMIZADAS =====================
    def registrar_fontes_customizadas():
        """Registra as fontes TTF customizadas para uso no ReportLab"""
        fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
        
        # Dicionário com as fontes disponíveis
        fontes_disponiveis = {
            'Arial-Regular': 'arial.ttf',
            'Corsiva': 'Arial Negrito.ttf',
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
                    print(f"[OK] Fonte registrada: {nome_fonte}")
                except Exception as e:
                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")
            else:
                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")
    
    # Registrar as fontes customizadas
    registrar_fontes_customizadas()
    
    # =========================================================================
    
    # Localizar template padrão de agradecimento
    imagem = find_model_image('Agradecimento')
    if imagem is None:
        raise FileNotFoundError('Modelo de Agradecimento não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Agradecimento.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)

    # ===================== PARÂMETROS AJUSTÁVEIS =====================
    PAGE_SIZE = (iw, ih)  # Usar tamanho da imagem de fundo
    MARGEM_ESQ   = 200 * mm
    MARGEM_DIR   = 50 * mm
    MARGEM_SUP   = 150 * mm
    MARGEM_INF   = 25 * mm

    # =============== CONFIGURAÇÃO DE FONTES CUSTOMIZADAS ===============
    # Fontes para agradecimentos (pode usar fontes mais elegantes)
    FONTE_CORPO_NOME = "Corsiva"        # Arial normal
    FONTE_TITULO_NOME = "Freestyle-Script"    # Fonte decorativa
    FONTE_ASSINATURA_NOME = "Freestyle-Script"      # Arial negrito
    FONTE_DECORATIVA_NOME = "Freestyle-Script" # Para elementos decorativos
    FONTE_ELEGANTE_NOME = "Corsiva"           # Monotype Corsiva para assinaturas elegantes
    
    # Tamanhos de fonte
    FONTE_CORPO     = 40
    FONTE_LOCALDATA = 40
    FONTE_ASSINAT   = 40
    FONTE_CARGO     = 38

    # Espaçamentos (leading = espaçamento entre linhas)
    LEADING_CORPO     = 50   # ajuste para mais/menos espaço entre linhas do parágrafo
    ESPACO_APOS_CORPO = 60   # espaço em pontos após o corpo até a data/local
    ESPACO_ENTRE_LINHAS_ASSINAT = 30

    # Altura reservada para o bloco do corpo do texto
    ALTURA_BLOCO_CORPO = 400 * mm  # aumente/diminua conforme o texto
    
    # Cores
    COR_TEXTO_PRINCIPAL = colors.black
    COR_DATA = colors.HexColor("#000000")  # Alterado para preto
    COR_ASSINATURA = colors.HexColor("#000000")
    COR_DESTAQUE = colors.red  # Nova cor para destacar elementos importantes
    
    # ==================================================================
    
    pw, ph = PAGE_SIZE
    centro_x = pw / 2
    
    # DEBUG: Mostrar todos os dados recebidos
    print(f"[DEBUG] Dados recebidos: {dados}")
    
    # Capturar dados do formulário
    nome_agradecido = (dados.get("nome_agradecido_agradecimento") or "").strip()
    funcao = (dados.get("funcao_agradecimento") or "").strip()
    local_funcao = (dados.get("local_funcao_agradecimento") or "").strip()
    pelo_que = (dados.get("pelo_que_agradecimento") or "").strip()
    tema = (dados.get("tema_agradecimento") or "").strip()
    local = (dados.get("local_agradecimento") or "").strip()
    data_evento = (dados.get("data_agradecimento") or "").strip()
    comandante = (dados.get("comandante_agradecimento") or "").strip()
    
    # DEBUG: Mostrar valores extraídos
    print(f"[DEBUG] Valores extraídos:")
    print(f"  nome_agradecido: '{nome_agradecido}'")
    print(f"  funcao: '{funcao}'")
    print(f"  local_funcao: '{local_funcao}'")
    print(f"  pelo_que: '{pelo_que}'")
    print(f"  tema: '{tema}'")
    print(f"  local: '{local}'")
    print(f"  data_evento: '{data_evento}'")
    print(f"  comandante: '{comandante}'")
    
    # Validar campos obrigatórios
    campos_obrigatorios = {
        'Nome do Agradecido': nome_agradecido,
        'Função': funcao,
        'Pelo que': pelo_que,
        'Local': local,
        'Data': data_evento,
        'Nome do Comandante': comandante
    }
    
    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]
    if campos_vazios:
        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")
    
    # Função para formatar data no padrão brasileiro
    def formatar_data_brasileira(data_str):
        """Converte data para formato brasileiro com formatação específica de cores"""
        if not data_str:
            return ""
        try:
            from datetime import datetime
            
            # Meses em português
            meses = {
                1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
                5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
                9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
            }
            
            # Converter data
            if len(data_str) == 10 and data_str.count('-') == 2:
                data_obj = datetime.strptime(data_str, '%Y-%m-%d')
                
                dia = data_obj.day
                mes = meses[data_obj.month]
                ano = data_obj.year
                
                # Formatação com cores específicas: só dia, mês e ano em vermelho
                return f'<font color="red">{dia}</font> de <font color="red">{mes}</font> de <font color="red">{ano}</font>'
            
            return data_str
        except:
            return data_str

    # Construir texto principal com verificação de campos vazios
    texto_partes = ["Agradecemos"]
    
    # Adicionar nome e função (nome em vermelho)
    if nome_agradecido and funcao:
        if local_funcao:
            texto_partes.append(f'à <font name="Corsiva" color="red">{nome_agradecido}</font> - {funcao}, {local_funcao},')
        else:
            texto_partes.append(f'à <font name="Corsiva" color="red">{nome_agradecido}</font> - {funcao},')
    elif nome_agradecido:
        texto_partes.append(f'à <font name="Corsiva" color="red">{nome_agradecido}</font>,')
    
    # Adicionar motivo (tema em vermelho)
    if pelo_que:
        if tema:
            texto_partes.append(f'pela {pelo_que} com o tema <font name="Corsiva" color="red">"{tema}"</font>.')
        else:
            texto_partes.append(f'pela {pelo_que}.')
    
    TEXTO_PRINCIPAL = " ".join(texto_partes)
    
    # Data formatada (só dia, mês e ano em vermelho, "de" e local em preto)
    DATA_FORMATADA = formatar_data_brasileira(data_evento)
    DATA_LOCAL = f'{local}, {DATA_FORMATADA}.'
    
    # Assinatura
    NOME_ASSINATURA = f"{comandante}"
    CARGO_ASSINATURA = "Comandante-Geral"
    
    # ================================================================
    
    # Estilos para diferentes seções
    estilo_principal = ParagraphStyle(
        "principal",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,
        alignment=4,  # Justificado
        textColor=COR_TEXTO_PRINCIPAL,
        firstLineIndent=60  # Recuo da primeira linha em pontos (ajuste conforme necessário)
    )
    
    estilo_data = ParagraphStyle(
        "data",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_LOCALDATA,
        leading=LEADING_CORPO,
        alignment=2,  # Centralizado
        textColor=COR_DATA  # Já está definido como vermelho
    )

    # Frame para todo o conteúdo
    x_frame = MARGEM_ESQ
    largura_frame = pw - MARGEM_ESQ - MARGEM_DIR
    y_base_frame = ph - MARGEM_SUP - 20*mm - ALTURA_BLOCO_CORPO
    frame_corpo = Frame(x_frame, y_base_frame, largura_frame, ALTURA_BLOCO_CORPO, showBoundary=0)

    # Criar a story com todos os elementos
    story = [
        Paragraph(TEXTO_PRINCIPAL, estilo_principal),
        Spacer(1, ESPACO_APOS_CORPO),  # Espaço entre parágrafo e data
        Paragraph(DATA_LOCAL, estilo_data),
        Spacer(1, ESPACO_APOS_CORPO * 2)  # Espaço para assinatura
    ]

    # Desenha todo o conteúdo no canvas
    frame_corpo.addFromList(story, c)
    
    # ============= ASSINATURA COM LINHA DECORATIVA =============
    # Calcular posição da assinatura (mais abaixo na página)
    y_linha_assinatura = 150  # Ajustar conforme necessário
    

    # Nome do comandante
    c.setFillColor(COR_ASSINATURA)
    c.setFont(FONTE_ASSINATURA_NOME, FONTE_ASSINAT)
    c.drawCentredString(450 * mm, y_linha_assinatura + 15, NOME_ASSINATURA)

    # Cargo do comandante
    c.setFillColor(colors.black)
    c.setFont(FONTE_ASSINATURA_NOME, FONTE_CARGO)
    c.drawCentredString(450 * mm, y_linha_assinatura - 40, CARGO_ASSINATURA)

    c.showPage()
    c.save()

    return out_path
