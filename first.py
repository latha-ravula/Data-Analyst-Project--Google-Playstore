import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('google_playstore_dataset_100.csv')
# print(df.head().sort_values(by='Reviews',ascending=False))
# print(df.shape)
# print(df.info())
# print(df['Rating'].mean())
# print((df['Category'] == 'SOCIAL').sum())


# print(df.groupby('Category')['Rating'].mean().sort_values(ascending=False))
# print(df['Category'].value_counts(normalize=True).sort_values())
# print(len(df[df['Rating']==5]))
# print(df['Reviews'].mean())
# print(df.columns)

print(df.groupby('Type')['Rating'].mean())

# max_review_app=df.loc[df['Reviews'].astype(int).idxmax(),'App']
# print(max_review_app)
# print(df[df['Reviews'].max()==df['Reviews']]['App'])
# . Display Top  5 Apps Having Maximum Installs

df['Installs']=df['Installs'].str.replace(',','')
df['Installs']=df['Installs'].str.replace('+','')

index=df['Installs'].sort_values(ascending=False).head().index
print(df.iloc[index])