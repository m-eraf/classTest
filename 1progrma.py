from itertools import combinations
a = int (input());
char = input().split()
b= int(input())
count = 0;
total = 0;
for i in combinations(char,b):
    count += 'a' in i
    total += 1
    
print(count/total)