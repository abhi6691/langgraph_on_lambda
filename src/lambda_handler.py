from custom_app import CustomLanggraphApp

from aws_lambda_powertools import Logger

logger = Logger(service="handler")

app_instance = CustomLanggraphApp()

# Initialize the application on the first load
app_instance.initialize()

def lambda_handler(event, context):    
    response = app_instance.invoke(event, context)
    logger.info(f"response: {response}")

    return response["messages"][-1].content
    