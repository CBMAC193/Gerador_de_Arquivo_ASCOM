# Configuração de Espaçamento e Formatação - Gerador de Documentos ASCOM

## 📝 Como Configurar o Espaçamento dos Textos

Todos os modelos de documentos foram padronizados com as seguintes configurações:

### 🎯 Configurações Atuais Aplicadas

- **Posição do corpo do texto**: `y_corpo = int(ih * 0.60)` (60% da altura)
- **Margem esquerda**: `margem_esquerda = int(iw * 0.25)` (25% da largura)  
- **Tamanho da fonte**: `tamanho_corpo = 30` pontos
- **Espaçamento entre linhas**: `espacamento_linha = 25` pontos (configurável)

### 📁 Modelos Atualizados

✅ **diploma.py** - Diplomas oficiais  
✅ **certificado.py** - Certificado Amigo dos Veteranos  
✅ **agradecimento.py** - Cartas de agradecimento  
✅ **convite.py** - Convites oficiais  
✅ **medalha.py** - Medalhas e condecorações  
✅ **moeda.py** - Moeda CBMAC  
✅ **nota_pesar.py** - Notas de pesar  

### ⚙️ Como Alterar o Espaçamento

#### Método 1: Alteração Individual (em cada modelo)
```python
# Encontre esta linha em qualquer modelo:
espacamento_linha = 25               # Espaçamento entre linhas de texto

# Altere o valor para:
espacamento_linha = 30               # Maior espaçamento
espacamento_linha = 20               # Menor espaçamento
```

#### Método 2: Configuração Centralizada (recomendado)
Edite o arquivo `app/models/config_texto.py`:

```python
# Encontre esta seção:
ESPACAMENTO_LINHA_PADRAO = 30        # Altere aqui o valor padrão
ESPACAMENTO_LINHA_CORPO = 28         # Para o corpo do texto
ESPACAMENTO_LINHA_ASSINATURA = 25    # Para assinaturas
```

### 🎨 Outras Configurações Disponíveis

#### Tamanhos de Fonte
```python
TAMANHO_TITULO = 32          # Títulos
TAMANHO_CORPO = 30           # Texto principal  
TAMANHO_ASSINATURA = 30      # Assinaturas
```

#### Posicionamento
```python
POSICAO_CORPO_PERCENT = 0.60      # 60% da altura (atual)
MARGEM_ESQUERDA_PERCENT = 0.25    # 25% da largura (atual)
```

#### Cores
```python
COR_TITULO = Color(0.8, 0, 0, 1)        # Vermelho institucional
COR_CORPO = black                        # Preto
COR_ASSINATURA = Color(0.3, 0.3, 0.3, 1)  # Cinza escuro
```

### 🔧 Configurações Específicas por Documento

Para ajustar apenas um tipo de documento, edite a seção `CONFIGURACOES_ESPECIAIS` em `config_texto.py`:

```python
CONFIGURACOES_ESPECIAIS = {
    'diploma': {
        'espacamento_linha': 35,     # Espaçamento maior para diplomas
        'tamanho_corpo': 32          # Fonte maior para diplomas
    },
    'agradecimento': {
        'espacamento_linha': 28,
        'tamanho_corpo': 28
    }
}
```

### 📏 Valores de Referência para Espaçamento

- **15-20**: Espaçamento compacto (textos longos)
- **25-30**: Espaçamento padrão (equilibrado)
- **35-40**: Espaçamento amplo (documentos formais)
- **45+**: Espaçamento muito amplo (certificados especiais)

### 🧪 Como Testar Alterações

1. Faça a alteração no arquivo desejado
2. Reinicie o servidor Flask: `Ctrl+C` e `python app.py`
3. Gere um documento de teste pelo navegador
4. Visualize o resultado e ajuste se necessário

### 💡 Dicas Importantes

- **Backup**: Sempre faça backup antes de alterar configurações
- **Consistência**: Use valores similares para manter uniformidade
- **Templates**: Teste com diferentes tipos de documentos
- **Resolução**: Considere que valores maiores podem causar sobreposição de texto

### 🎯 Configurações Recomendadas por Tipo

| Documento | Espaçamento | Fonte Corpo | Margem Esquerda |
|-----------|-------------|-------------|-----------------|
| Diploma | 30-35 | 30-32 | 25% |
| Certificado | 25-30 | 30 | 25% |
| Medalha | 25-28 | 30 | 25% |
| Agradecimento | 28-32 | 28-30 | 25% |
| Convite | 22-25 | 28-30 | 25% |
| Nota de Pesar | 30-35 | 30 | 25% |

### 🚀 Implementação Completa

Todos os modelos agora incluem:
- ✅ Função `quebrar_texto()` para quebra automática
- ✅ Configurações padronizadas de posicionamento  
- ✅ Sistema de cores institucionais
- ✅ Espaçamento configurável entre linhas
- ✅ Margens e fontes padronizadas