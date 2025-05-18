# Financial-Chatbot-Predefined-Queries
A simple AI-powered financial chatbot built with Python and Flask. It answers predefined financial queries—like total revenue, net income changes, and cash flow—for companies like Apple, Tesla, and Microsoft based on recent 10-K filings. Ideal for exploring basic financial analysis and chatbot logic using real-world data.

# Financial Chatbot

This is a simple AI-powered financial chatbot built with Python and Flask. It provides quick answers to predefined financial queries (e.g., total revenue, net income changes) based on company 10-K data for the last three fiscal years.

---

## Features

- Answers to 5 predefined financial questions
- Company-specific and year-specific responses
- Web interface using Flask
- Backend powered by a CSV dataset

---

## Predefined Queries Supported

- What is the total revenue?
- How has net income changed over the last year?
- What is the total assets?
- What is the total liabilities?
- How has cash flow from operating activities changed over the last year?

---

## Project Structure

financial_chatbot/

├── app.py # Flask web app
├── chatbot.py # Main chatbot logic
├── templates/
│ └── index.html # HTML template for user input
├── static/ # Optional: CSS or JS files
├── financial_data.csv # CSV file with financial metrics
└── README.md # This file


---

##  Requirements

- Python 3.7+
- Flask
- pandas

Install the dependencies:


pip install flask pandas

 How to Run Locally

Clone the repo or download ZIP
Place your financial_data.csv file in the project folder.
Run the app:
python3 app.py
Open your browser and go to:
http://127.0.0.1:5000/
⚠Limitations

Only supports exact company names and available years.
Only answers to predefined queries.
Doesn't support natural language or complex user input.
Limited to data available in the CSV file.
