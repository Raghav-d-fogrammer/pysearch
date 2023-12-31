import os
import requests
import json
import openai
from helper import Helper
from langchain.embeddings import OpenAIEmbeddings

#openai.api_key = os.getenv("AZURE_OPENAI_KEY")
#openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")


class AI:
    def get_open_ai_embedding(self):
       return OpenAIEmbeddings(
          deployment=deployment__embd_name,
          openai_api_base=openai.api_base,
          openai_api_type="azure",
          openai_api_key="7b7d41f1856e43dfaf6cfd5576f765dc",
          chunk_size=1
       )
    def promptCompletion(self, prompt):
        try:
            response = openai.Completion.create(
                engine = deployment_name,
                prompt = prompt,
                temperature = 0.7,
                max_tokens = 500
            )
            content = response.choices[0].text
            #jsonContent = json.loads(content)
            return content
        except openai.error.Timeout as e:
           Helper.makeError("OpenAI API request timed out: {e}")
        except openai.error.APIError as e:
           Helper.makeError("OpenAI API returned an API Error: {e}")
        except openai.error.APIConnectionError as e:
           Helper.makeError("OpenAI API request failed to connect: {e}")
        except openai.error.InvalidRequestError as e:
           Helper.makeError("OpenAI API request was invalid: {e}")
        except openai.error.AuthenticationError as e:
           Helper.makeError("OpenAI API request was not authorized: {e}")
        except openai.error.PermissionError as e:
           Helper.makeError("OpenAI API request was not permitted: {e}")
        except openai.error.RateLimitError as e:
           Helper.makeError("OpenAI API request exceeded rate limit: {e}")

    def prompt(self, system_prompt, user_prompt):

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
           ]
        try:
            response = openai.ChatCompletion.create(
                engine = deployment_name,
                messages = messages,
                temperature = 0.9,
                max_tokens = 1000
            )
            content = response.choices[0].message.content
            #jsonContent = json.loads(content)
            return content
        except openai.error.Timeout as e:
           Helper.makeError("OpenAI API request timed out: {e}")
        except openai.error.APIError as e:
           Helper.makeError("OpenAI API returned an API Error: {e}")
        except openai.error.APIConnectionError as e:
           Helper.makeError("OpenAI API request failed to connect: {e}")
        except openai.error.InvalidRequestError as e:
           Helper.makeError("OpenAI API request was invalid: {e}")
        except openai.error.AuthenticationError as e:
           Helper.makeError("OpenAI API request was not authorized: {e}")
        except openai.error.PermissionError as e:
           Helper.makeError("OpenAI API request was not permitted: {e}")
        except openai.error.RateLimitError as e:
           Helper.makeError("OpenAI API request exceeded rate limit: {e}")

#ai = AI()
#ai.prompt("How to go to a school?")
