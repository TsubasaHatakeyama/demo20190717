import psycopg2

try:
    # PostgreSQLへ接続
    conn = psycopg2.connect("dbname='weatherdb' user='manager@demo-db<社員番号>' host='demo-db<社員番号>.postgres.database.azure.com' password='password' port='5432'")
    cur = conn.cursor()
    conn.set_isolation_level(0)

    # テーブルを空にする
    cur.execute('truncate table tenki')

    # CSVファイルを読み込む
    with open('tenki_data.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        # COPYの実行
        cur.copy_from(f, 'tenki', sep=',')
        # sep='区切り文字'

    conn.commit() #　コミット
    f.close()
    print( "Copy Complete!" )

except psycopg2.Error as e:
   print( "NG Copy error! ")
   print(  e.pgerror )