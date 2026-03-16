from langchain_community.llms import Ollama

# Conectando ao modelo que você acabou de baixar com sucesso
llm = Ollama(model="llama3.2")

print("\n--- SISTEMA DE IA LOCAL INICIALIZADO ---")
pergunta = "Como um Engenheiro de IA iniciante, qual deve ser meu próximo projeto usando Python e Ollama?"

print("Sua IA está processando a resposta (isso pode levar alguns segundos)...")
resposta = llm.invoke(pergunta)

print("\nRESPOSTA DA IA:")
print(resposta)
print("\n----------------------------------------")