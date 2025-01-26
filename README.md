# AI-Driven-Supply-Chain-Disruption-Predictor-and-Inventory-Optimization-System

This project focuses on building an AI-powered system to predict supply chain disruptions and optimize inventory management with actionable insights. The system fetches real-time news articles, analyzes supply chain risks and sentiments, evaluates warehouse data, and generates alerts with email notifications to enable proactive decision-making. The solution is specifically designed for the semiconductor industry, but it can be adapted to other domains.

Milestones

Milestone 1: News Article Fetcher
Objective: Collect relevant news articles related to supply chain disruptions.
Implementation:
Utilizes the Event Registry API to search for articles based on specified keywords.
Saves results, including titles, sources, publication dates, and URLs, into a JSON file (event_registry_data.json).
Outcome:
A repository of curated articles for further analysis.
Milestone 2: Supply Chain Risk and Sentiment Analysis
Objective: Analyze fetched news articles for risks and sentiment insights.
Implementation:
Risk Analysis: Uses OpenAI's GPT-3.5-Turbo to identify supply chain vulnerabilities, such as geopolitical tensions, resource shortages, and logistical issues.
Sentiment Analysis: Leverages Hugging Face's distilbert-base-uncased-finetuned-sst-2-english model to classify article tones (positive, neutral, or negative).
Processes the event_registry_data.json file from Milestone 1 for analysis.
Outcome:
Detailed insights into risks and sentiments displayed on the console for actionable use.
Milestone 3: Semiconductor Supply Chain Analysis
Objective: Evaluate warehouse inventory data to generate actionable alerts for supply chain management.
Implementation:
Reads data from a CSV file (semiconductor_supply_chain_data_updated.csv) containing:
Monthly incoming stock.
Warehouse capacity.
Risk levels and sentiment scores.
Calculations:
Determines utilization rates (Monthly Incoming / Warehouse Capacity).
Defines thresholds:
High Utilization: >70%
Low Utilization: <40%
Alerts:
SELL: High utilization, high risk, negative sentiment.
MONITOR: High utilization with neutral/positive sentiment.
BUY: Low utilization (<40%).
Saves alerts to a CSV file (supply_chain_alerts.csv).
Outcome:
Alerts categorized as SELL, MONITOR, or BUY for decision-making.
Milestone 4: Warehouse Alert System with Email Notification
Objective: Extend the alert system by notifying stakeholders via email.
Implementation:
Analyzes the latest month’s data for relevant alerts.
Generates email content with:
The alert month.
Recommended actions (SELL, MONITOR, BUY).
Reasons for the action.
Uses Gmail’s SMTP server to send alerts to stakeholders automatically.
Outcome:
Email notifications ensure real-time updates and informed decision-making.
Key Features
Automated News Fetching: Retrieves supply chain-related news articles for analysis.
AI-Powered Risk & Sentiment Analysis: Identifies vulnerabilities and evaluates sentiment for actionable insights.
Warehouse Inventory Optimization: Calculates utilization rates and generates data-driven alerts.
Real-Time Email Notifications: Delivers alerts directly to stakeholders for proactive management.
Scalability: Designed for semiconductor supply chains but adaptable to other industries.
Applications
Supply Chain Management: Identify disruptions early and act swiftly to minimize risks.
Semiconductor Industry: Address industry-specific challenges like raw material shortages, geopolitical tensions, and logistical issues.
Risk Mitigation: Use AI-driven insights to prepare for potential disruptions.
