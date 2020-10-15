from selenium import webdriver
import csv

url_ids = ["BC26", "BC02", "BC23", "BXS", "BC25", "BC17", "BC08", "BC03", "BC24", 
"BC18", "BC10","BC05","BC07","BC24", "BC14","BC19","BC11","BC09","BC21","BC16",
"BC06","BC04","BC15","BXM", "BC01"]

all_conditions = []

for url_id in url_ids:
    url = 'https://clinicaltrials.gov/ct2/search/browse?brwse=cond_cat_'+url_id
    driver = webdriver.Firefox()
    driver.get(url)
    meta = driver.execute_script('return tableData1')
    for data in meta:
        raw_string = data[0]
        condition = raw_string[raw_string.find(">")+1:raw_string.find("</a>")]
        all_conditions.append(condition)

csv_file = 'all_conditions.csv'
with open(csv_file, 'w', newline='') as output:
    writer = csv.writer(output, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    for condition in all_conditions:
        writer.writerow([condition])