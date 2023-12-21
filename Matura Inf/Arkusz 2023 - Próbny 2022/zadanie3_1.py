N = 13

# SITO[2] czyli 2
# TRUE
# SITO[1] czyli 1
# FALSE
SITO = [False, False]

for i in range(2, N+1):
    SITO.append(True)

for i in range(2, N+1):
    if SITO[i] == True:
        j = i*i
        while j <= N:
            SITO[j] = False
            j = j+i

# for i in range(2, N+1):
#     if SITO[i] == True:
#         j = 2
#         while j < i:
#             if i % j == 0:
#                 SITO[i] = False
#                 break
#             j += 1            

print(SITO)