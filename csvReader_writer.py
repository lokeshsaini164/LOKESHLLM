import csv
from types import new_class

with open("test.csv","r+") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=",")
    out = list(csvReader)
    #print(out)
    name= []
    status = []
    for x in out:
        name.append(x[0])
        status.append(x[1])
    print(name)
    print(status)
    index = name.index("Joe")
    print(index)
    print("Status of joe is:"+status[index])
    csvfile.close()


#write to csv file
with open("test.csv",mode="a", newline="") as csvfile1:
    write = csv.writer(csvfile1, )
    write.writerow(["Ankur","Approved"])
    csvfile1.close()


