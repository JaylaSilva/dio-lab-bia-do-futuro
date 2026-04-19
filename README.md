# Jay — Sua Educadora Financeira 💰

Este repositório contém a solução completa de um Agente de IA especializado em educação financeira e análise de investimentos, desenvolvida por **Jayla Silva**. O projeto integra uma interface amigável em Streamlit com o poder de processamento local do Ollama.

## 🚀 O Projeto
A **Jay** foi criada para democratizar o acesso à consultoria financeira, utilizando modelos de linguagem (LLM) para responder a dúvidas sobre finanças, analisar perfis de investidores e sugerir produtos financeiros com base em dados reais.

## 📁 Estrutura da Solução
- **`/src/app.py`**: Código-fonte principal da aplicação Streamlit, incluindo a lógica de integração com a API do Ollama e tratamento de erros de conexão.
- **`/data`**: Base de dados contendo históricos de transações, perfis de investidores e catálogos de produtos financeiros.
- **`/docs`**: Documentação detalhada do projeto:
  - `01-documentacao-agente.md`: Arquitetura, persona e objetivos da Jay.
  - `02-base-conhecimento.md`: Fundamentos técnicos e dados de suporte.
  - `03-prompts.md`: Engenharia de prompt utilizada para especializar a IA.
  - `04-metricas.md`: Indicadores de desempenho e sucesso do agente.
  - `05-pitch.md`: Apresentação da proposta de valor.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**: Linguagem base do projeto.
- **Streamlit**: Framework para a interface web do chat.
- **Ollama (Llama 3)**: Motor de IA para processamento local (privacidade de dados).
- **Requests**: Biblioteca para comunicação com a API local do Ollama.

## ⚙️ Como Executar
1. **Certifique-se de que o Ollama está instalado e a correr:**
   ```bash
   ollama run llama3

   Instale as dependências necessárias:
2. **Instale as dependências necessárias:**
    ```bash
    pip install streamlit requests
    
3. **Inicie a aplicação:**
   ```bash
   streamlit run src/app.py

## 📝 Notas de Desenvolvimento
Este projeto foi evoluído a partir de um desafio de bootcamp (DIO), onde a estrutura original foi personalizada e corrigida para implementar rotinas de segurança (ajuste de protocolos SSL/HTTP), tratamento de exceções de API (KeyErrors/404) e uma interface focada na experiência do utilizador.
