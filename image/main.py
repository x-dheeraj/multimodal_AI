import base64
from openai import OpenAI

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama",
)


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("falcon9.png")
#
response = client.chat.completions.create(
    model = "qwen2.5vl:7b",
    messages = [
        {"role": "user",
         "content": [
             {"type": "text", "text": "Generate a title for this image within 50 words"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
         ]}
    ]
)

print("Response:", response.choices[0].message.content)
 
# Output : Response: "Rocket Recovery: A Powerful Landing Moment Captured Against a Dramatic Sky"