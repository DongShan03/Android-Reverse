import pymysql
from pymysql.cursors import DictCursor

def change(sql, isInsert=False):
    try:
        count = cursor.execute(sql)
        conn.commit()
        if isInsert:
            new_id = cursor.lastrowid
            return new_id
        else:
            return count
    except Exception as e:
        print(e)
        conn.rollback()

def add(sql):
    return change(sql, isInsert=True)

def update(sql):
    return change(sql)

def delete(sql):
    return change(sql)

def get_all(sql):
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)

    # many = cursor.fetchmany(2)
    # print(many)

def get_one(sql):
    try:
        cursor.execute(sql)
        return cursor.fetchone()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    conn = pymysql.connect(
    user="root",
    password="",
    host="localhost",
    database="数据库学习",
    port=3306,
    )

    cursor = conn.cursor(cursor=DictCursor) #字典游标


    sql = "select * from stu_new"
    ret = get_one(sql)
    print(ret)

    if cursor:
        cursor.close()
    if conn:
        conn.close()
