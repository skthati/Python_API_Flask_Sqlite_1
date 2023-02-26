from db import get_db, post_db


def get_all_family():
    db = get_db()
    con = db.cursor()
    statement = "SELECT * FROM family"
    con.execute(statement)
    return con.fetchall()


def get_one_family(id1):
    db = get_db()
    con = db.cursor()
    statement = "SELECT * FROM family WHERE id = ?"
    con.execute(statement, [id1])
    return con.fetchone()


def insert_family(f_name, l_name, age):
    db = get_db()
    con = db.cursor()
    statement = "INSERT INTO family(first_name, last_name, age) values(?, ?, ?)"
    con.execute(statement, [f_name, l_name, age])
    db.commit()
    return True


def update_family_member(f_name, l_name, age, id1):
    db = get_db()
    conn = db.cursor()
    print(f_name, l_name, age, id1)
    print(type(id1))
    statement = "UPDATE family SET first_name = ?, last_name = ?, age = ? WHERE id = ?"
    conn.execute(statement, [f_name, l_name, age, id1])
    db.commit()
    return True


def delete_family_member(id1):
    db = get_db()
    conn = db.cursor()
    statement = "DELETE FROM family WHERE id = ?"
    conn.execute(statement, [id1])
    db.commit()
    return True




