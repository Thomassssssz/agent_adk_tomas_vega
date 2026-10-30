import os

os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm("ollama_chat/nemotron-3-nano:30b-cloud"),
    name="root_agent",
    description="Agente de soporte para estudiantes de programación",
    instruction="""
    Sos un agente de soporte para estudiantes de programación.

    Tu objetivo es ayudar al usuario a resolver consultas relacionadas
    con programación.

    Respondé de forma clara y sencilla.
    """,
)
