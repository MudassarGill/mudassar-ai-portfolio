import sqlite3

db1 = sqlite3.connect('portfolio.db')
try:
    print('Root DB tables:', [r[0] for r in db1.execute("SELECT name FROM sqlite_master WHERE type='table'")])
    print('Root DB rows:', db1.execute("SELECT count(*) FROM messages").fetchone()[0])
except Exception as e:
    print("Root DB:", e)

db2 = sqlite3.connect('backend/portfolio.db')
try:
    print('Backend DB tables:', [r[0] for r in db2.execute("SELECT name FROM sqlite_master WHERE type='table'")])
    print('Backend DB rows:', db2.execute("SELECT count(*) FROM messages").fetchone()[0])
except Exception as e:
    print("Backend DB:", e)
