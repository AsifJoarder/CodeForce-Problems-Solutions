num = int(input())   #Taking Number Input

words = [input() for i in range(num)]   # Making a list of input

i=0
for j in range(num):
    i=0
    if len(words[j]) > 10:   # Checking if the word length is more than 10
        for count in words[j]:
            i+=1
    else:
        print(words[j])
        continue

    a=i-2
    b=words[j][0]
    c=words[j][-1]
    print(b+str(a)+c)

