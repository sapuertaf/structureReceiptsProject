from interfaces.config import Config

from dynaconf import Dynaconf


class CloudConfig(Config):
    """A class for managing configuration settings."""

    _conf = None

    @classmethod
    def get(cls) -> Dynaconf:
        """Retrieve the configuration settings.

        Returns:
            Dynaconf: The configuration settings.

        """
        if cls._conf is None:
            cls._conf = Dynaconf(settings_files=["config.yaml"])

        return cls._conf


if __name__ == "__main__":
    print((CloudConfig().get()).to_dict())
