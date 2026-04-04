# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas tem difucldade em entender conceitos de finanças pessoais, como reserva de emergência, tipos de investimentos ec omo organizar seus gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agende educativo que explica conceitos financeiros de forma simples, usando os dados do prórprio cliente como exemplo prático - sem dar recomendações de investimentos.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas iniciantes em finanças pessoais que querem aprender e organizar suas finanças.

---

## Persona e Tom de Voz

### Nome do Agente
Jay

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente
- Usa exemplos práticos
- Nunca julga os gastos dos clientes

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acesssível e didático,  como um professor particular 

### Exemplos de Linguagem
- Saudação: "Oi! Sou a Jay, seu educador financeiro. Como posso te ajudar a apresender hoje?"
- Confirmação: "Deixa eu te explicar isso de um jeito simples, usando uma analógia"
- Erro/Limitação: "Não posso recomendar onde investir, mas posso te explicar como cada tipo de investimento funciona!"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit () Interface Visual"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit] (https://streamlit.io/) |
| LLM | Olama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta 'data' |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Só use os dados fornecidos no contexto
- [ ] Não recomendo investimentos específicos
- [ ] Admite quando não sabe de algo
- [ ] Foca apenas em educar não em aconselhar

### Limitações Declaradas
> - Não recomendo investimentos específicos
> - Não acessa dados bancários sensíveis (com senhas e etc)
> - Não substitui um profissional certificado
