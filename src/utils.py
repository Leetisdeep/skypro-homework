# utils.py
def get_user_input(prompt, convert_func=str):
    """Функция для безопасного получения ввода пользователя"""
    while True:
        user_input = input(prompt).strip()
        try:
            return convert_func(user_input)
        except ValueError:
            print("Некорректный ввод. Попробуйте ещё раз.")


def sort_vacancies_by_salary(vacancies, reverse=True):
    """Сортирует вакансии по зарплате"""
    return sorted(vacancies, reverse=reverse)


def filter_vacancies_by_keyword(vacancies, keyword):
    """Фильтрует вакансии по ключевому слову в описании"""
    if not keyword:
        return vacancies
    return [v for v in vacancies if v.description and keyword.lower() in v.description.lower()]


def print_vacancies(vacancies, title="Вакансии"):
    """Выводит список вакансий"""
    if not vacancies:
        print(f"{title} не найдены.")
        return
    
    print(f"\n{title} ({len(vacancies)}):")
    print("=" * 80)
    for vac in vacancies:
        print(vac)
        print("-" * 80)
