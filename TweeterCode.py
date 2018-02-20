
fhand= input("Enter the file Location : ")


with open (fhand, encoding = "latin-1") as file:
    line=file.readlines()
l = {}

for words in line:
    word = words.split()
    if word[0] in l:
        l[word[0]] +=1
    else:
        l[word[0]] = 1
l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)

outputFile = open('D:/UNC/2ND semester/Software Engineering/05/TopFootbalUsers.txt', 'w', encoding = "utf-8")
outputFile.write("Top 10 users who have tweeted the most for the entire timeline. :"+ "\n")
for i in range (0,10):
    outputFile.write(l[i][0] + " has tweeted this amount: " + str(l[i][1])+ "\n ")




fhand = input("Enter the file Location : ")


with open (fhand, encoding = "latin-1") as file:
    line=file.readlines()

l = {}
for words in line:
    word = words.split()
    word2 = word[1].split(":")
    wordBy = word[0] + " " + word2[1]
    if wordBy in l:
        l[wordBy]+=1
    else:
        l[wordBy]=1
l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)

k={}
count = 0
for word in l:
    count+=1
    if(word[0].split()[1]) in k:
        k[word[0].split()[1]]+=1
    else:
        k[word[0].split()[1]]=1
k = sorted(k.items(), key = operator.itemgetter(1))


outputFile = open('D:/UNC/2ND semester/Software Engineering/05/TopFootbalUserForEveryHour.txt', 'w', encoding = 'utf-8')

for x in range (0,len(k)):

    numSearch= 10


    for dat in l:
        if numSearch == 0:
            break
        if dat[0].split()[1] == k[x][0]:
            outputFile.write(dat[0].split()[0] + "\n Spend Hours: " + k[x][0] +"\n")

            numSearch-=1


fhand = input("Enter the file Location : ")


with open (fhand, encoding = "latin-1") as file:
    line=file.readlines()

l = {}
for words in line:
    word = words.split()
    if word[0] not in l:
        l[word[0]] = int(word[-2])

l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)
outputFile = open('D:/UNC/2ND semester/Software Engineering/05/Top 10 Footbal user with most followers.txt', 'w', encoding = "utf-8")
outputFile.write("Top 10 Footbal user with most followers: " + "\n\n")

for i in range (0, 10):
    outputFile.write(str(i+1) + "."+l[i][0] + " -> Number of Followers: " + str(l[i][1]) + "\n\n")



fhand = input("Enter the file Location : ")

with open (fhand, encoding = "latin-1") as file:
    line=file.readlines()

l = {}
for words in line:

    word = words.split()
    y = len(word)-2
    handle = "\""
    for x in range (4, y):
        handle += word[x] + " "
    handle += " ::::;:::: " + word[0]

    if handle not in l:
        l[handle] = int(word[-1])

outputFile = open('D:/UNC/2ND semester/Software Engineering/05/Top 10 retweet.txt', 'w', encoding = "utf-8")
l = sorted(l.items(), key = operator.itemgetter(1), reverse = True)
outputFile.write("Top 10 Footbal tweets that has the max number of retweets : " +"\n\n")

for k in range (0, 10):
    outputFile.write(str(k+1) + "." + l[k][0].split()[-1] + "\n Tweet: " +
                        l[k][0].split("::::;::::")[0] + "\n Number of retweets: " + str(l[k][1]) + "\n\n")

