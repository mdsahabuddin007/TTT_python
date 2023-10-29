[11:37 AM, 10/7/2023] Dipankar AWS Master Trainer: import pandas as salman
data={"Roll":[1,2,3,3],"Name":["Jhon",None,"Jack","Jack"]\
      ,"Age":[25,None,29,29]}
df=salman.DataFrame(data)
#print(df[df['Age']>25])
#print(df)
#df.to_csv("D:\\data.csv",index=False)
#print(df.info())
#print(df.shape)

#print(df.isna().sum())
print(df)
#df.dropna(inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Name'].fillna("NA",inplace=True)
df.drop_duplicates(inplace=True)
print(df)
[11:56 AM, 10/7/2023] Dipankar AWS Master Trainer: import pandas as salman
data={"Roll":[1,2,3,3],"Name":["Jhon",None,"Jack","Jack"]\
      ,"Age":[25,None,29,29]}
df=salman.DataFrame(data)
#print(df[df['Age']>25])
#print(df)
#df.to_csv("D:\\data.csv",index=False)
#print(df.info())
#print(df.shape)

#print(df.isna().sum())
'''print(df)
#df.dropna(inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Name'].fillna("NA",inplace=True)
df.drop_duplicates(inplace=True)
print(df)'''
#df.dropna(inplace=True)
#print(df.describe())
#address=['Kolkata','Delhi','Mumbai','Silong']
#df['Address']=address
df=df.assign(address=['Kolkata','Delhi','Mumbai','Silong'])

df.loc[len(df.index)]=[5,"Doe",36,"London"]
print(df)
