# f = open("E:\\python problem solving\\Practice\\file.txt", "w")
# f = open("E:\\python problem solving\\Practice\\file.txt", "a") # Append
# f.write("\nI love JavaScript")
# f = open("E:\\python problem solving\\Practice\\file.txt", "r")
# print(f.read())
# f.close()
f = open("E:\\python problem solving\\Practice\\file.txt", "r")
 
newFile = open("E:\\python problem solving\\Practice\\wordcout.txt", "w")

for line in f:
    tokens = line.split(" ")
    newFile.write("Wordcount :"+ str(len(tokens)) + " "+ line)
    print(str(tokens))

f.close()
newFile.close()

# close the file autometically with statement

with open("file.txt", "r") as fl: # location same as py file
    print(fl.readline()) # return first line
    print(fl.readline()) # return second line
    print("-------")
    

print(fl.closed) # true
