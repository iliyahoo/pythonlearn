#!/usr/bin/python3

import csv
import json
import datetime

with open("debug.csv", "wb+") as csv_file:
    f = csv.writer(csv_file)
    # Write CSV Header
    f.writerow([
        "action", "user_id", "show_name", "network_state", "os", "seq", "device_type", "responce time", "datetime"
        ])

    with open("debug.log") as log_file:
        x = log_file.readlines()
        for x in x:
            x = json.loads(x)
            if x.get("action",None) == 'vote' or x.get("user_id",None) is None:
                continue
    
            try:
                f.writerow([
                    x.get("action",None),
                    x.get("user_id",None),
                    x.get("show_name",None),
                    x.get("network_state",None),
                    x.get("os",None),
                    x.get("seq",None),
                    x.get("device_type",None),
                    x.get("ts_ack",None) -  x.get("ts_sent",None),
                    datetime.datetime.fromtimestamp(x.get("timestamp",None) / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
                ])
            except:
                continue

csv_file.close()
log_file.close()
