import os

os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from .tools.tools import web_search, index_data, retrieval


root_agent = Agent(
    model=LiteLlm("ollama_chat/nemotron-3-nano:30b-cloud"),
    name="root_agent",
    description="Agente de soporte para estudiantes de programación",
    instruction="""
    Sos un agente de soporte para estudiantes de programación.

    Tu objetivo es ayudar al usuario a resolver consultas relacionadas
    con programación.

    Cuando una pregunta necesite información actualizada de internet,
    utiliza la herramienta web_search.

    Cuando el usuario solicite guardar información o un apunte,
    utiliza la herramienta index_data.

    Si alguna herramienta devuelve un error o no encuentra resultados,
    informa claramente al usuario.

    Respondé de forma clara y sencilla.

    Cuando el usuario consulte información guardada previamente,
    utiliza la herramienta retrieval.
    """,
    tools=[web_search, index_data, retrieval],
)
