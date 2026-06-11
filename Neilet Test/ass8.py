def find_even_odd(lst):
    even = []
    odd = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

numbers = [1,2,3,4,5,6,7,8,9,10]

even, odd = find_even_odd(numbers)

print("Even:", even)
print("Odd:", odd)
