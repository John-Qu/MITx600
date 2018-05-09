import math
digits = ""
ans = ""
for i in range(1, 10):
    p = math.log10(1 + 1.0/i)
    digits += str(i) + "     "
    ans += str(round(p*100, 1)) + "% "
print(digits)
print(ans)
