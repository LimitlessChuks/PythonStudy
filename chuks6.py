
def grade_classifier(score):
    
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    else:
        grade = 'F'

   
    return grade
print(grade_classifier(62))



