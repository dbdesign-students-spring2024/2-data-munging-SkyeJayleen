import os
filepath = os.path.join('data', 'nasadata.txt')
origfile = open(filepath, 'r', encoding = 'utf-8')
newfilepath = os.path.join('data', 'mungeddata.csv')
newfile = open(newfilepath, 'w', encoding = 'utf-8')

iterator = 0 # To be used for addressing multiple "Year" rows

# Let's write a function to clean up the lines & convert them to Fahrenheit
def cleanline(x):
    x = line[:-6] + '\n' # Address the repeating "Year" column at the end
    valuelist = x.split()
    if valuelist[0] != "Year": # Skip the label row, it messes with the J-D and D-N
        for i in range(1,len(valuelist)):
            if not valuelist[i].strip('-').isalnum(): # Take care of aesteriks
                valuelist[i] = "NaN"
            else:
                valuelist[i] = format((float(valuelist[i]) / 100) * 1.8,'.1f')
    x = ",".join(valuelist) + '\n' # Replace the spaces by commas
    return x

for line in origfile:
    if line[0] != '\n': # address empty lines
        if line[:4] == "Year" and iterator == 0: # address multiple "year" rows. Record only the first...
            newfile.write(cleanline(line))
            iterator += 1
        elif line[:4] == "Year" and iterator != 0: # ...and ignore the rest.
            continue
        else: # if it's not a "Year" row...
            if line[:4].isnumeric(): # ...and it's a proper row with data, leave it as is.
                newfile.write(cleanline(line))
            else: # address non-data descriptive lines.
                continue
