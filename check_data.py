import pandas as pd

df = pd.read_excel(r"C:\Users\ABC\Desktop\365 Coffee Cafe Dataset.xlsx")
top = df.loc[df["net_revenue"].idxmax()]

answers = [
    ("1. Highest net revenue (and its transaction_id)", f"{top['net_revenue']:.2f} (transaction {top['transaction_id']})"),
    ("2. Total net revenue", f"{df['net_revenue'].sum():,.2f}"),
    ("3. Top store_location by total net revenue", df.groupby("store_location")["net_revenue"].sum().idxmax()),
    ("4. Top product_category by total net revenue", df.groupby("product_category")["net_revenue"].sum().idxmax()),
    ("5. Most used payment_method", df["payment_method"].value_counts().idxmax()),
    ("6. Number of rows (transactions)", f"{len(df):,}"),
    ("7. Average wait_time_min", f"{df['wait_time_min'].mean():.2f}"),
    ("8. Average service_rating", f"{df['service_rating'].mean():.2f}"),
    ("9. Total transaction_qty", f"{df['transaction_qty'].sum():,}"),
    ("10. Weekday with most transactions", df["weekday"].value_counts().idxmax()),
]

lines = [f"{q}: {a}" for q, a in answers]
print("\n".join(lines))
open("answer_key.txt", "w", encoding="utf-8").write("\n".join(lines))