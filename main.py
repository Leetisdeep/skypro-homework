from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils.file_reader import read_transactions_from_csv, read_transactions_from_excel, read_transactions_from_json
from src.utils.operation_search import operation_search


def print_transaction(transaction, json=True):
    """Выводит информацию о транзакции."""
    date = transaction.get("date", "Дата не указана")
    description = transaction.get("description", "Описание отсутствует")
    amount = transaction.get("amount", "Сумма не указана")
    if json:
        if transaction.get("operationAmount"):
            currency = transaction.get("operationAmount").get("currency").get("code")
        else:
            currency = None
    else:
        currency = transaction.get("currency_code")
    print(f"{date} {description}")
    print(f"Сумма: {amount} {currency}\n")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ")
    if choice not in ["1", "2", "3"]:
        print("Некорректный выбор. Попробуйте снова.")
        return

    if choice == "1":
        transactions = read_transactions_from_json("data/operations.json")
    elif choice == "2":
        transactions = read_transactions_from_csv("data/transactions.csv")
    else:
        transactions = read_transactions_from_excel("data/transactions_excel.xlsx")

    if not transactions:
        print("Не удалось загрузить данные.")
        return

    status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Статус операции недоступен.")
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()

    filtered_transactions = filter_by_state(transactions, status)

    sort_answer = input("Отсортировать операции по дате? Да/Нет: ").lower() == "да"
    if sort_answer:
        order = input("По возрастанию или по убыванию? Введите 'возрастание' или 'убывание': ").lower()
        reverse = order == "убывание"
        filtered_transactions = sort_by_date(filtered_transactions, reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower() == "да"
    if rub_only:
        if choice == "1":
            filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        else:
            filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB", False))

    filter_description = input("Отфильтровать по описанию? Да/Нет: ").lower() == "да"
    if filter_description:
        search_string = input("Введите строку для поиска: ")
        filtered_transactions = operation_search(filtered_transactions, search_string)

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            if choice == "1":
                print_transaction(transaction)
            else:
                print_transaction(transaction, False)


if __name__ == "__main__":
    main()
