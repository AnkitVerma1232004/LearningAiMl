#check palindrome 
# def pal(s):
#     l = 0
#     r = len(s) - 1
#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True
# print(pal("madam"))
# print(pal("rage"))




#Given a list of integers, find the average of the list. 
# l=[6,5,8,4,6,4,8]
# def avg_list(l):
#     n=len(l)
#     if n==0:
#         return 0
#     s=sum(l)
#     return round(s/n,2)
# print(avg_list(l))
# Merge two lists into one list and sort them. 
# l=[1,2,7]
# r=[2,4,5]
# a=l+r
# print(a)
# print(sorted(a))




# Given a tuple of numbers, create two different tuples which contain odd numbers and Another contain even numbers. 
# og = (8, 4, 6, 8, 1, 3, 5)
# even = tuple(x for x in og if x % 2 == 0)
# odd = tuple(x for x in og if x % 2 != 0)
# print(f"this is an even tuple {even}")
# print(f"this is an odd tuple {odd}")




# d = {}

# while True:
#     print("\nA - Add student")
#     print("B - Update marks")
#     print("C - Search student")
#     print("D - Display all")
#     print("E - Exit")

#     ch = input("Enter choice: ").upper()

#     if ch == 'A':
#         n = input("Enter name: ")
#         m = int(input("Enter marks: "))
#         d[n] = m

#     elif ch == 'B':
#         n = input("Enter name: ")
#         if n in d:
#             m = int(input("Enter new marks: "))
#             d[n] = m
#         else:
#             print("Student not found")

#     elif ch == 'C':
#         n = input("Enter name: ")
#         if n in d:
#             print("Marks:", d[n])
#         else:
#             print("Student not found")

#     elif ch == 'D':
#         if not d:
#             print("No data")
#         else:
#             for k, v in d.items():
#                 print(k, ":", v)

#     elif ch == 'E':
#         break

#     else:
#         print("Invalid choice")




#Write a program to Construct a dictionary with word and word length as key-value pair. 
# words =["apple","banana","kiwi","cherry","mango"]
# d={}
# for i in words:
#     n=len(i)
#     d[i]=n
# print(d)



#Write a program such that the program takes a user input string and finds out the number of spaces there in the string. 
# def count_space(s):
#     res=0
#     for i in s:
#         if i==" ":
#             res+=1
#     return res
# print(count_space(input("Give me a string to count spaces: ")))




#Write a program to find out if two lists are common or not. 
# def commenornot(a,b):
#     s1=set(a)
#     s2=set(b)
#     s3=s1&s2
#     if s3:
#         return True
#     return False
# list1 =[1,2,3,4] 
# list2 =[5,6,7,8]
# list3 =[3,4,5,6]
# print(commenornot(list1,list2))
# print(commenornot(list1,list3))




#Write a program to filter out all the unique numbers, meaning repeated numbers should be displayed. 
# l = [1, 2, 3, 2, 4, 5, 1, 6]
# def fill(l):
#     seen = set()
#     dup = set()

#     for x in l:
#         if x in seen:
#             dup.add(x)
#         else:
#             seen.add(x)
#     return dup

# print(*fill(l))




#Print all unique characters and And count of different unit numbers.
# def uniq():
#     u = set(input("Enter string: "))
    
    
#     print("Unique characters:", u)
#     print("Count:", len(u))

# uniq() 