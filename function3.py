def find_largest_number(numbers):
# check if list is empty
    if not numbers:
return None


# Assume the largest number is first number
largest =  number[0]
for num in numbers:
    if num > largest:
        largest =  num

return largest