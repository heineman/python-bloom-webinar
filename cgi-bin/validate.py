# Simple application which validates a given CGI-BIN
# request is valid using an AccessKey API

import mysql.connector
from config import configInformation

def validateKey(key):
    """Validate Key and return info from database upon match"""
    cnx = mysql.connector.connect(**configInformation)

    cur = cnx.cursor()

    # Use binding. Note final ',' after key is necessary    
    cur.execute("SELECT info FROM Accounts where accessKey=%s", (key,))
    value = cur.fetchmany(size=1)
            
    cnx.close()
    return value
