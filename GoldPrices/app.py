from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)


def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=Neki;'
            'DATABASE=GoldPrices;'
            'UID=sa;'
            'PWD=2402'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def get_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM GoldPrices")
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()


@app.route('/table')
def show_table():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM GoldPrices")
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return render_template('inde.html', columns=columns, data=data)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()


@app.route('/chart')
def show_chart():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Could not connect to the database."})

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Metal, Currency, Exchange, Open_Price, Low_Price, High_Price FROM GoldPrices")
        rows = cursor.fetchall()

        metals = [row.Metal for row in rows]
        currencies = [row.Currency for row in rows]
        exchanges = [row.Exchange for row in rows]
        open_prices = [row.Open_Price for row in rows]
        low_prices = [row.Low_Price for row in rows]
        high_prices = [row.High_Price for row in rows]

        return render_template('chart.html',
                               metals=metals,
                               currencies=currencies,
                               exchanges=exchanges,
                               open_prices=open_prices,
                               low_prices=low_prices,
                               high_prices=high_prices)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
