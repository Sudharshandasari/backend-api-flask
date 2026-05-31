from db.database import get_connection


def create_expense(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses(title, amount, category)
        VALUES (?, ?, ?)
        """,
        (
            data["title"],
            data["amount"],
            data["category"]
        )
    )

    conn.commit()
    conn.close()


def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_expense_by_id(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def update_expense(expense_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET title = ?, amount = ?, category = ?
        WHERE id = ?
        """,
        (
            data["title"],
            data["amount"],
            data["category"],
            expense_id
        )
    )

    conn.commit()
    conn.close()


def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()