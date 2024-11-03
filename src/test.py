import json
import boto3

def invoke_lambda_with_response_stream(function_name):
    """Invokes a Lambda function with response streaming and prints the streamed chunks."""

    lambda_client = boto3.client('lambda')

    event_payload = {
        "inputs": {
            "messages": "What's the weather in Redmond like today?"
        },
        "config": {
            "thread_id": "123"
        }
    }

    response = lambda_client.invoke_with_response_stream(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(event_payload).encode('utf-8')
    )

    if 'EventStream' in response:
        event_stream = response['EventStream']

    for event in event_stream:
        print(f"event: {event}")
        if 'PayloadChunk' in event:
            payload_json = event['PayloadChunk']['Payload'].decode('utf-8')
                
            # Convert the JSON string to a dictionary
            payload_data = json.loads(payload_json)
            
            # Access the "output" field in the payload
            output = payload_data.get("output", "")
            print(output)
        elif 'InvokeComplete' in event:
            print("Streaming complete.")

if __name__ == "__main__":
    function_name = "arn:aws:lambda:us-west-2:061994666073:function:LanggraphOpenSourceConstructs"  # Replace with your actual function name
    invoke_lambda_with_response_stream(function_name)