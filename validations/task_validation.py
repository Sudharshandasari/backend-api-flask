def validate_task(data):
    errors = []
    if 'title' not in data or not str(data['title']).strip():
        errors.append('title is required')

    if 'status' not in data or not str(data['status']).strip():
        errors.append('status is required')

    elif data['status'] not in {'pending', 'in_progress', 'completed'}:
        errors.append('status must be one of: pending, in_progress, completed')

    if 'priority' not in data or not str(data['priority']).strip():
        errors.append('priority is required')

    elif data['priority'] not in {'low', 'medium', 'high'}:
        errors.append('priority must be one of: low, medium, high')

    return errors

def validate_pagination(page,limit):
    errors = []
    if page < 1:
        errors.append("page must be greater than or equal to 1")

    if limit < 1:
        errors.append("limit must be greater than or equal to  1")

    elif limit >= 100:
        errors.append("limit must be lesser than or equal to 100")

    return errors

def validate_search(search):
    errors = []
    if not search or not search.strip():
        errors.append("search term is required")
    return errors

def validate_filter(status_filter):
    errors = []
    if not status_filter or not status_filter.strip():
        errors.append("filter term is required")
    return errors

def validate_sort(sort):
    errors = []
    if sort not in ["asc" , "desc"]:
        errors.append("sort must be asc or desc")
    return errors


