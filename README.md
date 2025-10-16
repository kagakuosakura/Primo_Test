# Retail Sales Analysis - Top Spenders

This project demonstrates how to analyze retail sales data to find top spenders per month, handling large datasets efficiently (10M records).

From the table below, if we want to find the top 10 spenders for each month over 12 months, how would we use pandas to extract the data, and what if we have 10,000,000 records?Please provide the results and the project where the data was transformed into a GitHub project.

What I want on GitHub
1. Tools for generating 10M records.
2. File data: 10 million records
3. Script for pulling top spenders
4. file result top spender

## Project Structure

- `data_generator.py`: Script to generate 10 million sample records
- `analyze_top_spenders.py`: Script to analyze top spenders by month
- `requirements.txt`: Project dependencies
- Generated files:
  - `retail_data_10M.parquet`: Main dataset (generated)
  - `retail_data_sample.csv`: Sample of the dataset for quick verification
  - `top_spenders_YYYYMMDD.csv`: Results of top spenders analysis

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Generate sample data (10M records):
```bash
python data_generator.py
```

2. Analyze top spenders:
```bash
python analyze_top_spenders.py
```

## Data Format

The generated data includes:
- order_no: Unique order identifier
- amount: Transaction amount
- customer_no: Customer identifier
- branch: Store branch
- brand: Product brand
- sku: Stock keeping unit
- quantity: Number of items
- transaction_datetime: Transaction timestamp

## Performance Considerations

- Data is stored in Parquet format for efficient storage and faster reading
- Analysis is optimized for large datasets using pandas
- Results are saved in CSV format for easy viewing

## Sample Output

The analysis will generate a CSV file with top spenders for each month, showing:
- Year and month
- Customer number
- Total amount spent

## License

MIT