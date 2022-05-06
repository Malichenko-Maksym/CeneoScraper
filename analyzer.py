import os
import pandas as pd


print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

source=input("Your product id , or the full link: ") 

opinions= pd.read_json(f"opinions/{source}.json")
print(opinions)