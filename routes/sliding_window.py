from flask import Blueprint, request
from utils.validation import (validate_two_sum_subarray_input,validate_longest_unique_substring_input)
from services.sliding_window.two_sum_subarray import two_sum_subarray
from services.sliding_window.longest_unique_substring import longest_unique_substring

sliding_window_bp = Blueprint("sliding_window", __name__)

@sliding_window_bp.route("/two_sum_subarray", methods = ["GET", "POST"])

def validate_two_sum_subarray():
    nums, k, error = validate_two_sum_subarray_input(request)
    try:
        if error:
            return {
                "success": False,
                "data": None,
                "error": error
            }, 400
        
        result = two_sum_subarray(nums, k)
        return {
            "success" : True,
            "data": result,
            "error": None
        }, 200
    
    except  Exception:
        return {
            "success": False,
            "data": None,
            "error": "An error occurred while processing the request"
        }, 500


@sliding_window_bp.route("/longest_unique_substring", methods = ["GET", "POST"])
def longest_unique_substring_route():
    s, error = validate_longest_unique_substring_input(request)
    try:
        if error:
            return {
                "success": False,
                "data": None,
                "error": error
            }, 400

        result = longest_unique_substring(s)
        return {
            "success": True,
            "data": result,
            "error": None
        }, 200

    except Exception:
        return {
            "success": False,
            "data": None,
            "error": "An error occurred while processing the request"
        }, 500