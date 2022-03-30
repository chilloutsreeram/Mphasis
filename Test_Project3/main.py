import csv
import os
import pandas as pd

def PrintoutResp():
    # Use a breakpoint in the code line below to debug your script.

    Testdirectory = os.path.dirname(__file__)
    JTLFile = os.path.join(Testdirectory, 'TestFilesDir', 'Jmeter_log1.jtl')
    df = pd.read_csv(JTLFile)
    rdf = df[df['responseCode'] != 200]
    rdf = rdf[['label', 'responseCode', 'responseMessage', 'failureMessage', 'timeStamp']]
    rowcount: int = len(rdf.index) - 1

    for x in range(rowcount):
        print(rdf.iloc[x:x+1, [0,1,2,3,4]])

if __name__ == '__main__':
    PrintoutResp()

    1612879375436