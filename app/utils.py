import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def compute_kpis(df):
    total_orders = len(df)
    avg_delivery_time = df['Delivery_Time_min'].mean()
    delay_percentage = df['delay_flag'].mean() * 100

    return total_orders, avg_delivery_time, delay_percentage