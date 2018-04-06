# -*- coding: utf-8 -*-
string_of_num = "1.23,2.4,3.123"
s_num = ''
sum = 0
for c in string_of_num:
    if c == ',':
        num = float(s_num)
        sum += num
        s_num = ''
    else:
        s_num += c
num = float(s_num)
sum += num
print('sum is', sum)
