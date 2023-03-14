str_list = ['abcdefg', 'kkzz', 'aba', '3528', '6006', '3214', 'zrkz']

count = 0
for s in str_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(count)