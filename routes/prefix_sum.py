from flask import Blueprint, request
from utils.validation import validate_prefix_sum_array
from services.prefix_sum.prefix_sum_array import prefix_sum_array

prefix_sum_array_bp = Blueprint("prefix_sum_array", __name__)

@prefix_sum_array_bp.route("/prefix_sum_array", methods=["POST"])
def prefix_sum_array_route():
    nums, error = validate_prefix_sum_array(request)
    try:
        if error:
            return {
                "success": False,
                "data": None,
                "error": error
            }, 400
        
        result = prefix_sum_array(nums)
        if result:
            return {
                "success": True,
                "data": result,
                "error": None
            }, 200
    
    except Exception:
        return{
            "success": False,
            "data": None,
            "error": "An error occured while processing the result."
        }, 500


        
