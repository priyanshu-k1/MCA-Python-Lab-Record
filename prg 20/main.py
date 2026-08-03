"""
Write programs to use the pandas data structures: Frames and series as storage
containers and for a variety of data-wrangling operations, such as
 -> Single-level and hierarchical indexing
 -> Handling missing data
 -> Arithmetic and Boolean operations on entire columns and tables
 -> Database-type operations (such as merging and aggregation)
 -> Plotting individual columns and whole tables
 -> Reading data from files and writing data to files
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

df1 = pd.DataFrame({
    "employeeId": [101, 102, 103, 104, 105],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [70000, 50000, 80000, 65000, np.nan],
    "bonus": [5000, 3000, 7000, np.nan, 4000]
})

print("Series Element:", s1["b"])
print("Single-level DF Indexing:\n", df1[["employeeId", "salary"]])

hierarchicalData = pd.DataFrame(
    {"sales": [100, 150, 200, 120]},
    index=pd.MultiIndex.from_tuples(
        [("2025", "Q1"), ("2025", "Q2"), ("2026", "Q1"), ("2026", "Q2")],
        names=["year", "quarter"]
    )
)
print("Hierarchical Indexing:\n", hierarchicalData.loc["2025"])

print("Missing Values Mask:\n", df1.isna())

dfFilled = df1.copy()
dfFilled["salary"] = dfFilled["salary"].fillna(dfFilled["salary"].mean())
dfFilled["bonus"] = dfFilled["bonus"].fillna(0)
print("Filled Missing Data:\n", dfFilled)

dfDropped = df1.dropna()
print("Dropped Missing Data:\n", dfDropped)

df1["totalComp"] = df1["salary"] + df1["bonus"]
print("Column Arithmetic:\n", df1[["salary", "bonus", "totalComp"]])

highEarners = df1[(df1["salary"] > 60000) & (df1["department"] == "IT")]
print("Boolean Filtering:\n", highEarners)

deptDetails = pd.DataFrame({
    "department": ["IT", "HR", "Finance"],
    "location": ["Building A", "Building B", "Building A"]
})

mergedDf = pd.merge(dfFilled, deptDetails, on="department", how="left")
print("Merged DataFrame:\n", mergedDf)

aggregatedData = dfFilled.groupby("department").agg(
    avgSalary=("salary", "mean"),
    totalBonus=("bonus", "sum"),
    employeeCount=("employeeId", "count")
)
print("Aggregated Data:\n", aggregatedData)

dfFilled.to_csv("employees.csv", index=False)
readDf = pd.read_csv("employees.csv")
print("Read from CSV:\n", readDf)

dfFilled.plot(x="employeeId", y=["salary", "bonus"], kind="bar")
plt.title("Employee Salary and Bonus")
plt.xlabel("Employee ID")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("salary_bar_chart.png")

dfFilled[["salary", "bonus"]].plot(kind="box")
plt.title("Salary and Bonus Distribution")
plt.tight_layout()
plt.savefig("salary_box_plot.png")