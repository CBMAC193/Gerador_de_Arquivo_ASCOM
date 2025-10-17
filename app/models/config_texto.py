"""
Configurações Globais de Formatação de Texto
===========================================

Este arquivo centraliza todas as configurações de formatação de texto
para os documentos gerados pelo sistema ASCOM.

Para modificar a formatação dos documentos, edite apenas este arquivo.
"""

# =================================================================
# CONFIGURAÇÕES DE FONTE
# =================================================================

# Fontes disponíveis no ReportLab
FONTES_DISPONIVEIS = [
    'Helvetica',
    'Helvetica-Bold', 
    'Helvetica-Oblique',
    'Helvetica-BoldOblique',
    'Times-Roman',
    'Times-Bold',
    'Times-Italic',
    'Times-BoldItalic',
    'Courier',
    'Courier-Bold',
    'Courier-Oblique',
    'Courier-BoldOblique'
]

# Fontes padrão para diferentes elementos
FONTE_TITULO = 'Helvetica-Bold'
FONTE_CORPO = 'Helvetica'
FONTE_ASSINATURA = 'Helvetica'

# =================================================================
# CONFIGURAÇÕES DE TAMANHO
# =================================================================

# Tamanhos de fonte (em pontos)
TAMANHO_TITULO = 32
TAMANHO_CORPO = 30
TAMANHO_ASSINATURA = 30
TAMANHO_ASSINATURA_MENOR = 28  # Para local/data

# =================================================================
# CONFIGURAÇÕES DE POSICIONAMENTO
# =================================================================

# Margens (como porcentagem da largura/altura)
MARGEM_ESQUERDA_PERCENT = 0.25    # 25% da largura
MARGEM_DIREITA_PERCENT = 0.08     # 8% da largura

# Posições Y (como porcentagem da altura, de cima para baixo)
POSICAO_TITULO_PERCENT = 0.75     # 75% da altura
POSICAO_CORPO_PERCENT = 0.60      # 60% da altura
POSICAO_LOCAL_DATA_PERCENT = 0.30 # 30% da altura
POSICAO_COMANDANTE_PERCENT = 0.25 # 25% da altura
POSICAO_CARGO_PERCENT = 0.22      # 22% da altura

# =================================================================
# CONFIGURAÇÕES DE ESPAÇAMENTO
# =================================================================

# Espaçamento entre linhas (em pontos)
ESPACAMENTO_LINHA_PADRAO = 30
ESPACAMENTO_LINHA_CORPO = 30
ESPACAMENTO_LINHA_ASSINATURA = 25

# Espaçamento entre seções
ESPACAMENTO_ENTRE_SECOES = 40

# =================================================================
# CONFIGURAÇÕES DE COR
# =================================================================

from reportlab.lib.colors import Color, black

# Cores institucionais (valores RGB de 0 a 1)
COR_TITULO = Color(0.8, 0, 0, 1)        # Vermelho institucional
COR_CORPO = black                        # Preto
COR_ASSINATURA = Color(0.3, 0.3, 0.3, 1)  # Cinza escuro
COR_DESTAQUE = Color(0, 0.2, 0.8, 1)    # Azul institucional

# =================================================================
# FUNÇÕES UTILITÁRIAS
# =================================================================

def calcular_margem_esquerda(largura_imagem):
    """Calcula a margem esquerda baseada na largura da imagem"""
    return int(largura_imagem * MARGEM_ESQUERDA_PERCENT)

def calcular_margem_direita(largura_imagem):
    """Calcula a margem direita baseada na largura da imagem"""
    return int(largura_imagem * MARGEM_DIREITA_PERCENT)

def calcular_largura_texto(largura_imagem):
    """Calcula a largura útil para texto"""
    return largura_imagem - calcular_margem_esquerda(largura_imagem) - calcular_margem_direita(largura_imagem)

def calcular_posicao_y(altura_imagem, tipo_posicao):
    """
    Calcula a posição Y baseada no tipo de posição
    
    Args:
        altura_imagem: Altura da imagem em pixels
        tipo_posicao: 'titulo', 'corpo', 'local_data', 'comandante', 'cargo'
    """
    posicoes = {
        'titulo': POSICAO_TITULO_PERCENT,
        'corpo': POSICAO_CORPO_PERCENT, 
        'local_data': POSICAO_LOCAL_DATA_PERCENT,
        'comandante': POSICAO_COMANDANTE_PERCENT,
        'cargo': POSICAO_CARGO_PERCENT
    }
    
    if tipo_posicao not in posicoes:
        raise ValueError(f"Tipo de posição inválido: {tipo_posicao}")
    
    return int(altura_imagem * posicoes[tipo_posicao])

# =================================================================
# CONFIGURAÇÕES ESPECÍFICAS POR TIPO DE DOCUMENTO
# =================================================================

# Configurações especiais para documentos específicos
CONFIGURACOES_ESPECIAIS = {
    'agradecimento': {
        'espacamento_linha': ESPACAMENTO_LINHA_PADRAO + 5,
        'tamanho_corpo': TAMANHO_CORPO - 2
    },
    'convite': {
        'espacamento_linha': ESPACAMENTO_LINHA_PADRAO - 3,
        'tamanho_corpo': TAMANHO_CORPO - 1
    },
    'nota_pesar': {
        'cor_corpo': Color(1, 1, 1, 1),  # Cinza mais escuro para luto
        'espacamento_linha': ESPACAMENTO_LINHA_PADRAO + 2
    }
}

def obter_configuracao(tipo_documento, propriedade, valor_padrao):
    """
    Obtém configuração específica para um tipo de documento
    
    Args:
        tipo_documento: Tipo do documento (ex: 'agradecimento')
        propriedade: Propriedade desejada (ex: 'espacamento_linha')
        valor_padrao: Valor padrão se não houver configuração específica
    """
    if tipo_documento in CONFIGURACOES_ESPECIAIS:
        return CONFIGURACOES_ESPECIAIS[tipo_documento].get(propriedade, valor_padrao)
    return valor_padrao