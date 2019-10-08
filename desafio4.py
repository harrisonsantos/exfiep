# take second element for sort
def takeSecond(elem):
    return elem[1]

n = input("Numero de clientes: ")
n = int(n)

if n < 1:
    exit()

clients = []

for i in range(n):
    inp = input()
    try:
        slipted = inp.split(" ")
        clients.append([int(slipted[0]), int(slipted[1])])
    except Exception as identifier:
        clients.append([i,0])

clients.sort(key=takeSecond)
print(clients)

total_time = 0
times = []
for i in range(len(clients)):
    if i == 0:
        total_time = clients[i][1]
        times.append(total_time)
    else: 
        total_time = 0
        total_time = sum(times)
        total_time += clients[i][1] - 2
        times.append(total_time)

print(sum(times)/3)