from crewai import Crew, Process
from agents import data_collector,sentiment_analyser,strategiest
from task import gather_metrics_task,analyze_news_task,generate_strategy_task

trading_crew = Crew(
    agents=[data_collector,sentiment_analyser,strategiest],
    tasks=[gather_metrics_task,analyze_news_task,generate_strategy_task],
    process=Process.sequential
)

inputs = {'ticker': 'NVDA'}
result = trading_crew.kickoff(inputs=inputs)

print("\n\n########################")
print("## FINAL INVESTMENT REPORT ##")
print("########################\n")
print(result)