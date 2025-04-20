import hashlib
import os

# Функция для хэширования пароля
def hash_password(password: str) -> str:
    salt = os.urandom(32)  # Генерация случайной соли
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)  # Хэшируем пароль
    return salt + pwd_hash  # Возвращаем соль + хэш для хранения

# Функция для проверки пароля
def verify_password(stored_password: str, password: str) -> bool:
    salt = stored_password[:32]  # Извлекаем соль из хранилища
    stored_hash = stored_password[32:]  # Извлекаем хэш из хранилища
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)  # Хэшируем введенный пароль
    return stored_hash == pwd_hash  # Проверяем, совпадает ли хэш
