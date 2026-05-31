
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain.prompts import ChatPromptTemplate
from pydantic import Field, BaseModel 
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um guia de viagem especializado em destinos. Apresente-se como Sr. Passeio Paul"), 
        ("placeholder", "{historico}"),
        ("human", "{query}")
    ]

)

class Destino(BaseModel):
    cidade: str = Field(description="A cidade recomendada para visitar")
    motivo: str = Field(description="Motivo pelo qual é interessante visitar essa cidade")

class Restaurante(BaseModel):
    cidade: str = Field(description="A cidade recomendada para visitar")
    nome: str = Field(description="Restaurantes recomendados na cidade")

parseador_destino = JsonOutputParser(pydantic_object=Destino) #transforma a resposta em um estilo de json, e depois transforma esse json em um objeto do tipo Destino
parseador_restaurante = JsonOutputParser(pydantic_object=Restaurante)

# Wrapper simples para Groq, simulando interface de chain
class GroqWrapper:
    def __init__(self, client, model="llama-3.1-8b-instant", temperature=0.5):
        self.client = client
        self.model = model
        self.temperature = temperature

    def invoke(self, prompt_vars: dict, prompt_template: PromptTemplate):
        prompt_text = prompt_template.format(**prompt_vars)
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt_text}]
        )
        return response.choices[0].message.content

# Exemplo de uso:
prompt_cidade = PromptTemplate.from_template(
    "Sugira uma cidade dado o meu interesse por {interesse}."
    "{formato_de_saida}",
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()}

)

prompt_restaurante = PromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}."
    "{formato_de_saida}",
    partial_variables={"formato_de_saida": parseador_restaurante.get_format_instructions()}
    
)

prompt_cultura = PromptTemplate.from_template(
    "Sugira atividades e locais culturais para visitar em {cidade}."
    
)

groq_model = GroqWrapper(client)


# Funções que simulam as chains (cadeias)
def cadeia_restaurantes(cidade):
    resposta = groq_model.invoke({"cidade": cidade}, prompt_restaurante)
    return parseador_restaurante.parse(resposta)

def cadeia_cultural(cidade):
    resposta = groq_model.invoke({"cidade": cidade}, prompt_cultura)
    return StrOutputParser().parse(resposta)

# Exemplo de uso das cadeias:
interesse = "praias"
resposta_cidade = groq_model.invoke({"interesse": interesse}, prompt_cidade)
resultado_cidade = parseador_destino.parse(resposta_cidade)
print("Destino sugerido:", resultado_cidade)

restaurantes = cadeia_restaurantes(resultado_cidade["cidade"])
print("Restaurantes sugeridos:", restaurantes)

cultura = cadeia_cultural(resultado_cidade["cidade"])
print("Atividades culturais sugeridas:", cultura)