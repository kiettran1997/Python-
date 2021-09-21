# bài 7
def top_three_avg(grade1, grade2, grade3, grade4):
 total = grade1 + grade2 + grade3 + grade4
 top_three = total - min(grade1, grade2, grade3, grade4)
 return top_three / 3

 # hoặc
 #return max(average_grade(grade1, grade2, grade3)
 #return (grade1 + grade2 + grade3) / 3
 