# Passo a passo de Execução

## SETUP Ollama (5 minutos)

```bash
# 1. Instalar Ollama (ollama.ai)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo
Todo o código stá no arquivo 'app.py.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2.  Garantir que o Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run a.\src\pp.py
```

