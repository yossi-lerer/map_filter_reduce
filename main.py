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
