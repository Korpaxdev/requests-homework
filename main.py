from requests import get


def get_most_intelligence_char(char_list):
    response = get('https://akabab.github.io/superhero-api/api/all.json')
    response.raise_for_status()
    char_list = [c for c in response.json() if c['name'] in char_list]
    char_list.sort(key=lambda c: c['powerstats']['intelligence'], reverse=True)
    return char_list[0]


if __name__ == '__main__':
    chars = ['Hulk', 'Captain America', 'Thanos']
    most_intelligence = get_most_intelligence_char(chars)
    print(f"Самый умный из персонажей: {', '.join(chars)}, это - {most_intelligence['name']}")
