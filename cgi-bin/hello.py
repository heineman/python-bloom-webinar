import cgi
from validate import validateKey

# Mime header
print ("Content-Type: text/plain;charset=utf-8")
print ()

# Retrieve HTTP fields and make sure accessKey is there and
# contains a valid key by checking with database.
arguments = cgi.FieldStorage()

success = False
if "accessKey" in arguments:
    key = arguments["accessKey"].value
    info = validateKey(key)
    if info:
        print ("Access to ", info, " granted")
        success = True


if not success:            
    print ("Invalid Request.")
    

    
