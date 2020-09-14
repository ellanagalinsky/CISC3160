import csv
import operator


rows = []

with open("/Users/ellanagalinsky/Documents/GitHub/CISC3160/Assignments/Lab_2/Marriage_and_Divorce_Rates_2019.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #saving csv.reader as csvreader object
    for row in csvreader:
        rows.append(row)
    sortRate = sorted(csvreader, key=operator.itemgetter(2))
    
    sortYears = sorted(csvreader, key=operator.itemgetter(0))





