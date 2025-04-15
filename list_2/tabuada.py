count1 = 1
count2 = 1

while count1 <= 10:
    while count2 <= 10:
        print(f'{count1} * {count2} = {count1 * count2}')
        count2 += 1
    count2 = 1
    print('')
    count1 += 1