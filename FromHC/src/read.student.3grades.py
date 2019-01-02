# read student.3grades.txt file into a dictionary,
# where key is the student's name, value is the list of 3 integers.
# The input file has format of:
# name,gradeOfMath,gradeOfLanguage,gradeOfEnglish

fhand = open("../data/student.3grades.txt")
data = {}
for line in fhand:
    line = line.rstrip()
    words = line.split(",")
    name = words[0]
    grade = [int(words[1]), int(words[2]), int(words[3])]
    data[name] = grade

print(data)
fhand.close()
