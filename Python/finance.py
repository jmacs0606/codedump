import csv
annualData = [[],[],[]]
iter = 2021
while iter > 1899:
    annualData[0].append(str(iter))
    iter -= 1
gdp = open("gdpgrowth.csv",newline="")
gdpRead = csv.reader(gdp, delimiter=',', quotechar='|')
for ret in gdpRead:
    print(ret)
    if ret[1] in annualData[0]:
        annualData[1].append(ret[1])
    else:
        annualData[1].append("N/D")
print(annualData)

gdp.close()
