import json
import base64
import time

def main():
    #parse data from exercise-02/data/data.json
    with open("exercise-02/data/data.json") as json_file:
        data = json.load(json_file)

    #initialize variables
    value_total = 0
    uuids = []

    #iterate through devices
    for device in data["Devices"]:
        #check if timestamp is before current time
        if int(device["timestamp"]) < int(time.time()):
            continue
        #decode value and add to total
        value_total += int(base64.b64decode(device["value"]))
        #parse uuid from info field
        uuid = device["Info"].split("uuid:")[1].split(",")[0]
        uuids.append(uuid)

    #create output object
    output = {
        "ValueTotal": value_total,
        "UUIDS": uuids
    }

    #write output to file
    with open("exercise-02/output.json", "w") as outfile:
        json.dump(output, outfile)

if __name__ == '__main__':
    main()