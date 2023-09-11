# this is a demo of how to use the OpenAI API with Azure APIM
# the headers are required to be passed in the request 

import os
import openai
openai.api_type = "azure"
openai.api_base = "<TEPLACE_WITH_AZURE_APIM_ENDPOINT>"
openai.api_version = "2023-07-01-preview"
openai.api_key = "<REPLACE_WITH_APIM_KEY>"

response = openai.ChatCompletion.create(
  engine="gpt-35-turbo",
  messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"hi"}],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  headers={
    "Ocp-Apim-Subscription-Key": openai.api_key,
  },
  stop=None)

print(response['choices'][0]['message']['content'])


