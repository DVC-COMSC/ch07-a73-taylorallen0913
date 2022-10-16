

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))

index_to_insert = len(numbers)

for n in range(5):
    if numbers[n] > insval:
        index_to_insert = n
        break

if len(numbers) == index_to_insert:
    numbers.append(insval)
else:
    numbers.insert(index_to_insert, insval)
