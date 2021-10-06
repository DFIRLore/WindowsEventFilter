report = [] 
with open("systemevt.txt", "r") as file: 
    for line in file: 
        splits = line.split('\t') 
        if '107' in line: 
            print(f'System power status changed {splits[1].rstrip()}') 
            report.append(f'Power status changed {splits[1]}') 
            
    print(report)

with open("Report_for_systemevt.txt", "w") as file2:
    for value in report:
        file2.write(value)
        
 
