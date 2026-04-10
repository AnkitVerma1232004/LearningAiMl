# wap to create a file name names.txt in write mode and write names in the same file (one per line) open same file in read mode and print the name

# file = open("names.txt", "w")
 
# print("Please enter 5 names:")
# for i in range(5):
#     name = input("Enter name: ")
#     file.write(name + "\n")

# file.close()
# file = open("names.txt", "r")

# print("\nNames stored in file are:")
# for line in file:
#     print(line)

# file.close()




# wap to create a file log.txt in append mode and add a new log entry(like program run successfully) then open the file in read mode and print logs


# file = open("log.txt", "a")
# log = input("Enter a log message: ")
# file.write(log + "\n")

# file.close()
# file = open("log.txt", "r")

# print("\nAll log entries:")
# for line in file:
#     print(line)




# Write a program which has the numbers 5, 10, 15, 20, 25.
# Use list comprehension to create a new list only greater than 15. 
# Print the new list. 

# l=[5,10,15,20,25]
# print(*l)
# l=[x for x in l if x>15]
# print(*l)




# Create a dictionary of three cities and
#  their population, and save it in a JSON file.
#  Named as "cities.json" .

# import json

# Step 1: create dictionary and save
# cities = {
#     "Delhi": 19000000,
#     "Mumbai": 20000000,
#     "Pune": 7000000
# }

# with open("cities.json", "w") as f:
#     json.dump(cities, f, indent=4)

# Step 2: load and print
# with open("cities.json", "r") as f:
#     data = json.load(f)

# for city, pop in data.items():
#     print(city, ":", pop)

# Step 3: take user input and update
# new_city = input("Enter city: ")
# new_pop = int(input("Enter population: "))

# data[new_city] = new_pop

# save updated data
# with open("cities.json", "w") as f:
#     json.dump(data, f, indent=4)

# Write a program to open a file named data.
# txt in read mode. If the file does not exist,
# catch the exception and print "File not found". 

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")