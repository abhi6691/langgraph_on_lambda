from abc import ABC, abstractmethod
from typing import Any, Dict, Union


class BedrockManagedAppsBase(ABC):
    def __init__(self):
        super().__init__()

    def __new__(cls, *args, **kwargs):
        if args or kwargs:
            raise TypeError("This class does not accept parameters in the constructor.")
        return super().__new__(cls)

    def initialize():
        """
        Application initialization. Ran once at the time of app environment setup.
        """
        pass

    @abstractmethod
    def invoke(self, event: Dict[str, Any], context: Any):
        """
        Application invocation. Ran for every invocation of the application.

        Args:
            event (Dict[str, Any]): Event data. Contains the Langgraph payload
            context (Any): Context data provided by service. May contain details such 
            as streaming_config.
        """
        pass

    def destory():
        """
        Application destory. Ran once at the time of app environment teardown.
        """
        pass