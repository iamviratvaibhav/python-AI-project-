

from groq import Groq

# Replace 'your_api_key_here' with your actual API key
client = Groq(api_key="your_api_key")

prompt = "Generate 5 multiple-choice question about the solar system with four options and indicate the correct answer."
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": prompt}],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
