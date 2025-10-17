"""
Gerador de Convites Oficiais CBMAC
==================================

Responsável pela geração de convites oficiais para eventos, cerimônias
e solenidades do Corpo de Bombeiros Militar do Acre.

Os convites seguem o protocolo oficial e incluem informações sobre:
- Autoridade que convida (Comandante Geral)
- Pessoa/instituição convidada
- Evento específico
- Data, horário e local do evento
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


def gerar_certificado_convite(dados: dict) -> str:
    """
    Gera um convite oficial em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - cargo_convidado: Cargo da pessoa convidada
            - nome_convidado: Nome do convidado
            - pra_que_convidado: Descrição do evento/finalidade
            - data_convite: Data do evento
            - horario_convite: Horário do evento
            - local_convite: Local do evento
            - cidade_convite: Cidade onde ocorrerá
            - endereco_convite: Endereço específico
            - posto_convite: Posto do comandante
            - comandante_convite: Nome do comandante
    
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
                    print(f"[OK] Fonte registrada: {nome_fonte}")
                except Exception as e:
                    print(f"[ERRO] Erro ao registrar fonte {nome_fonte}: {e}")
            else:
                print(f"[AVISO] Fonte não encontrada: {arquivo_fonte}")
    
    # Registrar as fontes customizadas
    registrar_fontes_customizadas()
    
    # ============================================================================
    
    # Localizar template padrão de convites
    imagem = find_model_image('Convite')
    if imagem is None:
        raise FileNotFoundError('Modelo de Convite não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'Convite.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)

    # ===================== PARÂMETROS AJUSTÁVEIS =====================
    PAGE_SIZE = (iw, ih)  # Usar tamanho da imagem de fundo
    MARGEM_ESQ   = 230 * mm
    MARGEM_DIR   = 100 * mm
    MARGEM_SUP   = 150 * mm
    MARGEM_INF   = 25 * mm

    # =============== CONFIGURAÇÃO DE FONTES CUSTOMIZADAS ===============
    # Fontes para convites (pode usar fontes mais decorativas)
    FONTE_CORPO_NOME = "Arial-Unicode"        # Arial normal
    FONTE_TITULO_NOME = "Freestyle-Script"    # Fonte decorativa para convites
    FONTE_ASSINATURA_NOME = "Arial-Bold"      # Arial negrito
    FONTE_DECORATIVA_NOME = "Freestyle-Script" # Para elementos decorativos
    FONTE_ELEGANTE_NOME = "Corsiva"           # Monotype Corsiva para assinaturas elegantes
    
    # Tamanhos de fonte
    FONTE_TITULO    = 20
    FONTE_CORPO     = 48
    FONTE_LOCALDATA = 60
    FONTE_ASSINAT   = 60
    FONTE_CARGO     = 60

    # Espaçamentos (leading = espaçamento entre linhas)
    LEADING_CORPO     = 60   # ajuste para mais/menos espaço entre linhas do parágrafo
    ESPACO_APOS_CORPO = 40   # espaço em pontos após o corpo até a data/local
    ESPACO_ENTRE_LINHAS_ASSINAT = 20

    # Altura reservada para o bloco do corpo do texto
    ALTURA_BLOCO_CORPO = 500 * mm  # aumente/diminua conforme o texto
    # ==================================================================
    
    pw, ph = PAGE_SIZE
    centro_x = pw / 2
    
    # Cores
    from reportlab.lib.colors import black
    
    # Função para formatar data e hora no padrão solicitado
    def formatar_data_hora_completa(data_str, horario_str):
        """Converte para formato: 10 de Setembro de 2025, Quarta-Feira, 7h30min"""
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
            
            # Dias da semana em português
            dias_semana = {
                0: 'Segunda-Feira', 1: 'Terça-Feira', 2: 'Quarta-Feira',
                3: 'Quinta-Feira', 4: 'Sexta-Feira', 5: 'Sábado', 6: 'Domingo'
            }
            
            # Converter data
            if len(data_str) == 10 and data_str.count('-') == 2:
                data_obj = datetime.strptime(data_str, '%Y-%m-%d')
                
                dia = data_obj.day
                mes = meses[data_obj.month]
                ano = data_obj.year
                dia_semana = dias_semana[data_obj.weekday()]
                
                # Formatar horário
                hora_formatada = ""
                if horario_str:
                    try:
                        # Se horário estiver no formato HH:MM
                        if ':' in horario_str:
                            hora_obj = datetime.strptime(horario_str, '%H:%M')
                            hora_formatada = f"{hora_obj.hour}h{hora_obj.minute:02d}min"
                        else:
                            hora_formatada = horario_str
                    except:
                        hora_formatada = horario_str
                
                # Montar string completa
                data_completa = f"{dia} de {mes} de {ano}, {dia_semana}"
                if hora_formatada:
                    data_completa += f", {hora_formatada}"
                
                return data_completa
            
            return data_str
        except:
            return data_str
    
    # DEBUG: Mostrar todos os dados recebidos
    print(f"[DEBUG] Dados recebidos: {dados}")
    
    # Capturar dados do formulário (todos os campos são obrigatórios)
    posto = (dados.get("posto") or "").strip()
    comandante = (dados.get("comandante") or "").strip()
    genero_convidado = (dados.get("genero_convidado") or "senhor").strip()
    cargo_convidado = (dados.get("cargo_convidado") or "").strip()
    nome_convidado = (dados.get("nome_convidado") or "").strip()
    pra_que = (dados.get("pra_que_convidado") or "").strip()
    endereco = (dados.get("endereco_convite") or dados.get("endereco") or "").strip()
    local = (dados.get("local_convite") or dados.get("local") or "").strip()
    cidade = (dados.get("cidade_convite") or dados.get("cidade") or "").strip()
    data_evento = (dados.get("data_convite") or dados.get("data") or "").strip()
    horario_evento = (dados.get("horario_convite") or dados.get("horario") or "").strip()
    
    # DEBUG: Mostrar valores extraídos
    print(f"[DEBUG] Valores extraídos:")
    print(f"  genero_convidado: '{genero_convidado}'")
    print(f"  endereco: '{endereco}'")
    print(f"  local: '{local}'")
    print(f"  cidade: '{cidade}'")
    print(f"  data_evento: '{data_evento}'")
    print(f"  horario_evento: '{horario_evento}'")
    
    # Validar campos obrigatórios - falhar se estiver vazio
    campos_obrigatorios = {
        'Posto do Comandante': posto,
        'Nome do Comandante': comandante,
        'Cargo do Convidado': cargo_convidado,
        'Nome do Convidado': nome_convidado,
        'Finalidade do Convite': pra_que,
        'Endereço': endereco,
        'Local': local,
        'Cidade': cidade,
        'Data': data_evento,
        'Horário': horario_evento
    }
    
    campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]
    if campos_vazios:
        raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")
    
    
    # Determinar o artigo baseado no gênero
    artigo_genero = "o senhor" if genero_convidado == "senhor" else "a senhora"
    
    # Construir texto principal com verificação de campos vazios
    posto_formatado = f"{posto} " if posto else ""
    cargo_formatado = f'<font name="Arial-Unicode">{cargo_convidado}</font>, ' if cargo_convidado else ""
    
    TEXTO_PRINCIPAL = (
        f'    O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
        f'<font name="Arial-Bold">{posto_formatado}{comandante}</font>, tem a honra de convidar {artigo_genero} '
        f'{cargo_formatado}'
        f'<font name="Arial-Bold">{nome_convidado}</font>, para prestigiar '
        f'{pra_que}.'
    )
    
    # Data e hora
    DATA_HORA = formatar_data_hora_completa(data_evento, horario_evento)
    
    # Conteúdo formatado (todos os campos são obrigatórios)
    ENDERECO = f'<font name="Arial-Bold">Endereço:</font> <font name="Arial-Bold">{endereco}</font>'
    LOCAL = f'<font name="Arial-Bold">Local:</font> <font name="Arial-Bold">{local}</font>'
    CIDADE = f'<font name="Arial-Bold">{cidade}/AC</font>'
    # ================================================================
    
    # Utilitários
    def draw_centered_text(canv, txt, y, size=12, font=None):
        """Desenha texto centralizado com fonte especificada ou padrão"""
        if font is None:
            font = FONTE_CORPO_NOME
        canv.setFont(font, size)
        canv.drawCentredString(pw/2, y, txt)

    # Estilos para diferentes seções
    estilo_principal = ParagraphStyle(
        "principal",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,
        alignment=1,  # Justificado
        textColor=black
    )
    
    estilo_data = ParagraphStyle(
        "data",
        fontName="Arial-Bold",
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,
        alignment=1,  # Centralizado
        textColor=black
    )
    
    estilo_endereco = ParagraphStyle(
        "endereco",
        fontName=FONTE_CORPO_NOME,
        fontSize=FONTE_CORPO,
        leading=LEADING_CORPO,
        alignment=1,  # Centralizado
        textColor=black
    )

    # Frame para todo o conteúdo
    x_frame = MARGEM_ESQ
    largura_frame = pw - MARGEM_ESQ - MARGEM_DIR
    y_base_frame = ph - MARGEM_SUP - 20*mm - ALTURA_BLOCO_CORPO
    frame_corpo = Frame(x_frame, y_base_frame, largura_frame, ALTURA_BLOCO_CORPO, showBoundary=0)

    # Verificar se é modo individual ou coletivo
    modo_convite = dados.get("modo_convite", "individual")
    
    if modo_convite == "coletivo":
        # Modo coletivo - campos específicos
        tropa = (dados.get("tropa_convite") or "").strip()
        traje = (dados.get("traje_convite") or "").strip()
        
        # Validar campos obrigatórios para modo coletivo
        modo_convite = dados.get("modo_convite", "individual")

        if modo_convite == "individual":
            campos_obrigatorios = {
                'Posto do Comandante': posto,
                'Nome do Comandante': comandante,
                'Cargo do Convidado': cargo_convidado,
                'Nome do Convidado': nome_convidado,
                'Finalidade do Convite': pra_que,
                'Endereço': endereco,
                'Local': local,
                'Cidade': cidade,
                'Data': data_evento,
                'Horário': horario_evento
            }

        elif modo_convite == "coletivo":
            tropa = (dados.get("tropa_convite") or "").strip()
            traje = (dados.get("traje_convite") or "").strip()

            campos_obrigatorios = {
                'Posto do Comandante': posto,
                'Nome do Comandante': comandante,
                'Tropa': tropa,
                'Finalidade do Convite': pra_que,
                'Endereço': endereco,
                'Local': local,
                'Cidade': cidade,
                'Data': data_evento,
                'Horário': horario_evento,
                'Traje': traje
            }

        campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]
        if campos_vazios:
            raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")

        # Construir texto principal para modo coletivo
        posto_formatado = f"{posto} " if posto else ""
        
        TEXTO_PRINCIPAL = (
            f'    O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
            f'<font name="Arial-Bold">{posto_formatado}{comandante}</font>, tem a honra de convidar '
            f'<font name="Arial-Bold">{tropa}</font>, para prestigiar '
            f'{pra_que}.'
        )
        
        # Story para modo coletivo (incluindo traje)
        story = [
            Paragraph(TEXTO_PRINCIPAL, estilo_principal),
            Spacer(1, 75),  # Espaço entre parágrafo e data
            Paragraph(f'<font name="Arial-Bold">{DATA_HORA}</font>', estilo_data),
            Spacer(1, 75),  # Espaço entre data e endereço
            Paragraph(ENDERECO, estilo_endereco),
            Spacer(1, 75),  # Espaço entre endereço e traje
            Paragraph(f'<font name="Arial-Bold">Traje:</font> <font name="Arial-Bold">{traje}</font>', estilo_endereco),
            Spacer(1, 75),  # Espaço entre traje e local
            Paragraph(LOCAL, estilo_endereco),
            Spacer(1, 75),  # Espaço entre local e cidade
            Paragraph(CIDADE, estilo_endereco),
            Spacer(1, ESPACO_APOS_CORPO)  # Espaço final
        ]
        
    else:
        # Modo individual - campos específicos (código existente)
        genero_convidado = (dados.get("genero_convidado") or "senhor").strip()
        cargo_convidado = (dados.get("cargo_convidado") or "").strip()
        nome_convidado = (dados.get("nome_convidado") or "").strip()
        
        # Validar campos obrigatórios para modo individual
        campos_obrigatorios = {
            'Posto do Comandante': posto,
            'Nome do Comandante': comandante,
            'Cargo do Convidado': cargo_convidado,
            'Nome do Convidado': nome_convidado,
            'Finalidade do Convite': pra_que,
            'Endereço': endereco,
            'Local': local,
            'Cidade': cidade,
            'Data': data_evento,
            'Horário': horario_evento
        }
        
        campos_vazios = [nome for nome, valor in campos_obrigatorios.items() if not valor]
        if campos_vazios:
            raise ValueError(f"Campos obrigatórios não preenchidos: {', '.join(campos_vazios)}")
        
        # Determinar o artigo baseado no gênero
        artigo_genero = "o senhor" if genero_convidado == "senhor" else "a senhora"
        
        # Construir texto principal com verificação de campos vazios
        posto_formatado = f"{posto} " if posto else ""
        cargo_formatado = f'<font name="Arial-Unicode">{cargo_convidado}</font>, ' if cargo_convidado else ""
        
        TEXTO_PRINCIPAL = (
            f'    O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
            f'<font name="Arial-Bold">{posto_formatado}{comandante}</font>, tem a honra de convidar {artigo_genero} '
            f'{cargo_formatado}'
            f'<font name="Arial-Bold">{nome_convidado}</font>, para prestigiar '
            f'{pra_que}.'
        )
        
        # Story para modo individual (sem traje)
        story = [
            Paragraph(TEXTO_PRINCIPAL, estilo_principal),
            Spacer(1, 75),  # Espaço entre parágrafo e data
            Paragraph(f'<font name="Arial-Bold">{DATA_HORA}</font>', estilo_data),
            Spacer(1, 75),  # Espaço entre data e endereço
            Paragraph(ENDERECO, estilo_endereco),
            Spacer(1, 75),  # Espaço entre endereço e local
            Paragraph(LOCAL, estilo_endereco),
            Spacer(1, 75),  # Espaço entre local e cidade
            Paragraph(CIDADE, estilo_endereco),
            Spacer(1, ESPACO_APOS_CORPO)  # Espaço final
        ]

    # Desenha todo o conteúdo no canvas
    frame_corpo.addFromList(story, c)
    c.setFillColor(black)

    c.showPage()
    c.save()

    return out_path
