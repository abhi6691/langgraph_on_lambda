from typing import Any, Dict
from app import create_graph
from bedrock_managedapps_base import BedrockManagedAppsBase
from langgraph.checkpoint.memory import MemorySaver

from aws_lambda_powertools import Logger

logger = Logger(service="custom-langgraph-app")

class CustomLanggraphApp(BedrockManagedAppsBase):
    def initialize(self):
        # logger.info("Initializing CustomLanggraphApp")
        self.app = create_graph().compile(MemorySaver())

    def invoke(self, event: Dict[str, Any], context: Any):
        # logger.info("Invoking CustomLanggraphApp")
        input = event.get("inputs", {})
        config = event.get("config", {})

        return self.app.invoke(input=input, config=config)
    
    def stream(self, event: Dict[str, Any], context: Any):
        # logger.info("Streaming CustomLanggraphApp")
        input = event.get("inputs", {})
        config = event.get("config", {})

        for output in self.app.stream(input=input, config=config):
            yield {"output": output}