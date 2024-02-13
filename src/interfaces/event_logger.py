from abc import ABC, abstractmethod


class EventLoggerInterface(ABC):
    @abstractmethod
    def build(self):
        ...

    @abstractmethod
    def info(self, message: str) -> None:
        ...

    @abstractmethod
    def error(self, error: Exception or str) -> None:
        ...
