from flask import Blueprint, request
from services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    get_paginated_tasks,
    search_tasks,
    filter_tasks,
    sorting_tasks,
    get_tasks,
    PaginationError
)

from validations.task_validation import validate_task
from validations.task_validation import validate_pagination
from validations.task_validation import validate_search
from validations.task_validation import validate_filter
from validations.task_validation import validate_sort

from utils.response import (
    success_response,
    error_response
)

task_bp = Blueprint("task_bp", __name__)
@task_bp.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()
    errors = validate_task(data)
    if errors:
        return error_response(errors), 400
    
    create_task(data)

    return success_response(
        message = "task added successfully"
    )

# @task_bp.route("/tasks", methods=["GET"])
# def get_tasks():

#     tasks = get_all_tasks()
#     return success_response(tasks)

@task_bp.route("/tasks/<int:task_id>", methods=["GET"])

def get_single_task(task_id):

    task = get_task_by_id(task_id)

    if not task:
        return error_response("Task not found"), 404
    
    return success_response(task), 200

@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])

def update_single_task(task_id):

    data = request.get_json()
    errors = validate_task(data)

    if errors:
        return error_response(errors), 400
    
    task = get_task_by_id(task_id)

    if not task:
        return error_response("Task not found"), 404
    
    update_task(task_id, data)

    return success_response(
        message = "Task updated successfully"
    )

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])

def delete_single_task(task_id):

    task = get_task_by_id(task_id)

    if not task:
        return error_response("Task not found"), 404
    
    delete_task(task_id)

    return success_response(
        message = "Task deleted successfully"
    )

@task_bp.route("/tasks", methods=["GET"])
def get_paged_tasks():
    search = request.args.get("search")
    status_filter = request.args.get("status_filter")
    sort = request.args.get("sort")
    # page = request.args.get("page", 1, type=int)
    # limit = request.args.get("limit", 10, type=int)

    raw_page = request.args.get("page")
    raw_limit = request.args.get("limit")

    if raw_page is None:
        page = 1
    else:
        try:
            page = int(raw_page)
        except ValueError:
            return error_response("Invalid page"), 400
        if page < 1:
            return error_response("page must be greater than or equal to 1"), 400

    if raw_limit is None:
        limit = 10

    else:
        try:
            limit = int(raw_limit)
        except ValueError:
            return error_response("Invalid limit value"), 400
        if limit < 1:
            return error_response("limit must be greater than or equal to 1"), 400
        if limit > 100:
            return error_response("limit must be less than or equal to 100"), 400

    if sort:
        errors = validate_sort(sort)
        if errors:
            return error_response(errors), 400


    if status_filter:
        errors = validate_filter(status_filter)
        if errors:
            return error_response(errors), 400
        
    
    if search:
        errors = validate_search(search)
        if errors:
            return error_response(errors), 400
        
    
    
    errors = validate_pagination(page, limit)
    if errors:
        return error_response(errors), 400

    try:
        tasks = get_tasks(
            search=search,
            status_filter=status_filter,
            sort=sort,
            page=page,
            limit=limit
        )
    except PaginationError as e:
        return error_response(str(e)), 400
    
    return success_response(tasks)


    
