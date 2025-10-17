# Sistema Gerador de Certificados CBMAC

## 📋 Descrição

Sistema web para geração automática de documentos oficiais do **Corpo de Bombeiros Militar do Acre (CBMAC)**.

Permite a criação de:
- 🏅 **Diplomas** (Bravura, Ordem do Mérito Dom Pedro II, etc.)
- 🥇 **Medalhas** (Amigo, Tempo de Serviço, Mérito, etc.) 
- 📜 **Certificados** (Certificado Amigo dos Veteranos)
- 💌 **Convites** (Eventos e cerimônias)
- 🖤 **Notas de Pesar** (Condolências oficiais)
- 🙏 **Agradecimentos** (Reconhecimentos)
- 🪙 **Moedas** (Moedas comemorativas CBMAC)

---

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### 1. Configurar Ambiente Virtual
```bash
# Navegue até a pasta do projeto
cd "c:\Ascom - Certificados"

# Ative o ambiente virtual (se já existir)
.\.venv\Scripts\activate

# Ou crie um novo ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Sistema
```bash
python app.py
```

O sistema estará disponível em: http://127.0.0.1:5000

---

## 📁 Estrutura do Projeto

```
📦 Sistema CBMAC
├── 📄 app.py                    # Aplicação Flask principal
├── 📄 requirements.txt          # Dependências Python
├── 📁 app/                      # Módulos da aplicação
│   ├── 📄 __init__.py
│   ├── 📁 models/               # Geradores de documentos
│   │   ├── 📄 diploma.py        # Gerador de diplomas
│   │   ├── 📄 medalha.py        # Gerador de medalhas
│   │   ├── 📄 certificado.py    # Gerador de certificados
│   │   ├── 📄 convite.py        # Gerador de convites
│   │   ├── 📄 nota_pesar.py     # Gerador de notas de pesar
│   │   ├── 📄 agradecimento.py  # Gerador de agradecimentos
│   │   ├── 📄 moeda.py          # Gerador de moedas
│   │   └── 📄 utils.py          # Funções auxiliares
│   └── 📁 static/               # Arquivos estáticos
│       ├── 📁 Certificado/      # Templates de documentos
│       ├── 📁 bootstrap/        # Framework CSS
│       └── 📄 brasao.png        # Logo CBMAC
├── 📁 templates/                # Templates HTML
│   └── 📄 index.html            # Interface principal
├── 📁 uploads/                  # PDFs gerados (temporários)
├── 📁 archive/                  # Arquivos de desenvolvimento
└── 📄 README.md                 # Esta documentação
```

---

## 🎯 Como Usar

### 1. Acessar o Sistema
- Abra o navegador e vá para: http://127.0.0.1:5000
- Você verá a interface principal com o brasão do CBMAC

### 2. Selecionar Tipo de Documento
- Escolha o tipo no dropdown "Tipo de Documento"
- Os campos específicos aparecerão automaticamente

### 3. Preencher Campos (Opcional)
- **Todos os campos são opcionais**
- Campos vazios aparecerão em branco no documento final
- Preencha apenas as informações necessárias

### 4. Gerar Documento
- Clique no botão "Gerar Documento"
- O PDF será baixado automaticamente

---

## 📋 Tipos de Documentos Disponíveis

### 🏅 Diplomas
- Bravura Bombeiro Militar
- Ordem do Mérito Dom Pedro II (Cavaleiro, Comendador, Grã-Oficial)

**Campos**: Nome, Decreto, Local, Data, Comandante

### 🥇 Medalhas
- Medalhas simples: Amigo, Bombeiro Durão, Mérito, etc.
- Medalhas de tempo: 10, 20, 30 anos de serviço

**Campos**: Nome do Agraciado, Decreto, Local, Data, Comandante

### 💌 Convites
**Campos**: Cargo do Convidado, Nome, Evento, Data, Horário, Local, Cidade, Endereço, Posto, Comandante

### 🖤 Notas de Pesar
**Campos**: Nome do Falecido, Parentesco, Pessoa Enlutada, Local, Data, Comandante

### 🙏 Agradecimentos  
**Campos**: Nome do Agradecido, Função, Local da Função, Motivo, Tema, Local, Data, Comandante

### 🪙 Moedas CBMAC
**Campos**: Nome, Decreto, Local, Data, Comandante

---

## 🔧 Configuração Avançada

### Adicionar Novos Templates
1. Coloque a imagem (JPG/PNG) na pasta correspondente em `app/static/Certificado/`
2. Siga a estrutura de pastas existente
3. O sistema detectará automaticamente novos templates

### Logs do Sistema
- Logs são salvos em `app.log`
- Incluem informações de debug e erros
- Úteis para diagnóstico de problemas

### Personalização Visual
- Edite `templates/index.html` para alterar a interface
- Cores e estilos estão definidos nas variáveis CSS `:root`
- Logo pode ser substituído em `app/static/brasao.png`

---

## 🛠️ Desenvolvimento

### Estrutura do Código
- **app.py**: Servidor Flask e roteamento
- **models/**: Geradores específicos para cada tipo de documento
- **utils.py**: Funções auxiliares para localizar templates
- **index.html**: Interface web completa com JavaScript

### Validação de Campos
- Sistema **não requer** campos obrigatórios
- Validação removida tanto no frontend quanto backend
- Todos os documentos podem ser gerados mesmo com campos vazios

### Debugging
- Arquivos de teste estão em `/archive/`
- Use `debug_*.js` para testar funcionalidades específicas
- Logs detalhados no console do navegador e arquivo `app.log`

---

## 🆘 Solução de Problemas

### Erro: "Modelo não encontrado"
- Verifique se a imagem existe na pasta correta
- Confirme que o arquivo tem extensão `.jpg` ou `.png`
- Verifique os logs em `app.log`

### Erro: "Módulo não encontrado" 
- Execute: `pip install -r requirements.txt`
- Confirme que o ambiente virtual está ativo

### PDF não gerado
- Verifique permissões da pasta `uploads/`
- Consulte `app.log` para detalhes do erro
- Teste com campos preenchidos primeiro

### Interface não carrega
- Confirme que o servidor está rodando: http://127.0.0.1:5000
- Verifique se a porta 5000 não está sendo usada por outro programa

---

## 👥 Créditos

**Desenvolvido para**: Corpo de Bombeiros Militar do Acre (CBMAC)  
**Tecnologias**: Python, Flask, Bootstrap, ReportLab  
**Compatibilidade**: Windows, Linux, macOS  

---

## 📝 Licença

Sistema desenvolvido para uso interno do CBMAC.  
Todos os direitos reservados.