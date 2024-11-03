from custom_app import CustomLanggraphApp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = CustomLanggraphApp()
app.initialize()
logger.info("App initialized")

result = app.invoke(event={
    "inputs": {
        "messages": "What's the weather in Redmond like today?"
    },
    "config": {
        "thread_id": "123"
    }
}, context={})

logger.info(f"\n\nApp invoked without stream, response: {result}")

result = app.invoke(event={
    "inputs": {
        "messages": "What's the weather in Redmond like today?"
    },
    "config": {
        "thread_id": "123"
    }
}, context={"streaming_config": {"stream_mode": "values"}})

logger.info(f"\n\nApp invoked with stream, response: {result}")