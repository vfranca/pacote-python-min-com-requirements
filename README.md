# Pacote Python mínimo com requirements.txt

Template para criação de pacotes Python utilizando `setuptools`, `setup.py` e `requirements.txt` para gerenciamento das dependências.

O objetivo é fornecer uma estrutura inicial simples, organizada e reutilizável para novos projetos Python.

## Características

- Estrutura de código utilizando o diretório `src/`.
- Configuração de empacotamento com `setuptools`.
- Dependências de execução declaradas em `requirements.txt`.
- Dependências de desenvolvimento declaradas em `requirements-dev.txt`.
- Docstrings nos módulos e funções.
- Execução do pacote utilizando `python -m`.
- Geração de distribuições nos formatos Wheel e Source Distribution.
- Publicação de pacotes utilizando Twine.

## Estrutura do projeto

```text
pacote-python-min-com-requirements/
    .gitignore
    LICENSE
    README.md
    requirements.txt
    requirements-dev.txt
    setup.py
    src/
        pacote_python_min_com_requirements/
            __init__.py
            __main__.py
            core.py
```

## Requisitos

- Python instalado.
- pip para instalação de dependências.
- Git, caso o projeto seja obtido por meio de um repositório.

## Instalação

Clone o repositório ou crie um novo repositório utilizando este template.

Entre no diretório do projeto e instale as dependências de desenvolvimento:

```bash
python -m pip install -r requirements-dev.txt
```

Instale o pacote em modo editável:

```bash
python -m pip install -e .
```

A instalação em modo editável permite modificar o código-fonte sem precisar reinstalar o pacote a cada alteração.

## Execução

Execute o pacote como um módulo Python:

```bash
python -m pacote_python_min_com_requirements
```

Saída esperada:

```text
Hello world!
```

## Desenvolvimento

O código-fonte está localizado em:

```text
src/pacote_python_min_com_requirements/
```

O módulo `core.py` contém a implementação principal.

O arquivo `__init__.py` define a interface pública do pacote.

O arquivo `__main__.py` permite executar o pacote utilizando `python -m`.

### Dependências

As dependências necessárias para executar o pacote devem ser declaradas em:

```text
requirements.txt
```

As ferramentas necessárias durante o desenvolvimento e a publicação devem ser declaradas em:

```text
requirements-dev.txt
```

Quando uma nova dependência de execução for adicionada ao projeto, inclua-a em `requirements.txt`.

## Geração das distribuições

Para gerar os arquivos de distribuição, execute:

```bash
python -m build
```

Os arquivos serão gerados no diretório:

```text
dist/
```

Serão produzidos dois formatos:

- Wheel (`.whl`): distribuição binária instalável.
- Source Distribution (`.tar.gz`): distribuição contendo o código-fonte.

## Verificação das distribuições

Antes de publicar o pacote, verifique os arquivos gerados:

```bash
python -m twine check dist/*
```

## Publicação no PyPI

Depois de configurar suas credenciais do PyPI, publique as distribuições com:

```bash
python -m twine upload dist/*
```

Para testar a publicação no ambiente de homologação do PyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

Consulte a documentação oficial do PyPI para obter informações sobre contas, tokens e publicação:

https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Utilização como template do GitHub

Este repositório pode ser utilizado como ponto de partida para novos pacotes Python.

Ao criar um novo projeto a partir deste template, revise os seguintes itens:

1. Altere o nome da distribuição no `setup.py`.
2. Altere o nome do diretório do pacote dentro de `src/`.
3. Atualize as referências ao nome do pacote em `__init__.py`, `__main__.py` e no README.
4. Defina a versão inicial do projeto.
5. Atualize a descrição do pacote.
6. Adicione as dependências necessárias em `requirements.txt`.
7. Atualize o README com as informações do novo projeto.
8. Revise a licença conforme as necessidades do projeto.

## Licença

Este projeto está disponibilizado sob a licença definida no arquivo `LICENSE`.
