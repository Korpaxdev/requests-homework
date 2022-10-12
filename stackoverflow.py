from datetime import datetime, timedelta

from requests import get


class StackOverflow:
    BASE_URL = 'https://api.stackexchange.com/2.3'
    BASE_PARAMS = dict(order='desc', sort='activity', site='stackoverflow')

    @staticmethod
    def __get_timestamp_from_date(date_: str):
        base_hours = timedelta(hours=3)
        date_ = datetime.strptime(date_, "%d-%m-%Y") + base_hours
        return int(date_.timestamp())

    def get_questions(self, from_date: str = None, to_date: str = None, tag_name: str = 'python'):
        from_date = self.__get_timestamp_from_date(from_date) if from_date else from_date
        to_date = self.__get_timestamp_from_date(to_date) if to_date else to_date
        url = self.BASE_URL + "/questions"
        params = dict(fromdate=from_date, todate=to_date, tagged=tag_name)
        params.update(self.BASE_PARAMS)
        response = get(url, params=params)
        response.raise_for_status()
        return response.json()
