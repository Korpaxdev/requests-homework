from requests import get
from yandex_disk import YandexDisk
from stackoverflow import StackOverflow


def get_most_intelligence_char(char_list):
    response = get('https://akabab.github.io/superhero-api/api/all.json')
    response.raise_for_status()
    char_list = [c for c in response.json() if c['name'] in char_list]
    char_list.sort(key=lambda c: c['powerstats']['intelligence'], reverse=True)
    return char_list[0]


if __name__ == '__main__':
    # Lesson_1
    chars = ['Hulk', 'Captain America', 'Thanos']
    most_intelligence = get_most_intelligence_char(chars)
    print(f"Самый умный из персонажей: {', '.join(chars)}, это - {most_intelligence['name']}")
    # Lesson_2
    auth_token = 'PASTE_YOUR_AUTH_TOKEN_HERE'
    ya = YandexDisk(auth_token)
    # В качестве upload_path можете указывать директорию, которой не существует.
    # Внутри стоит проверка если директории нет, он создаст ее
    ya.upload_file('test.txt', 'netology-lesson2/test.txt')
    # Lesson_2
    stackoverflow = StackOverflow()
    # Формат дат %d-%m-%Y
    questions = stackoverflow.get_questions('10-10-2022')
    print(questions)
