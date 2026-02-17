from db import get_connection


def add_club(name, city):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO clubs (name, city) VALUES (?, ?)",
            (name, city)
        )
        conn.commit()
        print("Клубът е добавен успешно.")
    except Exception as e:
        print("Грешка при добавяне:", e)

    conn.close()


def get_all_clubs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clubs")
    clubs = cursor.fetchall()

    conn.close()
    return clubs


def update_club(club_id, new_name, new_city):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE clubs SET name = ?, city = ? WHERE id = ?",
        (new_name, new_city, club_id)
    )

    conn.commit()
    conn.close()
    print("Клубът е обновен.")


def delete_club(club_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clubs WHERE id = ?", (club_id,))
    conn.commit()
    conn.close()
    print("Клубът е изтрит.")
