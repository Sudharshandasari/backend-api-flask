from flask import Blueprint, request
from services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

from validations.task_validation import validate_task

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

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = get_all_tasks()
    return success_response(tasks)

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

