# from flask import Flask , request

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "backend running"

# @app.route("/add")
# def add():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return str(a+b)

# @app.route("/sub")
# def sub():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return str(a-b)

# # Query params: request.args

# @app.route("/twosum")
# def twosum():
#     nums = list(map(int,request.args.get("nums").split(",")))
#     target = int(request.args.get("target"))
#     seen = {}
#     for i,num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return str([seen[diff],i])
#         seen[num] = i
#     return "No solution"

# # JSON body: request.get_json()

# @app.route("/twosumjson", methods=["POST"])
# def twosumjson():
#     data = request.get_json()
#     nums = data["nums"]
#     target = data["target"]
#     if not nums or not target:
#         return "Invalid input", 400
#     seen = {}
#     for i,num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return str([seen[diff],i])
#         seen[num] = i
#     return "No solution"

# # Query params: request.args

# @app.route("/maxsum")
# def maxsum():
#     nums = list(map(int,request.args.get("nums").split(",")))
#     k = int(request.args.get("k"))
#     max_sum = float('-inf')
#     current_sum = 0
#     for i in range(len(nums)):
#         current_sum += nums[i]
#         if i >= k - 1:
#             max_sum = max(max_sum, current_sum)
#             current_sum -= nums[i - (k -1)]

#     return str(max_sum)

# # JSON body: request.get_json()

# @app.route("/maxsumjson", methods=["POST"])
# def maxsumjson():
#     data = request.get_json()
#     nums = data["nums"]
#     k = data["k"]
#     if not nums or not k:
#         return "Invalid input", 400
#     max_sum = float('-inf')
#     current_sum = 0
#     for i in range(len(nums)):
#         current_sum += nums[i]
#         if i >= k -1:
#             max_sum = max(max_sum,current_sum)
#             current_sum -= nums[i - (k - 1)]

#     return {"max_sum": max_sum}


    
# app.run()




from flask import Flask, request


app = Flask(__name__)
@app.route("/")
def home():
    return "backend running"

@app.route("/twosum", methods=["GET", "POST"])
def twosum():
    if request.method == "GET":
        nums = request.args.get("nums")
        target = request.args.get("target")

        if nums is None or target is None:
            return {"success": False, "data": None, "error": "Invalid input"}, 400

        nums = list(map(int, nums.split(",")))
        target = int(target)

    else:
        data = request.get_json()
        if not data:
            return {"success": False, "data": None, "error": "Invalid JSON"}, 400

        nums = data.get("nums")
        target = data.get("target")

        if nums is None or target is None:
            return {"success": False, "data": None, "error": "Invalid input"}, 400

    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return {
                "success": True,
                "data": [seen[diff], i],
                "error": None
            }
        seen[num] = i

    return {
        "success": False,
        "data": None,
        "error": "No solution found"
    }, 404

@app.route ("/maxsum", methods = ["GET","POST"])
def maxsum():
    if request.method == "GET":
        nums = request.args.get("nums")
        k = request.args.get("k")
        if nums is None or k is None:
            return {"error": "Invalid Input"}, 400
        nums = list(map(int,nums.split(",")))
        k = int(k)

    else: # POST
        data = request.get_json()
        if not data:
            return {"error": "Invalid Input"}, 400
        nums = data["nums"]
        k = data["k"]
        if nums is None or k is None:
            return {"error": "Invalid Input"}, 400
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - (k - 1)]
    return {
        "success": True,
        "data": max_sum,
        "error": None
        }, 200

from collections import Counter
@app.route("/firstuniquenumber",methods = ["GET","POST"])
def firstuniquenumber():
    if request.method == "GET":
        nums = request.args.get("nums")
        if nums is None or not isinstance(nums,str):
            return {
                "success": False,
                "data": None,
                "error": "Invalid input"
            },400
        
        nums = list(map(int,nums.split(",")))
    else: # POST
        data = request.get_json()
        if not data:
            return {
                "success": False,
                "data": None,
                "error": "Invalid input"
            },400
        nums = data.get("nums")
        if nums is None or not isinstance(nums,list):
            return {
                "success": False,
                "data": None,
                "error": "Invalid input"
            }, 400
    # Continue with the rest of the function logic
    # ... (implementation details)
    count = Counter(nums)
    for num in nums:
        if count[num] == 1:
            return {
                    "success": True,
                    "data": num,
                    "error": None
                }, 200

        return{
            "success": False,
            "data": None,
            "error": "No unique number found"
            }, 404

if __name__ == "__main__":
    app.run(debug=True)
