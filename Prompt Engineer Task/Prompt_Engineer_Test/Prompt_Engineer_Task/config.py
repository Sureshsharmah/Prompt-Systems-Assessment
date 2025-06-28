import os
from dataclasses import dataclass
from dotenv import load_dotenv
import logging
from openai import AzureOpenAI

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Config:
    azure_openai_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    azure_openai_key: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    azure_openai_version: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01")
    
    model_text_deployment: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")
    model_image_deployment: str = os.getenv("AZURE_OPENAI_IMAGE_DEPLOYMENT", "dall-e-3")
    
    temperature: float = 0.7
    max_tokens: int = 2000
    
    brand_color: str = "#30C9CB"

def get_azure_openai_client():
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Azure OpenAI client: {str(e)}")
        return None

config = Config()

test_client = get_azure_openai_client()
if test_client is None:
    raise ValueError("Failed to initialize Azure OpenAI client. Check your credentials.")
