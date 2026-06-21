from db.database import get_connection

def create_task(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(title, status, priority, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["title"],
            data["status"],
            data["priority"],
            data["created_at"]
        )
    )

    conn.commit()
    conn.close()


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None

def update_task(task_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, status = ?, priority = ?, created_at = ?
        WHERE id = ?""",
        (
            data["title"],
            data["status"],
            data["priority"],
            data["created_at"],
            task_id

        )
    )

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def get_paginated_tasks(page,limit):
    conn = get_connection()
    cursor = conn.cursor()

    offset = (page - 1) * limit

    cursor.execute(
        "SELECT * FROM tasks LIMIT ? OFFSET ?",
        (limit,offset,),
        
    )
    rows = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]
    pages = (total + limit - 1) // limit

    if page == 1:
        previous_page = None
    else:
       previous_page = page - 1


    if page == pages:
        next_page = None

    else:
        next_page = page + 1


    has_previous = previous_page is not None
    has_next = next_page is not None  

    conn.close()
    return {
        "Tasks": [dict(row) for row in rows],
        "total_tasks": total,
        "total_pages": pages,
        "page" : page,
        "limit" : limit,
        "previous_page" : previous_page,
        "next_page" : next_page,
        "has_previous" : has_previous,
        "has_next" : has_next

    }

def search_tasks(search):
    conn = get_connection()
    cursor = conn.cursor()

    pattern = f"%{search}%"

    cursor.execute(
        "SELECT * FROM tasks WHERE title LIKE ?",
        (pattern,)

    )
    rows = cursor.fetchall()
    conn.close()
    return{
        "search" : [dict(row) for row in rows]
    }

def filter_tasks(status_filter):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE status = ?",
        (status_filter,)
    )
    rows = cursor.fetchall()
    conn.close()
    return{
        "filters": [dict(row) for row in rows]
    }
def sorting_tasks(sort):
    conn = get_connection()
    cursor = conn.cursor()
    if sort == "asc":
        # ORDER BY created_at ASC
        cursor.execute(
            "SELECT * FROM tasks ORDER BY created_at ASC",
        )

    elif sort == "desc":
        # ORDER BY created_at DESC 
        cursor.execute(
            "SELECT * FROM tasks ORDER BY created_at DESC"
        )

    rows = cursor.fetchall()

    conn.close()

    return{
        "sort": [dict(row) for row in rows]
    }


def get_tasks(search=None,
              status_filter=None,
              sort=None,
              page=1,
              limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    # Search
    if search:
        query += " AND title LIKE ?"
        params.append(f"%{search}%")

    # Filter
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter)

    # Sort
    if sort == "asc":
        query += " ORDER BY created_at ASC"

    elif sort == "desc":
        query += " ORDER BY created_at DESC"

    # Pagination
    offset = (page - 1) * limit

    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, tuple(params))

    rows = cursor.fetchall()

    conn.close()

    return {
        "tasks": [dict(row) for row in rows]
    }