import pandas as pd
import numpy as np
input_file="table_data.xlsx"
employee_df=pd.read_excel(input_file,1)
devices_df=pd.read_excel(input_file,2)
df=employee_df.merge(devices_df,how="left",left_on="id",right_on="employee_id")
ans_df=df[df['employee_id'].isna()]
print(ans_df[["first_name","last_name"]])
