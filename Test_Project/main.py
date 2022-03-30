# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xml.etree.ElementTree as XMLT
import os
from datetime import datetime
from datetime import timedelta

def UpdateXML(X, Y):

    todaysdate = datetime.now()

    print("Today's Date:", str(todaysdate))
    Departdate = todaysdate + timedelta(days=X)
    Retrundate = Departdate + timedelta(days=Y)

    CurrDate = todaysdate.strftime('%Y%m%d')
    Ddate = Departdate.strftime('%Y%m%d')
    Rdate = Retrundate.strftime('%Y%m%d')

    Testdirectory = os.path.dirname(__file__)
    print(Testdirectory)
    XMLFile = os.path.join(Testdirectory, 'TestFilesDir','test_payload1')
    print(XMLFile)

    XMLtree = XMLT.parse(XMLFile+'.xml')
    XMLRoot = XMLtree.getroot()

    for departtags in XMLRoot.iter('DEPART'):
        departtags.text = str(Ddate)

    for retruntags in XMLRoot.iter('RETURN'):
        retruntags.text = str(Rdate)

    XMLtree.write('New_test_payload1.xml')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Number of Days to depart:')
    X = int(input())
    print('Enter number of days you plan to retrun after depart:')
    Y = int(input())

    UpdateXML(X, Y)