from langchain.schema import Document
from ..states.state import SportsAnalystState
from ..tools.web_search import WEB_SEARCH


async def retrieve(state: SportsAnalystState):
    question: str = state["question"]
    documents: list = state.get("documents", [])
    web_results: dict = await WEB_SEARCH.ainvoke({"query": question})

    documents.extend(
        [
            Document(page_content=d["content"], metadata={"url": d["url"]})
            for d in web_results
        ]
    )

    return {"documents": documents, "question": question}
