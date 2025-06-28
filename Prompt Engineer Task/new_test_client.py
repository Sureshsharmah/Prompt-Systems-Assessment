from config import get_azure_openai_client

print("Testing new Azure OpenAI client initialization...")

client = get_azure_openai_client()

if client:
    print("✅ Client initialized successfully!")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        print("✅ API call successful!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"❌ API call failed: {e}")
else:
    print("❌ Client initialization failed")
