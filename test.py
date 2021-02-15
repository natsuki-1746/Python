#Comment

# print("Hello World!")
# print("派手派手だぜ！")
# print("Carat")


#演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

#変数
# dust = 'l_size'
# housedust = 0
# housedust_times = 5.5

# print(dust)

#条件分岐と関係演算子
#if else elif
# ==, !=, <, >, >=, <=
# if housedust > 6:
#     print("ooi")
# elif housedust == 0:
#     print("nai!")
# else:
#     print("sukunai")

#関数
# def ko_funbaru(arg):
#     ko_status = arg
#
#     if(ko_status < 10):
#         return "mada daijyoubu"
#     else:
#         return "yabai"

# print(ko_funbaru(5))

#list
# ko_list = ["ko_small", "ko_midium", "ko_large"]
# print(ko_list[0])

#for文
# for index in range(11):
    # print(index)
    # print(ko_funbaru(index))

# for item in ko_list:
#     print(item)


#with
#open()
# with open("./ko.txt", "r") as file:
#     print(file)

#class
# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name
#     def message(self):
#         return "この投稿は" + self.user_name + "さんが" + self.date + "に投稿しました"
#
# date_a = "2020-01-01"
# user_name_a = "Taro"
# card_a = Card(date_a, user_name_a)
#
# date_b = "2021-2-15"
# user_name_b = "Kanako"
# card_b = Card(date_b, user_name_b)
#
# print(card_b.message())


#import
# import math
# print(math.pi)

#外部モジュールの例↓
#NumPy
#Flask
#Django

import numpy
numpy_list =[3, 1, 5, 10, 2093, 304, 123]
print(numpy.sum(numpy_list))
