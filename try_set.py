import random
import datetime

checkedlist = [random.randint(0,100000000) for i in range (10000000)]
checklist = [random.randint(0,100000000) for i in range (100)]
start = datetime.datetime.now()
for check in checklist:
    if check in checkedlist:
        print(f"{check}checkedlist")

end = datetime.datetime.now()
print(end - start)

checkedlist2 = set([random.randint(0,100000000) for i in range (10000000)])
checklist = [random.randint(0,100000000) for i in range (100)]
start = datetime.datetime.now()
for check in checklist:
    if check in checkedlist2:
        print(f"{check}checkedlist2")

end = datetime.datetime.now()
print(end - start)