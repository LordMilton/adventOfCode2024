file = open('input')
reports = []
for line in file:
    splitline = line.split()
    reports.append([int(x) for x in splitline])
print(reports)

transformedReports = [[x-y for x,y in zip(report,report[1:])] for report in reports]
safeReports = [report for report in transformedReports
                if 1 <= abs(report[0]) <= 3 
                    and len([y for x,y in zip(report,report[1:])
                        if 1 <= abs(y) <= 3 and x*y > 0]) == len(report)-1]

print(len(safeReports))
