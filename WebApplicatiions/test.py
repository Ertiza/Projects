import pandas as pd

file_path = 'file.xlsx'

df = pd.read_excel(file_path)


# Assuming 'df' is your DataFrame
df['Formula'] = df['Formula'].replace({'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'}, regex=True)
print(df)