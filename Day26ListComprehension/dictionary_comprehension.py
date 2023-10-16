# Dictionary Comprehension 
import random
names=["Ren", "Beth", "Rudo","Bruno","Noell","Emmet","Eloise","Elaine","Regetha", "Inegear"]

student_scores={item: random.randint(50,100) for item in names}

highscore_students={student:value for student,value in student_scores.items() if value>80}

print(highscore_students)