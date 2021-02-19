#given dicionary representing a student name as a key and corresponding value is a grade which
#he obtained in different subjects. wap update each dict value with average score obtained by
#each student respectively

scores = {"st1":[65,68,59,52,69,65,55,59],"st2":[60,64,60,60,88,64,68,75],"st3":[59,72,64,62,66,68,72,73],"st4":[82,62,61,54,71,89,75,73]}
for i in scores.keys():
    count = 0
    x=0
    for j in scores[i]:
        count = count + j
        x=count/800*100
    scores[i] = x
print(scores)
        
