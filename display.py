import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [40000, 90000, 70000, 10000]
    }
plt.figure(figsize=(8,5))
plt.bar(d['Name'],d['Salary'],color=['red','blue','green','purple'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Bar chart')
plt.show()
def show(val):
    print(val)
    total=sum(d['Salary'])
    ab=int(val/100*total)
    return f'{ab}'

plt.figure(figsize=(8, 5))
plt.pie(d['Salary'],labels=d['Name'],autopct=show,colors=['gold', 'blue', 'red','green'])
plt.title('SALARY INFORMATION FOR THE COMPMANY\n EMPLOYEES')
plt.show()

plt.barh(d['Name'],d['Age'],color=['red','blue','green','purple'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Age difference for Senior')
plt.show()

