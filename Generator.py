lst = [1,4,7,9]
gen = (x**2 for x in lst)

for item in gen:
    print(item)