import os
from dotenv import load_dotenv
from crewai import LLM, Agent
from tools import fetch_stock_metrics, fetch_stock_news

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

crewai_llm = LLM(
    model="openai/gpt-4o-mini", 
    temperature=0.2,
    timeout=60,
    max_retries=3
)

# collect Data from ytfinance-->sentiment analyser
data_collector = Agent(
    role='Senior Stock analyst',
    goal='fetch the latest data of given {ticker} stock',
    verbose=True,
    memory=True,
    backstory="Driven by the curiosity to find out how the stock behaves as per current market",
    tools=[fetch_stock_metrics],
    llm=crewai_llm,
    allow_delegation=True
)

# Agent2-->analyse the Google news via SERPER API
sentiment_analyser = Agent(
    role='Sentiment Analyser',
    goal='find out the sentiment of given {ticker} as per current market',
    verbose=True,
    memory=True,
    backstory='Needs to find out the sentiment of stock to give more insights to our clients',
    tools=[fetch_stock_news],
    llm=crewai_llm,
    allow_delegation=True
)
# Agent3-->Give the recommendation BUY/SALE/NeuTRAL

strategiest = Agent(
    role='Recommendation for stock',
    goal='give the final sale/buy/neutral call for given {ticker} stock ',
    verbose=True,
    memory=True,
    backstory='give the final verdict for stock',
    llm=crewai_llm
)