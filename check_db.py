import sqlite3

conn = sqlite3.connect('sanskrit_engine.db')
cursor = conn.cursor()
cursor.execute("SELECT text_sa, pada_sa FROM gita_verses WHERE id = '1:1'")
row = cursor.fetchone()

print("\n--- DATABASE DIAGNOSTIC FOR 1:1 ---")
if row:
    print(f"1. text_sa (The Clean Array): {row[0]}")
    print(f"2. pada_sa (The Numbered String): {row[1]}")
else:
    print("Verse 1:1 not found in database!")
print("-----------------------------------\n")