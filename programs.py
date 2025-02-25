# Program 1: Find the sum of all elements in a list
l = [1, 2, 3, 4, 5]
sum_l = sum(l)
print("Sum:", sum_l)

# Program 2: Find the largest element in a list
l = [12, 13, 14, 15, 16]
largest = max(l)
print("Largest:", largest)

# Program 3: Find the smallest element in a list
l = [12, 13, 14, 15, 16]
smallest = min(l)
print("Smallest:", smallest)

# Program 4: Find the average of all elements in a list
l = [12, 13, 14, 15, 16]
avg = sum(l) / len(l)
print("Average:", avg)

# Program 5: Print all the keys of a dictionary
d = {"1": "siva", "2": "ram", "3": "harish"}
print("Keys:", d.keys())

# Program 6: Print all the values of a dictionary
d = {"1": "siva", "2": "ram", "3": "harish"}
print("Values:", d.values())

# Program 7: Print the multiplication table of a given number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Program 8: Print the Fibonacci series up to a given number
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Program 9: Find the factorial of a given number
n = int(input("\nEnter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")

# Program 10: Find the sum of all natural numbers from 1 to n
n = int(input("Enter a number: "))
print(sum(range(1, n + 1)))

# Program 11: Find the median of a list
import statistics
l = [5, 3, 8, 9, 4, 1, 7]
print("Median:", statistics.median(l))

# Program 12: Sort a list in ascending order
l = [1, 5, 7, 89, 60, 4]
print("Sorted List:", sorted(l))

# Program 13: Reverse a list
l = [1, 2, 3, 4, 5, 6]
print("Reversed List:", l[::-1])

# Program 14: Find the second largest element in a list
l = [10, 20, 30, 40, 50]
print("Second Largest:", sorted(set(l))[-2])

# Program 15: Merge two lists and sort them
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
merged_list = sorted(l1 + l2)
print("Merged List:", merged_list)

# Program 16: Check if a list is empty
l = []
print("List is empty" if not l else "List is not empty")

# Program 17: Remove duplicates from a list
l = [1, 2, 3, 1, 2, 4]
print("Unique List:", list(set(l)))

# Program 18: Find the index of an element in a list
l = [10, 20, 30, 40, 50]
element = 30
print("Index of element:", l.index(element))

# Program 19: Insert an element at a specific position in a list
l = [10, 20, 40, 50]
l.insert(2, 30)
print("List after insertion:", l)

# Program 20: Remove all elements except the first and last
l = [1, 2, 3, 4, 5]
print([l[0], l[-1]])

# Program 21: Find the product of all elements in a list
l = [1, 2, 3, 4]
product = 1
for num in l:
    product *= num
print("Product:", product)

# Program 22: Find the maximum and minimum elements in a list
l = [1, 2, 3, 4, 95, 30]
print("Max:", max(l), "Min:", min(l))

# Program 23: Find the second smallest element in a list
l = [10, 1, 5, 9, 4, 11]
print("Second Smallest:", sorted(set(l))[1])

# Program 24: Remove elements divisible by a given number
l = [10, 20, 30, 40, 50, 60]
divisor = 10
print("Filtered List:", [i for i in l if i % divisor != 0])

# Program 25: Reverse a string
s = "hello"
print("Reversed String:", s[::-1])

# Program 26: Swap two numbers
a, b = 5, 10
a, b = b, a
print("Swapped:", a, b)

# Program 27: Check if a number is prime
n = int(input("Enter a number: "))
is_prime = all(n % i != 0 for i in range(2, n))
print(f"{n} is prime" if is_prime else f"{n} is not prime")

# Program 28: Find the GCD of two numbers
import math
print("GCD:", math.gcd(12, 18))

# Program 29: Find the LCM of two numbers
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
print("LCM:", lcm(12, 18))

# Program 30: Count occurrences of an element in a list
l = [1, 2, 3, 2, 4, 5, 2]
print("Occurrences of 2:", l.count(2))
