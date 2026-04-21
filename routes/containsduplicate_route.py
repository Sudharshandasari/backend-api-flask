from flask import Blueprint, request
from services.containsduplicate_service import solve_contains_duplicate
from utils.validation import validate_contains_duplicate_input

containduplicate_bp = Blueprint('containduplicate', __name__)

@containduplicate_bp.route("/containsduplicate", methods = ["GET", "POST"])
def contains_duplicate():
    nums, error = validate_contains_duplicate_input(request)
    if error:
        return {
            "success": False,
            "data": None,
            "error": None
        }, 400
    
    result = solve_contains_duplicate(nums)
    return {
        "success": True,
        "data": result,
        "error": None
    }, 200