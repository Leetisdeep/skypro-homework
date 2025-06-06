from collections import Counter


def operation_counter(operations, categories):
    counts = Counter()
    for operation in operations:
        description = operation["description"].lower()
        for category in categories:
            if category.lower() in description:
                counts[category] += 1
    return counts
