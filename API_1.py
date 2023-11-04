import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = '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'
openai.api_key  = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1, # lower the 随机性 it is
    )
    return response.choices[0].message["content"]

text = f"""
    My mom has a stroke! She can't breath at all now, and she\
"""
prompt = f"""
    Determine the emergency type.
    energency types: FIRE CALLS, POLICE CALLS, EMS CALLS
```{text}```
"""

# output
response = get_completion(prompt)
print(response)


'''
emergency -> 
type -> 
address -> street name / apartment number / N/A

medical -> 
fire -> 

number of ambulence
severity


special case -> emergency
'''
