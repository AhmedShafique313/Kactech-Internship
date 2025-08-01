import sys
import requests
import json

# Get user input from command line
user_input = sys.argv[1]

# Your OpenRouter API key
api_key = "fake"

# Set request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Create payload for the request
payload = {
    "model": "deepseek/deepseek-r1-0528",
    "max_tokens": 500,
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a text refinement assistant. "
                "Your job is to return an improved version of the input text by enhancing clarity, grammar, and completeness — "
                "**without any explanations, notes, or commentary**. Just return the refined text only."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
}


# Make the API request
try:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=15
    )

    # Parse and print the refined text
    if response.status_code == 200:
        result = response.json()
        refined = result["choices"][0]["message"]["content"].strip()
        print(refined)
    else:
        print(f"API Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)



# Dummy code for testing purposes
# import sys

# Dummy logic for testing
# user_input = sys.argv[1]
# refined_output = f"{user_input.capitalize()}"

# print(refined_output)

