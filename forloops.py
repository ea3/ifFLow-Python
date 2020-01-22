for i in range(1, 20):
    print(f"i is now {i}")

number = "9,223,372,036,854,775,807"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]
        #print(number[i], end='')
newNumber = int(cleanedNumber)
print(f"The number is {newNumber}")

for i in range(0, 100, 5):
    print(i)

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
    print('')

