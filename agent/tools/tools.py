from ddgs import DDGS
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def web_search(query: str, max_results: int = 5):
    """
    Herramienta para realizar búsquedas en internet.

    Args:
        query: consulta que se desea buscar.
        max_results: cantidad máxima de resultados.
    """
    try:
        if not query or not query.strip():
            return "Error: la consulta no puede estar vacía."

        if max_results < 1 or max_results > 10:
            return "Error: max_results debe estar entre 1 y 10."

        results = DDGS().text(query=query, max_results=max_results)

        results = list(results)

        if not results:
            return "No se encontraron resultados."

        return results

    except Exception as e:
        return f"Error al realizar la búsqueda: {str(e)}"


def index_data(query: str, collection_name: str):
    """
    Herramienta para guardar información en una base de datos vectorial.

    Args:
        query: texto que se desea guardar.
        collection_name: nombre de la colección donde se guardará.
    """
    try:
        if not query or not query.strip():
            return "Error: no hay información para guardar."

        if not collection_name or not collection_name.strip():
            return "Error: debe indicar un nombre de colección."

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

        docs = text_splitter.create_documents([query])

        vector_store = Chroma(
            embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
            persist_directory="./vector_store",
            collection_name=collection_name,
        )

        results = vector_store.add_documents(documents=docs)

        return f"Información guardada correctamente. Documentos vectorizados: {len(results)}"

    except Exception as e:
        return f"Error al guardar información: {str(e)}"
