"""
TESTE PRÁTICO DAS CONFIGURAÇÕES DE TEXTO
========================================

Este arquivo permite testar rapidamente as configurações de texto
sem precisar gerar um documento completo.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, black, red, blue
from reportlab.lib.utils import ImageReader
import os

def teste_configuracoes_basicas():
    """
    Cria um PDF de teste mostrando diferentes configurações de texto
    """
    # Configurar dimensões da página (A4)
    largura_pagina = 595  # pontos
    altura_pagina = 842   # pontos
    
    # Criar diretório de teste
    teste_dir = os.path.join(os.path.dirname(__file__), 'teste_configuracoes')
    os.makedirs(teste_dir, exist_ok=True)
    
    # Criar PDF de teste
    pdf_path = os.path.join(teste_dir, 'teste_textos.pdf')
    c = canvas.Canvas(pdf_path, pagesize=(largura_pagina, altura_pagina))
    
    # =================================================================
    # TESTE 1: DIFERENTES FONTES E TAMANHOS
    # =================================================================
    
    y_atual = altura_pagina - 50  # Começar próximo ao topo
    
    # Título do teste
    c.setFont('Helvetica-Bold', 20)
    c.setFillColor(Color(0.8, 0, 0, 1))  # Vermelho CBMAC
    c.drawString(50, y_atual, "TESTE DE CONFIGURAÇÕES DE TEXTO - CBMAC")
    y_atual -= 40
    
    # Teste de fontes
    fontes_teste = [
        ('Helvetica', 12, 'Helvetica padrão - tamanho 12'),
        ('Helvetica-Bold', 14, 'Helvetica Negrito - tamanho 14'),
        ('Helvetica-Oblique', 12, 'Helvetica Itálico - tamanho 12'),
        ('Times-Roman', 12, 'Times Roman - tamanho 12'),
        ('Times-Bold', 14, 'Times Negrito - tamanho 14'),
        ('Courier', 10, 'Courier (monospace) - tamanho 10')
    ]
    
    c.setFillColor(black)
    for fonte, tamanho, texto in fontes_teste:
        c.setFont(fonte, tamanho)
        c.drawString(50, y_atual, texto)
        y_atual -= 25
    
    y_atual -= 20
    
    # =================================================================
    # TESTE 2: DIFERENTES CORES
    # =================================================================
    
    c.setFont('Helvetica-Bold', 16)
    c.setFillColor(black)
    c.drawString(50, y_atual, "TESTE DE CORES:")
    y_atual -= 30
    
    cores_teste = [
        (Color(0.8, 0, 0, 1), 'Vermelho CBMAC (institucional)'),
        (Color(0, 0.2, 0.8, 1), 'Azul CBMAC (institucional)'),
        (Color(0.8, 0.7, 0, 1), 'Dourado (para medalhas)'),
        (Color(0, 0.6, 0.2, 1), 'Verde (para diplomas ambientais)'),
        (Color(0.3, 0.3, 0.3, 1), 'Cinza escuro (para assinaturas)'),
        (black, 'Preto (padrão)')
    ]
    
    c.setFont('Helvetica', 12)
    for cor, descricao in cores_teste:
        c.setFillColor(cor)
        c.drawString(70, y_atual, descricao)
        y_atual -= 20
    
    y_atual -= 20
    
    # =================================================================
    # TESTE 3: ALINHAMENTOS
    # =================================================================
    
    c.setFillColor(black)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(50, y_atual, "TESTE DE ALINHAMENTOS:")
    y_atual -= 30
    
    # Texto à esquerda
    c.setFont('Helvetica', 12)
    c.drawString(50, y_atual, "← Texto alinhado à esquerda")
    y_atual -= 20
    
    # Texto centralizado
    texto_centro = "Texto centralizado"
    largura_texto = c.stringWidth(texto_centro, 'Helvetica', 12)
    x_centro = (largura_pagina - largura_texto) / 2
    c.drawString(x_centro, y_atual, texto_centro)
    y_atual -= 20
    
    # Texto à direita
    texto_direita = "Texto alinhado à direita →"
    largura_texto = c.stringWidth(texto_direita, 'Helvetica', 12)
    x_direita = largura_pagina - 50 - largura_texto
    c.drawString(x_direita, y_atual, texto_direita)
    y_atual -= 40
    
    # =================================================================
    # TESTE 4: QUEBRA DE TEXTO
    # =================================================================
    
    c.setFont('Helvetica-Bold', 16)
    c.drawString(50, y_atual, "TESTE DE QUEBRA DE TEXTO:")
    y_atual -= 30
    
    # Função de quebra de texto (copiada do guia principal)
    def quebrar_texto_teste(canvas, texto, x, y, largura_maxima, altura_linha=18):
        palavras = texto.split()
        linha_atual = ""
        y_atual = y
        
        for palavra in palavras:
            linha_teste = linha_atual + " " + palavra if linha_atual else palavra
            largura_linha = canvas.stringWidth(linha_teste, canvas._fontname, canvas._fontsize)
            
            if largura_linha <= largura_maxima:
                linha_atual = linha_teste
            else:
                if linha_atual:
                    canvas.drawString(x, y_atual, linha_atual)
                    y_atual -= altura_linha
                linha_atual = palavra
        
        if linha_atual:
            canvas.drawString(x, y_atual, linha_atual)
        
        return y_atual
    
    # Texto longo para testar quebra
    texto_longo = ("O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, "
                   "usando das atribuições que lhe compete por meio do Decreto N° 123/2024, "
                   "confere ao Senhor João da Silva este certificado pelos relevantes serviços "
                   "prestados à comunidade acreana e ao Corpo de Bombeiros Militar.")
    
    c.setFont('Helvetica', 12)
    y_final = quebrar_texto_teste(c, texto_longo, 50, y_atual, 495, 18)
    y_atual = y_final - 30
    
    # =================================================================
    # TESTE 5: EXEMPLO DE ASSINATURA
    # =================================================================
    
    c.setFont('Helvetica-Bold', 16)
    c.drawString(50, y_atual, "EXEMPLO DE ÁREA DE ASSINATURA:")
    y_atual -= 50
    
    # Data e local (à direita)
    c.setFont('Helvetica', 11)
    c.setFillColor(Color(0.3, 0.3, 0.3, 1))
    data_local = "Rio Branco - Acre, 15 de outubro de 2024"
    largura_data = c.stringWidth(data_local, 'Helvetica', 11)
    x_data = largura_pagina - 50 - largura_data
    c.drawString(x_data, y_atual, data_local)
    y_atual -= 40
    
    # Nome do comandante (à direita)
    c.setFont('Helvetica', 12)
    comandante = "Cel. José Santos da Silva"
    largura_comandante = c.stringWidth(comandante, 'Helvetica', 12)
    x_comandante = largura_pagina - 50 - largura_comandante
    c.drawString(x_comandante, y_atual, comandante)
    
    # Linha de assinatura
    linha_inicio = x_comandante - 20
    linha_fim = largura_pagina - 30
    c.line(linha_inicio, y_atual - 3, linha_fim, y_atual - 3)
    y_atual -= 20
    
    # Cargo
    c.setFont('Helvetica', 10)
    cargo = "Comandante Geral do CBMAC"
    largura_cargo = c.stringWidth(cargo, 'Helvetica', 10)
    x_cargo = largura_pagina - 50 - largura_cargo
    c.drawString(x_cargo, y_atual, cargo)
    
    # Finalizar e salvar
    c.showPage()
    c.save()
    
    return pdf_path

def executar_teste():
    """Executa o teste e mostra o resultado"""
    try:
        pdf_gerado = teste_configuracoes_basicas()
        print(f"✅ Teste executado com sucesso!")
        print(f"📄 PDF de teste criado em: {pdf_gerado}")
        print(f"🔍 Abra o arquivo para ver os diferentes estilos de texto")
        print(f"📝 Use este PDF como referência para suas configurações")
        return True
    except Exception as e:
        print(f"❌ Erro ao executar teste: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DE CONFIGURAÇÕES DE TEXTO - CBMAC")
    print("=" * 50)
    executar_teste()