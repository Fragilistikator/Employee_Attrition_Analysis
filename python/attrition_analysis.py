import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

df = pd.read_csv("Employee_Attrition_Analysis/data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(df.head(10))