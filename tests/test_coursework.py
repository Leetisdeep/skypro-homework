import pytest
from unittest.mock import patch, Mock
from src.api_client import HH
from src.vacancy import Vacancy
from src.storage import JSONStorage
import tempfile
import json
import os


@pytest.fixture
def test_json_file():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as temp_file:
        temp_file.write(b'[]')
        temp_file.close()
        yield temp_file.name
    # Удаляем временный файл после теста
    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)


@pytest.fixture
def test_vacancy():
    return Vacancy(
        title="Python Developer",
        link="https://example.com",
        salary=(100000, "100000 - 150000 RUB"),  # Изменено на кортеж
        description="Development of web applications",
        company="Test Company",
        city="Moscow",
        experience="3-5 years"
    )


def test_add_and_get_vacancy(test_json_file, test_vacancy):
    storage = JSONStorage(test_json_file)
    # Создаем словарь для хранения (как в основном коде)
    vacancy_dict = {
        "name": test_vacancy.title,
        "alternate_url": test_vacancy.link,
        "salary": {"from": test_vacancy._get_numeric_salary(), "to": None, "currency": "RUB"},
        "description": test_vacancy.description,
        "company": test_vacancy.company,
        "city": test_vacancy.city,
        "experience": test_vacancy.experience
    }
    storage.add_vacancy(vacancy_dict)
    vacancies = storage.get_vacancies({"name": "Python Developer"})
    assert len(vacancies) == 1


def test_delete_vacancy(test_json_file, test_vacancy):
    storage = JSONStorage(test_json_file)
    vacancy_data = {
        "id": 1,
        "name": test_vacancy.title,
        "alternate_url": test_vacancy.link,
        "salary": {"from": test_vacancy._get_numeric_salary(), "to": None, "currency": "RUB"},
        "description": test_vacancy.description,
        "company": test_vacancy.company,
        "city": test_vacancy.city,
        "experience": test_vacancy.experience
    }
    storage.add_vacancy(vacancy_data)
    storage.delete_vacancy(1)
    vacancies = storage.get_vacancies({})
    assert len(vacancies) == 0


def test_vacancy_post_init():
    with pytest.raises(ValueError):
        Vacancy(title="", link="https://example.com", salary=(0, ""), description="")

    with pytest.raises(ValueError):
        Vacancy(title="Python Developer", link="", salary=(0, ""), description="")


def test_load_vacancies():
    mock_response = {
        'items': [
            {
                'name': 'Python Developer', 
                'alternate_url': 'https://example.com',
                'salary': {'from': 100000, 'to': 150000, 'currency': 'RUB'},
                'snippet': {'responsibility': 'Development'},
                'employer': {'name': 'Test Company'},
                'area': {'name': 'Moscow'},
                'experience': {'name': '3-5 years'}
            }
        ]
    }
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response
        hh = HH()
        hh.load_vacancies("Python")
        # Теперь проверяем, что вакансии загрузились
        assert len(hh.vacancies) > 0


def test_parse_salary():
    # Тестируем новый формат возвращаемых данных
    numeric, display = Vacancy.parse_salary({'from': 100000, 'to': 150000, 'currency': 'RUB'})
    assert numeric == 100000
    assert display == "от 100000 до 150000 RUB"
    
    numeric, display = Vacancy.parse_salary({})
    assert numeric == 0
    assert display == "Зарплата не указана"
    
    numeric, display = Vacancy.parse_salary(None)
    assert numeric == 0
    assert display == "Зарплата не указана"


def test_context_manager(test_json_file):
    with JSONStorage(test_json_file) as storage:
        storage.add_vacancy({
            "name": "Python Developer", 
            "alternate_url": "https://example.com",
            "salary": {"from": 100000, "to": None, "currency": "RUB"}
        })
    
    with open(test_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    assert len(data) == 1


def test_vacancy_comparison():
    # Тестируем магические методы сравнения
    vac1 = Vacancy("Dev1", "link1", (50000, "50000 руб"), "desc1")
    vac2 = Vacancy("Dev2", "link2", (100000, "100000 руб"), "desc2")
    vac3 = Vacancy("Dev3", "link3", (100000, "100000 руб"), "desc3")
    
    assert vac1 < vac2
    assert vac2 > vac1
    assert vac2 == vac3
    assert vac1 != vac2


def test_get_numeric_salary():
    vacancy = Vacancy("Test", "link", (80000, "80000 руб"), "desc")
    assert vacancy._get_numeric_salary() == 80000


def test_get_salary_display():
    vacancy = Vacancy("Test", "link", (80000, "80000 руб"), "desc")
    assert vacancy.get_salary_display() == "80000 руб"


def test_hh_private_attributes():
    # Тестируем, что приватные атрибуты существуют
    hh = HH()
    assert hasattr(hh, '_url')
    assert hasattr(hh, '_headers')
    assert hasattr(hh, '_params')
    assert not hasattr(hh, 'url')  # Публичного атрибута не должно быть


def test_json_storage_private_filename():
    # Тестируем приватный атрибут filename
    storage = JSONStorage("test.json")
    assert hasattr(storage, '_filename')
    assert not hasattr(storage, 'filename')  # Публичного атрибута не должно быть
