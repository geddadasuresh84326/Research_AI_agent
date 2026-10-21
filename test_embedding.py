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

response = client.embeddings.create(model=os.getenv("EMBEDDING_MODEL")
                                    , input="artificial engineering")


embedding = response.data[0].embedding

print(embedding)
print(f"length : {len(embedding)}")