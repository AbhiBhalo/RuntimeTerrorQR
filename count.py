fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else: counts[word] += 1
#print(counts)
hist=[None]*6
for key in counts:
    if key=='0':
        hist[0]=counts[key]
    elif key=='1':
        hist[1]= counts[key]
    elif key=='2':
        hist[2]=counts[key]

    elif key=='3':
        hist[3]= counts[key]
    elif key=='4':
        hist[4]=counts[key]
    elif key=='5':
        hist[5]= counts[key]

    else:
        continue

i=0
total=0
f=0
print("Score : Frequency")
while i < (len(hist)):
    print(i,"    :   ",hist[i])
    if hist[i]!=None:
        total=total+(hist[i]*i)
        f=f+hist[i]
    i+=1
avg=float(total/f)
print("Total no. of feedbacks is :",f)
print("Sum of all the scores is :",total)
print("Average score is : ",avg)



