
import requests
import json
import csv

url = "https://www.hko.gov.hk/wservice/tsheet/pms/ssdb_rank.js"
response = requests.get(url)
js_text = response.text
json_start = js_text.find('{')
json_data = js_text[json_start:]
data_obj = json.loads(json_data)

rank_list = data_obj["RANK_SURGE"]

header = ["Rank", "Storm Surge Height", "Tropical Cyclone", "DateTime"]
rows = []
for station in rank_list:
    if station["ENG"] == "Quarry Bay/North Point":
        for i, record in enumerate(station["RANK"], 1):
            height = record["HEIGHT"]
            cyclone = record["ENG"]
            dt = record["TIME"] if record["TIME"] else record["YEAR"]
            rows.append([i, height, cyclone, dt])

with open("storm_surge_json_selected.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Saved {len(rows)} storm surge ranking records to storm_surge_json_selected.csv")
