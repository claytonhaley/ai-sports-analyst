from langchain_core.output_parsers import JsonOutputParser

from ..llms.chat_open_ai import OPEN_AI_MODEL
from ..prompts.hallucination import HALLUCINATION
from ..prompts.answer_relevance import ANSWER_RELEVANCE

hallucination_grader = HALLUCINATION | OPEN_AI_MODEL | JsonOutputParser()
answer_grader = ANSWER_RELEVANCE | OPEN_AI_MODEL | JsonOutputParser()


async def grade_generation_v_documents_and_question(state):
    """
    Determines whether the generation is grounded in the document and answers question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Decision for next node to call
    """
    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]

    score = await hallucination_grader.ainvoke(
        {"documents": documents, "generation": generation}
    )
    grade = score["score"]

    # Check hallucination
    if grade == "yes":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        # Check question-answering
        print("---GRADE GENERATION vs QUESTION---")
        score = await answer_grader.ainvoke(
            {"question": question, "generation": generation}
        )
        grade = score["score"]
        if grade == "yes":
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return "not supported"
