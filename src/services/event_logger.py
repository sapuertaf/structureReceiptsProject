from interfaces.event_logger import EventLoggerInterface
from exceptions.custom_exceptions import NotExistingLoggerError

from logging import Logger, basicConfig, INFO, getLogger


class EventLogger(EventLoggerInterface):
    def __init__(self, name: str = __name__):
        self._name = name
        self._logger: None or Logger = None

    def build(self) -> 'EventLogger':
        basicConfig(level=INFO)
        self._logger = getLogger(self._name)
        self._logger.setLevel(INFO)
        return self

    def _check_existing_logger(self) -> None:
        if self._logger is None:
            raise NotExistingLoggerError("The event logger is not setup correctly try EventLogger.build() first")

    def info(self, message: str):
        self._check_existing_logger()
        self._logger.info(message)

    def error(self, error: Exception or str):
        self._check_existing_logger()
        self._logger.error(error)


if __name__ == "__main__":
    logger = EventLogger().build()
    logger.info("Informative message")
