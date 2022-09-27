from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('data.db')
    cur = conn.execute("SELECT * FROM sensors WHERE id=1")
    row = cur.fetchone()
    if int(row[1]) > 28:
        msg = "temperature is High"
    else:
        msg = "Normal"
    return render_template('home.html',row=row,msg=msg)

@app.route('/add/<t>/<h>')
def add_data(t,h):
    conn= sqlite3.connect("data.db")
    conn.execute("UPDATE sensors SET temp=?,humi=? WHERE id=?",(t,h,1))
    conn.commit()
    return ("Updated!")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=500)