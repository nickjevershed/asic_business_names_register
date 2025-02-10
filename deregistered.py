#%%
import requests 
import pandas as pd

# Get the URL for the latest ASIC business names dataset from data.gov.au

file_info_list = requests.get('https://data.gov.au/data/api/3/action/package_show?id=bc515135-4bb6-4d50-957a-3713709a76d3').json()

file_info = [x for x in file_info_list['result']['resources'] if x['format'] == 'CSV']

file_url = file_info[0]['url']

print(file_url)

#%%

# Use requests to download the full CSV to the temp_data folder

filename = file_url.split("/download/")[1]

print(f"Downloading {file_url}")
# r = requests.get(file_url)

df = pd.read_csv(file_url, sep='\t')

dereg = df[df['BN_STATUS'] == 'Deregistered']

dereg.to_csv(f'deregistered/deregistered_{filename}')
# #%%

# with open(f'temp_data/{filename}', "wb") as f_out:
#     print(f"Saving {filename}")
#     f_out.write(r.content)


