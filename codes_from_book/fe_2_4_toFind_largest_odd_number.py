print('You will be asked to enter ten integers, and I will find the largest odd number among them.')

num = 10
ans = 0
while num > 0:
    yourinput = int(input("Enter one integer: "))
    if ((yourinput % 2) == 1) & (yourinput > ans):
        ans = yourinput
    num -= 1
if ans == 0:
    print('None of your enter is odd number!')
else:
    print('The largest odd number among them is ' + str(ans) + '.' )

