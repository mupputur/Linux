#write a program the average of given list of elements representing a grade of student
marks=[84,84,93,78,86,73]
count=0
for i in marks:
    count=count+i
average=count/600*100
if average > 90.0:
    print("A+",average)
if average > 80.0 and average < 90.0:
    print("A", average)
if average > 70.0 and average < 80.0:
    print("B+", average)
if average > 60.0 and average < 70.0:
    print("B", average)
if average > 50.0 and average < 60.0:
    print("C" , average)
if average > 40.0 and average < 50.0:
    print("D", average)
