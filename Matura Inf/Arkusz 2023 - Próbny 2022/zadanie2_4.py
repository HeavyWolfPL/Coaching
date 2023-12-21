with open("Dane/pary.txt", mode="r") as file:
    dane = file.readlines()

pary = []
N = 100000

def rysuj(x, limit, orig_x):
    if x == limit:
        pary.append([orig_x, limit])
        return
    elif x > limit:
        return
    
    if 2*x <= N:
        rysuj(2*x, limit, orig_x)
    if 2*x+1 <= N:
        rysuj(2*x+1, limit, orig_x)


for para in dane:
    para = para.split(" ")
    para[0] = int(para[0])
    para[1] = int(para[1])
    # 1, 245, 1
    rysuj(para[0], para[1], para[0])

print(len(pary), pary)