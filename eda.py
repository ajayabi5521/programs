#EDA

""" import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("supermarket.csv")

#check

print(data.head())
city=data["City"].unique()
print(city)

cityvalue=data["City"].value_counts()
print(cityvalue)

cityvalue.plot()
plt.show() """

 
""" import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("supermarket.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# --- Daily Revenue ---
daily_revenue = data.groupby('Date')['Total'].sum()
print(daily_revenue)
plt.figure(figsize=(10, 4))
daily_revenue.plot(kind='line', marker='+')
plt.title("Daily Total Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Monthly Revenue ---
data['Month'] = data['Date'].dt.to_period('M')
monthly_revenue = data.groupby('Month')['Total'].sum()
print(monthly_revenue)
plt.figure(figsize=(8, 4))
monthly_revenue.plot(kind='bar', color='teal')
plt.title("Monthly Total Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show() """



# EDA Notebook for Sales Invoice Data

""" import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("supermarket.csv")  # replace with your actual file name

# Convert Date and Time
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y') """
# df['Time'] = pd.to_datetime(df['Time']).dt.time
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# df['Weekday'] = df['Date'].dt.day_name()
# df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

# ----- 1. Basic Info -----
""" print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# ----- 2. Descriptive Statistics -----
print("\nDescriptive Statistics:\n", df.describe(include='all'))

# ----- 3. Univariate Analysis -----
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include='object').columns """

# Numeric distributions
""" df[num_cols].hist(bins=15, figsize=(14,10))
plt.suptitle("Histograms of Numeric Columns")
plt.show() """

""" # Categorical distributions
for col in cat_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(x=col, data=df, palette='Set2')
    plt.title(f"Count Plot for {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show() """

# ----- 4. Bivariate Analysis -----
#  # Payment vs Total
""" plt.figure(figsize=(8, 5))
sns.boxplot(x="Payment", y="Total", data=df)
plt.title("Payment Method vs Total")
plt.show()

# Gender vs Total
sns.violinplot(x="Gender", y="Total", data=df)
plt.title("Gender vs Total Spending")
plt.show() """


""" # Product line vs Quantity
sns.barplot(x="Product line", y="Quantity", data=df, estimator=np.mean)
plt.title("Average Quantity Sold by Product Line")
plt.xticks(rotation=45)
plt.show() """

"""# ----- 6. Aggregated Insights -----
# Total Sales by City
print("\nTotal Sales by City:\n", df.groupby('City')['Total'].sum())

# Most Profitable Product Line
print("\nGross Income by Product Line:\n", df.groupby('Product line')['gross income'].sum().sort_values(ascending=False))

# Branch with Highest Revenue
print("\nRevenue by Branch:\n", df.groupby('Branch')['Total'].sum())

# ----- 7. Correlation Analysis -----
plt.figure(figsize=(10,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ----- 8. Ratings Distribution -----
sns.boxplot(x="Product line", y="Rating", data=df)
plt.title("Product Line vs Customer Rating")
plt.xticks(rotation=45)
plt.show()"""

# # ----- Optional: Export Cleaned Data -----
# df.to_csv("cleaned_sales_data.csv", index=False)


import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("supermarket.csv")

# -------------------------------
# 1. Data Type Conversion & Enrichment
# -------------------------------
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.day_name()
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour


print(df.head())

# -------------------------------
# 2. Basic Info
# -------------------------------
print("\n--- Basic Info ---")
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# -------------------------------
# 3. Descriptive Statistics
# -------------------------------
print("\n--- Descriptive Statistics (Numerical) ---")
print(df.describe())

print("\n--- Descriptive Statistics (Categorical) ---")
print(df.describe(include='object'))

# -------------------------------
# 4. Univariate Analysis
# -------------------------------
print("\n--- Value Counts (Categorical Columns) ---")
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    print(f"\n{col}:\n{df[col].value_counts()}")

# -------------------------------
# 5. Bivariate Analysis (Categorical vs Numerical)
# -------------------------------
print("\n--- Grouped Means (Total by Gender) ---")
print(df.groupby('Gender')['Total'].mean())

print("\n--- Grouped Means (Total by Customer type) ---")
print(df.groupby('Customer type')['Total'].mean())

print("\n--- Grouped Means (Total by Product line) ---")
print(df.groupby('Product line')['Total'].mean())

print("\n--- Grouped Means (Total by Payment Method) ---")
print(df.groupby('Payment')['Total'].mean())

print("\n--- Grouped Means (Gross Income by Branch) ---")
print(df.groupby('Branch')['gross income'].sum())

# -------------------------------
# 6. Time-Based Analysis
# -------------------------------
print("\n--- Total Sales by Date ---")
print(df.groupby('Date')['Total'].sum().head())

print("\n--- Total Sales by Hour ---")
print(df.groupby('Hour')['Total'].sum())

print("\n--- Total Sales by Weekday ---")
print(df.groupby('Weekday')['Total'].sum())

# -------------------------------
# 7. Correlation Matrix
# -------------------------------
print("\n--- Correlation Matrix ---")
print(df.select_dtypes(include=np.number).corr())

# -------------------------------
# 8. High-Level Insights
# -------------------------------
print("\n--- Most Profitable Product Line ---")
print(df.groupby('Product line')['gross income'].sum().sort_values(ascending=False))

print("\n--- Top Cities by Revenue ---")
print(df.groupby('City')['Total'].sum().sort_values(ascending=False))

print("\n--- Average Rating by Product Line ---")
print(df.groupby('Product line')['Rating'].mean())

# -------------------------------
# 9. Export Cleaned Version (Optional)
# -------------------------------
# df.to_csv("cleaned_sales_data.csv", index=False)
