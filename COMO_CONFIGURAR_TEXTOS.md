# RESUMO PRÁTICO - ONDE CONFIGURAR CADA ASPECTO DOS TEXTOS

## 📍 **LOCALIZAÇÃO DOS ARQUIVOS DE CONFIGURAÇÃO**

### **Configurações Centralizadas:**
- **`config_documentos.py`** - Configurações visuais principais
- **`GUIA_CONFIGURACAO_TEXTOS.py`** - Exemplos e referência técnica

### **Implementação nos Documentos:**
- **`app/models/diploma.py`** - Lógica específica dos diplomas
- **`app/models/medalha.py`** - Lógica específica das medalhas
- **`app/models/certificado.py`** - Lógica específica dos certificados
- **`app/models/convite.py`** - Lógica específica dos convites
- **`app/models/nota_pesar.py`** - Lógica específica das notas de pesar
- **`app/models/agradecimento.py`** - Lógica específica dos agradecimentos

---

## 🎨 **GUIA RÁPIDO DE CONFIGURAÇÕES**

### **1. MUDAR COR DO TEXTO**
```python
# Em config_documentos.py - Linha 38
CORES = {
    'vermelho_cbmac': Color(0.8, 0, 0, 1),    # ← MUDE AQUI
    'azul_cbmac': Color(0, 0.2, 0.8, 1),      # ← OU AQUI
}

# No arquivo do documento (ex: diploma.py) - Linha 75
c.setFillColor(cor_corpo)  # ← Aplica a cor
```

### **2. MUDAR FONTE E TAMANHO**
```python
# Em config_documentos.py - Linha 18
FONTES = {
    'titulo': {
        'nome': 'Helvetica-Bold',  # ← MUDE A FONTE
        'tamanho': 16              # ← MUDE O TAMANHO
    },
}

# No arquivo do documento - Linha 67
c.setFont(fonte_corpo, tamanho_corpo)  # ← Aplica fonte e tamanho
```

### **3. MUDAR POSIÇÃO DO TEXTO**
```python
# Em config_documentos.py - Linha 58
POSICOES = {
    'titulo': 0.85,           # ← 85% da altura (mude aqui)
    'corpo_principal': 0.60,  # ← 60% da altura (mude aqui)
    'comandante': 0.25,       # ← 25% da altura (mude aqui)
}

# No arquivo do documento - Linha 81
y_titulo = int(ih * 0.75)  # ← Use: int(ih * POSICOES['titulo'])
```

### **4. MUDAR MARGENS E LARGURA**
```python
# No arquivo do documento - Linha 78-80
margem_esquerda = int(iw * 0.08)     # ← 8% = mude para 0.10 (10%) 
margem_direita = int(iw * 0.08)      # ← 8% = mude para 0.10 (10%)
largura_texto = iw - margem_esquerda - margem_direita
```

### **5. MUDAR ALINHAMENTO**
```python
# Texto à esquerda (padrão)
c.drawString(margem_esquerda, y, texto)

# Texto centralizado
largura_texto = c.stringWidth(texto, fonte, tamanho)
x_centro = (iw - largura_texto) / 2
c.drawString(x_centro, y, texto)

# Texto à direita  
largura_texto = c.stringWidth(texto, fonte, tamanho)
x_direita = iw - margem_direita - largura_texto
c.drawString(x_direita, y, texto)
```

### **6. QUEBRA DE TEXTO EM LINHAS**
```python
# No arquivo do documento - Função na linha 87
def quebrar_texto(canvas, texto, x, y, largura_max, altura_linha=18):
    # altura_linha=18 ← MUDE o espaçamento entre linhas
    # largura_max ← MUDE a largura máxima antes de quebrar
```

---

## ⚡ **MUDANÇAS MAIS COMUNS**

### **Diploma com texto maior e mais centralizado:**
```python
# Em diploma.py - linha 67-69
tamanho_corpo = 14        # Era 12
y_corpo = int(ih * 0.50)  # Era 0.55 (mova mais para baixo)

# Para centralizar o corpo do texto:
largura_texto_corpo = c.stringWidth(texto_principal, fonte_corpo, tamanho_corpo)
if largura_texto_corpo <= largura_texto:  # Se cabe em uma linha
    x_centro = (iw - largura_texto_corpo) / 2
    c.drawString(x_centro, y_corpo, texto_principal)
```

### **Medalha com cor dourada:**
```python
# Em config_documentos.py - adicione na linha 41
'dourado': Color(0.8, 0.7, 0, 1),

# Em medalha.py - use:
c.setFillColor(obter_cor('dourado'))
```

### **Assinatura com linha mais grossa:**
```python
# No arquivo do documento - linha da assinatura
c.setLineWidth(2)  # ← Linha mais grossa (padrão é 1)
c.line(linha_inicio, y_comandante - 3, linha_fim, y_comandante - 3)
```

---

## 🔧 **COORDENADAS DE REFERÊNCIA**

```
SISTEMA DE COORDENADAS:
┌─────────────────────── (iw, ih) ← Canto superior direito
│                               │
│        Y cresce ↑             │
│                               │  
│                               │
│    ← X cresce →               │
│                               │
│                               │
(0,0) ─────────────────────────────┘
↑ Canto inferior esquerdo

POSIÇÕES TÍPICAS:
- Título: Y = 80-90% da altura
- Corpo: Y = 50-70% da altura  
- Assinatura: Y = 20-30% da altura
- Margens: X = 8-15% da largura
```

---

## 🎯 **EXEMPLO PRÁTICO DE PERSONALIZAÇÃO**

Para fazer um diploma com:
- Título vermelho, maior e mais alto
- Corpo azul, menor e centralizado  
- Assinatura verde à esquerda

```python
# 1. Em config_documentos.py - adicione cores
'vermelho_titulo': Color(0.9, 0, 0, 1),
'azul_corpo': Color(0, 0, 0.8, 1), 
'verde_assinatura': Color(0, 0.7, 0, 1),

# 2. Em diploma.py - modifique:
# Título
c.setFont('Helvetica-Bold', 20)  # Maior
c.setFillColor(Color(0.9, 0, 0, 1))  # Vermelho
y_titulo = int(ih * 0.90)  # Mais alto

# Corpo
c.setFont('Helvetica', 10)  # Menor  
c.setFillColor(Color(0, 0, 0.8, 1))  # Azul
# Centralizar texto...

# Assinatura
c.setFillColor(Color(0, 0.7, 0, 1))  # Verde
c.drawString(margem_esquerda, y_comandante, comandante)  # À esquerda
```

---

## 📝 **DICA IMPORTANTE**

Depois de fazer mudanças, teste sempre:

1. **Inicie o servidor:** `python app.py`
2. **Abra:** http://127.0.0.1:5000
3. **Gere um documento** para ver o resultado
4. **Ajuste** as configurações se necessário

**Principais arquivos para editar:**
- **Posições e cores gerais:** `config_documentos.py` 
- **Lógica específica:** `app/models/[tipo].py`