from abc import ABC, abstractmethod


class Config(ABC):
    """
    Interface for configuration classes.

    This abstract class defines the interface for configuration classes.

    Args:
        ABC (type): ABC class for defining abstract base classes.

    Attributes:
        Any: This class may have attributes specific to different implementations.

    Methods:
        get: Abstract method to retrieve configuration.    
    """
    @classmethod
    @abstractmethod
    def get(cls):
        """
        Abstract method to retrieve configuration.

        This method should be implemented by concrete subclasses to provide
        specific configuration retrieval logic.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        ...
