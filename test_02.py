import unittest
import json
import main
import base64
import time
from jsonschema import validate

class TestMain(unittest.TestCase):
    def test_02(self):
        with open("exercise-02/data/data.json") as json_file:
            data = json.load(json_file)
        devices = data["Devices"]
        #calculate expected value total
        expected_value_total = 0
        for device in devices:
            if int(device["timestamp"]) < int(time.time()):
                continue
            expected_value_total += int(base64.b64decode(device["value"]))
        #parse uuid from info field
        expected_uuids = []
        for device in devices:
            if int(device["timestamp"]) < int(time.time()):
                continue
            uuid = device["Info"].split("uuid:")[1].split(",")[0]
            expected_uuids.append(uuid)
        #call the main function
        main.main()
        #read the output.json
        with open("exercise-02/output.json") as json_file:
            output = json.load(json_file)
        self.assertEqual(output["ValueTotal"], expected_value_total)
        self.assertEqual(output["UUIDS"], expected_uuids)

    def test_schema(self):
        with open("exercise-02/output.json") as json_file:
            output = json.load(json_file)
        with open("exercise-02/output-schema/schema.json") as json_file:
            schema = json.load(json_file)
        #validate the output against the schema
        validate(output, schema)

if __name__ == '__main__':
    unittest.main()
