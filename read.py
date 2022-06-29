import random


with open('quotes.txt') as f:
    lines = f.read()
    myarray = lines.split("\n\n")


random.shuffle(myarray)
with open('quotes_shuffled.txt', 'w') as f:
    for i in range(len(myarray)):
        f.write(myarray[i] + "\n\n")
        if i == len(myarray) - 1:
            break
    f.close()

#remove first line of file 
with open('quotes_shuffled.txt', 'r') as f:
    lines = f.readlines()
    lines.pop(0)
    with open('quotes_shuffled_missing1.txt', 'w') as f:
        f.writelines(lines)
    f.close()