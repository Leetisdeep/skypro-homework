# main.py
from api_client import HH
from storage import JSONStorage
from vacancy import Vacancy
from utils import get_user_input, sort_vacancies_by_salary, filter_vacancies_by_keyword, print_vacancies


def convert_vacancy_data(vacancy_data):
    """Преобразует данные вакансии из API в объект Vacancy"""
    salary_numeric, salary_display = Vacancy.parse_salary(vacancy_data.get("salary"))
    
    return Vacancy(
        title=vacancy_data.get("name", "Без названия"),
        link=vacancy_data.get("alternate_url", "#"),
        salary=(salary_numeric, salary_display),
        description=vacancy_data.get("snippet", {}).get("responsibility", "Описание отсутствует"),
        company=vacancy_data.get("employer", {}).get("name", "Не указана"),
        city=vacancy_data.get("area", {}).get("name", "Не указан"),
        experience=vacancy_data.get("experience", {}).get("name", "Не указан"),
    )


def save_vacancies_to_json(vacancies, filename="vacancies.json"):
    """Сохраняет вакансии в JSON файл"""
    with JSONStorage(filename) as storage:
        for vac in vacancies:
            vacancy_dict = {
                "name": vac.title,
                "alternate_url": vac.link,
                "salary": {"from": vac._get_numeric_salary(), "to": None, "currency": ""},
                "description": vac.description,
                "company": vac.company,
                "city": vac.city,
                "experience": vac.experience
            }
            storage.add_vacancy(vacancy_dict)


def search_vacancies():
    """Основная функция для поиска и обработки вакансий"""
    hh = HH()

    # Запрос ключевого слова у пользователя
    keyword = input("Введите ключевое слово для поиска вакансий: ").strip()
    if not keyword:
        print("Ключевое слово не может быть пустым!")
        return

    print("\nЗагружаем вакансии...")
    hh.load_vacancies(keyword)

    if not hh.vacancies:
        print("По вашему запросу вакансий не найдено.")
        return

    # Преобразуем вакансии в объекты Vacancy
    vacancy_objects = [convert_vacancy_data(item) for item in hh.vacancies]
    print(f"Загружено {len(vacancy_objects)} вакансий.")

    # Сохранение всех вакансий в JSON
    save_vacancies_to_json(vacancy_objects)

    # Запрос у пользователя количества топ N вакансий по зарплате
    top_n = get_user_input("\nСколько топ-вакансий по зарплате вывести? ", int)
    
    # Сортировка вакансий по зарплате
    sorted_vacancies = sort_vacancies_by_salary(vacancy_objects)
    top_vacancies = sorted_vacancies[:top_n]

    # Сохранение топ вакансий в отдельный файл
    save_vacancies_to_json(top_vacancies, "top_vacancies.json")

    # Вывод топ вакансий
    print_vacancies(top_vacancies, f"Топ-{top_n} вакансий по зарплате")

    # Фильтрация вакансий по ключевому слову в описании
    keyword_desc = input("\nВведите ключевое слово для поиска в описании вакансий: ").strip().lower()
    filtered_vacancies = filter_vacancies_by_keyword(vacancy_objects, keyword_desc)

    # Вывод отфильтрованных вакансий
    print_vacancies(filtered_vacancies, f"Вакансии с ключевым словом '{keyword_desc}' в описании")


if __name__ == "__main__":
    search_vacancies()
