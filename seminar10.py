import pandas as pd  
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

one_hot = pd.DataFrame()
uniq_values = data['whoAmI'].unique()

for value in uniq_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

print(one_hot)