count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement and condition stopping before 5. Fixed by adding a colon and changing '< 5' to '<= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate string with int using '+'. Fixed by converting total to string using str() or using an f-string.
print("Sum of 1 to 5 is: " + str(total))