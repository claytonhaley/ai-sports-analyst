from langchain.prompts import PromptTemplate

ANSWER_RELEVANCE = PromptTemplate(
    template="""You are a grader assessing whether an LLM answer addresses / resolves a question \n 
     Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question.

    Generation: {generation} \n
    Question: \n\n {question} \n\n

    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    Provide the binary score as a JSON with a single key 'score' and no premable or explanation.
    'Yes' means that the answer is grounded in / supported by the set of facts.""",
    input_variables=["generation", "question"],
)
