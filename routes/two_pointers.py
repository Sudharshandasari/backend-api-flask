from flask import Blueprint, request
from services.two_pointers.palindrome import palindrome
from utils.validation import validate_palindrome_input

palindrome_bp = Blueprint("palindrome", __name__)

@palindrome_bp.route("/palindrome", methods = ["GET", "POST"])
def check_palindrome():
    s, error = validate_palindrome_input(request)
    if error:
        return {
            "success": False,
            "data": None,
            "error": error
        }, 400
   
    result = palindrome(s)
    return {
        "success": True,
        "data": result,
        "error": None
    }, 200
    
from flask import Blueprint, request
from services.two_pointers.two_sum_sorted import two__sum_sorted
from utils.validation import validate_two_sum_sorted_input

validate_two_sum_sorted_input_bp  = Blueprint("two_sum_sorted", __name__)
@validate_two_sum_sorted_input_bp.route("/two_sum_sorted", methods = ["GET", "POST"])
def two_sum_sorted_route():
    nums, target, error = validate_two_sum_sorted_input(request)
    if error:
        return {
            "success": False,
            "data": None,
            "error": error
        }
    
    result = two__sum_sorted(nums, target)
    try:
        if isinstance(result, str):
            return {
                "success": False,
                "data": None,
                "error": result
            }, 404
        return {
            "success": True,
            "data": result,
            "error": None
        }, 200
    
    except Exception:
        return {
            "success": False,
            "data": None,
            "error": "An error occured while processing the request"
        }, 500  