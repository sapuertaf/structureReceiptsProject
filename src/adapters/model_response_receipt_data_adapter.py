import json
from exceptions.custom_exceptions import JsonifyResponseError


class ModelResponseReceiptDataAdapter:
    """
    A class that adapts a Model class response containing JSON-formatted data related to receipts.

    Attributes:
        _model_response (str): The original model response containing JSON-formatted data.

    Args:
        model_response (str): The model response in string format.
    """
    def __init__(self, model_response: str):
        """
        Initializes the ModelResponseReceiptDataAdapter with the provided model response.

        Args:
            model_response (str): The model response in string format.
        """
        self._model_response = model_response

    def jsonify_response(self) -> list:
        """
        Parses and converts the model response into a list format.

        Raises:
            ValueError: If there is an issue with parsing the model response.

        Returns:
            list: The JSON-formatted data converted into a list.
        """
        model_response = (self._model_response.replace('```\n', ''))\
            .replace('\n```', '')
        try:
            model_response = json.loads(model_response)
            jsonified_response: list = model_response if isinstance(model_response, list) else [model_response]
            return jsonified_response
        except Exception as e:
            raise JsonifyResponseError("An error occurred while transforming the model's response to JSON", e)


if __name__ == "__main__":
    mock_response = """
    {
        "persona" : "Juan Perez",
        "direccion": "Calle n #x-y"
    }
    """
    print(ModelResponseReceiptDataAdapter(mock_response).jsonify_response())