# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 03:10:21 2020

@author: pixel
"""




from datetime import datetime
from typing import Dict
import pickle

input_dat = {'Date': ['2019-01-11 10:25:45', '2019-01-09 10:23:45', '2019-01-11 10:27:45',
                      '2019-01-11 10:24:45', '2019-01-11 10:30:45', '2019-01-11 10:35:45',
                      '2019-02-09 10:25:45'],
             'Id': ['100', '200', '300', '100', '100', '100', '200'],
             'NCC': ['100', '100', '200', '100', '100', '100', '100'],
             'Amount': [200, 400, 330, 100, 300, 200, 500],
             'Sys': [1, 0, 1, 1, 1, 0, 1]
             }

pickle_out = open("test.pkl","wb")
pickle.dump(input_dat, pickle_out)


d = pickle.dump(input_dat, 'test.pkl')



example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
a = pickle.dump(input_dat, pickle_out)
pickle_out.close()


with open(r'dict.pickle', 'rb') as pklfile:
    print(pklfile.read())
    
    
pickle_in = open("dict.pickle","rb")
input_dat = pickle.load(pickle_in)



input_dat['sum_amount'] = sorted([x[1] for x in sorted(amount_per_obsrv.items())])



pickle_in = open("test.pkl","rb")
example_dict = pickle.load(pickle_in)



def calculate_amount(data:Dict, ID: str, result: Dict, seconds: float) -> Dict:
    # Get data about the first row given ID appears in
    first_appearance = list(data['Id']).index(ID)
    end_date = datetime.fromisoformat(data['Date'][first_appearance])
    amount_sum = 0
    # Traverse through all the other rows for same ID
    for i, ident in enumerate(data['Id']):
        if ident == ID and i != first_appearance:
            start_date = datetime.fromisoformat(data['Date'][i])
            if start_date < end_date and (end_date - start_date).total_seconds() <= seconds and data['Sys'][i] == 1:
                # Difference between start_date and end_date is less than or equal to given `seconds`
                amount_sum += data['Amount'][i]
    # Update the results dict
    result[ID] = amount_sum
    return result
 

 
amount_per_ID = {}
amount_per_ID = calculate_amount(df, '100', amount_per_ID, 30 * 60)

input_dat = {'Date': ['2019-01-11 10:25:45', '2019-01-09 10:23:45', '2019-01-11 10:27:45',
                      '2019-01-11 10:24:45', '2019-01-11 10:30:45', '2019-01-11 10:35:45',
                      '2019-02-09 10:25:45'],
             'Id': ['100', '200', '300', '100', '100', '100', '200'],
             'NCC': ['100', '100', '200', '100', '100', '100', '100'],
             'Amount': [200, 400, 330, 100, 300, 200, 500],
             'Sys': [1, 0, 1, 1, 1, 0, 1]
             
             }





def calculate_amount(data:Dict, ID: str, result: Dict, seconds: float) -> Dict:
    # Get data about the first row given ID appears in
    first_appearance = data['Id'].index(ID)
    end_date = datetime.fromisoformat(data['Date'][first_appearance])
    amount_sum = 0
    # Traverse through all the other rows for same ID
    for i, ident in enumerate(data['Id']):
        if ident == ID and i != first_appearance:
            start_date = datetime.fromisoformat(data['Date'][i])
            if start_date < end_date and (end_date - start_date).total_seconds() <= seconds and data['Sys'][i] == 1:
                # Difference between start_date and end_date is less than or equal to given `seconds`
                amount_sum += data['Amount'][i]
    # Update the results dict
    result[ID] = amount_sum
    return result

amount_per_ID = {}
amount_per_ID = calculate_amount(input_dat, '100', amount_per_ID, 30 * 60)
print(f'Result after constructing for ID = 100: {amount_per_ID}')


def calculate_amount(data: Dict, ID: str, result: Dict) -> Dict:
    amount_sum = 0
    # Traverse through all observations for given ID
    for index, ident in enumerate(data['Id']):
        if ident == ID:
            end_date = datetime.fromisoformat(data['Date'][index])
            # Traverse through all the other observations for same ID
            for inner_index, inner_ident in enumerate(data['Id']):
                if inner_ident == ID and inner_index != index:
                    start_date = datetime.fromisoformat(
                        data['Date'][inner_index])
                    if start_date < end_date and divmod((end_date - start_date).total_seconds(), 60)[0] <= 30:
                        # Difference between start_date and end_date is less than or equal to 30 mins
                        amount_sum += data['Amount'][inner_index]
            result[index] = amount_sum
            amount_sum = 0

    return result

 
amount_per_obsrv = {}
amount_per_obsrv = calculate_amount(df, '100', amount_per_obsrv)


 
class Sig:
    
    def __init__(self):
        self.reset();
        
    def reset(self):
        self.amount = [None]*10
        self.datetimes = [None]*10
        self.curr_sig_length = 0
        self.30_amount_sum = 0
        
        
    def resolve(self, data):
        return data['ID']
    
    def update(self, data):
        
        if self.curr_sig_length ==10:
            self.amount.pop(0)
            self.amounts.append(data['Amount'])
            self.datetimes.pop(0)
            self.datetimes.append(dt)
        else:
            self.amounts[self.curr_sig_length] = data['Amount']
            self.datetimes[self.curr_sig_length] = dt
            self.curr_sig_length += 1
        
        
    def searlize(self):
        blob = pickle.dump(self)
        return blob


    def desearlize(self, blob):
        data = pickle.load(blob)
        self.__dict__.update(data.__dict__)

 

data_sig = sig()

df= dataframe
new_df = dict()

for index, row in df.iterrows():
    
    data_row = row.to_dict()
     
    data_sig.reset();
    
    id_lookup_key = data_sig.resolve(data)
    
    if id_lookup_key in new_df:
        data_fetch = new_df[id_lookup_key]
    else:
        data_fetch = None
        
    if id_lookup_key != None:
        data_sig.deserialize(data_fetch)
        
        
    data_sig.update(data_row)
    
    data_row['model_feature'] = data_sig;
    
    result = model1.score(data_row)
    
    data_fetch = data_sig.serilize()
    
    new_df[id_lookup_key] = data_fetch
    
    
        
    
        
    
    


  
def reset(self):
   self.amount = [None]*10
   self.datetimes = [None]*10
   self.curr_sig_length = 0
   
   self.30_sum_amount = 0
        
 def update(self, data):
       

    if self.curr_sig_length ==10:
        self.amount.pop(0)
        self.amounts.append(data['Amount'])
        self.datetimes.pop(0)
        self.datetimes.append(dt)
        
    else:
        self.amounts[self.curr_sig_length] = data['Amount']
        self.datetimes[self.curr_sig_length] = dt
        self.curr_sig_length += 1
            
            

def calculate_amount(data: Dict, ID: str, result: Dict) -> Dict:
    
    amount_sum = 30_sum_amount
    amount_sum = 0
    # Traverse through all observations for given ID
    for index, ident in enumerate(data['Id']):
        if ident == ID:
            end_date = datetime.fromisoformat(data['Date'][index])
            # Traverse through all the other observations for same ID
            for inner_index, inner_ident in enumerate(data['Id']):
                if inner_ident == ID and inner_index != index:
                    start_date = datetime.fromisoformat(
                        data['Date'][inner_index])
                    if start_date < end_date and divmod((end_date - start_date).total_seconds(), 60)[0] <= 30:
                        # Difference between start_date and end_date is less than or equal to 30 mins
                        amount_sum += data['Amount'][inner_index]
            result[index] = amount_sum
            amount_sum = 0

    return result

 
 










# find Dates in the 30-minute window ending at the max Date
mask = (df['Dates'].max() - df['Dates']) < pd.Timedelta('30min')
df_recent = df[mask]



df['count_ncc' = (df.set_index('Date')
                    .groupby(['Fruit id','NCC'])
                    ['Amount'].transform(lambda x: 
                                         x.rolling('30min', closed='left').sum()  
                                        )
                    .values
                 )
   
   
df['count_ncc'] = (df.merge(df.assign(Date_shift=df.Date-pd.to_timedelta('30M'),
                    idx=df.index),
          on=['Fruit id', 'NCC'])
    .query('Date_shift <= Date_x < Date_y')
    .groupby('idx')['Amount_x'].sum()
)



i, k, sdate = 0, 0, df.Date.iloc[0]
while df.Date.iloc[k] - sdate < timedelta(seconds=1800):
    k += 1
k -= 1 # found first row within 30min after start
count = df.iloc[i:k, :].groupby(['Fruit_id', 'NCC']).Amount.sum() # should be faster to do all tags instead of filtering because it's implemented in C
s.append(count.loc[(df.loc[k, 'Fruit_id'], df.loc[k, 'NCC'])])
while k < len(df):
    k += 1
    fdate = df.Date.iloc[k]
    while fdate - df.Date.iloc[i] > timedelta(seconds=1800):
        i += 1
    # repeat the groupby and append, probably should define a function
        
        
        
newdf = pd.pivot_table(df, columns='Fruit id', index='Date', aggfunc=np.sum, values='Amount')
print(newdf.rolling('30min', closed='left').sum())