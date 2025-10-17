# Recursos Locais - Gerador de Documento ASCOM

## 📦 Bibliotecas CSS e JavaScript Locais

O sistema agora utiliza **100% de recursos locais**, sem dependência de CDNs externos. Todos os arquivos estão localizados na pasta `app/static/`:

### 🎨 **CSS Frameworks**

#### Bootstrap 5.3.0
- **Localização**: `app/static/bootstrap/css/`
- **Arquivo usado**: `bootstrap.min.css`
- **Template**: `{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}`

#### Font Awesome 6.0.0
- **Localização**: `app/static/fontawesome/css/`
- **Arquivo usado**: `all.min.css`
- **Template**: `{{ url_for('static', filename='fontawesome/css/all.min.css') }}`
- **Fontes**: `app/static/fontawesome/webfonts/` (carregadas automaticamente)

#### Bootstrap Icons 1.11.0
- **Localização**: `app/static/bootstrap-icons/`
- **Arquivo usado**: `bootstrap-icons.min.css`
- **Template**: `{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.min.css') }}`
- **Fontes**: Incluídas no mesmo diretório

### ⚙️ **JavaScript Frameworks**

#### Bootstrap JS 5.3.0
- **Localização**: `app/static/bootstrap/js/`
- **Arquivo usado**: `bootstrap.bundle.min.js`
- **Template**: `{{ url_for('static', filename='bootstrap/js/bootstrap.bundle.min.js') }}`

### 🗂️ **Estrutura de Arquivos Locais**

```
app/static/
├── bootstrap/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.css.map
│   └── js/
│       ├── bootstrap.bundle.min.js
│       └── bootstrap.bundle.min.js.map
├── bootstrap-icons/
│   ├── bootstrap-icons.min.css
│   ├── bootstrap-icons.css
│   └── fonts/
│       └── bootstrap-icons.woff2
├── fontawesome/
│   ├── css/
│   │   └── all.min.css
│   └── webfonts/
│       ├── fa-solid-900.woff2
│       ├── fa-regular-400.woff2
│       └── fa-brands-400.woff2
└── Certificado/
    └── [templates de documentos]
```

### ✅ **Vantagens dos Recursos Locais**

1. **⚡ Performance**: Carregamento mais rápido sem dependência de CDN
2. **🔒 Segurança**: Sem riscos de CDN comprometido ou indisponível
3. **📱 Offline**: Funciona sem conexão com internet
4. **⏱️ Cache**: Browser pode cachear recursos locais eficientemente
5. **🎯 Controle**: Versões específicas sem updates automáticos

### 🔄 **Comparação Antes/Depois**

#### ❌ **Antes (CDN)**
```html
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Font Awesome para ícones -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<!-- Bootstrap Icons -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

#### ✅ **Depois (Local)**
```html
<!-- Bootstrap CSS -->
<link href="{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}" rel="stylesheet">

<!-- Font Awesome para ícones -->
<link rel="stylesheet" href="{{ url_for('static', filename='fontawesome/css/all.min.css') }}">

<!-- Bootstrap Icons -->
<link href="{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.min.css') }}" rel="stylesheet">

<!-- Bootstrap JS -->
<script src="{{ url_for('static', filename='bootstrap/js/bootstrap.bundle.min.js') }}"></script>
```

### 📊 **Status dos Recursos**

| Biblioteca | Versão | Status | Arquivo Local |
|------------|---------|--------|---------------|
| **Bootstrap CSS** | 5.3.0 | ✅ Local | `bootstrap/css/bootstrap.min.css` |
| **Bootstrap JS** | 5.3.0 | ✅ Local | `bootstrap/js/bootstrap.bundle.min.js` |
| **Font Awesome** | 6.0.0 | ✅ Local | `fontawesome/css/all.min.css` |
| **Bootstrap Icons** | 1.11.0 | ✅ Local | `bootstrap-icons/bootstrap-icons.min.css` |

### 🚀 **Verificação de Funcionamento**

Pelos logs do servidor, confirmamos que os recursos estão sendo carregados localmente:

```
GET /static/bootstrap/css/bootstrap.min.css HTTP/1.1" 200
GET /static/fontawesome/css/all.min.css HTTP/1.1" 200  
GET /static/bootstrap-icons/bootstrap-icons.min.css HTTP/1.1" 200
GET /static/bootstrap/js/bootstrap.bundle.min.js HTTP/1.1" 200
```

### 🔧 **Manutenção**

Para atualizar as bibliotecas futuramente:

1. **Bootstrap**: Baixar nova versão em [getbootstrap.com](https://getbootstrap.com)
2. **Font Awesome**: Baixar em [fontawesome.com](https://fontawesome.com)  
3. **Bootstrap Icons**: Baixar em [icons.getbootstrap.com](https://icons.getbootstrap.com)
4. Substituir arquivos em `app/static/` mantendo a estrutura de pastas
5. Verificar se os nomes dos arquivos coincidem com os usados no template

### 💡 **Todas as Funcionalidades Mantidas**

- ✅ **Ícones Font Awesome**: `<i class="fas fa-certificate"></i>`
- ✅ **Ícones Bootstrap**: `<i class="bi bi-file-earmark-plus"></i>`  
- ✅ **Components Bootstrap**: Cards, buttons, forms, modals, etc.
- ✅ **Bootstrap JavaScript**: Tooltips, dropdowns, modals, etc.
- ✅ **Responsividade**: Grid system e breakpoints
- ✅ **Estilos customizados**: Cores institucionais mantidas

O sistema **Gerador de Documento ASCOM** agora é totalmente **autônomo** e **independente** de recursos externos! 🎉