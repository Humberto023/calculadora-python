# Calculadora em Python

Calculadora simples (soma, subtração, multiplicação e divisão) com testes automatizados
e pipeline de CI no GitHub Actions.

## Como rodar

```bash
python calculadora.py
```

## Como testar

```bash
pip install -r requirements.txt
pytest -v
```

## Pipeline

A cada push ou pull request, o GitHub Actions (`.github/workflows/ci.yml`):
1. Instala o Python e as dependências
2. Verifica o estilo do código com `flake8`
3. Roda os testes com `pytest`
