from setuptools import setup, find_packages

setup(
    name="pacote_python_min_com_requirements",
    version="1.0.0",
    description="Pacote python minimalista usano requirements.txt para dependencias",
    long_description="Pacote python minimalista usando requirements.txt para dependencias",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)