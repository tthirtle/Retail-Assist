import sqlite3
from _global import database_file,item,store

def create_db():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        # Create Store Table
        cur.execute(
            """CREATE TABLE "store" (
                "key"	INTEGER,
                "name"	TEXT,
                "number"	TEXT,
                "address 1"	TEXT,
                "address 2"	TEXT,
                "city"	TEXT,
                "state"	TEXT,
                "zip"	TEXT,
                "tel"	TEXT,
                "fax"	TEXT,
                "other"	TEXT,
                PRIMARY KEY("key" AUTOINCREMENT)
                )"""
        )
        # Create Item Table
        cur.execute(
            """CREATE TABLE "item" (
                "key"	INTEGER,
                "upc"	TEXT,
                "item number"	TEXT,
                "desc"	TEXT,
                "size"	TEXT,
                "units"	TEXT,
                "alt desc"	TEXT,
                "disc"	INTEGER,
                "new item"	INTEGER,
                PRIMARY KEY("key" AUTOINCREMENT)
                )"""
        )
        # Create user Table
        cur.execute(
            """CREATE TABLE "user" (
                "key"	INTEGER,
                "username"	TEXT,
                "first name"	TEXT,
                "last name"	TEXT,
                "suffix"	TEXT,
                "tel"	TEXT,
                "email"	TEXT,
                PRIMARY KEY("key" AUTOINCREMENT)
                )"""
        )
        # Create Brand Table
        cur.execute(
            """CREATE TABLE "brands" (
            "key"   INTEGER,
            "brand" TEXT,
            "code"  TEXT,
            PRIMARY KEY("key" AUTOINCREMENT)
            )"""
        )

def add_item():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO "main"."item"
("upc", "item number", "desc", "size", "units", "alt desc", "disc", "new item")
VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",
(item.get_upc(),item.get_num(),item.get_descript_display(),item.get_size(),item.get_units(),item.get_descript_alt,False,-1)
        )

def add_store():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO "main"."store"
                ("name","number","address 1","address 2","city","state","zip","tel","fax","other")
                VALUES (?,?,?,?,?,?,?,?,?,?);""",
                (store.get_name(),store.get_number(),store.get_add1(),store.get_add2(),store.get_city(),store.get_state(),store.get_zip(),store.get_tel(),store.get_tel(),store.get_fax(),store.get_other())
        )

def brand_check(upc:str):
    from _global import auto_brand_lookup
    if auto_brand_lookup == False or len(upc) != 11:
        return ''
    lookup = upc[:6]
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        try:
            brand = cur.execute(
            """SELECT "brand" FROM "brands" WHERE "code" = ?""",(lookup)
            )
        except:
            return ''
        else:
            return brand

def add_brand(brand:str,upc:str):
    brand_code = upc[:6]
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("""INSERT INTO "main"."brand" VALUES(?,?)"""),()