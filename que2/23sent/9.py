string = input()
n = int(input())

rules = []
for i in range(n):
	rules.append(input().split())

for i in rules:
	string.replace(i[1],i[0])

print(string)
