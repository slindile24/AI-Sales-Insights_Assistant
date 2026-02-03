from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    print("API key:", os.getenv("OPENAI_API_KEY")[:10])

def generate_data_summary(df, date_col, price_col):
    """
    Generates a business summary from sales data
    """
    total_sales = df[price_col].sum()
    total_orders = len(df)
    average_order_value = df[price_col].mean()
    summary = f"""The total sales is {total_sales:.2f}.
    There were {total_orders} orders in total.
    The average order value is {average_order_value}
    """ 
    return summary

def generate_ai_insight(summary,user_question):
    """Sends sales summary and user_question to OpenAI for analysis"""

    prompt = f"""

    Business Analysis AI.


    Sales Summary :
    {summary}

    Please give us a clear short business insight based on the data presented
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system", "content": "Helpful business analyst"},
            {"role":"user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
