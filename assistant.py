from openai import OpenAI
from dotenv import load_dotenv
import os

# load the configuration from .env file
load_dotenv()

# create a client that communicates with ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),   
)

# send q question to the model
print("="*40)
print(" My Assistant")
print("="*40)


while True:
    user_input = input("\nYou : ")
    if user_input.lower() == "quit":
        print(f"\nAssistant : Good bye have a nice day")
        break
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ]
    )

    # display the response
    print(f"\nAssistant : {response.choices[0].message.content}")