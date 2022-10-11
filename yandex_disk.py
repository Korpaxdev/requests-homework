from os import path

from requests import get, put


class YandexDisk:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str):
        self.__token = token
        self.__headers = {"Authorization": self.__token}

    def __check_folder(self, upload_file: str) -> bool:
        params = {"path": upload_file}
        response = get(self.BASE_URL, params=params, headers=self.__headers)
        return response.status_code == 200

    def __create_folder(self, upload_path: str) -> None:
        params = {"path": upload_path}
        response = put(self.BASE_URL, params=params, headers=self.__headers)
        response.raise_for_status()

    def __get_href_for_upload(self, upload_path: str) -> str | None:
        upload_folders = path.split(upload_path)[0]
        if upload_folders and not self.__check_folder(upload_folders):
            self.__create_folder(upload_folders)
        params = {"path": upload_path, "overwrite": "true"}
        response = get(f"{self.BASE_URL}/upload", headers=self.__headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('href', None)

    def upload_file(self, file: str, upload_path: str) -> None:
        href = self.__get_href_for_upload(upload_path)
        if not href:
            raise ValueError('href is empty')
        response = put(href, data=open(file, 'rb'))
        response.raise_for_status()
        print("Файл успешно создан")
