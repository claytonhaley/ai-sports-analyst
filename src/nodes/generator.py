from langchain_core.output_parsers import StrOutputParser

from ..llms.chat_open_ai import OPEN_AI_MODEL
from ..prompts.generator import GENERATOR

rag_chain = GENERATOR | OPEN_AI_MODEL | StrOutputParser()


def decide_to_generate(state):
    """
    Determines whether to generate an answer, or re-generate a question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Binary decision for next node to call
    """
    print("---ASSESS GRADED DOCUMENTS---")
    state["question"]
    filtered_documents = state["documents"]

    if not filtered_documents:
        print(
            "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
        )
        return "transform_query"
    else:
        print("---DECISION: GENERATE---")
        return "generate"


async def generate(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]
    # generation = rag_chain.invoke({"documents": documents, "question": question})
    generation = await rag_chain.ainvoke({"documents": documents, "question": question})

    return {
        "documents": documents,
        "question": question,
        "generation": generation,
    }
