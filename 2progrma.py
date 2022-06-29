from itertools import combinations;
l = int(input().strip());
s = input().strip().split();
k = int(input().strip());

good = 0;
all=0;
for i in combinations(s,k):
	all+=1;
	if 'a' in i:
		good=good+1;
		
print(good/all);