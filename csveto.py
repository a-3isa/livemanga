import csv
import os 

fields = ['completed', 'remaining']
i =os.listdir("inp")
print(i)
with open("data.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(i)