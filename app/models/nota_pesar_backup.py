"""
BACKUP DO MODELO NOTA DE PESAR - Versão anterior
===============================================

Este é um backup da versão anterior do modelo de nota de pesar.
Criado em: 15/10/2025
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .utils import find_model_image


def gerar_certificado_nota_pesar_backup(dados: dict) -> str:
    """
    Gera uma nota de pesar oficial em formato PDF
    
    Args:
        dados (dict): Dados do formulário contendo:
            - falecido_nota_pesar: Nome da pessoa falecida
            - parentesco_nota_pesar: Relação com o bombeiro/servidor
            - pessoa_enlutada_nota_pesar: Nome do enlutado (bombeiro/servidor)
            - local_nota_pesar: Local de expedição da nota
            - data_nota_pesar: Data de expedição
            - comandante_nota_pesar: Nome do comandante geral
    
    Returns:
        str: Caminho absoluto para o arquivo PDF gerado
        
    Raises:
        FileNotFoundError: Se o template não for encontrado
    """
    # Localizar template padrão de nota de pesar
    imagem = find_model_image('Nota de Pesar')
    if imagem is None:
        raise FileNotFoundError('Modelo de Nota de Pesar não encontrado')

    img_reader = ImageReader(imagem)
    iw, ih = img_reader.getSize()

    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    out_path = os.path.join(uploads_dir, 'NotaDePesar_backup.pdf')

    c = canvas.Canvas(out_path, pagesize=(iw, ih))
    c.drawImage(img_reader, 0, 0, width=iw, height=ih)

    # =================================================================
    # CONFIGURAÇÕES PERSONALIZÁVEIS DE TEXTO
    # =================================================================
    
    # 1. CONFIGURAÇÕES DE FONTE E COR
    fonte_titulo = 'Helvetica-Bold'
    tamanho_titulo = 30
    fonte_corpo = 'Helvetica'
    tamanho_corpo = 24
    fonte_assinatura = 'Helvetica'
    tamanho_assinatura = 22
    
    # Cores (valores RGB de 0 a 1)
    from reportlab.lib.colors import Color, black
    cor_titulo = Color(0.8, 0, 0, 1)    # Vermelho institucional
    cor_corpo = black                    # Preto
    cor_assinatura = Color(0.3, 0.3, 0.3, 1)    # Cinza escuro
    
    # 2. CONFIGURAÇÕES DE POSICIONAMENTO
    margem_esquerda = int(iw * 0.15)     # 15% da largura como margem esquerda
    margem_direita = int(iw * 0.15)      # 15% da largura como margem direita
    largura_texto = iw - margem_esquerda - margem_direita  # Largura útil para texto
    centro_x = iw // 2                   # Centro horizontal da página
    
    # Posições Y (de cima para baixo)
    y_titulo = int(ih * 0.75)            # 75% da altura - posição do título
    y_corpo = int(ih * 0.60)             # 60% da altura - corpo principal
    y_local_data = int(ih * 0.30)        # 30% da altura - local e data  
    y_comandante = int(ih * 0.25)        # 25% da altura - nome do comandante
    y_cargo = int(ih * 0.22)             # 22% da altura - cargo do comandante
    
    # 3. CONFIGURAÇÃO DE ESPAÇAMENTO ENTRE LINHAS
    espacamento_linha = 40               # Espaçamento entre linhas de texto
    
    # 4. FUNÇÃO PARA QUEBRA DE TEXTO CENTRALIZADO
    def quebrar_texto_centralizado(canvas, texto, y_inicial, largura_max, altura_linha=espacamento_linha):
        """Quebra texto em múltiplas linhas centralizadas"""
        palavras = texto.split()
        linhas = []
        linha_atual = ""
        
        # Primeiro, criar as linhas
        for palavra in palavras:
            linha_teste = linha_atual + " " + palavra if linha_atual else palavra
            largura_linha = canvas.stringWidth(linha_teste, canvas._fontname, canvas._fontsize)
            
            if largura_linha <= largura_max:
                linha_atual = linha_teste
            else:
                if linha_atual:
                    linhas.append(linha_atual)
                linha_atual = palavra
        
        if linha_atual:
            linhas.append(linha_atual)
        
        # Agora desenhar as linhas centralizadas
        y_atual = y_inicial
        for linha in linhas:
            largura_linha = canvas.stringWidth(linha, canvas._fontname, canvas._fontsize)
            x_centralizado = centro_x - (largura_linha / 2)
            canvas.drawString(x_centralizado, y_atual, linha)
            y_atual -= altura_linha
        
        return y_atual
    
    # 5. CORPO PRINCIPAL DO TEXTO
    c.setFont(fonte_corpo, tamanho_corpo)
    c.setFillColor(cor_corpo)
    
    texto_principal = (
        f'O Corpo de Bombeiros Militar do Estado do Acre, através do Comandante-Geral, '
        f'lamenta o falecimento de {dados.get("falecido","")}, {dados.get("parentesco","")} '
        f'do {dados.get("pessoa_enlutada","")}. A corporação presta suas sinceras '
        f'condolências aos familiares e amigos por tão grande perda.'
    )
    
    # Desenhar texto com quebra automática centralizada
    y_final = quebrar_texto_centralizado(c, texto_principal, y_corpo, largura_texto)
    
    # 6. LOCAL E DATA (CENTRALIZADO)
    c.setFont(fonte_assinatura, tamanho_assinatura - 2)
    c.setFillColor(cor_assinatura)
    
    local_data = f'{dados.get("local","Rio Branco")} - Acre, {dados.get("data","")}'
    # Centralizar o local e data
    largura_local_data = c.stringWidth(local_data, fonte_assinatura, tamanho_assinatura - 2)
    x_local_data = centro_x - (largura_local_data / 2)
    c.drawString(x_local_data, y_local_data, local_data)
    
    # 7. ASSINATURA DO COMANDANTE (CENTRALIZADA)
    c.setFont(fonte_assinatura, tamanho_assinatura)
    
    comandante = dados.get('comandante', '')
    largura_comandante = c.stringWidth(comandante, fonte_assinatura, tamanho_assinatura)
    x_comandante = centro_x - (largura_comandante / 2)
    c.drawString(x_comandante, y_comandante, comandante)
    
    # 8. CARGO DO COMANDANTE (CENTRALIZADO)
    c.setFont(fonte_assinatura, tamanho_assinatura - 2)
    cargo = "Comandante Geral do CBMAC"
    largura_cargo = c.stringWidth(cargo, fonte_assinatura, tamanho_assinatura - 2)
    x_cargo = centro_x - (largura_cargo / 2)
    c.drawString(x_cargo, y_cargo, cargo)

    c.showPage()
    c.save()

    return out_path