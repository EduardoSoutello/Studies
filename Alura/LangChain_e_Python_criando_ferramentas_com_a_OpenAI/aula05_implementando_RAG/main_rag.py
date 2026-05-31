# type: ignore
# pyright: ignore[reportMissingImports]

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Carrega as variáveis de ambiente (.env)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Configura o modelo Groq para geração (Llama 3.3)
modelo = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.5, 
    api_key=api_key
)

# 3. Inicializa os Embeddings locais do Hugging Face (Gratuito e local)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Lista dos arquivos PDF (ajustados para a pasta anterior devido ao CWD ser aula05_implementando_RAG)
arquivos = [
    "../documentos/GTB_standard_Nov23.pdf",
    "../documentos/GTB_gold_Nov23.pdf",
    "../documentos/GTB_platinum_Nov23.pdf"
]

# 5. Carrega o conteúdo de cada PDF
documentos = sum(
    [
        PyPDFLoader(arquivo).load() for arquivo in arquivos
    ], []
)

# 6. Divide os documentos em pedaços menores (chunks)
pedacos = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=100
).split_documents(documentos)

# 7. Cria a base vetorial FAISS usando os embeddings locais e cria o retriever
dados_recuperados = FAISS.from_documents(
    pedacos, embeddings
).as_retriever(search_kwargs={"k": 2})

# 8. Define o prompt com base no modelo do professor
prompt_consulta_seguro = ChatPromptTemplate.from_messages(
    [
        ("system", "Responda usando exclusivamente o conteúdo fornecido"),
        ("human", "{query}\n\nContexto: \n{contexto}\n\nResposta:")
    ]
)

# 9. Monta a cadeia usando LCEL e ligando ao modelo do Groq
cadeia = prompt_consulta_seguro | modelo | StrOutputParser()

# 10. Função para responder perguntas buscando o contexto nos trechos indexados
def responder(pergunta: str):
    trechos = dados_recuperados.invoke(pergunta)
    contexto = "\n\n".join(um_trecho.page_content for um_trecho in trechos)
    return cadeia.invoke({
        "query": pergunta, "contexto": contexto
    })

# 11. Executa a pergunta final
print(responder("Como devo proceder caso tenha um item comprado roubado e caso eu tenha o cartão platinum"))
