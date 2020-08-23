import re
length = int(input())
voters = input()
def Elections(voters,length):
    a,b=0,0
    if('A' not in voters):
        return 'B'
    if('B' not in voters):
        return 'A'
    isA = voters.index('A') < voters.index('B')
    if isA and voters.index('A')>0:
        a+= voters.index("A")

    isB = voters.rindex('B')>voters.rindex('A')
    if isB and voters.rindex('B')<length:
        b += (length-voters.rindex('B'))-1

    mid = len(''.join(re.findall(r'B(-*?)A',voters)))
    a += len(''.join(re.findall(r'A(-*?)A',voters)))
    b += len(''.join(re.findall(r'B(-?)B',voters)))

    a += mid //2
    b += mid //2

    a += voters.count('A')
    b += voters.count('B')
    if a==b:
        return 'Coalition government'
    elif(a>b):
        return 'A'
    else:
        return 'B'

print(Elections(voters,length))