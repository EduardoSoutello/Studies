
from dotenv import load_dotenv
from langchain import PromptTemplate
from groq import Groq
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

#last functional model "llama-3.1-8b-instant"

numero_dias = 7
numero_criancas = 2
atividade = "praia"

modelo_de_prompt = PromptTemplate.from_template(
    template="""
    Crie um roteiro de viagem de {dias},
    para uma familia com {numero_criancas} crianças,
    que gostam de {atividade}
    """
)

prompt = modelo_de_prompt.format(
    dias=numero_dias, 
    numero_criancas=numero_criancas, 
    atividade=atividade
)

print("Prompt : \n", prompt)


modelo = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
resposta = modelo.choices[0].message.content
print(resposta)