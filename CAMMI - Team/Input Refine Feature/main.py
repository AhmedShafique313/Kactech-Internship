import sys
import re
from groq import Groq

GROQ_API_KEY = "fake"
client = Groq(api_key=GROQ_API_KEY)

system_prompt = (
    "You are a senior prompt engineer. Your task is to take user inputs and rewrite them as powerful, clear prompts "
    "that get the best results which focuses on clarity, specificity, and alignment with business objectives. "
    "Just give the refined prompt only as output, but think aloud between <think> and </think>."
)

user_prompt = input("Enter your prompt: ")


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response_text = ""

completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=messages,
    temperature=0.9,
    max_tokens=2048,
    top_p=1.0,
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content:
        response_text += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content, end="", flush=True)

response_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)  # remove <think> block
response_text = response_text.strip()
response_text = re.sub(r"^Refined Prompt:\s*", "", response_text, flags=re.IGNORECASE)  # remove prefix
if response_text.startswith('"') and response_text.endswith('"'):
    response_text = response_text[1:-1] 


print("\n\n Refined Prompt:\n" + response_text.strip())