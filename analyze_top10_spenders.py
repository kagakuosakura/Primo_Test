import pandas as pd
from datetime import datetime
import numpy as np

def load_data(file_path):
    """Load data from parquet file"""
    return pd.read_csv(file_path)

def get_top_spenders_by_month(df, top_n=10, values='customer'):
    """
    Calculate top spenders for each month
    
    Args:
        df: DataFrame with sales data
        top_n: Number of top spenders to return per month
        
    Returns:
        DataFrame with year_month and columns for each rank (1st through 10th)
    """
    # Convert transaction_datetime to datetime if it's not already
    df['transaction_datetime'] = pd.to_datetime(df['transaction_datetime'])
    
    # Extract month and year
    df['year_month'] = df['transaction_datetime'].dt.to_period('M')
    
    # Group by customer and month, calculate total spending
    monthly_spending = df.groupby(['year_month', 'customer_no'])['amount'].sum().reset_index()
    
    # Get top spenders for each month
    top_spenders = (monthly_spending.groupby('year_month')
                   .apply(lambda x: x.nlargest(top_n, 'amount'))
                   .reset_index(drop=True))
    
    # Create rank within each month
    top_spenders['rank'] = top_spenders.groupby('year_month').cumcount() + 1
    
    # Create rank column names
    rank_names = {
        1: '1st', 2: '2nd', 3: '3rd',
        **{i: f'{i}th' for i in range(4, top_n + 1)}
    }
    
    # Pivot the data to get one row per month with columns for each rank
    result = pd.pivot_table(
        top_spenders,
        values=values,
        index='year_month',
        columns='rank',
        aggfunc='first'
    ).rename(columns=rank_names).reset_index()
    
    return result

if __name__ == "__main__":
    # Load the data
    print("Loading data...")
    df = load_data('retail_data_sample.csv')
    
    # Calculate top spenders
    print("Calculating top spenders...")
    top_spenders = get_top_spenders_by_month(df, 10, 'amount')
    
    # Save results
    print("Saving results...")
    current_date = datetime.now().strftime("%Y%m%d")
    output_file = f'top_spenders_{current_date}.csv'
    top_spenders.to_csv(output_file, index=False)
    
    print(f"Results saved to {output_file}")
    
    # Display sample of results
    print("\nSample of top spenders:")
    print(top_spenders)