"""
Sistema Gerador de Certificados CBMAC
======================================
Aplicação Flask para geração automática de certificados, diplomas, medalhas,
convites e notas de pesar do Corpo de Bombeiros Militar do Acre.

Autor: Sistema CBMAC
Data: 2024
"""

from flask import Flask, render_template, request, send_file, redirect, url_for, jsonify
import os
import logging
import zipfile
from datetime import datetime
import uuid
import json

# Importar geradores específicos para cada tipo de documento
from app.models.agradecimento import gerar_certificado_agradecimento
from app.models.diploma import gerar_certificado_diploma
from app.models.medalha import gerar_certificado_medalha
from app.models.moeda import gerar_certificado_moeda
from app.models.convite import gerar_certificado_convite
from app.models.nota_pesar import gerar_certificado_nota_pesar
from app.models.certificado import gerar_certificado_certificado

# Configuração da aplicação Flask
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'app', 'static'))
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Arquivo para armazenar contador de documentos
CONTADOR_FILE = os.path.join('uploads', 'contador_documentos.json')

def get_contador_documentos():
    """Obtém o contador atual de documentos gerados"""
    try:
        if os.path.exists(CONTADOR_FILE):
            with open(CONTADOR_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('total_documentos', 0)
    except:
        pass
    return 0

def incrementar_contador(quantidade=1):
    """Incrementa o contador de documentos e retorna o novo total"""
    contador_atual = get_contador_documentos()
    novo_total = contador_atual + quantidade
    
    try:
        os.makedirs(os.path.dirname(CONTADOR_FILE), exist_ok=True)
        data = {
            'total_documentos': novo_total,
            'ultima_atualizacao': datetime.now().isoformat()
        }
        with open(CONTADOR_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        app.logger.error(f'Erro ao salvar contador: {e}')
    
    return novo_total

# Configuração do sistema de logs
app.logger.setLevel(logging.INFO)  # Nível de detalhamento dos logs

# Configurar arquivo de log para registrar operações
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)


@app.route('/')
def index():
    """Página principal do sistema - formulário para seleção e preenchimento de documentos"""
    contador = get_contador_documentos()
    return render_template('index.html', contador_documentos=contador)

@app.route('/contador-documentos')
def get_contador_api():
    """Retorna o contador atual de documentos gerados"""
    return jsonify({'total_documentos': get_contador_documentos()})

@app.route('/teste')
def teste():
    """Rota de teste (pode ser removida em produção)"""
    with open('teste_simples.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/gerar-certificado', methods=['POST'])
def gerar_certificado():
    """
    Endpoint principal para geração de documentos
    
    Recebe os dados do formulário, identifica o tipo de documento
    e chama o gerador apropriado para criar o PDF
    
    Returns:
        PDF file: Documento gerado para download
        Error: Mensagem de erro se algo falhar
    """
    tipo_documento = request.form.get('tipo')
    
    # Log dos dados recebidos para debug e auditoria
    app.logger.info(f'Dados recebidos - tipoDocumento: "{tipo_documento}" (len: {len(tipo_documento) if tipo_documento else 0})')
    app.logger.info(f'Todos os dados do form: {dict(request.form)}')
    
    # Validação básica - tipo de documento é obrigatório
    if not tipo_documento:
        app.logger.warning('tipoDocumento está vazio ou None')
        return 'Tipo de documento não fornecido', 400

    # Validação de campos obrigatórios removida - todos os campos são opcionais
    # REQUIRED = {
    #     'Diplomas': ['nome_diploma', 'decreto_diploma', 'local_diploma', 'data_diploma', 'comandante_diploma'],
    #     'Medalhas': ['nome_medalha', 'decreto_medalha', 'local_medalha', 'data_medalha', 'comandante_medalha'],
    #     'Moeda': ['nome_moeda', 'decreto_moeda', 'local_moeda', 'data_moeda', 'comandante_moeda'],
    #     'Certificado': ['nome_certificado', 'decreto_certificado', 'local_certificado', 'data_certificado', 'comandante_certificado'],
    #     'Agradecimento': ['nome_agradecido_agradecimento', 'funcao_agradecimento', 'local_funcao_agradecimento', 'pelo_que_agradecimento', 'tema_agradecimento', 'local_agradecimento', 'data_agradecimento', 'comandante_agradecimento'],
    #     'Convite': ['cargo_convidado_convite', 'nome_convidado_convite', 'pra_que_convidado_convite', 'data_convite', 'horario_convite', 'local_convite', 'cidade_convite', 'endereco_convite', 'posto_convite', 'comandante_convite'],
    #     'Nota de Pesar': ['falecido_nota_pesar', 'parentesco_nota_pesar', 'pessoa_enlutada_nota_pesar', 'local_nota_pesar', 'data_nota_pesar', 'comandante_nota_pesar']
    # }

    # def _validate_required(tipo):
    #     req = REQUIRED.get(tipo)
    #     if not req:
    #         return []
    #     missing = [k for k in req if not request.form.get(k)]
    #     return missing

    def _send_cert_file(caminho):
        """
        Função auxiliar para validar e enviar arquivo PDF gerado
        
        Args:
            caminho (str): Caminho para o arquivo PDF gerado
            
        Returns:
            Flask Response: Arquivo para download ou erro
        """
        # Validação do retorno do gerador
        if caminho is None:
            app.logger.error('Gerador retornou None em vez de caminho de arquivo')
            return 'Erro interno: arquivo não gerado', 500
        if not isinstance(caminho, str):
            app.logger.error('Gerador retornou valor não-string: %r', caminho)
            return 'Erro interno: caminho inválido', 500
        if not os.path.exists(caminho):
            app.logger.error('Arquivo não encontrado no disco: %s', caminho)
            return 'Erro interno: arquivo não encontrado', 500
        
        # Tudo validado - enviar arquivo para download
        return send_file(caminho, as_attachment=True)

    # Validação removida - todos os campos são opcionais
    # missing = _validate_required(tipo_documento)
    # if missing:
    #     return {'error': 'Campos obrigatórios faltando', 'missing': missing}, 400

    # Distribuidor de dados por tipo de documento
    # Cada tipo tem campos específicos que são mapeados para o formato padrão dos geradores
    
    if tipo_documento == 'Diplomas':
        # Mapear campos específicos de diplomas para formato padrão
        dados = {
            'nome': request.form.get('nome_diploma'),
            'decreto': request.form.get('decreto_diploma'), 
            'local': request.form.get('local_diploma'),
            'data': request.form.get('data_diploma'),
            'comandante': request.form.get('comandante_diploma'),
            'subtipo': request.form.get('subtipo'),  # Tipo específico do diploma
            'subsubtipo': request.form.get('subsubtipo')
        }
        try:
            caminho = gerar_certificado_diploma(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar diploma')
            return 'Erro interno ao gerar diploma', 500

    elif tipo_documento == 'Medalhas':
        # Mapear campos específicos de medalhas para formato padrão
        dados = {
            'nome': request.form.get('nome_medalha'),
            'nome_agraciado': request.form.get('nome_medalha'),  # Nome do agraciado
            'decreto': request.form.get('decreto_medalha'),
            'local': request.form.get('local_medalha'),
            'data': request.form.get('data_medalha'),
            'comandante': request.form.get('comandante_medalha'),
            'subtipo': request.form.get('subtipo'),
            'subsubtipo': request.form.get('subsubtipo')
        }
        try:
            caminho = gerar_certificado_medalha(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar medalha')
            return 'Erro interno ao gerar medalha', 500

    elif tipo_documento == 'Moeda':
        dados = {
            'nome': request.form.get('nome_moeda'),
            'nome_agraciado': request.form.get('nome_moeda'),
            'decreto': request.form.get('decreto_moeda'),
            'local': request.form.get('local_moeda'),
            'data': request.form.get('data_moeda'),
            'comandante': request.form.get('comandante_moeda')
        }
        try:
            caminho = gerar_certificado_moeda(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar moeda')
            return 'Erro interno ao gerar moeda', 500

    elif tipo_documento == 'Certificado':
        dados = {
            'nome': request.form.get('nome_certificado'),
            'decreto': request.form.get('decreto_certificado'),
            'local': request.form.get('local_certificado'),
            'data': request.form.get('data_certificado'),
            'comandante': request.form.get('comandante_certificado')
        }
        try:
            caminho = gerar_certificado_certificado(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar certificado')
            return 'Erro interno ao gerar certificado', 500

    elif tipo_documento == 'Agradecimento':
        # DEBUG: Log dos dados recebidos
        print(f"[DEBUG AGRADECIMENTO] Dados do formulário recebidos:")
        for key, value in request.form.items():
            print(f"  {key}: '{value}'")
        
        dados = {
            'nome_agradecido_agradecimento': request.form.get('nome_agradecido_agradecimento', '').strip(),
            'funcao_agradecimento': request.form.get('funcao_agradecimento', '').strip(),
            'local_funcao_agradecimento': request.form.get('local_funcao_agradecimento', '').strip(),
            'pelo_que_agradecimento': request.form.get('pelo_que_agradecimento', '').strip(),
            'tema_agradecimento': request.form.get('tema_agradecimento', '').strip(),
            'local_agradecimento': request.form.get('local_agradecimento', '').strip(),
            'data_agradecimento': request.form.get('data_agradecimento', '').strip(),
            'comandante_agradecimento': request.form.get('comandante_agradecimento', '').strip()
        }
        
        print(f"[DEBUG AGRADECIMENTO] Dados mapeados:")
        for key, value in dados.items():
            print(f"  {key}: '{value}'")
        try:
            caminho = gerar_certificado_agradecimento(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar agradecimento')
            return 'Erro interno ao gerar agradecimento', 500

    elif tipo_documento == 'Convite':
        # Verificar se é modo individual ou coletivo
        modo_convite = request.form.get('modo_convite', 'individual')
        
        dados = {
            'data_convite': request.form.get('data_convite', '').strip(),
            'horario_convite': request.form.get('horario_convite', '').strip(),
            'local_convite': request.form.get('local_convite', '').strip(),
            'cidade_convite': request.form.get('cidade_convite', '').strip(),
            'endereco_convite': request.form.get('endereco_convite', '').strip(),
            'posto_convite': request.form.get('posto_convite', '').strip(),
            'comandante_convite': request.form.get('comandante_convite', '').strip(),
            'pra_que_convidado_convite': request.form.get('pra_que_convidado_convite', '').strip(),
            'modo_convite': modo_convite
        }
        
        if modo_convite == 'individual':
            dados.update({
                'genero_convidado': request.form.get('genero_convidado_convite', '').strip(),
                'cargo_convidado': request.form.get('cargo_convidado_convite', '').strip(),
                'nome_convidado': request.form.get('nome_convidado_convite', '').strip()
            })
        else:  # coletivo
            dados.update({
                'tropa_convite': request.form.get('tropa_convite', '').strip(),
                'traje_convite': request.form.get('traje_convite', '').strip()
            })
        try:
            caminho = gerar_certificado_convite(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar convite')
            return 'Erro interno ao gerar convite', 500

    elif tipo_documento == 'Nota de Pesar':
        dados = {
            'falecido': request.form.get('falecido_nota_pesar'),
            'parentesco': request.form.get('parentesco_nota_pesar'),
            'pessoa_enlutada': request.form.get('pessoa_enlutada_nota_pesar'),
            'comandante': request.form.get('comandante_nota_pesar'),
            'local': request.form.get('local_nota_pesar'),
            'data': request.form.get('data_nota_pesar')
        }
        try:
            caminho = gerar_certificado_nota_pesar(dados)
            return _send_cert_file(caminho)
        except Exception:
            app.logger.exception('Erro ao gerar nota de pesar')
            return 'Erro interno ao gerar nota de pesar', 500

    return 'Tipo de documento inválido', 400

def processar_multiplos_nomes(nomes_texto):
    """
    Processa o campo de nomes que pode conter múltiplos nomes
    
    Args:
        nomes_texto (str): Texto com nomes separados por vírgula, ponto e vírgula ou linha
        
    Returns:
        list: Lista de nomes limpos
    """
    if not nomes_texto:
        return []
    
    # Separar por vírgula, ponto e vírgula ou quebra de linha
    import re
    nomes = re.split(r'[,;\n]+', nomes_texto)
    
    # Limpar espaços e filtrar nomes vazios
    nomes_limpos = [nome.strip() for nome in nomes if nome.strip()]
    
    return nomes_limpos

def gerar_documento_multiplas_paginas(dados_base, nomes, tipo_doc):
    """
    Gera um único PDF com múltiplas páginas, uma para cada nome
    
    Args:
        dados_base (dict): Dados base do documento
        nomes (list): Lista de nomes para gerar páginas
        tipo_doc (str): Tipo do documento
        
    Returns:
        str: Caminho do arquivo PDF gerado
    """
    from PyPDF2 import PdfMerger
    import tempfile
    
    try:
        # Gerar documentos individuais temporários
        arquivos_temporarios = []
        
        for nome in nomes:
            dados = dados_base.copy()
            
            # Atualizar o nome específico baseado no tipo do documento
            if tipo_doc == 'Diplomas':
                dados['nome'] = nome
                caminho_temp = gerar_certificado_diploma(dados)
            elif tipo_doc == 'Medalhas':
                dados['nome'] = nome
                dados['nome_agraciado'] = nome
                caminho_temp = gerar_certificado_medalha(dados)
            elif tipo_doc == 'Moeda' or tipo_doc == 'Moeda CBMAC':
                dados['nome'] = nome
                dados['nome_agraciado'] = nome
                caminho_temp = gerar_certificado_moeda(dados)
            elif tipo_doc == 'Certificado' or tipo_doc == 'Certificado Amigo dos Veteranos':
                dados['nome'] = nome
                caminho_temp = gerar_certificado_certificado(dados)
            else:
                raise ValueError(f'Tipo de documento não suportado para múltiplas páginas: {tipo_doc}')
            
            arquivos_temporarios.append(caminho_temp)
        
        # Mesclar PDFs
        merger = PdfMerger()
        
        for arquivo in arquivos_temporarios:
            merger.append(arquivo)
        
        # Gerar nome do arquivo final
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo_final = f"{tipo_doc.lower().replace(' ', '_')}_{timestamp}.pdf"
        
        # Diretório de uploads
        upload_dir = os.path.join(os.path.dirname(__file__), 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        caminho_final = os.path.join(upload_dir, nome_arquivo_final)
        
        # Salvar PDF mesclado
        with open(caminho_final, 'wb') as output_file:
            merger.write(output_file)
        
        merger.close()
        
        # Remover arquivos temporários
        for arquivo in arquivos_temporarios:
            try:
                os.remove(arquivo)
            except OSError:
                pass  # Ignorar erros ao remover temporários
        
        app.logger.info(f'PDF com múltiplas páginas criado: {caminho_final}')
        return caminho_final
        
    except Exception as e:
        app.logger.error(f'Erro ao gerar documento com múltiplas páginas: {str(e)}')
        raise

@app.route('/gerar-documento-visualizacao', methods=['POST'])
def gerar_documento_visualizacao():
    """
    Nova rota que gera documentos e retorna para visualização (não download direto)
    Suporta múltiplos nomes
    """
    app.logger.info('=== GERANDO DOCUMENTO PARA VISUALIZAÇÃO ===')
    
    # Obter dados do formulário
    tipo_documento = request.form.get('tipo')
    
    if not tipo_documento:
        return jsonify({'error': 'Tipo de documento não fornecido'}), 400
    
    # Função auxiliar para gerar um documento individual
    def gerar_documento_individual(dados_base, nome_individual, tipo_doc):
        """Gera um único documento com nome específico"""
        dados = dados_base.copy()
        
        # Atualizar o nome específico baseado no tipo do documento
        if tipo_doc == 'Diplomas':
            dados['nome'] = nome_individual
            return gerar_certificado_diploma(dados)
        elif tipo_doc == 'Medalhas':
            dados['nome'] = nome_individual
            dados['nome_agraciado'] = nome_individual
            return gerar_certificado_medalha(dados)
        elif tipo_doc == 'Moeda' or tipo_doc == 'Moeda CBMAC':
            dados['nome'] = nome_individual
            dados['nome_agraciado'] = nome_individual
            return gerar_certificado_moeda(dados)
        elif tipo_doc == 'Certificado' or tipo_doc == 'Certificado Amigo dos Veteranos':
            dados['nome'] = nome_individual
            return gerar_certificado_certificado(dados)
        elif tipo_doc == 'Agradecimento':
            dados['nome_agradecido_agradecimento'] = nome_individual
            return gerar_certificado_agradecimento(dados)
        elif tipo_doc == 'Convite':
            dados['nome_convidado'] = nome_individual
            return gerar_certificado_convite(dados)
        elif tipo_doc == 'Nota de Pesar':
            dados['falecido'] = nome_individual
            return gerar_certificado_nota_pesar(dados)
        
        raise ValueError(f'Tipo de documento inválido: {tipo_doc}')
    
    try:
        # Verificar modo (individual ou lista) PRIMEIRO
        modo = None
        if tipo_documento == 'Diplomas':
            modo = request.form.get('modo_diploma', 'individual')
        elif tipo_documento == 'Medalhas':
            modo = request.form.get('modo_medalha', 'individual')
        elif tipo_documento == 'Moeda' or tipo_documento == 'Moeda CBMAC':
            modo = request.form.get('modo_moeda', 'individual')
        elif tipo_documento == 'Certificado' or tipo_documento == 'Certificado Amigo dos Veteranos':
            modo = request.form.get('modo_certificado', 'individual')
        else:
            modo = 'individual'  # Para outros tipos sempre individual
        
        # Preparar dados baseado no tipo de documento
        if tipo_documento == 'Diplomas':
            # Verificar se é modo individual ou lista
            if modo == 'lista':
                nomes_texto = request.form.get('nome_diploma_lista', '')
            else:
                nomes_texto = request.form.get('nome_diploma', '')
            dados_base = {
                'decreto': request.form.get('decreto_diploma'),
                'local': request.form.get('local_diploma'),
                'data': request.form.get('data_diploma'),
                'comandante': request.form.get('comandante_diploma'),
                'subtipo': request.form.get('subtipo'),
                'subsubtipo': request.form.get('subsubtipo')
            }
        elif tipo_documento == 'Medalhas':
            # Verificar se é modo individual ou lista
            if modo == 'lista':
                nomes_texto = request.form.get('nome_medalha_lista', '')
            else:
                nomes_texto = request.form.get('nome_medalha', '')
            dados_base = {
                'decreto': request.form.get('decreto_medalha'),
                'local': request.form.get('local_medalha'),
                'data': request.form.get('data_medalha'),
                'comandante': request.form.get('comandante_medalha'),
                'subtipo': request.form.get('subtipo'),
                'subsubtipo': request.form.get('subsubtipo')
            }
        elif tipo_documento == 'Moeda' or tipo_documento == 'Moeda CBMAC':
            # Verificar se é modo individual ou lista
            if modo == 'lista':
                nomes_texto = request.form.get('nome_moeda_lista', '')
            else:
                nomes_texto = request.form.get('nome_moeda', '')
            dados_base = {
                'decreto': request.form.get('decreto_moeda'),
                'local': request.form.get('local_moeda'),
                'data': request.form.get('data_moeda'),
                'comandante': request.form.get('comandante_moeda')
            }
        elif tipo_documento == 'Certificado' or tipo_documento == 'Certificado Amigo dos Veteranos':
            # Verificar se é modo individual ou lista
            if modo == 'lista':
                nomes_texto = request.form.get('nome_certificado_lista', '')
            else:
                nomes_texto = request.form.get('nome_certificado', '')
            dados_base = {
                'decreto': request.form.get('decreto_certificado'),
                'local': request.form.get('local_certificado'),
                'data': request.form.get('data_certificado'),
                'comandante': request.form.get('comandante_certificado')
            }
        elif tipo_documento == 'Agradecimento':
            nomes_texto = request.form.get('nome_agradecido_agradecimento', '')
            dados_base = {
                'funcao_agradecimento': request.form.get('funcao_agradecimento'),
                'local_funcao_agradecimento': request.form.get('local_funcao_agradecimento'),
                'pelo_que_agradecimento': request.form.get('pelo_que_agradecimento'),
                'tema_agradecimento': request.form.get('tema_agradecimento'),
                'local_agradecimento': request.form.get('local_agradecimento'),
                'data_agradecimento': request.form.get('data_agradecimento'),
                'comandante_agradecimento': request.form.get('comandante_agradecimento')
            }
        elif tipo_documento == 'Convite':
            nomes_texto = request.form.get('nome_convidado_convite', '')
            dados_base = {
                'cargo_convidado': request.form.get('cargo_convidado_convite'),
                'pra_que_convidado': request.form.get('pra_que_convidado_convite'),
                'data': request.form.get('data_convite'),
                'horario': request.form.get('horario_convite'),
                'local': request.form.get('local_convite'),
                'cidade': request.form.get('cidade_convite'),
                'endereco': request.form.get('endereco_convite'),
                'posto': request.form.get('posto_convite'),
                'comandante': request.form.get('comandante_convite'),
                'genero_convidado': (request.form.get('genero_convidado_convite'))
            }
        elif tipo_documento == 'Nota de Pesar':
            nomes_texto = request.form.get('falecido_nota_pesar', '')
            dados_base = {
                'parentesco': request.form.get('parentesco_nota_pesar'),
                'pessoa_enlutada': request.form.get('pessoa_enlutada_nota_pesar'),
                'local': request.form.get('local_nota_pesar'),
                'data': request.form.get('data_nota_pesar'),
                'comandante': request.form.get('comandante_nota_pesar')
            }
        else:
            return jsonify({'error': 'Tipo de documento inválido'}), 400
        
        # Processar nomes (múltiplos ou único)
        nomes = processar_multiplos_nomes(nomes_texto)
        
        if not nomes:
            return jsonify({'error': 'Nenhum nome fornecido'}), 400
        
        # Gerar documentos
        arquivos_gerados = []
        session_id = str(uuid.uuid4())  # ID único para esta sessão
        
        if modo == 'lista' and len(nomes) > 1:
            # Modo lista: gerar um único PDF com múltiplas páginas
            try:
                caminho_arquivo = gerar_documento_multiplas_paginas(dados_base, nomes, tipo_documento)
                arquivos_gerados.append({
                    'nome_pessoa': f"Lista com {len(nomes)} nomes",
                    'caminho': caminho_arquivo,
                    'nome_arquivo': os.path.basename(caminho_arquivo)
                })
            except Exception as e:
                app.logger.error(f'Erro ao gerar documento com múltiplas páginas: {str(e)}')
                return jsonify({'error': f'Erro ao gerar documento: {str(e)}'}), 500
        else:
            # Modo individual: gerar documentos separados
            for i, nome in enumerate(nomes):
                try:
                    caminho_arquivo = gerar_documento_individual(dados_base, nome, tipo_documento)
                    
                    # Renomear arquivo para incluir nome da pessoa (para múltiplos)
                    if len(nomes) > 1:
                        nome_arquivo_limpo = ''.join(c for c in nome if c.isalnum() or c in ' -_').rstrip()
                        nome_arquivo_limpo = nome_arquivo_limpo.replace(' ', '_')[:50]  # Limitar tamanho
                        
                        diretorio = os.path.dirname(caminho_arquivo)
                        extensao = os.path.splitext(caminho_arquivo)[1]
                        novo_nome = f"{tipo_documento}_{nome_arquivo_limpo}_{i+1:03d}{extensao}"
                        novo_caminho = os.path.join(diretorio, novo_nome)
                        
                        os.rename(caminho_arquivo, novo_caminho)
                        caminho_arquivo = novo_caminho
                    
                    arquivos_gerados.append({
                        'nome_pessoa': nome,
                        'caminho': caminho_arquivo,
                        'nome_arquivo': os.path.basename(caminho_arquivo)
                    })
                    
                except Exception as e:
                    app.logger.error(f'Erro ao gerar documento para {nome}: {str(e)}')
                    return jsonify({'error': f'Erro ao gerar documento para {nome}: {str(e)}'}), 500
        
        app.logger.info(f'Gerados {len(arquivos_gerados)} documentos')
        
        # Incrementar contador global de documentos
        total_geral = incrementar_contador(len(arquivos_gerados))
        
        # Retornar dados diretos para visualização na mesma página
        return jsonify({
            'success': True,
            'total_documentos': len(arquivos_gerados),
            'total_geral_documentos': total_geral,
            'tipo_documento': tipo_documento,
            'arquivos': arquivos_gerados,
            'documento_unico': len(arquivos_gerados) == 1,
            'arquivo_principal': arquivos_gerados[0] if len(arquivos_gerados) == 1 else None
        })
        
    except Exception as e:
        app.logger.exception('Erro ao gerar documentos para visualização')
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/visualizar/<session_id>')
def visualizar_documentos(session_id):
    """
    Página de visualização dos documentos gerados
    """
    try:
        # Carregar dados da sessão
        session_file = os.path.join('uploads', 'temp_sessions', f'session_{session_id}.json')
        
        if not os.path.exists(session_file):
            return 'Sessão não encontrada ou expirada', 404
        
        import json
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        return render_template('visualizar_documentos.html', 
                             session_data=session_data, 
                             session_id=session_id)
        
    except Exception as e:
        app.logger.exception(f'Erro ao carregar visualização da sessão {session_id}')
        return f'Erro interno: {str(e)}', 500

@app.route('/download/<session_id>')
def download_documentos(session_id):
    """
    Download dos documentos gerados (único ou ZIP para múltiplos)
    """
    try:
        # Carregar dados da sessão
        session_file = os.path.join('uploads', 'temp_sessions', f'session_{session_id}.json')
        
        if not os.path.exists(session_file):
            return 'Sessão não encontrada', 404
        
        import json
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        arquivos = session_data['arquivos']
        
        # Se apenas um arquivo, enviar diretamente
        if len(arquivos) == 1:
            arquivo = arquivos[0]
            if os.path.exists(arquivo['caminho']):
                return send_file(arquivo['caminho'], as_attachment=True, 
                               download_name=arquivo['nome_arquivo'])
            else:
                return 'Arquivo não encontrado', 404
        
        # Múltiplos arquivos - criar ZIP
        zip_name = f"{session_data['tipo_documento']}_Lote_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        zip_path = os.path.join('uploads', zip_name)
        
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for arquivo in arquivos:
                if os.path.exists(arquivo['caminho']):
                    zip_file.write(arquivo['caminho'], arquivo['nome_arquivo'])
        
        return send_file(zip_path, as_attachment=True, download_name=zip_name)
        
    except Exception as e:
        app.logger.exception(f'Erro ao fazer download da sessão {session_id}')
        return f'Erro interno: {str(e)}', 500

@app.route('/download-individual/<session_id>/<int:arquivo_index>')
def download_individual(session_id, arquivo_index):
    """
    Download de um arquivo individual de uma sessão
    """
    try:
        # Carregar dados da sessão
        session_file = os.path.join('uploads', 'temp_sessions', f'session_{session_id}.json')
        
        if not os.path.exists(session_file):
            return 'Sessão não encontrada', 404
        
        import json
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        arquivos = session_data['arquivos']
        
        if arquivo_index >= len(arquivos):
            return 'Arquivo não encontrado', 404
        
        arquivo = arquivos[arquivo_index]
        
        if os.path.exists(arquivo['caminho']):
            return send_file(arquivo['caminho'], as_attachment=True, 
                           download_name=arquivo['nome_arquivo'])
        else:
            return 'Arquivo não encontrado no disco', 404
        
    except Exception as e:
        app.logger.exception(f'Erro ao fazer download individual da sessão {session_id}')
        return f'Erro interno: {str(e)}', 500

@app.route('/visualizar-pdf/<session_id>/<int:arquivo_index>')
def visualizar_pdf(session_id, arquivo_index):
    """
    Visualizar PDF diretamente no navegador (inline)
    """
    try:
        # Carregar dados da sessão
        session_file = os.path.join('uploads', 'temp_sessions', f'session_{session_id}.json')
        
        if not os.path.exists(session_file):
            return 'Sessão não encontrada', 404
        
        import json
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        if arquivo_index >= len(session_data['arquivos']):
            return 'Arquivo não encontrado', 404
        
        arquivo = session_data['arquivos'][arquivo_index]
        caminho = arquivo['caminho']
        
        if not os.path.exists(caminho):
            return 'Arquivo não encontrado no disco', 404
        
        # Enviar PDF para visualização inline
        return send_file(caminho, 
                        mimetype='application/pdf',
                        as_attachment=False,  # Inline, não download
                        download_name=arquivo['nome_arquivo'])
        
    except Exception as e:
        app.logger.exception(f'Erro ao visualizar PDF da sessão {session_id}')
        return f'Erro interno: {str(e)}', 500

@app.route('/visualizar-pdf-unico/<session_id>')
def visualizar_pdf_unico(session_id):
    """
    Visualizar PDF único diretamente no navegador (para quando há apenas 1 documento)
    """
    try:
        # Carregar dados da sessão
        session_file = os.path.join('uploads', 'temp_sessions', f'session_{session_id}.json')
        
        if not os.path.exists(session_file):
            return 'Sessão não encontrada', 404
        
        import json
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        if len(session_data['arquivos']) != 1:
            return 'Esta rota é apenas para documentos únicos', 400
        
        arquivo = session_data['arquivos'][0]
        caminho = arquivo['caminho']
        
        if not os.path.exists(caminho):
            return 'Arquivo não encontrado no disco', 404
        
        # Enviar PDF para visualização inline
        return send_file(caminho, 
                        mimetype='application/pdf',
                        as_attachment=False,  # Inline, não download
                        download_name=arquivo['nome_arquivo'])
        
    except Exception as e:
        app.logger.exception(f'Erro ao visualizar PDF único da sessão {session_id}')
        return f'Erro interno: {str(e)}', 500

@app.route('/visualizar-pdf/<path:nome_arquivo>')
def visualizar_pdf_direto(nome_arquivo):
    """
    Visualiza PDF diretamente da pasta uploads
    """
    try:
        caminho = os.path.join('uploads', nome_arquivo)
        
        if not os.path.exists(caminho):
            return 'Arquivo não encontrado', 404
        
        # Enviar PDF para visualização inline
        return send_file(caminho, 
                        mimetype='application/pdf',
                        as_attachment=False,  # Inline, não download
                        download_name=nome_arquivo)
        
    except Exception as e:
        app.logger.exception(f'Erro ao visualizar PDF {nome_arquivo}')
        return f'Erro interno: {str(e)}', 500

@app.route('/download-pdf/<path:nome_arquivo>')
def download_pdf_direto(nome_arquivo):
    """
    Faz download do PDF diretamente da pasta uploads
    """
    try:
        caminho = os.path.join('uploads', nome_arquivo)
        
        if not os.path.exists(caminho):
            return 'Arquivo não encontrado', 404
        
        # Enviar PDF para download
        return send_file(caminho, 
                        mimetype='application/pdf',
                        as_attachment=True,  # Download
                        download_name=nome_arquivo)
        
    except Exception as e:
        app.logger.exception(f'Erro ao fazer download do PDF {nome_arquivo}')
        return f'Erro interno: {str(e)}', 500

if __name__ == "__main__":
    app.run(debug=True)