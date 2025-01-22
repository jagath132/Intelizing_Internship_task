# 1.Get the name from given input data. (Note: Don't use direct slicing..)
def name_extraced():
    data1 = "From nandhini@gmail.com Sat Jan 21 11:24:32.008173"
    data2 = "From selvakumar@gmail.com Sat Jan 21 11:24:32.008173"
    data3= "From jagath@gmail.com Sat Jan 26 11:24:32.008173"

    def extract_name(data):
        email=data.split()[1]
        name=email.split('@')[0]
        return name
    name1=extract_name(data1)
    name2=extract_name(data2)
    name3=extract_name(data3)
    print (f'name1 = "{name1}", name2 = "{name2}","name3={name3}"')

#2.Reverse the 5-digit number entered by the user
def reverse():
    num=list(input("Enter the numbers to reverse:"))
    # num = [1,2,3,4,5]
    output=[]
    le=len(num)
    for c in range(le):
        last_dig =le - c -1
        output.append(num[last_dig])
    print(output)

# 3.Remove the duplicate elements from given Input list:
def removing_duplicate():
    duplicate_list= ["Apple" ,"Mango" , "Pineapple", "Orange", "Apple", "Mango", "Grapes","Grapes"]
    new_list=[]
    for d in duplicate_list:
        if d in new_list:
            pass
        else:
            new_list.append(d)
    print(new_list)

# 4.find the occurrence and count of vowels in an input string:
def vowels():
    input_string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    vowel_count = {}
    for char in input_string:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
    print(f"Vowel occurrences and count: {vowel_count}")

# 5.write a program to find the sum of first 10 nos which is divisible by 3 and 5
def sum():
    count = 0
    total_sum = 0
    num = 1
    while count<10:
        if num%3==0 and num%5==0:
            total_sum+=num
            count+=1
        num+=1
    print(f'the sum of first 10 nos which is divisible by 3 and 5:{total_sum}')

# 6.Find the second Largest & smallest nos from an Input list:
def second_value():
    num=[45,98,32,19,67,55,90]
    print(f'the user input list before sorting:',num)
    for a in range(0,len(num)):
        for b in range(a+1,len(num)):
            if num[a]>= num[b]:    
                num[a], num[b] = num[b], num[a]
    print(f'the user input list after sorting:',num)
    print(f'the second largest no from the input list:',num[1])
    print(f'the second smallest no from the input list:',num[-2])

# 7.Sort this list:['greeting', 'goodbye', 'thanks', 'about', 'name', 'help', 'create account', 'complaint']
def sorted(): 
    sorted_list = ['greeting', 'goodbye', 'thanks', 'about', 'name', 'help', 'create account', 'complaint']
    sorted_list.sort()
    print(sorted_list) 

# 8.Find the square of first 10 numbers:
def square():
    n=10
    number={}
    for i in range (1,n+1):
        number[i] =i*i
    print("the square of first 10 numbers:",number)

# 9.Write a program to bring the output
# Input: [{"id": 47,"name":"sravya", "game":"cricket"},
# {"id": 49,"name":"krishna", "game":"tennis"},
# {"id": 33,"name":"vinothini", "game":"volleyball"},
# {"id": 21,"name":"samuel", "game":"cricket"},
# {"id": 17,"name":"bhuvana", "game":"tennis"}]
# output: {"cricket":[sravya,samuel],"tennis":[krishna,bhuvana],"volleyball":[vinothini]}
def get_players():
    input = [{"id": 47,"name":"sravya", "game":"cricket"},
                {"id": 49,"name":"krishna", "game":"tennis"},
                {"id": 33,"name":"vinothini", "game":"volleyball"},
                {"id": 21,"name":"samuel", "game":"cricket"},
                {"id": 17,"name":"bhuvana", "game":"tennis"}]
    output = {}
    for a in input:
        if a["game"] in output:
            output[a["game"]].append(a["name"])
        else:
            output[a["game"]] = [a["name"]]
    print(output)

# 10.Input  = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
# output = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
def grouped_list():
    in_list={'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    op_list={}
    for a in in_list:
        b=in_list[a]
    
        if b not in op_list:
            op_list[b]=[]
        op_list[b]+=[a]
    print(op_list)

# 12. Input:a2b3c5 Output:aabbbccccc
def repeat():
    input_str = input("enter the input:") 
    output_str = " "
    for i in range(0,len(input_str),2):
        output_str += input_str[i] * int(input_str[i + 1])
    print(output_str)

# 13.convert Input sentence into list of words.
def sen_split():
    sen="The coding question of Java Programming will help you to crack the coding interview rounds"
    sentence = sen.split()
    print(sentence) 

# 14.Convert List of values into string:
def sen_join():
    sen1=["The", "coding", "question", "of", "Java", "Programming", "will" , "help", "you", "to", "crack" , "the", "coding", "interview", "rounds"]
    sentence_join=" ".join(sen1)
    print(sentence_join)

# 15.write a program to print following patterns:
# 1.
# *
# **
# ***
# ****
# *****
def pattern_1():
    n=int(input("enter the number to print the '*':"))
    for i in range(0,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
# 2.
# *****
# ****
# ***
# **
# *
def pattern_2():
    n=int(input("enter the number to print the '*':"))
    for i in range(0,n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        print()
# 3.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
def pattern_3():
    print("pattern_3")
    n=int(input("the no .of rows to print:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
# 4.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def pattern_4():
    print("pattern_4")
    n=int(input("the no .of rows to print:"))
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1
        print()
# 5.
# A
# A B
# A B C
# A B C D
# A B C D E
def pattern_5():
    print("pattern_5")
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
# 6.
# A
# B C
# D E F
# G H I J
def pattern_6():
     print("pattern_6")
     n = int(input("enter the number of rows:"))
     for i in range(1, n + 1):
          for j in range(i):
               print(chr(65 + j), end=" ")
          print()        

# 16.Python Program to Take in a String and Replace Every Blank Space with Hyphen
def sen_splited():
    sen="python is general purpose programming langauage"
    replace_sen=""
    for i in sen:
        if i == ' ':
            replace_sen +='-'
        else:
            replace_sen +=i
    print(replace_sen)

# 18. Remove Adjacent Duplicate characters form a input string
# Input=  bteechhgeeeekkkkssss
# Output =  btechgeks 
def remove_adjacent_duplicates():
    input_string = "aabbccddeeffgghh"
    print("Input String:", input_string)
    result = [] # empty list

    for char in input_string:
        if len(result) == 0 or result[-1] != char:
            result.append(char)
    output_string = "".join(result)
    print("Output String:", output_string)
 
# 19.Python Program to Calculate the Number of Words and the Number of Characters Present in a String
def count():
    demo_string=input("Enter string:")
    string = len(demo_string.split())
    print("The number of words_count in string are : " + str(string))
    print("The number of character_count in string are : "+len(demo_string))

# 20.Python Program to Remove the First Occurrence of Character in a String
# Remove First Occurence of "s"
# Input: goodmorningthisisbtechgeekspython
# Output: goodmorningthiisbtechgeekspython
def first_occur():
    input_string = "goodmorningthisisbtechgeekspython"
    char_to_remove = 's'
    result_string = ""
    found = False
    i = 0
    while i < len(input_string):
        if input_string[i] == char_to_remove and not found:
            found = True  # Mark as found and skip adding to result
        else:
           result_string += input_string[i]
        i += 1
    print("Output:", result_string)


# 24.Python Program to Extract Only Characters from a Given String
# Enter some random string = good morning23this is btechgeeks@19python
# The Given String after extracting only characters = goodmorningthisisbtechgeekspython
# py*th&#on^%in12ter765view
def char_ext():
    sp_char= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*','(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?','/','~','`']
    sen=input("enter the string: ")
    new_sen=''
    print(sp_char)
    for x in sen:
        if x not in sp_char:
            new_sen+=x
        else:
            pass
    print("the new string after removing all sp char: "+new_sen)

# 25.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
# given first string =btechgeeks
# given second string =python
def display_sen():
    a="btechgeeks"
    b="python"
    if len(a)>len(b):
        print(a)
    else:
        len(b)<len(a)
        print(b)

# 1. File Read and write (Text file, csv file, json file) 
def file_read_writetxt():
    f = open("file_read_writetxt.txt", "a")
    f.write("Now the file has more content!,this is text file")
    f.close()
    f=open("file_read_writetxt.txt","r")
    print(f.read())
    
def file_read_writecsv():
    f = open("file_read_writecsv.csv", "a")
    f.write("Now the file has more content!,this is csv file")
    f.close()
    f=open("file_read_writecsv.csv","r")
    print(f.read())

def file_read_writejson():
    f = open("file_read_writejson.json", "a")
    f.write("Now the file has more content!,this is json file")
    f.close()
    f=open("file_read_writejson.json","r")
    print(f.read())

# function calling stmt
if __name__ == "__main__":
    name_extraced()
    # reverse()   
    # vowels()
    # removing_duplicate()
    # sum()
    # square()
    # second_value()
    # get_players()
    # repeat()
    # sen_split()
    # sen_join()
    # count()
    # pattern_1()
    # pattern_2()
    # pattern_3()
    # pattern_4()
    # pattern_5()
    # pattern_6()
    # sen_splited()
    # display_sen()
    # sorted()
    # grouped_list()
    # first_occur()
    # remove_adjacent_duplicates()
    # file_read_writetxt()
    # file_read_writecsv()
    # file_read_writejson()
    # char_ext()
    pass
