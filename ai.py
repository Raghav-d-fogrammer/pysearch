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


class AI:
    def prompt(self, user_promt):
        print(user_promt)

        system_promt = """
            You are a shopping assistent responsible for helping shoppers with gifting ideas
            Create a list of suggestions for the given prompt.

            Provide a list of gifts by category. A Category can be toys, clothes etc, with appropriate age range
            ALWAYS RESPOND BACK IN JSON Array Format. DONT DEVIATE

            Never start your response like "Here are some gifting ideas ..."
            A SAMPLE RESPONSE WILL BE, JSON Array =
            [
               {"gift": "doll", "category": "toy", "ages": "4 and above"},
               {"gift": "doll house", "category": "toy", "ages": "4 and above"},
               {"gift": "jeans", "category": "clothes","ages": "7 and above"},
            ]
        """
        messages = [
            {"role": "system", "content": system_promt},
            {"role": "user", "content": user_promt}
           ]
        try:
            response = openai.ChatCompletion.create(
                engine = deployment_name,
                messages = messages,
                temperature = 0.7,
                max_tokens = 500
            )
            content = response.choices[0].message.content
            content = content.replace("The JSON object is: ", "")
            return { "status": "success", "response": content}
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
