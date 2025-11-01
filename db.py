# coding: utf8
import sqlite3
from config import DB_NAME

conn = sqlite3.connect(f'{DB_NAME}.db', check_same_thread=False)

def tgidregister(tid):
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (tgid) VALUES(?);", (tid,))
        conn.commit()
    except Exception as e:
        print(e)

def countusers(): # for admin
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users;")
        countusers = cur.fetchone()[0]
        return str(countusers)
    except Exception as e:
        print(e)
        return "0"

def getusers(): # for admin
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        getuser = cur.fetchall()
        return getuser
    except Exception as e:
        print(e)
        return []
