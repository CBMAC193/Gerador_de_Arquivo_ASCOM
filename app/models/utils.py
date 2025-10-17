"""
Utilitários para Localização de Templates - Sistema CBMAC
========================================================

Este módulo contém funções auxiliares para localizar arquivos de template
(imagens de fundo) para os diferentes tipos de certificados.

A estrutura esperada é:
app/static/Certificado/
├── Diplomas/
├── Medalhas/
├── Certificados/
└── etc...

Cada pasta pode conter subpastas com imagens específicas.
"""

import os
from typing import Optional


def find_model_image(*path_parts: str, subtype: Optional[str] = None) -> Optional[str]:
    """
    Localiza uma imagem de template baseada na estrutura de pastas do sistema
    
    Args:
        *path_parts: Sequência de pastas dentro de Certificado 
                    (ex: 'Diplomas', 'Medalhas', 'Tempo de Serviço')
        subtype: Parâmetro opcional para compatibilidade (não utilizado)
    
    Returns:
        str|None: Caminho absoluto para a imagem encontrada ou None se não existir
        
    Example:
        find_model_image('Medalhas', 'Tempo de Serviço', '10 ANOS de serviço')
        # Procura em: app/static/Certificado/Medalhas/Tempo de Serviço/10 ANOS de serviço.jpg
    """
    # Determinar diretório base do sistema de certificados
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    cert_root = os.path.join(base_dir, 'static', 'Certificado')
    
    # Construir caminho combinando todas as partes do path
    target = os.path.join(cert_root, *path_parts)

    # Estratégia 1: Se target é uma pasta, procurar imagens dentro dela
    if os.path.isdir(target):
        for f in os.listdir(target):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                return os.path.join(target, f)
    
    # Estratégia 2: Tentar localizar arquivo específico baseado no nome
    if path_parts:
        # Tentar arquivo com nome da última parte
        last_part = path_parts[-1]
        parent = os.path.join(cert_root, *path_parts[:-1]) if len(path_parts) > 1 else cert_root
        
        if os.path.isdir(parent):
            for ext in ('.jpg', '.jpeg', '.png'):
                candidate = os.path.join(parent, f"{last_part}{ext}")
                if os.path.exists(candidate):
                    return candidate

    # Sem subtipo ou não encontrado: procurar imagens diretamente na target
    if os.path.isdir(target):
        # tenta nome igual à última parte
        last = path_parts[-1]
        for ext in ('.jpg', '.jpeg', '.png'):
            candidate = os.path.join(target, f"{last}{ext}")
            if os.path.exists(candidate):
                return candidate
        # fallback: primeiro arquivo de imagem
        for f in os.listdir(target):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                return os.path.join(target, f)

    return None
