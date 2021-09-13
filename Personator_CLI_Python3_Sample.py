#Import the modules. You may have to download and install them.
import requests
import json


print()
print("===============================================")
print("       PERSONATOR WEB SERVICE EXAMPLE")
print("===============================================")
print()


# This is the enpoint we will end up hitting, actions to perform, and desired output properties
URL      = "http://personator.melissadata.net/v3/WEB/ContactVerify/doContactVerify?t=test_Standard_REST"
ACTIONS  = "&act=Check,Verify"
COLUMNS  = "&cols=GrpAll"

#Other actions and options. Please see out public wiki for full list
#ACTIONS  = "&act=Check,Verify,Move,Append"
#COLUMNS  = "&cols=GrpAll"
#COLUMNS  = "&cols=GrpNameDetails,GrpParsedAddress,GrpAddressDetails,GrpCensus,GrpParsedEmail,GrpParsedPhone"


# We'll prompt for basic inputs
IDENT    = "&id="+input("  Enter IDENT   : ")
FULLNAME = "&full="+input("  Enter FULLNAME: ")
ADDRESS1 = "&a1="+input("  Enter ADDRESS1: ")
CITY     = "&city="+input("  Enter CITY    : ")
STATE    = "&state="+input("  Enter STATE   : ")
ZIP      = "&postal="+input("  Enter ZIP     : ")
OTHER    = "&a2=&comp=&email=&phone=&ctry=USA&format=json"

# Join them together for a valid request
PERSWS_REQ = URL+IDENT+ACTIONS+COLUMNS+FULLNAME+ADDRESS1+CITY+STATE+ZIP+OTHER

print()
print("  Sent Request: ")
print()
print(PERSWS_REQ)
print()

# Create the request and get the response
r = requests.get(PERSWS_REQ)
r.text

# Convert it to a Python dictionary
#data = json.loads(r.text)


print("  Returned Response: ")
print()

#print out the entire response
python_obj = json.loads(r.text)
print(json.dumps(python_obj, sort_keys=True, indent=2))
