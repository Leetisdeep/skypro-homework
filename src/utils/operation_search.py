import re


def operation_search(operations, search_term):
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)

    return [op for op in operations if pattern.search(op.get("description", ""))]
