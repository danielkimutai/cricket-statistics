import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"test"}

headers = {
	"x-rapidapi-key": "ecc92bcc30msh3928ba40a1fa147p11127ejsn0c31aac1f716",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200: 
    # extracting the data 
    data = response.json().get('rank',[]) 
    csv_filename = "batsmen_rankings.csv"

    if data: 
        field_names = ['rank','name','country','avg']

        # write data to CSV file with only specified field names 
        with open (csv_filename,'w',newline='',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=field_names)
            writer.writeheader()
            for entry in data :
                writer.writerow({field: entry.get(field) for field in field_names})

        print (f"Data has been fetched successfully to '{csv_filename}'")
    else:
        print("No data available from the API")

else:
    print ("failed to fetch  data:",response.status_code)