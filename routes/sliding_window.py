from db.database import  insert_result
from flask import Blueprint, request
from services.sliding_window.min_window_substring import min_window_substring
from services.sliding_window.sliding_window_max import sliding_window_max
from utils.validation import validate_min_window_substring_input
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
        insert_result(nums, k, result)
        from db.database import get_connection

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results")
        print(cursor.fetchall())
        conn.close()
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
    

@sliding_window_bp.route("/min_window_substring", methods=["POST"])
def handle_min_window():
    s, t, error = validate_min_window_substring_input(request)

    if error:
        return {
            "success": False,
            "data": None,
            "error": error
        }, 400

    if not s or not t:
        return {"success": False, "data": None, "error": "Invalid input"}, 400

    result = min_window_substring(s, t)

    return {
        "success": True,
        "data": result,
        "error": None
    }, 200


@sliding_window_bp.route("/sliding_window_max", methods=["POST"])
def handle_sliding_max():
    data = request.get_json()

    nums = data.get("nums")
    k = data.get("k")

    if not nums or not k:
        return {"success": False, "data": None, "error": "Invalid input"}, 400

    result = sliding_window_max(nums, k)

    return {
        "success": True,
        "data": result,
        "error": None
    }, 200