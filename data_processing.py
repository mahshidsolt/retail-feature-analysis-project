import pandas as pd
df = pd.read_excel("online_retail_II.xlsx")
df.to_csv("online_retail_II.csv", index= False)