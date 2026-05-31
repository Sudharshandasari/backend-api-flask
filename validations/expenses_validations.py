def validate_expense(data):
    errors = []
    if "title" not in data or not data["title"]:
        errors.append("Title is required")


    if "amount" not in data:
        errors.append("Amount is required")

    elif data["amount"] <= 0:
        errors.append("Amount must be greater than zero")

    if "category" not in data or not data["category"]:
        errors.append("Category is required")

    return errors