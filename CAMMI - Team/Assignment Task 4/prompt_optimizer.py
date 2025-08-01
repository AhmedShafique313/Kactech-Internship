# optimize_prompt.py
import sys
import json
from groq import Groq

# Read input JSON from command line args
data = json.loads(sys.argv[1])
user_prompt = data.get("prompt")

# Groq setup
client = Groq(api_key="your_groq_api_key")

# Prompt optimization
messages = [
    {
        "role": "system",
        "content": (
            "You are a senior prompt engineer. Your task is to take user inputs and rewrite them as powerful, clear prompts that get the best results. Just give the refined prompt only."
        )
    },
    {"role": "user", "content": user_prompt}
]

completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=messages,
    temperature=0.7,
    max_tokens=512,
    stream=False
)

# Print output as JSON
optimized_prompt = completion.choices[0].message.content
print(json.dumps({"optimized_prompt": optimized_prompt}))
