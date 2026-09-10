import pandas as pd
from sqlalchemy import create_engine

# 1. Load
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 2. Clean TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)  # tenure=0 customers -> 0 spend

# 3. Standardize SeniorCitizen (0/1 -> Yes/No) for readability in Power BI
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

# 4. Trim whitespace in object columns
obj_cols = df.select_dtypes(include='object').columns
df[obj_cols] = df[obj_cols].apply(lambda x: x.str.strip())

# 5. Push to MySQL
from config import DB_PASSWORD
engine = create_engine(f"mysql+pymysql://root:{DB_PASSWORD}@localhost/churnguard")
df.to_sql('customer_churn_raw', con=engine, if_exists='replace', index=False)

print(f"Loaded {len(df)} rows into churnguard.customer_churn_raw")