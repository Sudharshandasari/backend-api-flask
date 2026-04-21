def validate_twosum_input(request):
    try:

        if request.method == "GET":
            nums = request.args.get("nums")
            target = request.args.get("target")
            if not nums or not target:
                return None, None, "Missing params"
            nums = list(map(int,nums.split(",")))
            target = int(target)

        else: # POST
            data = request.get_json()
            if not data:
                return None, None, "Invalid JSON"
            nums = data.get("nums")
            target = data.get("target")
            if nums is None or target is None:
                return None, None, "missing json body params"
            

        return nums, target, None
    
    except:
        return None, None, "Invalid input format"
        
def validate_contains_duplicate_input(request):
    try: 
        if request.method == "GET":
            nums = request.args.get("nums")
            if not nums:
                return None, "missing params"
            nums =  list(map(int,nums.split(",")))
        else:
            data = request.get_json()
            if not data:
                return None, "Invalid JSON"
            nums = data.get("nums")
            if nums is None or isinstance(nums, list):
                return None, "Invalid nums"
            
        return nums, None
        
    except:
        return None, "Invalid input format"

def validate_majority_input(request):
    try:
        if request.method == "GET":
            nums = request.args.get("nums")
            if not nums:
                return None, "Missing params"
            nums = list(map(int,nums.split(",")))

        else: # POST
            data = request.get_json()
            if not data:
                return None, "Invalid JSON"
            nums = data.get("nums")
            if nums is None or not isinstance(nums,list):
                return None, "missing json body params"
            
        return nums, None
        
    except:
        return None, "Invalid input format"
    


def validate_palindrome_input(request):
    try:
        if request.method == "GET":
            s = request.args.get("s")
            if s is None:
                return None, "Missing params"
        else: # POST
            data = request.get_json()
            if not data:
                return None, "Invalid JSON"
            s = data.get("s")
            if s is None or not isinstance(s,str):
                return None, "missing json body params"
        return s, None
            
    except:
        return None, "invalid input format", 404
    

def validate_two_sum_sorted_input(request):
    try: 
        if request.method == "GET":
            nums = request.args.get("nums")
            target = request.args.get("target")
            if not nums or not target:
                return None, None, "missing params"
            
            nums = list(map(int,nums.split(",")))
            target = int(target)

        else: # POST
            data = request.get_json()
            if not data:
                return None, None, "Invalid JSON"
            nums = data.get("nums")
            target = data.get("target")
            if nums is None or target is None or not isinstance(nums,list) or not isinstance(target,int):
                return None, None, "missing json body params"
            
        return nums, target, None
    
    except:
        return None, None, "Invalid input format"
    
    