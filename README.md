# ai-sports-analyst

This project utilizes the Langgraph framework to build out a LLM sports agent. It retrieves relevant information from the internet and forms informed and relevant opinions based on the user's prompt

## Getting Started
1. Get started with the [Tavily API](https://tavily.com/).

You will need to add the following to a `.env` file once your Tavily API account is set up:
```text
TAVILY_API_KEY=your-tavily-api-key
```
2. Get started with the [OpenAI API](https://platform.openai.com/docs/quickstart)

Add the following to your `.env` file:
```text
OPENAI_API_KEY=your-openai-api-key
```

3. Run the program
```shell
python analyst.py
```

4. Example Input
```
Enter your question or prompt (or 'exit' to quit): Who is the best team in college basketball?
```

5. Example Output
```
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---ASSESS GRADED DOCUMENTS---
---DECISION: GENERATE---
---GENERATE---
---CHECK HALLUCINATIONS---
---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
---GRADE GENERATION vs QUESTION---
---DECISION: GENERATION ADDRESSES QUESTION---
Right now, it looks like Auburn is strutting its stuff as the best team in college basketball. They held onto the No. 1 spot despite a hiccup against Florida, which shows some serious resilience. The Tigers are proving they can handle the pressure, and that’s what you want heading into March Madness. Plus, with the way the season's been shaking out, it’s clear Alabama is also in the mix, but Auburn's got that edge. Keep an eye on them; they’re not just a flash in the pan. So, if you’re looking for the top dog, it’s Auburn for now!
```