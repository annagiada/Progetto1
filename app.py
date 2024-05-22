from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config.from_object('config.Config')

def create_db_connection():
    db_config = {
        'host': app.config['MYSQL_HOST'],
        'user': app.config['MYSQL_USER'],
        'password': app.config['MYSQL_PASSWORD'],
        'database': app.config['MYSQL_DB']
    }
    return mysql.connector.connect(**db_config)

def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

#___________________________________________________________________________________________________________
# Lista di esempio di 1323 artisti
artists =  [execute_query('SELECT * FROM artist')]
artists_per_page = 20


#___________________________________________________________________________
@app.route('/')
def home():
    
    return render_template('home.html')


@app.route('/artisti')
def artisti():
    artisti = execute_query('SELECT * FROM artist')
    return render_template('artisti.html', artisti=artisti)


@app.route('/opere')
def opere():
    return render_template('opere.html')

@app.route('/artisti/opere')
def opere_artisti():
    artista = request.args.get('artista')
    return render_template('opere_artisti.html')


if __name__ == '__main__':
    app.run(debug=True)