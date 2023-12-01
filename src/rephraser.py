from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
client = OpenAI()


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.0):
    """
    This function sends the input text to the LLM for rephrasing.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
