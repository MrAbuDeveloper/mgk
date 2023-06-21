####1 vazifa

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# less = []
# more = []
#
# for element in a:
#     if element <= 5:
#         less.append(element)
#     else:
#         more.append(element)
# print(less)
# print(more)
#### 2 vazifa
# user_info = input('Ismingizni familiyangizni va yoshingizni kiriting: ')
# lst = user_info.split(' ')
# print(lst)

# name = input('Ismingizni kiriting: ')
# lastname = input('Familiyangizni kiriting: ')
# age = input('Yoshingizni kiriting: ')
# lst = [name, lastname, age]
# print(lst)

# user_text = input('Raqamlar kiriting: ')
# lst = user_text.split(', ')
# tpl = tuple(lst)
# print(lst)
# print(tpl)

# res = 0
# res = res + 1
# res = res + 5
# res = res + 3
# print(res)

# res = 0
# res += 1
# res += 5
# print(res)


# user_exam = input('Qo\'shish uchun misol kiriting: ')
# lst = user_exam.split(' + ')
# result = 0
# for elem in lst:
#     result += int(elem)
# print(result)


#  range(start, stop, step)

# for i in range(1, 4):
#     print(i)

# nums = []
# for i in range(1, 21):
#     nums.append(i)
# print(nums)

# for item in range(1, 11, 4):
#     print(item)

# for i in range(20, -1, -1):
#     print(i)

# squares = []
### 1-10

# for i in range(1, 11):
#     squares.append(i ** 2)
# print(squares)

# nums = [i for i in range(1, 11)] ## list generatori
# for i in range(1, 11):
#     nums.append(i)
# print(nums)

# squares = [num ** 2 for num in range(1, 11)]
# print(squares)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# less = [num for num in a if num <= 5]
# more = [num for num in a if num > 5]
# print(less)
# print(more)

### list(start stop step)

# lst = [1, 's', 2, 3, 'b', 'a', 'l', 5, 2]
# print(lst[0:3])
# print(lst[:3])
# print(lst[3:])
# print(lst[:])
# print(lst[::2])
# print(lst[2:7:2])
# print(lst[::-1])

# lst = [1, 's', 2, 3, 'b', 'a', 'l', 5, 2, '2']
#
# list_string = [item for item in lst if type(item) is str]
# list_int = [item for item in lst if type(item) is int]
# lst = [1, 's', 2, 3, 'b', 'a', 'l', 5, 2, '2']
# copy1_lst = [i for i in lst]
# print(lst)
# print(copy1_lst)
# print(id(lst))
# print(id(copy1_lst))

# copy2_lst = lst[:]
# print(id(lst))
# print(id(copy2_lst))

# copy3_lst = lst.copy()
# print(id(lst))
# print(id(copy3_lst))
# uncopy = lst
# print(id(lst))
# print(id(uncopy))

####### while True:
#     print(1)

# iterator = 0
# while iterator < 5:
#     print(iterator)
#     iterator += 1

while True:

    user_name = input('Ismizni yozing: ')
    if user_name.lower() == 'stop':
        break
    print(f"Salom, {user_name.capitalize()}")



