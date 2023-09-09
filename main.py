
import os
import json
from ai import AI

system_promt_prompter = """
    you are a Social Language Expert, generate some sencenses that ask for gifting ideas, the sentence must contain age group
    for example: 
        Give me a gifting idea for my 7 year old
        Give me a gifting idea for my grandma
        Give me a gifting idea for my highschooler

        ALWAYS RESPOND BACK IN JSON Array Format. DONT DEVIATE
        Provide your answer in JSON form:
        
        FOR EXAMPLE:
            [
               {"idea": "Give me a gifting idea for my 7 year old"},
               {"idea": "Give me a gifting idea for my grandma"}
            ]
        
        DONOT start the response with 'Sure, here are..'

"""
ai = AI()
count = 0
#try:
response = ai.prompt(system_prompt=system_promt_prompter, user_prompt="Give me 10 gifting ideas")
#except:
#    if count < 1:
        

response = response.replace("JSON Array: ", "")

print("Raw JSON String of Gift Ideas:")
print(response)
print("Validated JSON of Gift Ideas:\n")
jsonContent = json.loads(response)
print(jsonContent)


system_promt_assistent = """
             You are a shopping assistant responsible for helping shoppers with gifting ideas
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

for idea in jsonContent:
    response = ai.prompt(system_prompt=system_promt_assistent, user_prompt=idea['idea'])
    print("response of search result for :" + idea['idea'] + "\n")
    print(response)