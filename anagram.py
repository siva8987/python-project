# given two strings are anagrams or not
s1='listen'
s2='silent'
print(''.join(reversed(s2)))
print(sorted(s2))
print(''.join(sorted(s2)))

if ''.join(sorted(s1))==''.join(sorted(s2)):
    print('s1 and s2 anagram')
else:
    print('not a anagram')
