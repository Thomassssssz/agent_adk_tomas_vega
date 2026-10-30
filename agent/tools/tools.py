from ddgs import DDGS
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


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


def retrieval(query: str, collection_name: str, k: int = 5):
    """
    Herramienta para recuperar información de una base de datos vectorial.

    Args:
        query: consulta que se desea buscar.
        collection_name: nombre de la colección donde buscar.
        k: cantidad máxima de resultados.
    """
    try:
        if not query or not query.strip():
            return "Error: la consulta no puede estar vacía."

        if not collection_name or not collection_name.strip():
            return "Error: debe indicar un nombre de colección."

        if k < 1:
            return "Error: k debe ser mayor que cero."

        vector_store = Chroma(
            embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
            persist_directory="./vector_store",
            collection_name=collection_name,
        )

        results = vector_store.similarity_search_with_relevance_scores(query=query, k=k)

        if not results:
            return "No se encontró información relacionada."

        return results

    except Exception as e:
        return f"Error al recuperar información: {str(e)}"

    import chromadb


def list_collection():
    """
    Herramienta para listar las colecciones disponibles
    en la base de datos vectorial.
    """
    try:
        client = chromadb.PersistentClient(path="./vector_store")

        collections = client.list_collections()

        if not collections:
            return "No hay colecciones disponibles."

        return [collection.name for collection in collections]

    except Exception as e:
        return f"Error al listar colecciones: {str(e)}"
