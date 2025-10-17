# 🎯 RESUMO SIMPLES - CONFIGURAÇÃO DE TEXTOS CBMAC

## 📍 **ONDE CONFIGURAR CADA ASPECTO**

### **1. POSIÇÃO DO TEXTO**
```python
# No arquivo: app/models/diploma.py (ou medalha.py, etc.)
# Linhas 81-86

y_titulo = int(ih * 0.75)      # 75% da altura (mude o 0.75)
y_corpo = int(ih * 0.55)       # 55% da altura (mude o 0.55)  
y_comandante = int(ih * 0.25)  # 25% da altura (mude o 0.25)

margem_esquerda = int(iw * 0.08)  # 8% da largura (mude o 0.08)
margem_direita = int(iw * 0.08)   # 8% da largura (mude o 0.08)
```

### **2. COR DO TEXTO**
```python
# No arquivo: app/models/diploma.py
# Linhas 70-72

cor_titulo = Color(0.8, 0, 0, 1)      # Vermelho (mude os números)
cor_corpo = black                      # Preto (mude para Color(r,g,b,1))
cor_assinatura = Color(0.3, 0.3, 0.3, 1)  # Cinza (mude os números)

# Valores RGB: 0 = nada, 1 = máximo
# Color(1,0,0,1) = vermelho puro
# Color(0,1,0,1) = verde puro  
# Color(0,0,1,1) = azul puro
```

### **3. FONTE E TAMANHO**
```python
# No arquivo: app/models/diploma.py
# Linhas 64-69

fonte_titulo = 'Helvetica-Bold'    # Mude para 'Times-Bold', etc.
tamanho_titulo = 16               # Mude o número

fonte_corpo = 'Helvetica'         # Mude a fonte
tamanho_corpo = 12               # Mude o tamanho

fonte_assinatura = 'Helvetica'    # Mude a fonte
tamanho_assinatura = 10          # Mude o tamanho
```

### **4. LIMITAÇÃO E QUEBRA DE TEXTO**
```python
# No arquivo: app/models/diploma.py  
# Função quebrar_texto (linha 87)

largura_texto = iw - margem_esquerda - margem_direita  # Largura máxima
altura_linha=18  # Espaçamento entre linhas (mude o número)
```

### **5. ALINHAMENTO**
```python
# ESQUERDA (padrão)
c.drawString(margem_esquerda, y, texto)

# CENTRO
largura_texto = c.stringWidth(texto, fonte, tamanho)
x_centro = (iw - largura_texto) / 2
c.drawString(x_centro, y, texto)

# DIREITA
largura_texto = c.stringWidth(texto, fonte, tamanho)
x_direita = iw - margem_direita - largura_texto
c.drawString(x_direita, y, texto)
```

## 📝 **ARQUIVOS PRINCIPAIS**

- **`app/models/diploma.py`** - Configurações dos diplomas
- **`app/models/medalha.py`** - Configurações das medalhas  
- **`app/models/certificado.py`** - Configurações dos certificados
- **`app/models/convite.py`** - Configurações dos convites
- **`app/models/nota_pesar.py`** - Configurações das notas de pesar
- **`app/models/agradecimento.py`** - Configurações dos agradecimentos

## 🎨 **CORES INSTITUCIONAIS CBMAC**

```python
# Cores prontas para usar
Color(0.8, 0, 0, 1)      # Vermelho CBMAC
Color(0, 0.2, 0.8, 1)    # Azul CBMAC
Color(0.8, 0.7, 0, 1)    # Dourado (medalhas)
Color(0, 0.6, 0.2, 1)    # Verde (meio ambiente)
Color(0.3, 0.3, 0.3, 1)  # Cinza escuro
```

## 📏 **POSIÇÕES TÍPICAS** 

```python
# Para uma página de altura 'ih':
ih * 0.90  # 90% = bem no topo
ih * 0.75  # 75% = título principal
ih * 0.55  # 55% = corpo do texto
ih * 0.25  # 25% = área de assinatura  
ih * 0.10  # 10% = rodapé

# Para uma página de largura 'iw':
iw * 0.08  # 8% = margem padrão
iw * 0.50  # 50% = centro da página
iw * 0.92  # 92% = próximo à direita
```

## ⚡ **MUDANÇA RÁPIDA**

**Para mudar TUDO de um diploma:**
1. Abra `app/models/diploma.py`
2. Encontre as linhas 64-86 (configurações)
3. Mude os valores conforme desejado
4. Salve o arquivo
5. Teste gerando um diploma

**Para testar suas configurações:**
Execute: `python teste_configuracoes_texto.py`

## 🔧 **EXEMPLO PRÁTICO**

**Diploma com texto maior, azul e mais centralizado:**

```python
# Em diploma.py, mude as linhas:

# Linha 65 - tamanho maior
tamanho_corpo = 16  # Era 12

# Linha 71 - cor azul  
cor_corpo = Color(0, 0, 0.8, 1)  # Era black

# Linha 83 - mais centralizado
y_corpo = int(ih * 0.50)  # Era 0.55
```

---

**💡 DICA:** Use o arquivo `teste_configuracoes_texto.py` para ver exemplos visuais de todas essas configurações!