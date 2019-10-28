import re
import codecs

source = 'C:\SomeFolder\Backup.srt'
destination = 'C:\SomeFolder\\result.txt'
cleanedtext = []

# Read source file
with open(source) as f:
    alltext = f.readlines()

# Write text to array + correct if ending time
for line in alltext:
    if re.match('\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}',line):
        originalnumbers = int(line[-4:])
        newNumbers = originalnumbers - 100
        if(newNumbers < 100):
            newNumbers = '000'

        newNumbers = str(newNumbers)


        buffer = line[:-4]
        line = f"{buffer}{newNumbers}\n"
    
    cleanedtext.append(line)

# Write result to file
file = codecs.open(destination,'w', 'utf-8') 
for line in cleanedtext:
    file.write(line)

file.close()
print('Clean up finished')


 
