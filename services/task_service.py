from db.database import get_connection


def create_task(data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks(title, status, priority, created_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                data["title"],
                data["status"],
                data["priority"],
                data["created_at"]
            )
        )
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:

        cursor.close()
        conn.close()


def get_all_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")

        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    except Exception:
        conn.rollback()
        raise

    finally:

        cursor.close()
        conn.close()


def get_task_by_id(task_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE id = %s",
            (task_id,)
        )

        row = cursor.fetchone()
        return dict(row) if row else None


    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

def update_task(task_id, data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = %s, status = %s, priority = %s, created_at = %s
            WHERE id = %s""",
            (
                data["title"],
                data["status"],
                data["priority"],
                data["created_at"],
                task_id

            )
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


def delete_task(task_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = %s",
            (task_id,)
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

def get_paginated_tasks(page,limit):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        offset = (page - 1) * limit

        cursor.execute(
            "SELECT * FROM tasks LIMIT %s OFFSET %s",
            (limit, offset)
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
    finally:
        cursor.close()
        conn.close()

def search_tasks(search):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        pattern = f"%{search}%"

        cursor.execute(
            "SELECT * FROM tasks WHERE title LIKE %s",
            (pattern,)

        )
        rows = cursor.fetchall()
        return{
            "search" : [dict(row) for row in rows]
        }
    finally:
        cursor.close()
        conn.close()

def filter_tasks(status_filter):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE status = %s",
            (status_filter,)
        )
        rows = cursor.fetchall()
        return{
            "filters": [dict(row) for row in rows]
        }
    finally:
        cursor.close()
        conn.close()
    # cursor = conn.cursor()

    # cursor.execute(
    #     "SELECT * FROM tasks WHERE status = %s",
    #     (status_filter,)
    # )
    # rows = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # return{
    #     "filters": [dict(row) for row in rows]
    # }
def sorting_tasks(sort):
    try:
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

        return{
            "sort": [dict(row) for row in rows]
        }
    finally:
        cursor.close()
        conn.close()


class PaginationError(Exception):
    pass

def get_tasks(search=None,
              status_filter=None,
              sort=None,
              page=1,
              limit=10):
    try:

        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM tasks WHERE 1=1"
        count_query = "SELECT COUNT(*) FROM tasks WHERE 1=1"

        params = []
        count_params = []

        # Search
        if search:
            query += " AND title LIKE %s"
            count_query += " AND title LIKE %s"
            params.append(f"%{search}%")
            count_params.append(f"%{search}%")

        # Filter
        if status_filter:
            query += " AND status = %s"
            count_query += " AND status = %s"
            params.append(status_filter)
            count_params.append(status_filter)


        #count total matchining rows
        cursor.execute(count_query, tuple(count_params))
        total = cursor.fetchone()["count"]

        pages = (total + limit - 1) // limit


        # Semantic Validation
        if total > 0 and page > pages:
            raise PaginationError("Page number exceeds total pages")

        # Sort
        if sort == "asc":
            query += " ORDER BY created_at ASC"

        elif sort == "desc":
            query += " ORDER BY created_at DESC"

        # Pagination
        offset = (page - 1) * limit

        query += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])

        #Fetch rows
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()




        previous_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < pages else None

        has_previous = previous_page is not None
        has_next = next_page is not None

        return {
            "tasks": [dict(row) for row in rows],
            "total_tasks": total,
            "total_pages" : pages,
            "page" : page,
            "limit" : limit,
            "previous_page" : previous_page,
            "has_previous" : has_previous,
            "next_page" : next_page,
            "has_next" : has_next
        }
    finally:
        cursor.close()

        conn.close()
