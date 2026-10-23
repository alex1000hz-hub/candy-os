lazy import sys
lazy import sqlite3
lazy import os
args = sys.argv[1:]
if args[0] == ">" and args [1] == "sql":
    ruta = args[2]
    if os.path.exists(ruta):
        if args[3] == "inyect":
            con = sqlite3.connect(ruta)
            cur = con.cursor()
            cur.execute("SELECT * FROM " + args[4])
            for row in cur:
                print(row)
            con.close()
        elif args[3] == "insert":
            con = sqlite3.connect(ruta)
            cur = con.cursor()
            cur.execute("INSERT INTO " + args[4] + " VALUES (?,?,?,?,?)", (args[5], args[6], args[7], args[8], args[9]))
            con.commit()
            con.close()
        elif args[3] == "update":
            con = sqlite3.connect(ruta)
            cur = con.cursor()
            cur.execute("UPDATE " + args[4] + " SET " + args[5] + "=? WHERE " + args[6] + "=?", (args[7], args[8]))
            con.commit()
            con.close()
        elif args[3] == "delete":
            con = sqlite3.connect(ruta)
            cur = con.cursor()
            cur.execute("DELETE FROM " + args[4] + " WHERE " + args[5] + "=?", (args[6],))
            con.commit()
            con.close()
    else:
        print("File not found")
