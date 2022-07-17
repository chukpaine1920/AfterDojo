for i in range(1, 350, 4):
    print(i)

for i in range(500, 120, -10):
    print(i)

my_list = ['yellow', 'orange', 'blue', 'green', 'purple']
for i in range(0, len(my_list)):
    print(my_list)

for count in range(0,5):
    print("looping -", count)

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


for val in "string":
    if val == "i":
        break
    print(val)

for val in "string":
    if val == "i":
        continue
    print(val)

    y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1





