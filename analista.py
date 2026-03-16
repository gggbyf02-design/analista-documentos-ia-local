from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
import os

llm = OllamaLLM(model="llama3.2")

def processar_documento():
    print("\n=== ANALISTA DE DOCUMENTOS PROFISSIONAL ===")
    nome_arquivo = input("Digite o nome do arquivo (ex: documento.pdf): ")

    if not os.path.exists(nome_arquivo):
        print("Erro: Arquivo não encontrado!")
        return

    loader = PyPDFLoader(nome_arquivo)
    paginas = loader.load()
    
    # Vamos pegar as páginas 10 a 30, onde as leis costumam começar nesse PDF
    conteudo_focado = "\n".join([p.page_content for p in paginas[10:30]])

    pergunta = input("\nO que você deseja saber? ")

    prompt = f"""
    Você é um assistente que analisa o livro 'As 48 Leis do Poder'.
    Baseado APENAS no texto abaixo, responda de forma direta.
    Se não encontrar a resposta exata, diga que não encontrou.

    TEXTO:
    {conteudo_focado}

    PERGUNTA:
    {pergunta}
    """

    print("\nAnalisando...")
    resposta = llm.invoke(prompt)
    print(f"\nRESPOSTA DA IA:\n{resposta}")

processar_documento()
