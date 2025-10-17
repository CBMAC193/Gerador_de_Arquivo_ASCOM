# 🎨 GUIA DE USO DAS FONTES CUSTOMIZADAS NO SISTEMA ASCOM

## 📂 Localização das Fontes
As fontes estão localizadas em: `app/static/`

### 🔤 Fontes Disponíveis:
- **Arial Regular** (`arial.ttf`) → `Arial-Regular`
- **Arial Negrito** (`Arial Negrito.ttf`) → `Arial-Bold`
- **Arial Unicode** (`Arial Unicode Regular.TTF`) → `Arial-Unicode`
- **Freestyle Script** (`Freestyle Script Regular.TTF`) → `Freestyle-Script`
- **Monotype Corsiva** (`Monotype Corsiva Itálico.TTF`) → `Corsiva`

## 💻 Como Usar no Código

### 1. **Importar as Bibliotecas Necessárias:**
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
```

### 2. **Registrar as Fontes:**
```python
def registrar_fontes_customizadas():
    """Registra as fontes TTF customizadas para uso no ReportLab"""
    fonts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    
    fontes_disponiveis = {
        'Arial-Regular': 'arial.ttf',
        'Arial-Bold': 'Arial Negrito.ttf',
        'Arial-Unicode': 'Arial Unicode Regular.TTF',
        'Freestyle-Script': 'Freestyle Script Regular.TTF',
        'Corsiva': 'Monotype Corsiva Itálico.TTF'
    }
    
    for nome_fonte, arquivo_fonte in fontes_disponiveis.items():
        caminho_fonte = os.path.join(fonts_dir, arquivo_fonte)
        if os.path.exists(caminho_fonte):
            try:
                pdfmetrics.registerFont(TTFont(nome_fonte, caminho_fonte))
                print(f"✅ Fonte registrada: {nome_fonte}")
            except Exception as e:
                print(f"❌ Erro ao registrar fonte {nome_fonte}: {e}")

# Chamar a função no início do código
registrar_fontes_customizadas()
```

### 3. **Usar as Fontes nos Documentos:**

#### **Para Canvas (drawString):**
```python
c.setFont('Arial-Bold', 16)
c.drawString(x, y, "Texto com Arial Bold")

c.setFont('Corsiva', 14) 
c.drawString(x, y, "Texto elegante com Corsiva")

c.setFont('Freestyle-Script', 18)
c.drawString(x, y, "Texto decorativo")
```

#### **Para ParagraphStyle:**
```python
estilo = ParagraphStyle(
    "meu_estilo",
    fontName="Arial-Regular",  # Usar fonte customizada
    fontSize=12,
    leading=14,
    alignment=1  # Centralizado
)

paragrafo = Paragraph("Meu texto", estilo)
```

## 🎯 Exemplos de Uso por Tipo de Documento

### **📜 Diplomas/Certificados:**
- **Título**: `Arial-Bold` (tamanho 18-24)
- **Corpo**: `Arial-Regular` (tamanho 12-14)
- **Assinatura**: `Corsiva` (tamanho 14-16) - mais elegante

### **🏅 Medalhas:**
- **Título**: `Arial-Bold` (tamanho 16-20)
- **Texto**: `Arial-Regular` (tamanho 11-13)
- **Decorações**: `Freestyle-Script` (tamanho 14-18)

### **💌 Convites:**
- **Título**: `Freestyle-Script` (tamanho 20-24) - decorativo
- **Corpo**: `Arial-Regular` (tamanho 12-14)
- **Assinatura**: `Corsiva` (tamanho 12-14)

### **🖤 Nota de Pesar:**
- **Corpo**: `Arial-Regular` (tamanho 14) - mais legível
- **Local/Data**: `Arial-Regular` (tamanho 12)
- **Assinatura**: `Corsiva` (tamanho 12-14) - elegante e solene

## ⚙️ Configuração Recomendada

### **Variáveis de Configuração:**
```python
# Fontes principais
FONTE_CORPO_NOME = "Arial-Regular"
FONTE_TITULO_NOME = "Arial-Bold"  
FONTE_ASSINATURA_NOME = "Arial-Bold"

# Fontes especiais
FONTE_DECORATIVA_NOME = "Freestyle-Script"
FONTE_ELEGANTE_NOME = "Corsiva"
FONTE_UNICODE_NOME = "Arial-Unicode"  # Para caracteres especiais
```

## 🔧 Implementação em Outros Modelos

Para aplicar em outros modelos (diploma, medalha, etc.):

1. **Copie a função `registrar_fontes_customizadas()`**
2. **Adicione as importações necessárias**
3. **Chame a função no início do código**
4. **Configure as variáveis de fonte**
5. **Use as fontes nos elementos desejados**

## ✅ Vantagens das Fontes Customizadas

- 🎨 **Visual Profissional**: Fontes mais elegantes que Times/Helvetica
- 📱 **Consistência**: Mesma aparência em qualquer sistema
- 🌍 **Unicode**: Suporte a caracteres especiais
- 🎭 **Versatilidade**: Diferentes estilos para diferentes documentos
- 💼 **Institucional**: Pode usar fontes da marca CBMAC

---
**💡 Dica**: Teste as fontes em um documento pequeno primeiro para ver como ficam antes de aplicar em todos os modelos!

*Sistema ASCOM - Fontes Customizadas CBMAC* 🚒