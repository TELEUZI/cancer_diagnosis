import timeit
from patient import *

a = Classification_chars()
b = Classification_chars()
num_2 = 0
num_4 = 0
with open("training_data.txt") as file:
    for line in file.read().split("\n"):
        if "?" in line:
            continue
        p = [int(z) for z in line.split(",")]
        q = Patient_chars(p)
        if q.patient_class == 2: 
            a += q
            num_2 += 1
        else:
            b += q
            num_4 += 1
classificator = (a/num_2+b/num_4)/2
l_2 = []
l_4 = []
good = 0
with open("testing_data.txt") as file:
    for line in file.read().split("\n"):
        p = [int(z) for z in line.split(",")]
        q = Patient_chars(p)
        if q > classificator:
            if q.patient_class == 4:
                good += 1
            l_4.append(q)
        else:
            
            l_2.append(q)
            if q.patient_class == 2:
                good += 1
print("ZDOROVIE")
for i in range(len(l_2)):
    print(l_2[i].__str__())
print("BOLNUI")
for i in range(len(l_4)):
    print(l_4[i].__str__())
print (good/(len(l_2)+len(l_4)))