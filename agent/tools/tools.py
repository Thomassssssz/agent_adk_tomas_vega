from ddgs import DDGS


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
