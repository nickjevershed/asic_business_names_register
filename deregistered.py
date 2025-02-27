#%%
import requests 
import pandas as pd
import os

# Get the URL for the latest ASIC business names dataset from data.gov.au

file_info_list = requests.get('https://data.gov.au/data/api/3/action/package_show?id=bc515135-4bb6-4d50-957a-3713709a76d3').json()

file_info = [x for x in file_info_list['result']['resources'] if x['format'] == 'CSV']

file_url = file_info[0]['url']

print(file_url)

#%%

# Get the current ASIC file and read into pandas df

filename = file_url.split("/download/")[1]

print(f"Downloading {file_url}")
# r = requests.get(file_url)

df = pd.read_csv(file_url, sep='\t')

#%%

# Get historical data of deregistered businesses

historical = pd.read_csv('historical_data/deregistered_2010_to_2024.csv', sep='\t')

#%%

# Join the two DFs and drop duplicates

merged = pd.concat([df, historical])

print(len(merged))

#%%
merged = merged.drop_duplicates()
print(len(merged))
# check_dupes = merged[merged.duplicated(subset=['BN_NAME'], keep=False)]

#%% Write the merged file

merged.to_csv('complete_asic_business_data.gz', compression='gzip', index=False)

#%%
os.makedirs("deregistered", exist_ok=True)

dereg = df[df['BN_STATUS'] == 'Deregistered']

dereg.to_csv(f'deregistered/deregistered_{filename}', index=False)
# #%%

# with open(f'temp_data/{filename}', "wb") as f_out:
#     print(f"Saving {filename}")
#     f_out.write(r.content)


