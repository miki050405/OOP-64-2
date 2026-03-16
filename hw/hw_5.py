print('Домашнее задание №5')

print('Задание №1')
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print('У вас нет доступа')
    return wrapper

@is_admin
def delete_video(user):
    print('Видео удалено')

admin = User("Malika", "admin")
delete_video(admin)
user = User("Bermet", "user")
delete_video(user)

import time

print('Задание №2')

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {end - start:.1f} сек.")
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print('Видео загружено')

download_video()