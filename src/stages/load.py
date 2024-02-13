from interfaces.config import Config
from interfaces.event_logger import EventLoggerInterface
from exceptions.custom_exceptions import (
    CheckConfigsError,
    Load2BigQueryError,
    BuildError,
)

from dynaconf.base import LazySettings
from pandas import DataFrame
from pandas_gbq import to_gbq


class LoadStage:
    """A class for loading data into a BigQuery table in batches using Pandas.

    Attributes:
        _config (LazySettings): An instance of LazySettings representing the configuration settings.
        _load_data (DataFrame or None): The data to be loaded into the BigQuery table.

    Args:
        config (Config): A configuration object.
    """
    def __init__(self, config: Config, event_logger: EventLoggerInterface):
        """Initialize the LoadStage.

        Args:
            config (Config): A configuration object.
        """
        self._config: LazySettings = config.get()
        self._event_logger = event_logger
        self._load_data: None or DataFrame = None

    @property
    def load_data(self) -> None or DataFrame:
        return self._load_data

    @load_data.setter
    def load_data(self, new_load_data: DataFrame):
        self._load_data = new_load_data

    def _check_configs(self) -> 'LoadStage':
        """Check the required configurations.

        Raises:
            CheckConfigsError: Raised if required configurations are missing.
        """
        try:
            if (self._config.get("BIGQUERY_CONFS").get("TABLE_PATH") is not None
                    and
                    self._config.get("BIGQUERY_CONFS").get("TABLE_PATH") != ""):
                return self
        except AttributeError as e:
            raise CheckConfigsError(f"An error occurred while checking the required configurations for {__name__}", e)
        raise CheckConfigsError(f"An error occurred while checking the required configurations for {__name__}")

    def _load_2_bigquery(self) -> None:
        """Load the data into BigQuery.

        Raises:
            Load2BigQueryError: Raised if there is an error while loading data into BigQuery.
        """
        try:
            to_gbq(self._load_data,
                   self._config.get("BIGQUERY_CONFS").get("TABLE_PATH"),
                   project_id=self._config.get("BIGQUERY_CONFS").get("PROJECT_ID"),
                   if_exists="append")
        except Exception as e:
            raise Load2BigQueryError("An error occurred while trying to load data to BigQuery", e)

    def build(self, load_data: DataFrame = None) -> 'LoadStage':
        """Build the LoadStage.

        Args:
            load_data (DataFrame, optional): The data to be loaded. Defaults to None.

        Raises:
            BuildError: Raised if the data to be loaded is not provided.
        """
        if self._load_data is None and load_data is None:
            raise BuildError("")
        self._load_data = load_data
        self._check_configs()
        return self

    def execute(self) -> None:
        """Execute the data loading process."""
        self._event_logger.info("Loading to BigQuery process about to execute")
        self._load_2_bigquery()
