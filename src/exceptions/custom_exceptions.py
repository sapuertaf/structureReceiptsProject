import traceback
import json


class CapturedException(Exception):
    """
    Custom exception class for capturing and providing detailed information about an exception.

    Attributes:
        _message (str): The error message.
        _original_error (Exception, optional): The original exception that occurred. Defaults to None.

    Args:
        message (str): The error message.
        source_error (Exception, optional): The original exception that occurred. Defaults to None.
    """
    def __init__(
            self,
            message: str,
            source_error: Exception = None
    ):
        """
        Initializes the CapturedException with an error message and an optional original exception.

        Args:
            message (str): The error message.
            source_error (Exception, optional): The original exception that occurred. Defaults to None.
        """
        self._message = message
        self._original_error = source_error
        super().__init__(self._message)

    def _get_traceback_info(self) -> list:
        """
        Retrieves traceback information from the original error.

        Returns:
            list: A list of strings containing traceback information.
        """
        traceback_list = traceback.extract_tb(self._original_error.__traceback__)
        return [
            f"{frame.filename} line {frame.lineno} {frame.name}"
            for frame in traceback_list
        ]

    def _to_dict(self):
        """
        Converts the exception information to a dictionary.

        Returns:
            dict: A dictionary containing exception information.
        """
        return {
            "message": self._message,
            "source": self._get_traceback_info(),
            "original_error": str(self._original_error)
        }

    def __str__(self):
        """
        Returns a string representation of the exception.

        Returns:
            str: A string representation of the exception in JSON format.
        """
        return json.dumps(self._to_dict())


class ProcessError(CapturedException):
    """Exception raised when there is an error during the execution of a pipeline stages."""


class CheckConfigsError(CapturedException):
    """Exception raised when there is an error during the execution of a pipeline stages."""


class AskPromptError(CapturedException):
    """raise this when there's a validation error"""


class StructureDataError(CapturedException):
    """raise this when there's a validation error"""


class GetCloudStorageImgError(CapturedException):
    """raise this when there's a validation error"""


class JsonifyResponseError(CapturedException):
    """raise this when there's a validation error"""


class Load2BigQueryError(CapturedException):
    """raise this when there's a validation error"""


class BuildError(CapturedException):
    """raise this when there's a validation error"""


class NotExistingLoggerError(CapturedException):
    """"""
