for i in range(5):
    pass
# continue skips current iteration.
print("Output of for loop")
for i in range(5):
 if i == 2:
    continue
 print(i)
# break exits loop immediately.
print("Output of for loop with break")
for i in range(5):
    if i == 3:
        break
    print(i)
# Loop else
print("Output of for loop with else")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")