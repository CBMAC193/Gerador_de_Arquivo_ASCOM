"""
Módulo de Geradores de Documentos CBMAC
=======================================

Este pacote contém todos os geradores específicos para diferentes
tipos de documentos oficiais do Corpo de Bombeiros Militar do Acre.

Geradores disponíveis:
- agradecimento.py: Certificados de agradecimento
- certificado.py: Certificados gerais
- convite.py: Convites para eventos e cerimônias
- diploma.py: Diplomas e condecorações
- medalha.py: Medalhas de mérito e tempo de serviço
- moeda.py: Moedas comemorativas CBMAC
- nota_pesar.py: Notas de pesar oficiais
- utils.py: Funções auxiliares para todos os geradores

Cada gerador segue o padrão:
- Recebe um dicionário com os dados do formulário
- Localiza o template de imagem apropriado
- Gera um PDF com as informações sobrepostas
- Retorna o caminho para o arquivo gerado
"""