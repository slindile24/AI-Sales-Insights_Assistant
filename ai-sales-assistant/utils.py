from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":
    print("API key:", os.getenv("OPENAI_API_KEY")[:10])