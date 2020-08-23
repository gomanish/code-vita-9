herbivorous, carnivorous, aquatic = map(int, input().split())
max_herbivorous, max_carnivorous, max_aquatic = map(int, input().split())

M_herbivorous, N_herbivorous = map(int, input().split())
M_carnivorous, N_carnivorous = map(int, input().split())
M_aquatic, N_aquatic = map(int, input().split())

total_area = int(input())

temp = min(herbivorous, carnivorous, aquatic)
if temp == herbivorous:
    a1 = max_herbivorous * temp
    x = max_herbivorous
elif temp == carnivorous:
    a1 = max_carnivorous * temp
    x = max_carnivorous
else:
    a1 = max_aquatic * temp
    x = max_aquatic

temp = max(herbivorous, carnivorous, aquatic)
if temp == herbivorous:
    a2 = M_herbivorous * N_herbivorous *herbivorous
    y = M_herbivorous * N_herbivorous
elif temp == carnivorous:
    a2 = M_carnivorous * N_carnivorous * carnivorous
    y = M_carnivorous * N_carnivorous
else:
    a2 = M_aquatic*N_aquatic * aquatic
    y = M_aquatic*N_aquatic


z = total_area - (x + y)
arr = []
arr.append(herbivorous)
arr.append(carnivorous)
arr.append(aquatic)
sor_arr = sorted(arr)
a3 = z * sor_arr[1]


print(a1 + a2 + a3)