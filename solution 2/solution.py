import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import unquote

# Список всех букв русского алфавита
#letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']

letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
letters.insert(6, 'Ё')


with open('beasts.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Буква', 'Количество животных'])
    # Проходим по каждой букве
    for letter in letters:
        url = f'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from={letter}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем все ссылки на страницы животных
        links = soup.find_all('a', href=True)
        animals = [
            link for link in links
            if link['href'].startswith('/wiki/')
            and unquote(link['href'][6:])[0].upper() == letter
        ]

        # print(f'\nБуква: {letter} — Количество: {len(animals)}')
        
        # for link in animals:
        #     if letter == 'Ё':
                
            
        #       print(f'— {link.text.strip()}')

        writer.writerow([letter, len(animals)])

print("успешно записаны в 'beasts.csv'")
