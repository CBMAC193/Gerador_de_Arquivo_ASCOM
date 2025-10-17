"""
CONFIGURAÇÕES PERSONALIZÁVEIS PARA DOCUMENTOS CBMAC
==================================================

Este arquivo centraliza todas as configurações visuais dos documentos.
Modifique aqui para alterar cores, fontes, posições e tamanhos.
"""

from reportlab.lib.colors import Color, black, white, red, blue, green

# =================================================================
# CONFIGURAÇÕES GERAIS
# =================================================================

class ConfiguracaoDocumentos:
    """Classe com todas as configurações personalizáveis"""
    
    # =================================================================
    # FONTES
    # =================================================================
    FONTES = {
        'titulo': {
            'nome': 'Helvetica-Bold',
            'tamanho': 16
        },
        'subtitulo': {
            'nome': 'Helvetica-Bold', 
            'tamanho': 14
        },
        'corpo': {
            'nome': 'Helvetica',
            'tamanho': 12
        },
        'assinatura': {
            'nome': 'Helvetica',
            'tamanho': 11
        },
        'cargo': {
            'nome': 'Helvetica',
            'tamanho': 10
        },
        'rodape': {
            'nome': 'Helvetica',
            'tamanho': 8
        }
    }
    
    # =================================================================
    # CORES INSTITUCIONAIS CBMAC
    # =================================================================
    CORES = {
        'vermelho_cbmac': Color(0.8, 0, 0, 1),      # Vermelho institucional
        'azul_cbmac': Color(0, 0.2, 0.8, 1),        # Azul institucional  
        'dourado_cbmac': Color(0.8, 0.7, 0, 1),     # Dourado para medalhas
        'verde_cbmac': Color(0, 0.6, 0.2, 1),       # Verde para diplomas ambientais
        'preto': black,
        'cinza_escuro': Color(0.3, 0.3, 0.3, 1),
        'cinza_claro': Color(0.7, 0.7, 0.7, 1),
        'branco': white
    }
    
    # =================================================================
    # POSICIONAMENTO (% da altura/largura da página)
    # =================================================================
    POSICOES = {
        # Margens
        'margem_esquerda': 0.08,    # 8% da largura
        'margem_direita': 0.08,     # 8% da largura
        'margem_superior': 0.95,    # 95% da altura (quase no topo)
        'margem_inferior': 0.05,    # 5% da altura (quase no fundo)
        
        # Elementos principais
        'titulo': 0.85,             # 85% da altura
        'subtitulo': 0.78,          # 78% da altura  
        'corpo_principal': 0.60,    # 60% da altura
        'local_data': 0.30,         # 30% da altura
        'comandante': 0.25,         # 25% da altura
        'cargo_comandante': 0.22,   # 22% da altura
        'rodape': 0.08,             # 8% da altura
        
        # Específicos por documento
        'medalha': {
            'titulo': 0.80,
            'corpo': 0.55,
            'assinatura': 0.28
        },
        'diploma': {
            'titulo': 50.75, 
            'corpo': 50.55,
            'assinatura': 0.25
        },
        'certificado': {
            'titulo': 0.78,
            'corpo': 0.58,
            'assinatura': 0.30
        }
    }
    
    # =================================================================
    # ESPAÇAMENTOS E DIMENSÕES
    # =================================================================
    ESPACAMENTOS = {
        'altura_linha': 18,         # Espaçamento entre linhas de texto
        'espacamento_paragrafo': 25, # Espaçamento entre parágrafos
        'espacamento_titulo': 30,   # Espaço após título
        'margem_assinatura': 50,    # Margem da área de assinatura
        'altura_linha_assinatura': 3, # Altura da linha de assinatura
        'largura_maxima_texto': 0.84 # 84% da largura para texto corrido
    }
    
    # =================================================================
    # CONFIGURAÇÕES POR TIPO DE DOCUMENTO
    # =================================================================
    
    # DIPLOMAS
    DIPLOMA = {
        'cor_principal': 'vermelho_cbmac',
        'fonte_titulo': FONTES['titulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': POSICOES['diploma']['titulo'],
        'posicao_corpo': POSICOES['diploma']['corpo'],
        'posicao_assinatura': POSICOES['diploma']['assinatura'],
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'esquerda',
        'alinhamento_assinatura': 'direita'
    }
    
    # MEDALHAS
    MEDALHA = {
        'cor_principal': 'dourado_cbmac',
        'fonte_titulo': FONTES['titulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': POSICOES['medalha']['titulo'],
        'posicao_corpo': POSICOES['medalha']['corpo'],
        'posicao_assinatura': POSICOES['medalha']['assinatura'],
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'esquerda', 
        'alinhamento_assinatura': 'direita'
    }
    
    # CERTIFICADOS
    CERTIFICADO = {
        'cor_principal': 'azul_cbmac',
        'fonte_titulo': FONTES['subtitulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': POSICOES['certificado']['titulo'],
        'posicao_corpo': POSICOES['certificado']['corpo'],
        'posicao_assinatura': POSICOES['certificado']['assinatura'],
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'esquerda',
        'alinhamento_assinatura': 'direita'
    }
    
    # CONVITES
    CONVITE = {
        'cor_principal': 'verde_cbmac',
        'fonte_titulo': FONTES['titulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': 0.82,
        'posicao_corpo': 0.50,
        'posicao_assinatura': 0.25,
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'centro',  # Convites geralmente são centralizados
        'alinhamento_assinatura': 'centro'
    }
    
    # NOTAS DE PESAR
    NOTA_PESAR = {
        'cor_principal': 'preto',
        'fonte_titulo': FONTES['titulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': 0.80,
        'posicao_corpo': 0.55,
        'posicao_assinatura': 0.28,
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'esquerda',
        'alinhamento_assinatura': 'direita'
    }
    
    # AGRADECIMENTOS
    AGRADECIMENTO = {
        'cor_principal': 'azul_cbmac',
        'fonte_titulo': FONTES['subtitulo'],
        'fonte_corpo': FONTES['corpo'],
        'posicao_titulo': 0.78,
        'posicao_corpo': 0.58,
        'posicao_assinatura': 0.30,
        'alinhamento_titulo': 'centro',
        'alinhamento_corpo': 'esquerda',
        'alinhamento_assinatura': 'direita'
    }

# =================================================================
# FUNÇÕES UTILITÁRIAS
# =================================================================

def obter_cor(nome_cor):
    """Obtém cor pelo nome definido na configuração"""
    return ConfiguracaoDocumentos.CORES.get(nome_cor, black)

def obter_fonte(tipo_fonte):
    """Obtém configuração de fonte pelo tipo"""
    return ConfiguracaoDocumentos.FONTES.get(tipo_fonte, ConfiguracaoDocumentos.FONTES['corpo'])

def calcular_posicao_x(largura_pagina, tipo_alinhamento, largura_texto=0, margem_personalizada=None):
    """Calcula posição X baseada no alinhamento desejado"""
    config = ConfiguracaoDocumentos
    
    if margem_personalizada:
        margem_esq = largura_pagina * margem_personalizada
        margem_dir = largura_pagina * margem_personalizada
    else:
        margem_esq = largura_pagina * config.POSICOES['margem_esquerda']
        margem_dir = largura_pagina * config.POSICOES['margem_direita']
    
    if tipo_alinhamento == 'centro':
        return (largura_pagina - largura_texto) / 2
    elif tipo_alinhamento == 'direita':
        return largura_pagina - margem_dir - largura_texto
    else:  # esquerda (padrão)
        return margem_esq

def calcular_posicao_y(altura_pagina, percentual):
    """Calcula posição Y baseada no percentual da altura"""
    return int(altura_pagina * percentual)

def obter_config_documento(tipo_documento):
    """Obtém configuração específica para um tipo de documento"""
    config = ConfiguracaoDocumentos
    
    configs = {
        'Diplomas': config.DIPLOMA,
        'Medalhas': config.MEDALHA,
        'Certificado': config.CERTIFICADO,
        'Convite': config.CONVITE,
        'Nota de Pesar': config.NOTA_PESAR,
        'Agradecimento': config.AGRADECIMENTO
    }
    
    return configs.get(tipo_documento, config.DIPLOMA)  # Diploma como padrão

# =================================================================
# EXEMPLO DE USO
# =================================================================

def exemplo_uso():
    """
    Exemplo de como usar as configurações em um documento:
    
    # Obter configuração do documento
    config_doc = obter_config_documento('Diplomas')
    
    # Obter cor principal
    cor = obter_cor(config_doc['cor_principal'])
    canvas.setFillColor(cor)
    
    # Obter fonte do título
    fonte_titulo = obter_fonte('titulo')
    canvas.setFont(fonte_titulo['nome'], fonte_titulo['tamanho'])
    
    # Calcular posição do título (centralizado)
    titulo = "DIPLOMA DE HONRA"
    largura_titulo = canvas.stringWidth(titulo, fonte_titulo['nome'], fonte_titulo['tamanho'])
    x_titulo = calcular_posicao_x(largura_pagina, 'centro', largura_titulo)
    y_titulo = calcular_posicao_y(altura_pagina, config_doc['posicao_titulo'])
    
    canvas.drawString(x_titulo, y_titulo, titulo)
    """
    pass

# =================================================================
# PERSONALIZAÇÃO RÁPIDA
# =================================================================
"""
PARA PERSONALIZAR RAPIDAMENTE:

1. MUDAR CORES:
   - Edite os valores em ConfiguracaoDocumentos.CORES
   - Use valores RGB de 0 a 1: Color(vermelho, verde, azul, opacidade)

2. MUDAR FONTES:
   - Edite ConfiguracaoDocumentos.FONTES
   - Fontes disponíveis: Helvetica, Times-Roman, Courier (e suas variações Bold/Italic)

3. MUDAR POSIÇÕES:
   - Edite ConfiguracaoDocumentos.POSICOES
   - Use valores de 0 a 1 (percentual da altura/largura)

4. CONFIGURAR POR DOCUMENTO:
   - Edite as seções DIPLOMA, MEDALHA, etc.
   - Defina cor_principal, posições específicas, alinhamentos

EXEMPLO DE MUDANÇA:
Para deixar os diplomas com texto azul e posição mais alta:

DIPLOMA = {
    'cor_principal': 'azul_cbmac',  # Era 'vermelho_cbmac'
    'posicao_titulo': 0.90,         # Era 0.75
    # ... resto das configurações
}
"""