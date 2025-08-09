import pandas as pd
import matplotlib.pyplot as plt
s=pd.read_csv("adult.csv")
print(s.head())
print(s.tail())
print(s["education"])
'''print(s["occupation"])'''
selectedfield=["7th-8th","Masters",'Assoc-acdm','Assoc-voc','10th',' 11th','9th','Prof-school']
f=s[s["education"].isin(selectedfield)]
e=f['education'].value_counts().reindex(selectedfield)
print(e)
d=s["workclass"]
print(d.unique())
print(d.value_counts())

'''e.plot()
plt.show()'''

colors=["#e5ff66",'#99ff99','red','orange','yellow','purple','pink','brown','coral','darkblue']
e.plot.pie(autopct='%1.1f%%',colors=colors ,startangle=360,wedgeprops={'edgecolor':'black'})
plt.axis('equal')

plt.show()
