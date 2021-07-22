import json
source_dip_1 = [{"id": x, "name": "Test {}".format(x)} for x in range(1, 11)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(31, 41)]
source_dip_2 = [{"id": x, "name": "Test {}".format(x)} for x in range(11, 21)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(41, 51)]
source_dip_3 = [{"id": x, "name": "Test {}".format(x)} for x in range(21, 31)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(51, 61)]
with open('jsons/source_1.json', 'w') as outfile:
    json.dump({"1": source_dip_1}, outfile)
with open('jsons/source_2.json', 'w') as outfile:
    json.dump({"2": source_dip_2}, outfile)
with open('jsons/source_3.json', 'w') as outfile:
    json.dump({"3":  source_dip_3}, outfile)