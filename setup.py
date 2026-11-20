"""
Configuração de instalação e distribuição do pacote.

As dependências de execução são carregadas de requirements.txt.
"""

from pathlib import Path

from setuptools import find_packages, setup


ROOT_DIR = Path(__file__).parent
README_FILE = ROOT_DIR / "README.md"
REQUIREMENTS_FILE = ROOT_DIR / "requirements.txt"


def read_requirements():
    """
    Lê as dependências de execução definidas em requirements.txt.

    Ignora linhas vazias e comentários.

    Returns:
        list[str]: Lista de dependências do pacote.
    """
    if not REQUIREMENTS_FILE.exists():
        return []

    return [
        line.strip()
        for line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def read_readme():
    """
    Lê o conteúdo do README.md para a descrição do pacote.

    Returns:
        str: Conteúdo do arquivo README.md.
    """
    if not README_FILE.exists():
        return ""

    return README_FILE.read_text(encoding="utf-8")


setup(
    name="pacote-python-min-com-requirements",
    version="1.0.0",
    description="Pacote Python minimalista usando requirements.txt",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    include_package_data=True,
    zip_safe=False,
)
