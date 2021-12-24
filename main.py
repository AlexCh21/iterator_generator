import hashlib
import json

wiki_link = 'wiki.txt'
countries = 'countries.json'
wiki_url = 'https://en.wikipedia.org/wiki/'

class WikiLink:
    def __init__(self, countries_file_path):
        with open(countries_file_path) as file:
            countries_data = json.load(file)
            countries_names = (countries['name']['common'] for countries in countries_data)
            self.countries_names_iter = iter(countries_names)

    def get_links(self, countries_name: str):
        countries_name = countries_name.replace(' ', '_')
        country_wiki_url = f'{wiki_url}{countries_name}'
        return country_wiki_url

    def __iter__(self):
        return self

    def __next__(self):
        countries_name = next(self.countries_names_iter)
        log = f'{countries_name} - {self.get_links(countries_name)}'
        return log

def get_hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

if __name__ == '__main__':
    with open(wiki_link, 'w') as countries_name_file:
        for countries_link in WikiLink(countries):
            countries_name_file.write(f'{countries_link}\n')
    for hash_str in get_hash(wiki_link):
        print(hash_str)