from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="what is CS50 in one word?",
    model="gpt-5"
)

print(response.output_text)

