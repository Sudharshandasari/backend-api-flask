from db.database import get_connection


def create_expense(data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO expenses(title, amount, category)
            VALUES (%s, %s, %s)
            """,
            (
                data["title"],
                data["amount"],
                data["category"]
            )
        )

        conn.commit()
    except Exception:
        conn.rollback()
        raise

    finally:

        cursor.close()
        conn.close()


def get_all_expenses():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM expenses")

        rows = cursor.fetchall()

    finally:
        cursor.close()
        conn.close()

    return [dict(row) for row in rows]


def get_expense_by_id(expense_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM expenses WHERE id = %s",
            (expense_id,)
        )

        row = cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

    return dict(row) if row else None


def update_expense(expense_id, data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE expenses
            SET title = %s, amount = %s, category = %s
            WHERE id = %s
            """,
            (
                data["title"],
                data["amount"],
                data["category"],
                expense_id
            )
        )

        conn.commit()
    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


def delete_expense(expense_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM expenses WHERE id = %s",
            (expense_id,)
        )
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()