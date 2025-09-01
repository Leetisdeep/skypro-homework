# vacancy.py
from dataclasses import dataclass

@dataclass
class Vacancy:
    """Класс для представления вакансии."""

    title: str
    link: str
    salary: str
    description: str
    company: str = "Не указана"
    city: str = "Не указан"
    experience: str = "Не указан"

    def __post_init__(self):
        """Валидация данных после инициализации."""
        if not self.title:
            raise ValueError("Название вакансии не может быть пустым.")
        if not self.link:
            raise ValueError("Ссылка на вакансию не может быть пустой.")

    @staticmethod
    def parse_salary(salary):
        """Обрабатывает зарплату из API HH и преобразует в числовое значение для сравнения"""
        if isinstance(salary, dict):
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            currency = salary.get('currency', '')
            
            # Преобразуем зарплату в числовое значение для сравнения
            if salary_from is not None:
                numeric_salary = salary_from
            elif salary_to is not None:
                numeric_salary = salary_to
            else:
                numeric_salary = 0
            
            # Форматируем строку для отображения
            salary_str = ""
            if salary_from:
                salary_str += f"от {salary_from}"
            if salary_to:
                if salary_str:
                    salary_str += " "
                salary_str += f"до {salary_to}"
            if currency:
                salary_str += f" {currency}"
            
            return numeric_salary, salary_str if salary_str else "Зарплата не указана"
        
        return 0, salary if salary else "Зарплата не указана"

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньше)"""
        return self._get_numeric_salary() < other._get_numeric_salary()

    def __gt__(self, other):
        """Сравнение вакансий по зарплате (больше)"""
        return self._get_numeric_salary() > other._get_numeric_salary()

    def __eq__(self, other):
        """Сравнение вакансий по зарплате (равно)"""
        return self._get_numeric_salary() == other._get_numeric_salary()

    def _get_numeric_salary(self):
        """Возвращает числовое значение зарплаты для сравнения"""
        if isinstance(self.salary, tuple) and len(self.salary) == 2:
            return self.salary[0]  # numeric value
        return 0

    def get_salary_display(self):
        """Возвращает строковое представление зарплаты"""
        if isinstance(self.salary, tuple) and len(self.salary) == 2:
            return self.salary[1]  # display string
        return str(self.salary)

    def __str__(self):
        """Возвращает строковое представление вакансии."""
        return (f"Название: {self.title}\n"
                f"Компания: {self.company}\n"
                f"Город: {self.city}\n"
                f"Опыт: {self.experience}\n"
                f"Зарплата: {self.get_salary_display()}\n"
                f"Ссылка: {self.link}\n"
                f"Описание: {self.description[:100] + '...' if self.description and len(self.description) > 100 else self.description or 'Описание отсутствует'}\n")
