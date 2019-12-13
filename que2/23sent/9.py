string = input()
n = int(input())

rules = []
for i in range(n):
	rules.append(input().split())
    
rules.reverse()
print(rules)
for i in rules:
    string = string.replace(i[1],i[0])

print(string)