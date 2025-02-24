from langchain.prompts import PromptTemplate

REWRITE = PromptTemplate(
    template="""You're a question re-writer that converts an input question to a better version 
    that is optimized for web search retrieval. Look at the input and try to reason about 
    the underlying semantic intent / meaning.
    
    "Here is the initial question: 
    
    {question} 

    Formulate an improved question.""",
    input_variables=["question"],
)
