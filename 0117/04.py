number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people = number_of_people + 1
    # number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {
        'name': name, 
        'age': age, 
        'address': address
    }
    print(f'{name}님 반갑습니다.')
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 1. zip으로 푸는 방법
# 1.3 일단 zip으로 만든 결과와 함께 쓰기 위해 create_user 함수의 구조를 변경
# def create_user(user_info):
#     name, age, address = user_info
#     increase_user()
#     user_info = {
#         'name': name, 
#         'age': age, 
#         'address': address
#     }
#     print(f'{name}님 반갑습니다.')
#     return user_info

# # 1.1 zip 으로 묶기
# zip_user = list(zip(name, age, address))
# print(zip_user)

# # 1.2 map 함수를 사용해서 zip으로 묶인 사용자들에게
# # 각각 create_user 함수를 적용
# result = list(map(create_user, zip_user))
# print(result)


# 2. map 그 자체로 하는 방법
def create_user(name, age, address):
    increase_user()
    user_info = {
        'name': name, 
        'age': age, 
        'address': address
    }
    print(f'{name}님 반갑습니다.')
    return user_info

result = list(map(create_user, name, age, address))
print(result)
