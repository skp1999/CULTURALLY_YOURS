from openai import AzureOpenAI
import json
import os
import requests


def get_deployment_and_client(model):

    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("ENDPOINT_URL")

    if(model == 'gpt35'):
        deployment = os.getenv("DEPLOYMENT_NAME", "gpt35turbo") #gpt35turbo, gpt-4-turbo
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key, #azure_ad_token_provider=token_provider,
            api_version="2024-05-01-preview", #2024-02-15-preview, 2024-05-01-preview
        )
    elif(model == 'gpt4'):
        deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4-turbo") 
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key, #azure_ad_token_provider=token_provider,
            api_version="2024-02-15-preview", #2024-02-15-preview, 2024-05-01-preview
        )
    elif(model == 'gpt4o'):
        deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o") 
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key, #azure_ad_token_provider=token_provider,
            api_version="2024-02-15-preview", #2024-02-15-preview, 2024-05-01-preview
        )
    
    return deployment, client


def generate_output(deployment, client, messages):

    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.0,
        max_tokens=4096
    )

    generated_text = response.choices[0].message.content.strip()
    return json.loads(generated_text)

def predict(payload):

    query_parameters = payload

    model = 'gpt4o'
    print(f'Using {model} in the backend !!!')
    deployment, client = get_deployment_and_client(model)

    messages = query_parameters['messages']
    response = generate_output(deployment, client, messages)
    
    return response
