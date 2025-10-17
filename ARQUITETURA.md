"""
ARQUITETURA DO SISTEMA GERADOR CBMAC
===================================

Este documento descreve a arquitetura geral do sistema de geração
de certificados do Corpo de Bombeiros Militar do Acre.

VISÃO GERAL:
-----------
Sistema web desenvolvido em Flask para automatizar a geração de
documentos oficiais da corporação. Utiliza templates de imagem
como base e sobrepõe informações fornecidas pelo usuário.

ESTRUTURA MODULAR:
-----------------

1. FRONTEND (templates/index.html)
   - Interface web responsiva com Bootstrap
   - JavaScript para controle dinâmico de campos
   - Formulários específicos por tipo de documento
   - Validação opcional (atualmente desabilitada)

2. BACKEND (app.py)
   - Servidor Flask com roteamento RESTful
   - Sistema de logs para auditoria
   - Dispatcher para geradores específicos
   - Mapeamento de campos por tipo de documento

3. GERADORES (app/models/)
   - Módulos especializados para cada tipo de documento
   - Localização automática de templates
   - Geração de PDFs com ReportLab
   - Tratamento de erros e validações

4. TEMPLATES (app/static/Certificado/)
   - Imagens de fundo organizadas por tipo
   - Estrutura hierárquica de pastas
   - Suporte a subtipos e variações
   - Formatos: JPG, PNG

FLUXO DE OPERAÇÃO:
-----------------

1. Usuário acessa interface web (/)
2. Seleciona tipo de documento (JavaScript dinâmico)
3. Preenche campos específicos (todos opcionais)
4. Submete formulário (/gerar-certificado POST)
5. Backend valida tipo e mapeia campos
6. Gerador específico localiza template
7. PDF é criado com informações sobrepostas
8. Arquivo é enviado para download

PADRÕES DE DESENVOLVIMENTO:
--------------------------

• NOMENCLATURA: Português brasileiro para comentários e variáveis
• LOGGING: Sistema completo de auditoria e debug  
• MODULARIDADE: Cada tipo de documento em arquivo separado
• FLEXIBILIDADE: Campos opcionais, templates automáticos
• ROBUSTEZ: Tratamento de erros e fallbacks
• MANUTENIBILIDADE: Código documentado e estruturado

TECNOLOGIAS UTILIZADAS:
----------------------

• Python 3.8+: Linguagem principal
• Flask: Framework web minimalista
• ReportLab: Geração de PDFs
• Bootstrap 5: Interface responsiva  
• JavaScript: Interatividade frontend
• PIL/Pillow: Manipulação de imagens

CONFIGURAÇÃO DE AMBIENTE:
------------------------

• Ambiente virtual Python (.venv/)
• Dependências em requirements.txt
• Logs em app.log
• PDFs temporários em uploads/
• Arquivos estáticos em app/static/

EXTENSIBILIDADE:
---------------

Para adicionar novo tipo de documento:

1. Criar gerador em app/models/novo_tipo.py
2. Adicionar template em app/static/Certificado/NovoTipo/
3. Configurar campos em templates/index.html
4. Mapear no dispatcher de app.py
5. Testar e documentar

SEGURANÇA:
----------

• Validação de tipos de arquivo (imagens)
• Sanitização de nomes de arquivo
• Logs de auditoria completos
• Ambiente isolado (virtual env)
• Sem execução de código externo

PERFORMANCE:
-----------

• Templates carregados sob demanda
• PDFs gerados em diretório temporário
• Cache natural do sistema de arquivos
• Processamento síncrono (adequado para uso interno)

MANUTENÇÃO:
----------

• Código totalmente comentado em português
• Estrutura modular facilita updates
• Logs detalhados para troubleshooting
• Testes automatizáveis (pasta archive/)
• Documentação completa (README.md)

COMPATIBILIDADE:
---------------

• Windows (desenvolvimento)
• Linux/Unix (produção)
• Python 3.8+
• Navegadores modernos
• Arquivos PDF universais

Desenvolvido para CBMAC - Corpo de Bombeiros Militar do Acre
"""