from abc import ABC, abstractmethod

from vertexai.preview.generative_models import Part


class ModelInterface(ABC):
    """
    Interface for models.

    This abstract class defines the interface for model classes.

    Args:
        ABC (type): ABC class for defining abstract base classes.

    Attributes:
        Any: This class may have attributes specific to different implementations.

    Methods:
        build: Abstract method to build the model.
        ask_prompt: Abstract method to prompt the model with an image.
    """
    @abstractmethod
    def build(self):
        """Abstract method to build the model.

        This method should be implemented by concrete subclasses to build
        the model.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        ...

    @abstractmethod
    def ask_prompt(self, img: Part) -> str:
        """
        Abstract method to prompt the model with an image.

        This method should be implemented by concrete subclasses to prompt
        the model with an image and return a response.

        Args:
            img (Part): The image to prompt the model with.

        Returns:
            str: The response from the model.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        ...
