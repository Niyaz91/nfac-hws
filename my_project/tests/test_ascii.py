import pytest
from io import StringIO
from unittest.mock import patch
from my_project.ascii import process_text, build_banner  # Заменить на имя модуля


# Тестируем функцию process_text
def test_process_text():
    # Пример текста с двойными переводами строки
    text = "Hello\n\nWorld"
    expected = "Hello\nWorld"  # После обработки, ожидаем текст без лишних переносов
    result = process_text(text)
    assert result == expected


# Тестируем функцию build_banner
def test_build_banner():
    # Пример данных баннера для символов 'A' и 'B'
    banner_data = [
        ["A_line1", "A_line2"],  # ASCII арт для 'A'
        ["B_line1", "B_line2"]  # ASCII арт для 'B'
    ]
    text = "AB"  # Ожидаем, что будет собран баннер для 'A' и 'B'

    expected = "A_line1A_line2\nB_line1B_line2"
    result = build_banner(banner_data, text)

    assert result == expected