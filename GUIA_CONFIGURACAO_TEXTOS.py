"""
GUIA DE CONFIGURAÇÃO DE TEXTOS - CBMAC
=====================================

Este arquivo mostra todas as opções disponíveis para configurar:
- Posição do texto (coordenadas X, Y)
- Limitação de texto (quebra de linha, largura máxima)
- Cor do texto (RGB, CMYK)
- Fonte e tamanho
- Alinhamento e espaçamento
- Efeitos especiais (sombra, contorno)

EXEMPLO COMPLETO DE CONFIGURAÇÕES
"""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, red, blue, green, white, Color
from reportlab.lib.units import cm, mm, inch
from reportlab.pdfbase import pdfutils
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfutils
import textwrap

def exemplo_configuracoes_completas(c, iw, ih, dados):
    """
    Exemplo completo de todas as configurações de texto disponíveis
    
    Args:
        c: Canvas do ReportLab
        iw: Largura da imagem/página
        ih: Altura da imagem/página
        dados: Dados do formulário
    """
    
    # =================================================================
    # 1. CONFIGURAÇÕES DE FONTE
    # =================================================================
    
    # Fontes padrão disponíveis
    fontes_padrao = [
        'Helvetica',           # Sans-serif padrão
        'Helvetica-Bold',      # Negrito
        'Helvetica-Oblique',   # Itálico
        'Helvetica-BoldOblique', # Negrito + Itálico
        'Times-Roman',         # Serif padrão
        'Times-Bold',
        'Times-Italic',
        'Times-BoldItalic',
        'Courier',             # Monospace
        'Courier-Bold',
        'Courier-Oblique',
        'Courier-BoldOblique'
    ]
    
    # Definir fonte e tamanho
    c.setFont('Helvetica-Bold', 18)  # Fonte e tamanho
    
    # =================================================================
    # 2. CONFIGURAÇÕES DE COR
    # =================================================================
    
    # Cores RGB (valores de 0 a 1)
    c.setFillColor(Color(0, 0, 0, 1))      # Preto
    c.setFillColor(Color(1, 0, 0, 1))      # Vermelho
    c.setFillColor(Color(0, 0, 1, 1))      # Azul
    c.setFillColor(Color(0.5, 0.5, 0.5, 1)) # Cinza
    
    # Cores predefinidas
    c.setFillColor(black)
    c.setFillColor(red)
    c.setFillColor(blue)
    
    # Cor CMYK (para impressão profissional)
    c.setFillColorCMYK(0, 0, 0, 1)  # Preto CMYK
    
    # =================================================================
    # 3. POSICIONAMENTO
    # =================================================================
    
    # Coordenadas absolutas (0,0 = canto inferior esquerdo)
    x = 100  # pixels da esquerda
    y = 500  # pixels de baixo
    
    # Posicionamento relativo ao tamanho da página
    x_centro = iw / 2           # Centro horizontal
    y_centro = ih / 2           # Centro vertical
    margem_esquerda = iw * 0.1  # 10% da largura como margem
    margem_superior = ih * 0.9  # 90% da altura (próximo ao topo)
    
    # Posicionamento com unidades
    x_cm = 5 * cm      # 5 centímetros
    y_mm = 200 * mm    # 200 milímetros
    x_inch = 2 * inch  # 2 polegadas
    
    # =================================================================
    # 4. TEXTO SIMPLES
    # =================================================================
    
    # Texto simples em posição específica
    c.drawString(100, 700, "Texto simples")
    
    # Texto centralizado
    texto = "Texto Centralizado"
    largura_texto = c.stringWidth(texto, 'Helvetica', 14)
    x_centralizado = (iw - largura_texto) / 2
    c.drawString(x_centralizado, 650, texto)
    
    # Texto alinhado à direita
    texto_direita = "Alinhado à direita"
    largura = c.stringWidth(texto_direita, 'Helvetica', 12)
    x_direita = iw - largura - 50  # 50px de margem
    c.drawString(x_direita, 600, texto_direita)
    
    # =================================================================
    # 5. TEXTO COM QUEBRA DE LINHA MANUAL
    # =================================================================
    
    def desenhar_texto_quebrado(canvas, texto, x, y, largura_maxima, altura_linha=20):
        """
        Quebra texto manualmente em múltiplas linhas
        """
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
        
        return y_atual  # Retorna Y final para continuar texto abaixo
    
    # Usar quebra manual
    texto_longo = "Este é um texto muito longo que precisa ser quebrado em múltiplas linhas para caber adequadamente no documento sem sair das margens estabelecidas."
    c.setFont('Helvetica', 12)
    y_final = desenhar_texto_quebrado(c, texto_longo, 100, 550, 400)
    
    # =================================================================
    # 6. TEXTO AVANÇADO COM PARAGRAPH (Melhor opção)
    # =================================================================
    
    # Criar estilo personalizado
    styles = getSampleStyleSheet()
    estilo_personalizado = ParagraphStyle(
        'CustomStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,           # Espaçamento entre linhas
        alignment=TA_CENTER,  # Alinhamento (TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY)
        textColor=black,
        spaceAfter=10,
        leftIndent=20,
        rightIndent=20,
        firstLineIndent=0,
        wordWrap='CJK',       # Quebra de palavra
    )
    
    # Texto com formatação HTML básica
    texto_formatado = """
    <b>Texto em Negrito</b><br/>
    <i>Texto em Itálico</i><br/>
    <font color="red">Texto em Vermelho</font><br/>
    <font size="16">Texto Maior</font><br/>
    Texto normal com quebra automática de linha que será processada 
    automaticamente pelo sistema de parágrafo do ReportLab.
    """
    
    # Criar parágrafo
    paragrafo = Paragraph(texto_formatado, estilo_personalizado)
    
    # Criar frame (área de texto) e renderizar
    frame = Frame(50, 200, 400, 200, showBoundary=0)  # x, y, largura, altura
    frame.addFromList([paragrafo], c)
    
    # =================================================================
    # 7. CONFIGURAÇÕES ESPECÍFICAS PARA CERTIFICADOS
    # =================================================================
    
    def configurar_texto_titulo(canvas, iw, ih):
        """Configuração específica para títulos de certificados"""
        canvas.setFont('Helvetica-Bold', 24)
        canvas.setFillColor(Color(0.8, 0, 0, 1))  # Vermelho institucional
        
        titulo = "CORPO DE BOMBEIROS MILITAR DO ACRE"
        largura = canvas.stringWidth(titulo, 'Helvetica-Bold', 24)
        x = (iw - largura) / 2
        y = ih * 0.85  # 85% da altura
        
        canvas.drawString(x, y, titulo)
        return y - 40  # Retorna posição para próximo texto
    
    def configurar_texto_corpo(canvas, dados, x_inicial, y_inicial, largura_maxima):
        """Configuração para o corpo principal do texto"""
        canvas.setFont('Helvetica', 14)
        canvas.setFillColor(black)
        
        texto = f"""
        O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, 
        usando das atribuições que lhe compete por meio do Decreto N° {dados.get('decreto', '')}, 
        confere ao(à) Senhor(a) {dados.get('nome', '')}, o presente certificado pelos 
        relevantes serviços prestados à comunidade acreana.
        """
        
        # Limpar texto
        texto = ' '.join(texto.split())
        
        return desenhar_texto_quebrado(canvas, texto, x_inicial, y_inicial, largura_maxima, 20)
    
    def configurar_assinatura(canvas, dados, iw, y_base):
        """Configuração para área de assinatura"""
        canvas.setFont('Helvetica', 12)
        canvas.setFillColor(black)
        
        # Data e local
        data_local = f"{dados.get('local', 'Rio Branco')} - Acre, {dados.get('data', '')}"
        x_data = iw * 0.6
        canvas.drawString(x_data, y_base, data_local)
        
        # Nome do comandante
        y_comandante = y_base - 60
        comandante = dados.get('comandante', '')
        x_comandante = iw * 0.6
        canvas.drawString(x_comandante, y_comandante, comandante)
        
        # Linha para assinatura
        canvas.line(x_comandante, y_comandante - 5, x_comandante + 200, y_comandante - 5)
        
        # Cargo
        y_cargo = y_comandante - 20
        canvas.setFont('Helvetica', 10)
        canvas.drawString(x_comandante, y_cargo, "Comandante Geral do CBMAC")
    
    # =================================================================
    # 8. EXEMPLO DE USO COMPLETO
    # =================================================================
    
    # Aplicar configurações
    y_atual = configurar_texto_titulo(c, iw, ih)
    y_atual = configurar_texto_corpo(c, dados, iw * 0.1, y_atual, iw * 0.8)
    configurar_assinatura(c, dados, iw, y_atual - 50)

# =================================================================
# EXEMPLO DE IMPLEMENTAÇÃO EM DIPLOMA.PY
# =================================================================

def exemplo_diploma_completo(dados, template_path, output_path):
    """
    Exemplo de como implementar todas essas configurações em um diploma
    
    Args:
        dados: Dicionário com dados do formulário
        template_path: Caminho para a imagem de fundo do diploma
        output_path: Caminho onde salvar o PDF gerado
    """
    from reportlab.lib.utils import ImageReader
    import os
    
    # Carregar imagem de fundo e obter dimensões
    img_reader = ImageReader(template_path)
    iw, ih = img_reader.getSize()
    
    # Criar diretório se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Criar canvas e desenhar fundo
    c = canvas.Canvas(output_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)
    
    # Aplicar todas as configurações
    exemplo_configuracoes_completas(c, iw, ih, dados)
    
    c.showPage()
    c.save()
    
    return output_path

# =================================================================
# EXEMPLO DE USO PRÁTICO
# =================================================================

def exemplo_uso_pratico():
    """
    Exemplo de como usar este guia na prática
    """
    # Dados de exemplo
    dados_teste = {
        'nome': 'João Silva',
        'decreto': '123/2024',
        'local': 'Rio Branco',
        'data': '15 de outubro de 2024',
        'comandante': 'Cel. José Santos'
    }
    
    # Caminhos de exemplo (ajuste conforme sua estrutura)
    template_path = 'app/static/Certificado/Diplomas/template.png'
    output_path = 'uploads/diploma_exemplo.pdf'
    
    # Gerar documento (descomente para usar)
    # resultado = exemplo_diploma_completo(dados_teste, template_path, output_path)
    # print(f"Diploma gerado em: {resultado}")
    
    print("Para usar este exemplo:")
    print("1. Ajuste os caminhos template_path e output_path")
    print("2. Descomente a linha exemplo_diploma_completo")
    print("3. Execute o script")

# =================================================================
# COORDENADAS DE REFERÊNCIA
# =================================================================
"""
SISTEMA DE COORDENADAS DO REPORTLAB:
- Origem (0,0) = Canto inferior esquerdo
- X cresce para a direita
- Y cresce para cima
- Unidades padrão: pontos (1 ponto = 1/72 polegada)

CONVERSÕES ÚTEIS:
- 1 cm = 28.35 pontos
- 1 mm = 2.835 pontos  
- 1 inch = 72 pontos

POSIÇÕES TÍPICAS PARA CERTIFICADOS:
- Título: Y = 85% da altura
- Subtítulo: Y = 75% da altura
- Corpo do texto: Y = 40-60% da altura
- Assinatura: Y = 15-25% da altura
- Margens laterais: 8-15% da largura
"""