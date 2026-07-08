from functools import reduce
# part 1
# step 1
numbers = [3, 7, 10, 15]
res = map(lambda num: num + 10, numbers)
print(list(res))
# step 2
prices = [100, 50, 200, 80]
res = map(lambda num: num * 1.17, prices)
print(list(res))
# step 3
words = ["cat", "elephant", "dog", "python"]
res = map(lambda word: len(word), words)
print(list(res))
# step 4
names = ["dan", "maya", "ron", "lea"]
res = map(lambda name: name.upper(), names)
print(list(res))
# step 5
users = ["Noa", "Adam", "Lior", "Tamar"]
res = map(lambda user: f"Hello {user}", users)
print(list(res))
# step 6
meters = [1.5, 2, 0.75, 3.2]
res = map(lambda meter: meter * 100, meters)
print(list(res))
# step 7
grades = [95, 40, 67, 88, 52]
res = map(lambda grade: "pass" if grade >= 60 else "fail", grades)
print(list(res))
# step 8
products = [
    {"name": "Bread", "price": 8},
    {"name": "Milk", "price": 6},
    {"name": "Eggs", "price": 15}
]
res = map(lambda product: f'{product["name"]} costs {product["price"]}' , products)
print(list(res))
# step 9
players = [
    {"name": "Dana", "score": 70},
    {"name": "Yoni", "score": 85},
    {"name": "Rami", "score": 40}
]
res = map(lambda player: {"name": player["name"], "score": player["score"] + 5} , players)
print(list(res))
# step 10
orders = [
    {"id": 1, "item": "Book", "amount": 3, "price": 40},
    {"id": 2, "item": "Pen", "amount": 10, "price": 5},
    {"id": 3, "item": "Bag", "amount": 1, "price": 120}
]
res = map(lambda order: f'order {order["id"]}: {order["item"]} total is {order["amount"] * order["price"]}', orders)
print(list(res))
# part 2
# step 1
numbers = [4, 7, 10, 13, 18, 21]
res = filter(lambda num: True if num % 2 == 0 else False, numbers)
print(list(res))
# step 2
grades = [100, 55, 70, 40, 88, 59]
res = filter(lambda grade: True if grade >= 60  else False, grades)
print(list(res))
# step 3
words = ["dog", "elephant", "cat", "computer", "sun"]
res = filter(lambda word: True if len(word) <= 3  else False, words)
print(list(res))
# step 4
names = ["Adam", "Dana", "Amit", "Noa", "Alon"]
res = filter(lambda name: True if name[0] == "A"  else False, names)
print(list(res))
# step 5
numbers = [-5, 3, 0, 12, -2, 8]
res = filter(lambda num: True if num > 0  else False, numbers)
print(list(res))
# step 6
products = [
    {"name": "Book", "price": 40},
    {"name": "Bag", "price": 120},
    {"name": "Pen", "price": 5},
    {"name": "Shirt", "price": 60}
]
res = filter(lambda product: True if product["price"] < 60  else False, products)
print(list(res))
# step 7
users = [
    {"name": "Dana", "active": True},
    {"name": "Ron", "active": False},
    {"name": "Maya", "active": True},
    {"name": "Gil", "active": False}
]
res = filter(lambda user: True if user["active"] == True  else False, users)
print(list(res))
# step 8
passwords = ["abc", "hello123", "Python2026", "pass", "GoodPass99"]
res = filter(lambda password: True if len(password) >= 8  else False, passwords)
print(list(res))
# step 9
tasks = [
    {"title": "Clean room", "done": True, "priority": 2},
    {"title": "Study Python", "done": False, "priority": 1},
    {"title": "Play game", "done": False, "priority": 5},
    {"title": "Send email", "done": True, "priority": 1}
]
res = filter(lambda task: True if task["done"] == False and task["priority"] <= 3 else False, tasks)
print(list(res))
# step 10
students = [
    {"name": "Noa", "grade": 90, "attendance": 95},
    {"name": "Dan", "grade": 55, "attendance": 100},
    {"name": "Rina", "grade": 80, "attendance": 70},
    {"name": "Eli", "grade": 75, "attendance": 85}
]
res = filter(lambda student: True if student["grade"] >= 70 and student["attendance"] >= 80 else False, students)
print(list(res))
# Part 4
# 1. Basic idea
# reduce works in a way that it goes through everything and knows how to perform a cyclic operation and return the final output.
# 2. Step-by-step thinking
# What will happen first is multiplying 2 times three, which is 6, and then 6 times 4, the final result is 24.
# 3. Compare tools
# I would use map if I wanted to perform an operation on each part of the list and save it as a list.
# If I wanted to understand something related to the entire list and get one value at the end, I would use reduce.
# 4. Function parameters
# The process of reduce is the addition of index 0 and then 1 after it is initially X AND Y. After that, it takes the result and places it in X and takes index 2 and places it in y. It needs x and y to run in an orderly manner.
# 5. Readability
# If using list traversal requires more than one condition, it would be easier to do a for loop.
# part 5
# 1. Sum all numbers
numbers = [5, 10, 20, 15]
res = reduce(lambda num1, num2: num1 + num2, numbers)
print(res)
# 2. Multiply all numbers
numbers = [2, 3, 4, 5]
res = reduce(lambda num1, num2: num1 * num2, numbers)
print(res)
# 3. Find the longest word
words = ["cat", "elephant", "dog", "computer"]
res = reduce(lambda word1, word2: word1 if len(word1) >= len(word2) else word2, words)
print(res)
# 4. Join words into one sentence
words = ["Python", "is", "very", "useful"]
res = reduce(lambda word1, word2: word1 + " " + word2, words)
print(res)
