import pandas as pd

df = pd.read_csv("data.csv")

df.columns = df.columns.str.strip()
df.rename(columns={
    'Fiscal Year': 'Year',
    'Total Revenue (in millions USD)': 'Total Revenue',
    'Net Income (in millions USD)': 'Net Income',
    'Total Assets (in millions USD)': 'Total Assets',
    'Total Liabilities (in millions USD)': 'Total Liabilities',
    'Cash Flow from Operating Activities (in millions USD)': 'Cash Flow from Operating Activities'
}, inplace=True)

def simple_chatbot(user_query, company, year):
    data = df[(df['Company'].str.lower() == company.lower()) & (df['Year'] == year)]

    if data.empty:
        return "Sorry, no data available for that company and year."

    row = data.iloc[0]

    if user_query == "What is the total revenue?":
        return f"The total revenue for {company} in {year} was ${row['Total Revenue']} million."
    elif user_query == "How has net income changed over the last year?":
        prev_data = df[(df['Company'].str.lower() == company.lower()) & (df['Year'] == year - 1)]
        if prev_data.empty:
            return "No previous year data available to compare net income."
        diff = row['Net Income'] - prev_data.iloc[0]['Net Income']
        trend = "increased" if diff > 0 else "decreased"
        return f"The net income has {trend} by ${abs(diff)} million from {year - 1} to {year}."
    elif user_query == "What is the total assets?":
        return f"The total assets for {company} in {year} were ${row['Total Assets']} million."
    elif user_query == "What is the total liabilities?":
        return f"The total liabilities for {company} in {year} were ${row['Total Liabilities']} million."
    elif user_query == "How has cash flow from operating activities changed over the last year?":
        prev_data = df[(df['Company'].str.lower() == company.lower()) & (df['Year'] == year - 1)]
        if prev_data.empty:
            return "No previous year data available to compare cash flow."
        diff = row['Cash Flow from Operating Activities'] - prev_data.iloc[0]['Cash Flow from Operating Activities']
        trend = "increased" if diff > 0 else "decreased"
        return f"The cash flow from operating activities has {trend} by ${abs(diff)} million from {year - 1} to {year}."
    else:
        return "Sorry, I can only provide information on predefined queries."

