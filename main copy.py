from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

print("================================")
print("   Personal AI Agent Started")
print("   Type 'exit' to stop")
print("================================")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = client.responses.create(
        model="llama3.2:3b",
        input=user_input
    )

    print("Agent:", response.output_text)