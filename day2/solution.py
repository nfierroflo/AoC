import os

def safe_reports(reports):
    safe_reports = 0

    for report in reports:
        report_offset = report.copy()[1:]
        report_offset.append(0)

        increment = [x-y for x,y in zip(report_offset, report)][:-1]
        if (all(x < 0 for x in increment) or all(x > 0 for x in increment)) and (all(abs(x) <= 3 for x in increment)):
            safe_reports += 1
    return safe_reports

def can_be_made_safe(report):
    # Try removing each element and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        report_offset = modified_report.copy()[1:]
        report_offset.append(0)
        
        increment = [x-y for x,y in zip(report_offset, modified_report)][:-1]
        if (all(x < 0 for x in increment) or all(x > 0 for x in increment)) and (all(abs(x) <= 3 for x in increment)):
            return True
    return False

def safe_reports_with_deletion(reports):
    safe_reports = 0
    for report in reports:
        if can_be_made_safe(report):
            safe_reports += 1
    return safe_reports

def text2list(text):
    with open(text, 'r') as file:
        lines = file.readlines()
        reports = []
        for line in lines:
            reports.append(list(map(int, line.split())))
        return reports

if __name__ == "__main__":
    reports_test = [[7,6,4,2,1],[1,2,7,8,9],[1,3,2,4,5],[1,3,6,7,9]]
    
    # Test the original safe_reports function
    assert safe_reports(reports_test) == 2
    
    # Test the new function with deletion
    assert safe_reports_with_deletion(reports_test) == 3  # The third report can be made safe by removing 2

    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")

    reports = text2list(input_file)
    print(f"Part 1: {safe_reports(reports)}")
    print(f"Part 2: {safe_reports_with_deletion(reports)}")


        
