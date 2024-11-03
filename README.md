## Local Testing
```
IMAGE_ID=$(docker build -t langgraph-on-lambda . -q)
docker run -p 9000:8080 $IMAGE_ID
```

In another terminal:
```
curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -H "Content-Type: application/json" -d '{
    "inputs": {
        "messages": "What'\''s the weather in Redmond like today?"
    },
    "config": {
        "thread_id": "123"
    },
    "context": {
        "streaming_config": {
            "stream_mode": "values"
        }
    }
}'
```