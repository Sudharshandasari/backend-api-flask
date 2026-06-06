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
