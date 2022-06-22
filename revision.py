# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:44:44 2022

@author: user
"""

mahsulotlar=['olma','macbook','iphone13pro','olcha','pirog','quloqchin','sumka','kitob',
              'bolg\'a','mix']
savat=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-kerakli mahsulotni qo'shing:"))

bor_mahsulotlar=[]
mavjud_emas=[]

for mahsulot in savat:
    if mahsulot in mahsulotlar :
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do\'konimizda quydagi mahsulotlar yo\'q::: ")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("siz soragan barcha mahsulotlar bor:")        
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")        