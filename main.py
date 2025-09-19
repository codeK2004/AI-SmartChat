from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a research assistant helping User. "
         "Return the answer ONLY in this format:\n{format_instructions}"),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())


tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("Enter your query: ")
auto_save = False

if "save to a file" in query.lower():
    auto_save = True
    query = query.lower().replace("save to a file", "").strip()  # clean query

raw_response = agent_executor.invoke({
    "query": query,
    "chat_history": [],
    "agent_scratchpad": ""
})

try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)

    if auto_save:
        save_tool.func(
            data=f"Topic: {structured_response.topic}\n"
                 f"Summary: {structured_response.summary}\n"
                 f"Sources: {structured_response.sources}"
        )
        print("✅ Output saved to research_output.txt automatically!")

except Exception as e:
    print("Error parsing response", e, "Raw response:", raw_response.get("output"))
