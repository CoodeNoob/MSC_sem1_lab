import pandas as pd

marks = pd.Series([10,20,30])


#A DataFrame is a collection of Series arranged as rows and columns.

dataf = pd.DataFrame({
    "Name": ["Aung", "Su", "Ko"],
    "Age": [22, 21, 23],
    "Marks": [85, 90, 76]
})