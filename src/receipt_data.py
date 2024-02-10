from exceptions.custom_exceptions import StructureDataError

from pandas import DataFrame


class ReceiptData:
    """
    A class representing receipt data that can be either unstructured or structured.

    Attributes:
        _unstructured_data (list): The unstructured receipt data in list format.
        _structured_data (None or DataFrame): The structured receipt data in DataFrame format.

    Args:
        unstructured_json_data (list): The unstructured receipt data in list format.
    """
    def __init__(self, unstructured_json_data: list):
        """
        Initializes the ReceiptData with unstructured receipt data.

        Args:
            unstructured_json_data (list): The unstructured receipt data in list format.
        """
        self._unstructured_data = unstructured_json_data
        self._structured_data: None or DataFrame = None

    @property
    def unstructured_data(self):
        """
        Getter method for accessing the unstructured receipt data.

        Returns:
            list: The unstructured receipt data in list format.
        """
        return self._unstructured_data

    @unstructured_data.setter
    def unstructured_data(self, new_unstructured_json_data):
        """
        Setter method for updating the unstructured receipt data.

        Args:
            new_unstructured_json_data (list): The new unstructured receipt data.
        """
        self._unstructured_data = new_unstructured_json_data

    def structure_data(self) -> DataFrame:
        """
        Converts unstructured receipt data into structured DataFrame.

        Raises:
            ValueError: If there is an issue with structuring the data.

        Returns:
            DataFrame: The structured receipt data in DataFrame format.
        """
        try:
            self._structured_data = DataFrame(self._unstructured_data)
        except Exception as e:
            raise StructureDataError("", e)
        return self._structured_data


if __name__ == "__main__":
    import json
    mock_json = """
    [{
        "persona" : "Juan Perez",
        "direccion": "Calle n #x-y"
    }]
    """
    receipt = ReceiptData(json.loads(mock_json)).structure_data()
    print(receipt)
