number_of_people = 0
number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
many_user = None


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


def decrease_book(books):
    global number_of_book
    number_of_book = number_of_book - books
    print(f'남은 책의 수: {number_of_book}')


# 4. 3번까지해서 만든 result1 리스트의 요소인 각 딕셔너리를 하나씩 받아 몇권의 책을 대여했는지 진행하는 함수
def rental_book(info):
    decrease_book(info['books'])
    print(f'{info["name"]}님이 {info["books"]}권의 책을 대여했습니다.')

# 1. 실습 4에서 작성한 코드를 활용하여 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트 생성
many_user = list(map(create_user, name, age, address))


# 람다로 바뀔 함수
# 2. 고객 정보 중 이름과 나이만 추출하여 이름은 그대로 사용하고 나이를 활용해 빌린 책수를 계산한 새로운 딕셔너리를 만드는 함수
def lambda_maker(user_info):
    result = {
        'name': user_info['name'],
        'books': user_info['age'] // 10
    }
    return result


# 3. many_user를 반복하면서 뽑아낸 각각의 유저 정보를 취합하여, 이름과 빌린 책의 수만 남긴 새로운 정보의 딕셔너리를 만들어서 새로운 큰 리스트를 만드는 과정
result1 = list(map(lambda_maker, many_user))
# result1 = list(map(lambda user_info: {'name': user_info['name'],'books': user_info['age'] // 10}, many_user))
# print(result1)
"""
result1의 모습
[
    {'name': '김시습', 'books': 2}, 
    {'name': '허균', 'books': 1}, 
    {'name': '남영로', 'books': 5}, 
    {'name': '임제', 'books': 3}, 
    {'name': '박지원', 'books': 6}
]
"""

# 5. 마지막 렌탈 진행
list(map(rental_book, result1))
