import pandas as pd
import json
import numpy as np
import pprint
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-env", "--environ",dest="environ", help="environment")
parser.add_argument("-json", "--jsonfile",dest="jsonfile", help="jsonfile path and name")
parser.add_argument("-csv", "--csvfile",dest="csvfile", help="csvfile path and name")

args = parser.parse_args()
csv_file=args.csvfile
json_file=args.jsonfile
env=args.environ

#---------------------Read Data from csv-----------
res={}
df=pd.read_csv(csv_file)
column_names=list(df.columns)
env_list=df.loc[df["ENV"]==env]
val_list=np.array(env_list.values)
val_list=val_list.flatten()
for i,val in enumerate(column_names):
    res[val]=val_list[i]

#------------------------Update data to json-------------

with open(json_file, "r") as jsonFile:
    data = json.load(jsonFile)
    data[env]['host'] = res["host"]
    data[env]['port'] = res["port"]
    data[env]['dbname'] = res["dbname"]
    data[env]['user'] = res["user"]
    data[env]['password'] = res["password"] 
pprint.pprint(data)
pretty_print_json = pprint.pformat(data).replace("'", '"')
with open(json_file, 'w') as f:
    f.write(pretty_print_json)

    







