import re
import string


def get_list_words(text: str) -> list:
    """
    Функция, которая строку превращает в список слов без знаков препинаний
    :param text: строка
    :return: список
    """
    try:
        if not isinstance(text, str) or text == "" or text == " ":
            raise ValueError("Некорректный входной параметр у функции get_list_words.")
        else:
            text = text.translate(str.maketrans('', '', string.punctuation))
            lst = text.lower().split()
            return lst
    except ValueError as val:
        print(val)
    except Exception as ex:
        print(f"Ошибки в функции get_list_words{ex}")


def is_keywords_in_text_use_list(check_words: list, text: str) -> bool:
    """
    Функция, которая проверяет есть ли ключевые слова в тексте, преобразовав его в список.
    :param check_words: Список из ключевых слов
    :param text: строка, которую нужно проверить на наличие ключевых слов
    :return: True (если какое-то из ключевых слов есть в списке) или False (если нет)
    """
    try:
        lst_word = get_list_words(text)
        for check_word in check_words:
            if check_word in lst_word:
                return True
        return False
    except Exception as e:
        print(f"Ошибка в функции is_keywords_in_text_use_list. {e}")


def is_keywords_in_text_use_regexp(check_words: list, text: str) -> bool:
    """
    Функция, которая проверяет есть ли ключевые слова в тексте, использовав re.
    :param check_words: Список из ключевых слов
    :param text: строка, которую нужно проверить на наличие ключевых слов
    :return: True (если какое-то из ключевых слов есть в списке) или False (если нет)
    """
    try:
        for check_word in check_words:
            result = re.search(rf"\s?{check_word}[\.?;:,!]?\s", text.lower())
            if result:
                return True
        return False
    except Exception as e_re:
        print(f"Ошибка в функции is_keywords_in_text_use_regexp. {e_re}")


def format_date(date: str):
    """
    Функция, которая преобразует дату.
    :param date: Дата в виде строки: 2024-12-22, 21:24
    :return: строка в виде: 21:24 22.12.2024
    """
    try:
        date_time = date.split(", ")
        time = date_time[1]
        date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", date_time[0])
        return f"{time} {date}"
    except Exception as e_date:
        print(f"Ошибка в функции format_date{e_date}")
