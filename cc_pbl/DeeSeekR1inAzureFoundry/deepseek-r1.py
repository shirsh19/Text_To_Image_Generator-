import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Set your environment variables or replace with your actual values
endpoint = "https://rajsh-m9on6bbo-swedencentral.cognitiveservices.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01"
api_key = "D4rpkVYXR4zT09sV2nOBIrwrTU0tyR92L1ej1gBVjfTgbq52AYHeJQQJ99BDACfhMk5XJ3w3AAAAACOG99ga"

# Initialize the client
client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Define the messages for the chat
messages = [
    {"role": "system", "content": "You are a math expert who explains concepts in a simple way."},
    {"role": "user", "content": "Can you explain the Pythagorean Theorem in simple terms?"}
]

# Send the request to the DeepSeek API
response = client.complete(
    messages=messages,
    max_tokens=200,
    stream=False
)

# Process and display the response
for choice in response.choices:
    print(f"Assistant: {choice.message['content']}")
