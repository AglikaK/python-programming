'''
count = 3
symbol = *

*
**
***
'''

count = int(input("enter count: "))
symbol = input('enter symbol:')

for i in range(1, count+1):
    print(i * symbol)