with open('day2.txt') as prompt:
    reports = prompt.read().splitlines()
safe_reports_count_pt_1, safe_reports_count_pt_2 = 0, 0
reports = [[int(level) for level in report.split(' ')] for report in reports]

def test_safety(report):
    safe = True
    increasing = report[0] < report[1]
    for idx, level in enumerate(report):
        if not safe: break
        if idx > 0:
          if increasing:
              if report[idx - 1] > level: safe = False
              else:
                  difference = level - report[idx - 1]
                  safe = difference >= 1 and difference <= 3
          else:
              if report[idx - 1] < level: safe = False
              else:
                  difference = report[idx - 1] - level
                  safe = difference >= 1 and difference <= 3
    return safe

for report in reports:
    if test_safety(report):
        safe_reports_count_pt_1 += 1
        safe_reports_count_pt_2 += 1
    else:
        for idx in range(len(report)):
            if test_safety(report[:idx] + report[idx + 1:]):
                safe_reports_count_pt_2 += 1
                break

print("pt 1:", safe_reports_count_pt_1)
print("pt 2:", safe_reports_count_pt_2)
