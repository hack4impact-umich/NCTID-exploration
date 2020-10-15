import csv
import json
import requests

id_and_conditions = {}

index = 1
nctid_index = 1
with open('all_conditions.csv', 'r') as csvfile:
    condition_reader = csv.reader(csvfile, delimiter=' ')
    for condition in condition_reader:
        new_condition = condition[0].replace(',', '').lower().replace(' ', '+')
        print("Currently grabbing: " + condition[0] + ", #"+str(index)+"/6593")
        r = requests.get('https://clinicaltrials.gov/api/query/field_values?expr='+new_condition+'&field=nctid&fmt=json')
        r = r.json()
        for trial in r['FieldValuesResponse']['FieldValues']:
            trial_num = trial['FieldValue']
            if trial_num not in id_and_conditions:
                new_conditions = condition[0]
                id_and_conditions[trial_num] = [new_conditions]
            else:
                # handle dupes
                if condition[0] not in id_and_conditions[trial_num]:
                    id_and_conditions[trial_num].append(condition[0])
        nctid_index += 1
        index += 1
        if nctid_index > 300:
            break

json_file = "nctid_and_conditions.json"
with open(json_file, 'w') as outfile:
    json.dump(id_and_conditions, outfile, indent=2, sort_keys=True)
