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
res = map(lambda player: {player["name"], player["score"] + 5} , players)
print(list(res))
# step 10
orders = [
    {"id": 1, "item": "Book", "amount": 3, "price": 40},
    {"id": 2, "item": "Pen", "amount": 10, "price": 5},
    {"id": 3, "item": "Bag", "amount": 1, "price": 120}
]
res = map(lambda order: f'order {order["id"]}: {order["item"]} total is {order["amount"] * order["price"]}', orders)
print(list(res))
