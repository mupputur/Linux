import os
import sqlite3
import requests
path = os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default'
files = os.listdir(path)
history_db = os.path.join(path, 'history')
con = sqlite3.connect(history_db)
cursor = con.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)
results = cursor.fetchall()
#print(results)

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