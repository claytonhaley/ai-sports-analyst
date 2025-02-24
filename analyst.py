import asyncio
from src.states.state import SportsAnalystState
from langgraph.graph import END, StateGraph, START
from src.nodes.generator import decide_to_generate, generate
from src.nodes.grader import grade_documents
from src.nodes.hallucination_check import grade_generation_v_documents_and_question
from src.nodes.retrieval import retrieve
from src.nodes.rewriter import transform_query
from dotenv import load_dotenv

load_dotenv()

workflow = StateGraph(SportsAnalystState)

# Define the nodes
workflow.add_node("retrieve", retrieve)  # retrieve
workflow.add_node("grade_documents", grade_documents)  # grade documents
workflow.add_node("generate", generate)  # generatae
workflow.add_node("transform_query", transform_query)

# Build graph
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "transform_query": "transform_query",
        "generate": "generate",
    },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_conditional_edges(
    "generate",
    grade_generation_v_documents_and_question,
    {
        "not supported": "generate",
        "useful": END,
        "not useful": "transform_query",
    },
)

analyst_graph = workflow.compile()

def main():
    print("\nYou can now chat with the AI sports analyst.")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter your question or prompt (or 'exit' to quit): ").strip()
            
        if prompt.lower() == 'exit':
            print("Exiting the Q&A session.")
            break
    
        inputs = {
            "question": prompt
        }

        asyncio.run(process_stream(inputs))

async def process_stream(inputs):
    async for output in analyst_graph.astream(inputs):
        if "generate" in output:
            print(output["generate"]["generation"])

if __name__ == "__main__":
    main()
