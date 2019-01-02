# read student.3grades.txt file into a dictionary,
# where key is the student's name, value is the list of 3 integers.
# The input file has format of:
# name,gradeOfMath,gradeOfLanguage,gradeOfEnglish

fhand = open("../data/student.3grades.txt")
data = {}
for line in fhand:
    words = line.rstrip().split(',')
    data[words[0]] = [int(v) for v in words[1:]]

print(data)
fhand.close()
