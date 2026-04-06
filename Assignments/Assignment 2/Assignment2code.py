#calculating final taxrate
# s=int(input("salary: "))
# if s <30000:
#     print("5% taxrate")
# elif s>70000:
#     print("25% taxrate")
# else:
#     print("15% taxrate")
# Write a function that takes two integers and and prints all even numbers between them (inclusive).
# def numbers(a,b):
#     if not a%2==0:
#         a+=1
    
#     print(*range(a,b+1,2))
# numbers(3,10)
# Write a function that prints the of a number's digit
# def digitWise(n):
#     s=str(n)
#     for i in s:
#         print(i,end=" ")
#     print()
# digitWise(312)
# digitWise(5438)
# Write a function to return the count the number of digits in a number n.
# def countDigits(n):
#     s=str(n)
#     return len(s)


# def countDigits(n):
#     s = str(abs(n))  # Use abs() to remove the sign
#     return len(s)
# print(countDigits(1234))
# def sumofdigit(n):
#     sum=0
#     while n:
#         sum+=n%10
#         n//=10
#     print(sum)
# sumofdigit(55468)
# def writeaprogramtoprintallthenumberswhicharedivisibleby5and8():
#     for i in range(1,101):
#         if i%15==0:
#             print(i,end="\t")
# writeaprogramtoprintallthenumberswhicharedivisibleby5and8()
# def calculator(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         return a / b
#     else:
#         return "Invalid Operation"

# Calling calculator function
# print(calculator(10, 5, '+'))
# print(calculator(10, 5, '-'))
# print(calculator(10, 5, '*'))
# print(calculator(10, 5, '/'))
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True



# Calling is_prime function
# print(is_prime(7))
# print(is_prime(10))
# def guess_game():
#     sec = 7
    
#     while True:
#         g = int(input("Guess the number: "))
        
#         if g > sec:
#             print("Too high")
#         elif g < sec:
#             print("Too low")
#         else:
#             print("Correct!")
#             break

# guess_game()