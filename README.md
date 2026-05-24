# Stock_Recommendation_Report_CrewAI
This CrewAI project automates stock research using three specialized AI agents. Running on GPT-4o-mini, it uses yfinance to pull live market metrics and the Serper API to analyze real-time Google News sentiment. The crew compiles these insights into a structured markdown investment report with a clear Buy/Sell/Hold verdict.

# 🤖 Multi-Agent AI Stock Analysis & Recommendation Crew

An automated, multi-agent financial research desk powered by **CrewAI**, **LangChain**, and **OpenAI (GPT-4o-mini)**. This system coordinates specialized AI agents to extract live market data, evaluate real-time financial news sentiment, and output a structured investment thesis with an actionable verdict (Buy/Sell/Hold).

---

## 🏗️ Architecture Overview

The project relies on a sequential multi-agent workflow where agents pass critical technical context down the pipeline:
[User Input: Ticker]
│
▼
┌───────────────┐        ┌──────────────────┐
│  Data Agent   ├───────>│ yfinance Python  │ -> Fetches current price, Market Cap,
└───────┬───────┘        └──────────────────┘    P/E ratios, & 52-week boundaries
│
▼ (Passes Technical Metrics)
┌───────────────┐        ┌──────────────────┐
│ Sentiment Agt ├───────>│ Serper Dev Tool  │ -> Scans Google Financial News
└───────┬───────┘        └──────────────────┘    for real-time market sentiment
│
▼ (Passes Narrative Summary)
┌───────────────┐
│ Strategy Agt  │ -> Evaluates quantitative + qualitative data to produce
└───────┬───────┘    the final Investment Memo & Markdown Report.
│
▼
[Nvidia_Market_Report.md]

---

## 🛠️ Project Structure

*   `agents.py`: Configures the LLM profile and establishes the 3 primary CrewAI Agents (`data_collector`, `sentiment_analyser`, `strategiest`) along with their roles, memories, goals, and security profiles.
*   `task.py`: Outlines the procedural execution tasks, sets expectations for data formatting, and declares the local file output paths.
*   `tools.py`: Builds a custom `@tool` wrapper around Yahoo Finance (`yfinance`) and integrates the native `SerperDevTool` search utility.
*   `crew.py`: Instantiates the workspace setup, registers inputs (`{'ticker': 'NVDA'}`), and kicks off the sequential execution loop.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10 to 3.12 installed on your system. 

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Environment setup-->.env file
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_dev_api_key_here

### 4. Running pipeline
python crew.py
