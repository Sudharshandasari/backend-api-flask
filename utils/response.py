def success_response(data = None, message = "success"):
    return{
        "success": True,
        "message": message,
        "data": data
    }

def error_response(message = "something went wrong"):
    return {
        "success": False,
        "message": message,
        "data": None
    }

