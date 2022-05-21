#!/usr/bin/python3

"""
Questo programma serve solamente a convertire quel testo 
copia-incollato da iana.org in un file json per poterne
usufruire in javascript.
"""

import json
import pprint

text = []
with open("rootservers.txt") as f:
    for i in f.readlines():
        i = i.strip().split("\t")
        i[1] = i[1].split(",")
        text.append(i)


res = []
for host,ip,operator in text:
    entry = {}
    # bad solution, using strip to remove trailing and leading whitespace
    # for each entry
    entry["hostname"] = host.strip()
    entry["ipv4"] = ip[0].strip()
    entry["ipv6"] = ip[1].strip()
    entry["operator"] = operator.strip()
    res.append(entry)
    
json_res = json.dumps(res)

pprint.pprint(res)

with open("rootservers.json", "w") as json_file:
    json_file.write(json_res)

print("CREATED file rootservers.json")

