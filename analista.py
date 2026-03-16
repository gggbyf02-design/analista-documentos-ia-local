from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_ollama import OllamaLLM
import os

# Configura o modelo Llama 3.2 que você já tem no PC
llm = OllamaLLM(model="llama3.2")

def processar_documento():
    print("\n=== ANALISTA DE DOCUMENTOS PRIVADO ===")
    nome_arquivo = input("Digite o nome do arquivo com extensão (ex: teste.txt ou aula.pdf): ")
    
    if not os.path.exists(nome_arquivo):
        print("Erro: Arquivo não encontrado nesta pasta!")
        return

    print(f"Lendo {nome_arquivo}...")
    
    # Escolhe o leitor certo conforme a extensão
    if nome_arquivo.endswith(".pdf"):
        loader = PyPDFLoader(nome_arquivo)
    else:
        loader = TextLoader(nome_arquivo, encoding="utf-8")

    docs = loader.load()
    conteudo = "\n".join([d.page_content for d in docs])

    pergunta = input("\nO que você deseja saber sobre este documento? ")

    # Monta a instrução para a IA
    prompt = f"""
    Você é um assistente de IA especializado em análise de documentos.
    Use o conteúdo abaixo para responder à pergunta de forma clara e em português.
    
    CONTEÚDO:
    {conteudo[:3000]}  # Limita para não travar a memória
    
    PERGUNTA:
    {pergunta}
    """

    print("\nIA Analisando...")
    resposta = llm.invoke(prompt)
    print(f"\nRESPOSTA DA IA:\n{resposta}")

if __name__ == "__main__":
    processar_documento()