import os
import requests
import json
import openai
from helper import Helper

#openai.api_key = os.getenv("AZURE_OPENAI_KEY")
#openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")

openai.api_key = "7b7d41f1856e43dfaf6cfd5576f765dc"
openai.api_base = "https://rd-aoai-new.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='rd-turbo'
https://colab.research.google.com/drive/1_lhSWbqVEarzfdSrwAkR9cncUsX4e7NW#scrollTo=HYqyhoB2KCMV&line=1&uniqifier=1

class AI:
    def prompt(self, system_prompt, user_prompt):

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
           ]
        try:
            response = openai.ChatCompletion.create(
                engine = deployment_name,
                messages = messages,
                temperature = 0.7,
                max_tokens = 500
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
