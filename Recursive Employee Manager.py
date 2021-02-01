emp_hiercy = {1:6,2:6,3:6,4:6,5:6,6:7,7:0}

def find_hrchy(emp_hiercy : dict(),tatget : int):
    ans_reports = []
    for key,value in emp_hiercy.items():
        if value == tatget and value != 0:
            ans_reports.append(key)
    return ans_reports

print(find_hrchy(emp_hiercy,6))     
