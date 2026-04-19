import json
import pandas as pd
import requests
import streamlit as st

# ========================= CONFIGURAÇÃO ==========================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ======================== CARREGAR DADOS  ========================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

#  ======================== MONTAR CONTEXTO  ========================
contexto = f"""
CLIENTE: {perfil['nome']}. {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ======================== SYSTEM PROMPT ========================
SYSTEM_PROMPT = """Você é a Jay, uma educadora financeira amigável e didática.

OBEJTIVO: 
Ensinar conceitos de finanças pessoais de forma simples, usando os dados de cliente como exemplo práticos.

REGRAS:
 - NUNCA recomende investimentos específicos, apneas explique como funcionam;
 - JAMAIS responda a pergunta fora do tema ensino de finanças finaceiras pessoais;
 - Quando ocorrer, responda lembrando o seu papel de educador financeiro;
 - Use os dados forncecidos para dar exemplos personalizados.
 - Linguagem simples, como se explicasse ara um amigo;
 - Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
 - Sempre Pergunte se o cliente entendeu;
 - Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""
# =============== CHAMA OLLAMA ==================
def perguntar(pergunta):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {perguntar}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ====================== INTERFACE =====================
st.title("🎓 Jay, a Educadora Financeira")

pergunta = st.chat_input("Sua dúvida sobre finanças...")
if pergunta:
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
