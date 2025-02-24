from typing import List
from langchain.schema import Document
from langchain_core.output_parsers import JsonOutputParser

from ..llms.chat_open_ai import OPEN_AI_MODEL
from ..prompts.grader import GRADER

retrieval_grader = GRADER | OPEN_AI_MODEL | JsonOutputParser()


async def grade_documents(state):
    """
    Determines whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with only filtered relevant documents
    """
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question: str = state["question"]
    documents: List[Document] = state["documents"]
    filtered_docs = []
    for d in documents:
        score = await retrieval_grader.ainvoke(
            {"question": question, "documents": d.page_content}
        )
        grade = score["score"]
        if grade == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            continue

    return {"documents": filtered_docs, "question": question}
