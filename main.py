from yandex_disk import YandexDisk

if __name__ == '__main__':
    auth_token = 'PASTE_YOUR_AUTH_TOKEN_HERE'
    ya = YandexDisk(auth_token)
    # В качестве upload_path можете указывать директорию, которой не существует.
    # Внутри стоит проверка если директории нет, он создаст ее
    ya.upload_file('test.txt', 'netology-lesson2/test.txt')
