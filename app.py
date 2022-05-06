from flask import Flask, render_template, request, redirect,  url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)



# MYSQL Connection
app.config['MYSQL_HOST'] = 'webdav-keylor-db.alwaysdata.net'
app.config['MYSQL_USER'] = 'keylor-db'
app.config['MYSQL_PASSWORD'] = '*KylR2407*'
app.config['MYSQL_DB'] = 'keylor-db_kfeend'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

# Route

@app.route('/')
def Home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tipo_local')
    data = cur.fetchall()
    return render_template('pag_principal.html', locals=data)


#@app.route('/test/<name>')
#def test(id):
 #   cur = mysql.connection.cursor()
  #  cur.execute('SELECT * FROM info_locales WHERE id = %s', (id))
   # data = cur.fetchall()
    #return render_template('perfiles.html', local=data[0])


@app.route('/tipo_local/<id>')
def Tipo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM info_locales WHERE tipo_local = %s', [id])
    data = cur.fetchall()
    return render_template('tipo_local.html', locals=data)

@app.route('/local/<id>')
def Perfil(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM info_locales WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('perfiles.html', locals=data)


@app.route('/register')
def register():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM register')
    data = cur.fetchall()
    return render_template('register.html', registers=data)


@app.route('/new_register', methods=['POST'])
def new_register():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO register (user, email, password) 
                             VALUES (%s, %s, %s)''',
                    (user, email, password))
        mysql.connection.commit()
        flash('Registro exitoso')

        return redirect(url_for('Home'))


@app.route('/añadir_local')
def añadir_local():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM info_locales')
    data = cur.fetchall()
    return render_template('add_local.html', local=data)


@app.route('/nuevo_local', methods=['POST'])
def nuevo_local():
    if request.method == 'POST':
        name = request.form['name']
        image = request.form['image']
        description = request.form['description']
        link_1 = request.form['link_1']
        link_2 = request.form['link_2']
        link_3 = request.form['link_3']
        phone_number = request.form['phone_number']
        tipo_local = request.form['tipo_local']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO info_locales (name, image, description, 
                        link_1, link_2, link_3, phone_number, tipo_local) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                    (name, image, description, link_1, link_2, link_3, phone_number, tipo_local))
        mysql.connection.commit()
        flash('Local agregado exitosamente')

        return redirect(url_for('Home'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
