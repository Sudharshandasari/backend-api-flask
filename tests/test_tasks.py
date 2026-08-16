from datetime import datetime
def test_get_tasks_default_Pagination(client):
    response = client.get("/tasks")
    assert response.status_code == 200

    data = response.get_json()

def test_get_tasks_invalid_page(client):
    response = client.get("/tasks?page=abc")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "Invalid page"


def test_get_tasks_page_zero(client):
    response = client.get("/tasks?page=0")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "page must be greater than or equal to 1"


def test_get_tasks_page_exceeds_total_pages(client):
    response = client.get("/tasks?page=2")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "Page number exceeds total pages"


def test_get_tasks_limit_five(client):
    response = client.get("/tasks?limit=5")


    assert response.status_code == 200

    data = response.get_json()

    assert data["data"]["limit"] == 5

    assert data["success"] == True
    assert data["data"] is not None
    assert data["message"] == "success"


def test_get_tasks_limit_zero(client):
    response = client.get("/tasks?limit=0")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "limit must be greater than or equal to 1"

def test_get_tasks_negative_limit(client):
    response = client.get("/tasks?limit=-5")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "limit must be greater than or equal to 1"

def test_get_tasks_limit_exceeds_max(client):
    response = client.get("/tasks?limit=101")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None
    assert data["message"] == "limit must be less than or equal to 100"

def test_get_tasks_valid_limit(client):
    response = client.get("/tasks?limit=1")
    assert response.status_code == 200

    data = response.get_json()
    assert data["data"]["limit"] == 1

    assert data["success"] == True

    assert data["message"] == "success"

def test_get_tasks_limit_minimum(client):
    response = client.get("/tasks?limit=100")

    assert response.status_code == 200

    data = response.get_json()

    assert data["data"]["limit"] == 100
    assert data["success"] == True
    assert data["message"] == "success"


def test_get_tasks_limit_and_page(client):
    response = client.get("/tasks?page=1&limit=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["data"]["page"] == 1
    assert data["data"]["limit"] == 5

    assert data["success"] == True
    assert data["data"]["total_tasks"] == 7
    assert data["data"]["total_pages"] == 2
    assert data["data"]["has_previous"] == False
    assert data["data"]["has_next"] == True
    assert data["data"]["previous_page"] is None
    assert data["data"]["next_page"] == 2
    assert len(data["data"]["tasks"]) == 5

def test_get_tasks_page_two_limit_five(client):
    response = client.get("/tasks?page=2&limit=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["page"] == 2
    assert data["data"]["limit"] == 5
    assert data["data"]["total_tasks"] == 7
    assert data["data"]["total_pages"] == 2
    assert data["data"]["has_previous"] == True
    assert data["data"]["has_next"] == False
    assert data["data"]["previous_page"] == 1
    assert data["data"]["next_page"] is None
    assert len(data["data"]["tasks"]) == 2

def test_get_tasks_with_search(client):
    response = client.get("/tasks?search=sql")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["total_tasks"] > 0
    assert len(data["data"]["tasks"]) > 0

def test_get_tasks_with_zero_results(client):
    response = client.get("/tasks?search=THIS_sHOULD_NOT_EXIST")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["total_tasks"] == 0
    assert data["data"]["total_pages"] == 0
    assert len(data["data"]["tasks"]) == 0


def test_get_tasks_with_status_filter(client):
    response = client.get("/tasks?status_filter=completed")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True

    for task in data["data"]["tasks"]:
        assert task["status"] == "completed"

def test_get_tasks_with_invalid_status_filter(client):
    response = client.get("/tasks?status_filter=accepted")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None

def test_get_tasks_with_sort_asc(client):
    response = client.get("/tasks?sort=asc")

    assert response.status_code == 200

    data = response.get_json()

    tasks = data["data"]["tasks"]

    dates = [
        datetime.strptime(
            task["created_at"],
            "%a, %d %b %Y %H:%M:%S GMT"
        )
        for task in tasks
    ]

    assert dates == sorted(dates)
    assert data["success"] == True

def test_get_tasks_with_sort_desc(client):
    response = client.get("/tasks?sort=desc")

    assert response.status_code == 200

    data = response.get_json()

    tasks = data["data"]["tasks"]

    dates = [
        datetime.strptime(
            task["created_at"],
            "%a, %d %b %Y %H:%M:%S GMT"
        )
        for task in tasks
    ]

    assert dates == sorted(dates, reverse=True)
    assert data["success"] == True

def test_get_tasks_with_invalid_sort(client):
    response = client.get("/tasks?sort=invalid_sort")

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] == False
    assert data["data"] is None

def test_get_tasks_with_search_status_filter_sort_pagination(client):
    response = client.get("/tasks?search=sql&status_filter=completed&sort=desc&page=1&limit=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["page"] == 1
    assert data["data"]["limit"] == 5

def test_get_tasks_with_combined_query_with_zero_results(client):
    response = client.get("/tasks?search=THIS_sHOULD_NOT_EXIST&status_filter=completed&sort=desc&page=1&limit=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["total_tasks"] == 0
    assert len(data["data"]["tasks"]) == 0

def test_get_tasks_with_unsupported_method_contract(client):

    response = client.put("/tasks")
    assert response.status_code == 405

    response = client.delete("/tasks")
    assert response.status_code == 405

def test_get_tasks_with_successful_response_structure(client):
    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert "success" in data
    assert "data" in data
    assert "message" in data