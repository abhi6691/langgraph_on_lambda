# Use the official AWS Lambda Python 3.8 base image
FROM public.ecr.aws/lambda/python:3.9

# Copy all necessary files into the container
# Assuming lambda_handler.py, bedrock_managedapps_base.py, document_loader.py, 
# graph_workflow.py, vector_store.py, and other dependencies are in the same directory
COPY src/ ${LAMBDA_TASK_ROOT}

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

RUN curl -L -o /usr/bin/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie
RUN chmod +x /usr/bin/aws-lambda-rie

# Set the Lambda handler function
CMD ["lambda_handler.lambda_handler"]
