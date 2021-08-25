import os
import sqlite3
import requests
path = os.path.expanduser('~')+r'\AppData\Roaming\Mozilla\Firefox\Profiles\4h7w3w2n.default-release'
files = os.listdir(path)
history_db = os.path.join(path, 'places.sqlite')
con = sqlite3.connect(history_db)
cursor = con.cursor()
select_statement = "SELECT * from moz_places;"
cursor.execute(select_statement)
results = cursor.fetchall()
for r in results:
    print(r)
def url_ok(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e
print(url_ok("https://www.geeksforgeeks.org/test-the-given-page-is-found-or-not-on-the-server-using-python/"))