import random 

pole = [["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "чо", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "чо", "*", "*"],
        ["чо", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "чо"],]

poleVrag = [["*", "*", "*", "*", "*", "*"],
        ["*", "*", "чо", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "чо", "*"],
        ["*", "чо", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "чо", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],]

xpVrag = 4
xpYa = 4

bot = False
player = True
while True:
    if player == True:
        a = int(input("Введите строку: "))
        b = int(input("Введите столб: "))
        if poleVrag [a][b] == "чо":
            print("Попал")
            xpVrag -= 1
        else:
            player = False
            print("Не попал")
            bot = True
        
    if bot == True:
        a1 = random.randint(0, 5)
        b1 = random.randint(0, 5)
        if pole[a1][b1] == "чо":
            print ("Меня подбили")
            xpYa -= 1
        else:
            bot = False
            player = True































# while True:
#     a = int(input("Введите страку: "))
#     b = int(input("Введите столб: "))
#     if poleVrag[a][b] == "чо":
#         poleVrag [a][b] = "X!!!"
#         print("Попал")
#         xpVrag -= 1
#     else:
#         print("Не попал")
#         for i in pole:
#             for j in i:
#                 print(j, end= " ")
#             print()
#             a1 = random.randint(0, 5)
#             b1 = random.randint(0, 5)
#             if pole[a1][b1] == "чо":
#                 pole [a1][b1] = "X!!!"
#                 print ("Меня подбили")
#                 xpYa -= 1
# 
#    
#     if xpYa == 0:
#         print("У вас не осталось кораблей")
#         continue
#     if xpVrag == 0:
#         print("Победа")
#         continue