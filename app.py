from typing import List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messages)
    return (response.choices[0].message.content)


prompt_role = '''You are an acedemic researcher in field of immunology. 
Your task is to write an abstract for publication, based on the topics that are given to you. 
You should respect the instructions: the TONE, the LENGTH, and the STYLE'''


def assist_journalist(
        facts: List[str],
        tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f'{prompt_role}\nTOPIC: {facts}\nTONE: {tone}\nLENGTH: {length_words} words\nSTYLE: {style}'
    return ask_chatgpt([{"role": "user", "content": prompt}])


print(
    assist_journalist(
        ['Role of SUMO1 in BCR signaling'],
        'academic', 200, 'Publication abstract'))