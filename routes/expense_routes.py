from flask import Blueprint, request

from services.expense_service import (
    create_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense
)

from validations.expenses_validations import validate_expense

from utils.response import (
    success_response,
    error_response
)

expense_bp = Blueprint("expense_bp", __name__)


@expense_bp.route("/expenses", methods=["POST"])
def add_expense():

    data = request.get_json()

    errors = validate_expense(data)

    if errors:
        return error_response(errors), 400

    create_expense(data)

    return success_response(
        message="Expense added successfully"
    )


@expense_bp.route("/expenses", methods=["GET"])
def get_expenses():

    expenses = get_all_expenses()

    return success_response(expenses)


@expense_bp.route("/expenses/<int:expense_id>", methods=["GET"])
def get_single_expense(expense_id):

    expense = get_expense_by_id(expense_id)

    if not expense:
        return error_response("Expense not found"), 404

    return success_response(expense)


@expense_bp.route("/expenses/<int:expense_id>", methods=["PUT"])
def update_single_expense(expense_id):

    data = request.get_json()

    errors = validate_expense(data)

    if errors:
        return error_response(errors), 400

    existing_expense = get_expense_by_id(expense_id)

    if not existing_expense:
        return error_response("Expense not found"), 404

    update_expense(expense_id, data)

    return success_response(
        message="Expense updated successfully"
    )


@expense_bp.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_single_expense(expense_id):

    existing_expense = get_expense_by_id(expense_id)

    if not existing_expense:
        return error_response("Expense not found"), 404

    delete_expense(expense_id)

    return success_response(
        message="Expense deleted successfully"
    )