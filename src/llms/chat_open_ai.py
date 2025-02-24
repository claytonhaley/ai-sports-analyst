from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_MODEL = ChatOpenAI(
    model="gpt-4o-mini", temperature=0, max_completion_tokens=1024
)
