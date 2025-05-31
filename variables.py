from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

tavily_api = os.getenv('TAVILY_API')
auth_token = os.getenv('AUTH_TOKEN')