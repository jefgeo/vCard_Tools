

# PREP INPUT FILE:  Take output from Outlook, limit to first_name, last_name, org, phone, and email.

import csv

fileOut = open('Outlook for iCloud.vcf', 'w')

with open('Outlook for iCloud.CSV', 'r') as fileIn:
    reader = csv.reader(fileIn)
    for rec in reader:
        fileOut.write('BEGIN:VCARD' + "\n")
        fileOut.write('VERSION:3.0' + "\n")
        fileOut.write('N:' + rec[1] + ';' + rec[0] + ";;;\n")
        fileOut.write('FN:' + rec[0] + ' ' + rec[1] + "\n")
        if len(rec[2]) > 0:
            fileOut.write('ORG:' + rec[2]+ ";\n")
        if len(rec[3]) > 0:
            fileOut.write('TEL;type=CELL:' + rec[3] + "\n")
        if len(rec[4]) > 0:
            fileOut.write('EMAIL;type=WORK:' + rec[4] + "\n")
        fileOut.write('END:VCARD' + "\n")
    fileOut.close()
