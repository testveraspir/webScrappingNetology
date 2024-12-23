import requests
import bs4
from fake_headers import Headers
from extra_function import is_keywords_in_text_use_list, is_keywords_in_text_use_regexp, format_date


def print_data_about_articles(key_words: list,
                              url_articles: str,
                              base_url: str = "https://habr.com",
                              func=is_keywords_in_text_use_list) -> None:
    """
    Функция, которая печатает информацию по найденным статьям, содержащих искомые ключевые слова.
    :param key_words: Список из ключевых слов
    :param url_articles: url на обзор статей
    :param base_url: основной адрес сайта
    :param func: название функции, по которой идёт поиск ключевых слов в тексте
    """
    try:
        headers = Headers(browser="chrome", os="mac").generate()
        response = requests.get(url_articles, headers=headers)
        soup = bs4.BeautifulSoup(response.text, features="lxml")
        articles_list = soup.find("div", attrs={"data-test-id": "articles-list"})
        articles = articles_list.find_all("article", attrs={"data-test-id": "articles-list-item"})
        name_data, name_header, name_link = ("Дата", "Заголовок", "Ссылка")
        print(f"{name_data:<20} {name_header:<100} {name_link}")

        for article in articles:
            data = article.find("time")["title"]
            title = article.find("h2", attrs={"data-test-id": "articleTitle"}).span.text
            link_relative = article.select_one("a.tm-title__link")["href"]
            link = base_url + link_relative
            format_data = format_date(data)

            # получение текста в обзоре статьи
            preview_div = article.select_one("div.article-formatted-body")
            preview = preview_div.get_text()

            # получение текста из статьи
            article_response = requests.get(link)
            article_soup = bs4.BeautifulSoup(article_response.text, features="lxml")
            text_div = article_soup.select_one("div.article-formatted-body")
            text = text_div.get_text()

            if func(key_words, preview) or func(key_words, text):
                print(f"{format_data:<20} {title:<100} {link}")

    except Exception as ex_get_data:
        print(f"Ошибка при получении информации из статьи. {ex_get_data}")


if __name__ == '__main__':
    KEYWORDS = ["дизайн", "фото", "web", "python"]
    address_site = "https://habr.com/ru/articles"

    print("Вариант 1. Использование функции is_keywords_in_text_use_list")
    print_data_about_articles(key_words=KEYWORDS,
                              url_articles=address_site)
    print()

    print("Вариант 2. Использование функции is_keywords_in_text_use_regexp")
    print_data_about_articles(key_words=KEYWORDS,
                              url_articles=address_site,
                              func=is_keywords_in_text_use_regexp)
