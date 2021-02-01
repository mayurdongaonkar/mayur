classroom = [["Bob","87"],["Mike","35"],["Bob","52"],["Jason","35"],["Mike","55"],["Jessica","99"]]

def avg_salary_finder(classroom : list):
    student_total = {}
    student_subj  = {}
    for student in classroom:
        if student[0] not in student_total:
            student_total[student[0]] =  int(student[1])
            student_subj[student[0]]  =  1
        else:
            student_total[student[0]] =  int(student[1]) + int(student_total.get(student[0]))
            student_subj[student[0]]  += 1
        
    b = dict((k, student_total[k] // student_subj[k]) for k in student_subj)
    print(b)
    
    ###d3 = dict((k, float(d2[k]) / d1[k]) for k in d2)
            
    print(student_subj)        
    return student_total
        
print(avg_salary_finder(classroom))