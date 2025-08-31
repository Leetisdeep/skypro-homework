# api_client.py
import requests
import time
import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class Parser(ABC):
    """Абстрактный класс для загрузки вакансий из API."""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Загружает вакансии по ключевому слову."""
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """Инициализирует параметры запроса к API."""
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Загружает вакансии с HeadHunter по ключевому слову."""
        self._params['text'] = keyword
        self._params['page'] = 0
        
        while self._params['page'] < 20:
            try:
                response = requests.get(self._url, headers=self._headers, params=self._params)
                if response.status_code == 200:
                    data = response.json()
                    if not data.get('items'):
                        break  # Если вакансий нет, прерываем цикл
                    
                    self.vacancies.extend(data['items'])
                    logging.info(f"Загружена страница {self._params['page']} ({len(data['items'])} вакансий)")
                    self._params['page'] += 1
                    time.sleep(0.5)  # Задержка для предотвращения блокировки API
                else:
                    logging.error(f"Ошибка {response.status_code}: {response.text}")
                    break
            except requests.RequestException as e:
                logging.error(f"Ошибка запроса: {e}")
                break
