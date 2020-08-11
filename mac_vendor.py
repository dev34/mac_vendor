#!/usr/bin/python
import optparse  # Command Line arguments
from json import load # Handling json files
parser=optparse.OptionParser()
parser.add_option('-m','--mac',dest='mac',help='Displays vendor for given mac')
options,arguments=parser.parse_args()
if not options.mac:
    parser.error('You must specify a mac address with option -m --mac\n\nOptions:\n  -h, --help         show this help message and exit\n  -m MAC, --mac=MAC  Displays vendor for given mac')
# Handling given mac address format
if ':' in options.mac:
    given_mac=''.join(str(options.mac).upper().strip()[0:8].split(':'))
elif '-' in options.mac:
    given_mac=''.join(str(options.mac).upper().strip()[0:8].split('-'))
else:
    given_mac=str(options.mac).upper().strip()[0:6]
file1=load(open('Database/Vendor_database.json',encoding='utf-8')) 
try:
    print(file1[given_mac]) # Extracting given mac from database and then output to the user
except:
    print('Error: Invalid MAC Address')