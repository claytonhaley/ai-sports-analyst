from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from ..llms.chat_open_ai import OPEN_AI_MODEL
from ..prompts.rewrite import REWRITE

load_dotenv()

transform = REWRITE | OPEN_AI_MODEL | StrOutputParser()


async def transform_query(state):
    """
    Transform the query to produce a better question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates question key with a re-phrased question
    """
    print("---TRANSFORM QUERY---")
    question = state["question"]
    documents = state["documents"]

    # Re-write question
    better_question = await transform.ainvoke({"question": question})
    return {"documents": documents, "question": better_question}
