import re
#-----------------------------------functions------------------------------

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

#----linear search func------
def linear_search(list,word):
    i = 0
    while i < len(list) and list[i] != word.upper():
        i += 1    
    if i  >= len(list):
        print("Line",line_num, "possible misspelled word: ",word)

#----Binary search func------

def binary_search(list,word):
    lower_bound = 0
    upper_bound = len(list)-1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if list[middle_pos] <(word.upper()):
            lower_bound = middle_pos + 1
        elif list[middle_pos] > (word.upper()):
            upper_bound = middle_pos - 1
        else:
            found = True
    
    if not found:
          print("Line",line_num, "possible misspelled word: ",word)
   
#--------------------------------Main program--------------------------------

dictionary_file = open("dictionary.txt")
dictionary_list = []

for line in dictionary_file:
    line = line.strip()
    dictionary_list.append(line)
 
dictionary_file.close()

print("--- Linear Search ---") 

AliceInWonderLand_file = open("AliceInWonderLand200.txt")

line_num = 0
for line in AliceInWonderLand_file:
    words = split_line(line)
    line_num +=1
    for word in words:
        linear_search(dictionary_list,word)
   

AliceInWonderLand_file.close()


print("--- Binary Search ---") 

AliceInWonderLand_file = open("AliceInWonderLand200.txt")

line_num = 0
for line in AliceInWonderLand_file:
    words = split_line(line)
    line_num +=1
    for word in words:
        binary_search(dictionary_list,word)
   

AliceInWonderLand_file.close()