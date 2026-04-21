from flask import Blueprint, request
from utils.validation import validate_majority_input
from services.majority_service import solve_majority

majority_bp = Blueprint("majority", __name__)

@majority_bp.route("/majority", methods = ["GET", "POST"])
def majority():
    nums, error = validate_majority_input(request)
    if error:
        return {
            "success": False,
            "data": None,
            "error": error
        }, 400
    
    result = solve_majority(nums)
    if result:
        return {
            "success": True,
            "data": result,
            "error": None
        }, 200
    
    return {
        "success": False,
        "data": None,
        "error": "No majority element found"
    },404