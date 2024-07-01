import pandas as pd
df = pd.read_excel("excel.xlsx")

# cols3 = df.columns[3:3+5]
# data3 = df [cols3]
# print(df[df['ID (QRcode)']==340268])


# for index,row3 in data3.iterrows():
#     print(row3)

# import openpyxl as onx

# excel=onx.load_workbook("excel.xlsx")

# sheet=excel['Sheet1']

# son=3
# while sheet[f"n{son}"].value:
#     print(sheet[f"n{son}"].value)
#     son+=1

# cols2 = df.columns[114:114+50]
# data2 = df [cols2]

# for index,row2 in data2.iterrows():
# # Define mapping for co`nversion
#     mapping = {
#         '0': '❌',
#         '1': '✅',
#     }

#     # Convert elements
#     converted = [mapping[el] for el in row2[-1]]

#     # Print each converted value on a new line
#     for item in converted:
#         print(item)

# df = pd.read_excel("excel.xlsx")
olish=df[df['ID (QRcode)']==340268]
# # Filter rows where the city is either 'New York' or 'Chicago'
# qayerga=olish.columns[14:14+50]
# filtered_df = olish[olish['ID (QRcode)'].isin([qayerga])]
# print(filtered_df)

lis=[]
for i in olish.values[0][114:114+50]:
    if i==1:
        lis.append('✅')
    elif i==0:
        lis.append('❌')