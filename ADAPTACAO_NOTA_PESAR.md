# Adaptação do Modelo Nota de Pesar - Resumo das Alterações

## 📅 Data: 15/10/2025

## 🔄 Alterações Realizadas

### 1. **Backup Criado**
- ✅ Arquivo `nota_pesar_backup.py` criado com a versão anterior
- ✅ Função backup: `gerar_certificado_nota_pesar_backup()`

### 2. **Novas Configurações Implementadas**

#### **Parâmetros Ajustáveis:**
```python
# Margens
MARGEM_ESQ   = 25 * mm
MARGEM_DIR   = 25 * mm
MARGEM_SUP   = 25 * mm
MARGEM_INF   = 25 * mm

# Tamanhos de fonte
FONTE_TITULO    = 18
FONTE_CORPO     = 14
FONTE_LOCALDATA = 12
FONTE_ASSINAT   = 12
FONTE_CARGO     = 11
FONTE_RODAPE    = 10

# Espaçamentos
LEADING_CORPO     = 18   # espaçamento entre linhas do parágrafo
ESPACO_APOS_CORPO = 10   # espaço após o corpo até a data/local
ESPACO_ENTRE_LINHAS_ASSINAT = 4

# Altura do bloco de texto
ALTURA_BLOCO_CORPO = 130 * mm
```

### 3. **Nova Estrutura de Layout**

#### **Elementos Centralizados:**
- ✅ **Título**: "NOTA DE PESAR" (Times-Bold, 18pt)
- ✅ **Corpo do texto**: Frame justificado com quebra automática
- ✅ **Local e data**: Centralizado abaixo do corpo
- ✅ **Nome do comandante**: Centralizado (Times-Bold, 12pt)
- ✅ **Cargo**: "Comandante-Geral" centralizado (Times-Roman, 11pt)
- ✅ **Rodapé**: "ASSESSORIA DE COMUNICAÇÃO" (Times-Roman, 10pt)

### 4. **Melhorias Técnicas**

#### **Novo Sistema de Frames:**
- ✅ Utiliza `Frame` do ReportLab para controle preciso do texto
- ✅ `ParagraphStyle` com justificação e espaçamento controlado
- ✅ Quebra automática de texto sem sobreposição

#### **Função Utilitária:**
```python
def draw_centered_text(canv, txt, y, size=12, font="Times-Roman"):
    canv.setFont(font, size)
    canv.drawCentredString(pw/2, y, txt)
```

### 5. **Conteúdo Dinâmico**
O texto mantém as variáveis do formulário:
- `dados.get("falecido","")` - Nome do falecido
- `dados.get("parentesco","")` - Parentesco
- `dados.get("pessoa_enlutada","")` - Pessoa enlutada
- `dados.get("local","Rio Branco")` - Local
- `dados.get("data","")` - Data
- `dados.get("comandante","")` - Nome do comandante

## 🎯 **Resultados Obtidos**

### **Layout Profissional:**
- ✅ Texto perfeitamente centralizado
- ✅ Espaçamentos consistentes e legíveis
- ✅ Quebra de linha automática sem sobreposição
- ✅ Tipografia adequada para documentos oficiais
- ✅ Estrutura hierárquica clara

### **Flexibilidade:**
- ✅ Parâmetros facilmente ajustáveis no topo do arquivo
- ✅ Sistema baseado em Frame para maior controle
- ✅ Compatibilidade mantida com o sistema existente

### **Backup de Segurança:**
- ✅ Versão anterior preservada
- ✅ Possibilidade de rollback se necessário

## 📝 **Conclusão**
O modelo de Nota de Pesar foi successfully adaptado com as configurações fornecidas, mantendo a funcionalidade original mas com melhor layout, espaçamento e profissionalismo visual.

---
*Sistema ASCOM - Gerador de Documentos CBMAC*