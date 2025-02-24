from dotenv import load_dotenv

from langchain_community.tools import TavilySearchResults

load_dotenv()

WEB_SEARCH = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
)
