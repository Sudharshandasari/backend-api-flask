from flask import Blueprint, request
from services.twosum_service import solve_twosum
from utils.validation import validate_twosum_input


twosum_bp = Blueprint("twosum", __name__)

@twosum_bp.route("/twosum", methods = ["GET", "POST"])
def twosum():
    nums, target, error = validate_twosum_input(request)
    if error:
        return {"success": False, "data": None, "error": error}, 400
    
    result = solve_twosum(nums,target)
    if result:
        return {"success": True, "data": result, "error": None}, 200
    return {"success": False, "data": None, "error": "No solution found"}, 404
