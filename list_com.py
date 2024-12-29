numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With list comprehension
odd_numbers = [n for n in numbers if n % 2]
even_numbers = [n for n in numbers if not n % 2]

print(odd_numbers)
print(even_numbers)

# No list comprehension
odd_numbers = []
even_numbers = []
for number in numbers:
    if number % 2:
        odd_numbers.append(number)
    else:
        even_numbers.append(number)
print(odd_numbers)
print(even_numbers)
