import pyodbc

server = "192.168.1.5\SQLEXPRESS"
username = "sa"
password = "taiyo3553"
dbname = "IoTtest"

#接続文字列の組み立て
conn_str = "DRIVER={SQL Server};SERVER=" + server + \
    ";uid=" + username + \
    ";pwd=" + password + \
    ";DATABASE=" + dbname
#データベースへ接続
print("接続")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

table_name = "T_製品名変換"

# データ取得
rows = cursor.execute(f"SELECT 製品名_成形機,製品ID FROM {table_name}").fetchall()

for row in rows:
    print(row)