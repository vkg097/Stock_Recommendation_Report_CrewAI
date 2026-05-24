from crewai import Task
from agents import data_collector, sentiment_analyser, strategiest

# Task 1: Gather Metrics
gather_metrics_task = Task(
    description="Fetch financial metrics for {ticker} using the provided tools. Identify the current price, market valuation, and extreme ranges.",
    expected_output="A structured markdown report listing the specific technical and foundational numbers for {ticker}.",
    agent=data_collector
)

# Task 2: Analyze News

analyze_news_task = Task(
    description="Search for the latest news articles for the stock {ticker} by executing a query like 'latest financial news for {ticker} stock'. Assess whether the overall market sentiment is positive, neutral, or negative.",
    expected_output="A bulleted summary of current news sentiment with a net sentiment score (Bullish/Neutral/Bearish).",
    agent=sentiment_analyser
)

# Task 3: Generate Strategy Report
generate_strategy_task = Task(
    description="Review the quantitative metrics and the sentiment analysis report. Compile a final Investment Thesis providing a firm 'Buy', 'Sell', or 'Hold' recommendation with risk mitigations.",
    expected_output="A final comprehensive investment memo containing a Summary, Metrics Table, Sentiment Breakdown, Final Actionable Verdict, and Risk Risks.",
    agent=strategiest,
    output_file="Nvidia_Market_Report.md"
)