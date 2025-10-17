# Funcionalidade de Gênero no Convite

## Resumo
Implementação de uma caixa de seleção no formulário de convite para escolher entre "Senhor" e "Senhora", alterando dinamicamente o texto do convite conforme a seleção.

## Alterações Implementadas

### 1. Template HTML (templates/index.html)

#### Novo Campo no Formulário de Convite
```javascript
{ nome: 'genero_convidado_convite', label: 'Gênero do Convidado', tipo: 'select', obrigatorio: true, tamanho: 'col-md-3', opcoes: [
    { valor: 'senhor', texto: 'Senhor' },
    { valor: 'senhora', texto: 'Senhora' }
]}
```

#### Suporte para Campos de Seleção
- Adicionado suporte para `tipo: 'select'` no gerador de campos
- Campos select são renderizados como `<select class="form-select">` com opções dinâmicas
- Validação visual incluída para campos obrigatórios

#### Ajustes de Layout
- Campo de gênero: `col-md-3`
- Campo de cargo: `col-md-5` (era `col-md-6`)
- Campo de nome: `col-md-4` (era `col-md-6`)
- Campo "pra que foi convidado": `col-md-12` para ocupar linha inteira

### 2. Backend Flask (app.py)

#### Mapeamento do Novo Campo
```python
'genero_convidado': request.form.get('genero_convidado_convite')
```

### 3. Modelo de Convite (app/models/convite.py)

#### Lógica de Gênero
```python
genero_convidado = dados.get("genero_convidado", "senhor")  # padrão para 'senhor'
artigo_genero = "o senhor" if genero_convidado == "senhor" else "a senhora"
```

#### Texto Dinâmico
```python
TEXTO_PRINCIPAL = (
    f'    O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, '
    f'<font name="Arial-Bold">{posto} {comandante}</font>, tem a honra de convidar {artigo_genero} '
    f'<font name="Arial-Unicode">{cargo_convidado}</font>, '
    f'<font name="Arial-Bold">{nome_convidado}</font>, para prestigiar '
    f'{pra_que}.'
)
```

## Como Funciona

1. **Formulário**: O usuário seleciona "Senhor" ou "Senhora" na caixa de seleção
2. **Validação**: Campo é obrigatório com indicador visual
3. **Processamento**: Backend recebe a seleção e passa para o modelo
4. **Geração**: Texto do convite é ajustado automaticamente:
   - "Senhor" → "tem a honra de convidar o senhor"
   - "Senhora" → "tem a honra de convidar a senhora"

## Resultado

- ✅ Formulário responsivo com campo de seleção
- ✅ Validação visual em tempo real
- ✅ Texto dinâmico baseado na seleção
- ✅ Layout otimizado para melhor organização
- ✅ Compatibilidade com sistema de fontes customizadas

## Exemplo de Uso

**Selecionando "Senhora":**
> O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, **Coronel João Silva**, tem a honra de convidar **a senhora** **Diretora**, **Maria Santos**, para prestigiar a cerimônia de formatura da turma de bombeiros.

**Selecionando "Senhor":**
> O Comandante Geral do Corpo de Bombeiros Militar do Estado do Acre, **Coronel João Silva**, tem a honra de convidar **o senhor** **Diretor**, **João Santos**, para prestigiar a cerimônia de formatura da turma de bombeiros.