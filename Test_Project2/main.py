# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import os

def UpdateJSON():

    Testdirectory = os.path.dirname(__file__)
    JSONFile = os.path.join(Testdirectory, 'TestFilesDir', 'test_payload.json')

    #f = open(JSONFile)

    # returns JSON object as
    # a dictionary
    #data = json.load(f)

    f = open(JSONFile,'r')

    data = json.loads((f.read()))

    data["inParams"].pop("appdate")

    data.pop("outParams")

    NewJSONFile = os.path.join(Testdirectory, 'TestFilesDir', 'New_test_payload.json')

    with open(NewJSONFile, 'w', encoding='utf-8') as x:

         json.dump(data, x, indent=4)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    UpdateJSON()