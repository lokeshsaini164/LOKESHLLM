import csv
import os
import mysql.connector

"""This function first connect my-sql server fetch the records and write this to csv file"""

def db_conn_write_csv():
    file = "db3.csv"
    if os.path.exists(file):
        print("file exists")
    conn = mysql.connector.connect(host="localhost",database="rahulshettyacademy",user="Lokesh",password="AI_learn@12345")
    print(conn.is_connected())
    cursor = conn.cursor()
    cursor.execute("use rahulshettyacademy;")
    cursor.execute("select * from Customers")
    row= cursor.fetchall()
    # 1. Check if file exists and has content
    if os.path.exists(file) and os.path.getsize(file) > 0:
        #Open in read/append binary mode to check the absolute last character safely
        with open(file, "rb+") as file:
            file.seek(-1, os.SEEK_END)
            last_char = file.read(1)
            # If the last character is NOT a newline, inject one manually
            if last_char != b"\n":
                file.write(b"\n")
    with open("db3.csv", "a", newline="\n", encoding="utf-8") as myfile:
        writer = csv.writer(myfile)
        for row1 in row:
            writer.writerow(row1)
