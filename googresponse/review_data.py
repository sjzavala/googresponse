import pandas as pd 
import csv
from pandas.io.json import json_normalize
from datetime import datetime, timedelta

# get list of locations for the first account in the list

print("List of locations for account " + firstAccount)
body ={
    "locationNames": [
        "accounts/xxx/locations/XXXX",
        "accounts/xxx/locations/XXXX"
    ]
}

locationlist = service.accounts().locations().batchGetReviews (name = firstAccount,body =body).excute()
print(json.dumps(locationslist, indent=2))

#covert JSON data into CSV

with open('gmb_batchreviews.json', 'w') as json_files:
    d = json.load(f)


    # Normalize the nested JSON File

    df = json_normalize(d['locationReviews'])
    df.to_csv('gmb_batchreviews.csv')
    outfile.close()



    #cleaning and filtering the incoming data 

#filter results by time

df2 = pd.read_csv ('gmb_batchreview.csv')
df2 = df2.drop(['unamed: 0'], axis=1)

#convert review date/time format 

df2=['review.createTime'] = pd.to_datetime(df2['review.createTime'])
df2 = df2.set_index(['review.createTime'])


#set end range for day current day minus 30 days. Create Data frame for this.

end_range = datetime.now().date()
d = d = datetime.today() - timedelta(days=30)
start_range = d.date()
start_date = str(start-range)
df3 =df2[start_date:]

#alternatively you can set a custom range like date in a place of the start_range variable:
#df3 = df2['2019-05-01' : '2019-06-01']


#use a .drop() function to remove columns you dont need.  use .columns to rename columns
df3 = df3.drop(columns=['review.name', 'review.reviewId', 'review.reviewer.profilePhotoUrl'])
df3.columns = ['location', 'comment', 'reply_date', ' reviewer', 'star_rating', 'date']


#making end product readable for the user. Translate Location ID to text.

df3 = df3.replace('accounts/xxxxxx/locations/xxxxxx','Location Name')


#export new dataframe as XLSX file with date attached to the file name. convert end date to a string to combine in the first line.

export_name = 'gmb_reviews_export_' + str(end_range) +'.xlsx'
df3.to_excel(export_name, index=False)
