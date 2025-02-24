from langchain.prompts import PromptTemplate

HALLUCINATION = PromptTemplate(
    template="""You are a grader assessing whether an LLM generation is grounded in / supported 
    by a set of retrieved facts. 

    Generation: {generation} \n
    Facts: \n\n {documents} \n\n

    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    Provide the binary score as a JSON with a single key 'score' and no premable or explanation.
    'Yes' means that the answer is grounded in / supported by the set of facts.""",
    input_variables=["generation", "documents"],
)
