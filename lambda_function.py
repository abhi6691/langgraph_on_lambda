#! /usr/bin/env python

import json

from aws_lambda_powertools import Logger

from custom_app import CustomLanggraphApp

logger = Logger(service="handler")

app_instance = CustomLanggraphApp()

# Initialize the application on the first load
app_instance.initialize()

def handler(event, context):
    for response in app_instance.stream(event, context):
        logger.info(f"Response: {response}")
        yield json.dumps({"output": response}) + "\n"
 

    