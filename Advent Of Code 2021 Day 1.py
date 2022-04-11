def sumOfThree(l, s):
    return(int(l[s])+int(l[s+1])+int(l[s+2]))
with open('aocp12021.txt', 'r') as f:
    input = []
    for line in f:
        strip_lines = line.strip()
        inputi = strip_lines.split()
        m = input.append(inputi[0])
a,b,lb = 0,0,1
for i in range(len(input)):
    if int(input[i]) > int(input[i-1]):
        a += 1
    try:
        if lb == 1:
            if sumOfThree(input, i) < sumOfThree(input, i+1):
                b += 1
    except IndexError:
        lb = 0
print('BEEP BOOP BOP...\n'+'The answer to part 1 is...\n'+str(a)+'!')
print('BOOP BOP BEEP...\n'+'The answer to part 2 is...\n'+str(b)+'!')