import pandas as pd

data = [1,7,5,2,8,3,6,4]
bins = [0,3,6,9]

label = ["low", "mid", "high"]

cat = pd.cut(data, bins, True, label)
print(cat)
cat = pd.cut(data, bins, False, label)
print(cat)