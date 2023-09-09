import os
import json
from ai import AI
import pandas as pd
import re


system_promt_prompter = """
    You are a real estate assistant.
"""
ai = AI()

r = ai.promptCompletion(prompt="Generate 15 profiles home buyers like A family of two, A family of 2")

print(r)

with open('d.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        #house = "Generate 10 search criteria for real estate listings based on the following data: " + line
        house = "Which type of buyer will be interested in this property : " + line
        response = ai.prompt(system_prompt=system_promt_prompter, user_prompt=house)
        #line = line.split(",")
        #line = line[0].replace("Property details\\nBeautiful Residential at ", "")
        print(line)
        print(response)
        
        
        #print({"address":line, "questions": response})