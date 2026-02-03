from dotenv import load_dotenv
import os

load_dotenv()


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
