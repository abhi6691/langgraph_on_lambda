#! /usr/bin/env python

import json, boto3
from typing import Generator
import time

client = boto3.client("bedrock-runtime")

def generate_stream() -> Generator[str, None, None]:
    """
    Generator function that yields dummy data in chunks,
    simulating a streaming response.
    """
    yield "Starting the stream...\n"
    time.sleep(1)
    
    for i in range(1, 6):
        yield f"Chunk {i}: Here's some data!\n"
        time.sleep(1)  # Simulate processing time
    
    yield "Stream complete!\n"

def handler(event, context):
    for response in generate_stream():
        yield json.dumps({"output": response}) + "\n"
 

    