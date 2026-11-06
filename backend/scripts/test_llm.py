from app.services.llm_service import generate_response

response = generate_response(
    "You are a helpful assistant.",
    "Say hello and confirm Azure OpenAI is working."
)

print(response)
