file = open('input')
reports = []
for line in file:
    splitline = line.split()
    reports.append([int(x) for x in splitline])

transformedReports = [[y-x for x,y in zip(report,report[1:])] for report in reports]
safeReports = []
for num,report in enumerate(transformedReports):
    for i in range(-1,len(report)+1):
        ensafenedReport = []
        if i == -1:
            ensafenedReport = report
        elif i == 0:
            ensafenedReport = (report[i+1:])
        elif i < len(report):
            ensafenedReport = report[:i-1]
            ensafenedReport.append(report[i-1]+report[i])
            ensafenedReport.extend(report[i+1:])
        else:
            ensafenedReport = report[:i-1]
        if (1 <= abs(ensafenedReport[0]) <= 3 
            and len([y for x,y in zip(ensafenedReport,ensafenedReport[1:])
                if 1 <= abs(y) <= 3 and x*y > 0]) == len(ensafenedReport)-1):
            safeReports.append(ensafenedReport)
            break  
print(len(safeReports))

# 2 2 1 2 1 3 -3
#   2 1 2 1 3 -3
# 4   1 2 1 3 -3
# 2 3   2 1 3 -3
# 2 2 3   1 3 -3
# 2 2 1 3   3 -3
# 2 2 1 2 4   -3
# 2 2 1 2 1 0
# 2 2 1 2 1 3