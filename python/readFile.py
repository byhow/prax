filename = input()
# filename = filename[8:]

with open(filename, 'r') as f:
    content = f.readlines()

contents = [ i.strip().split() for i in content]

# print(contents)

occur = dict()

for i in contents:
    if i[0] not in occur:
        occur[i[0]] = 1
    else:
        occur[i[0]] += 1

for k, v in occur.items():
    print(k + " " + str(v))