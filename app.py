from flask import Flask, render_template, redirect, g, request
import pymysql.cursors
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

def cursorSQL(sql, tuple=()):
    mycursor = get_db().cursor()
    mycursor.execute(sql, tuple)
    return mycursor.fetchall()

def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost", # à modifier
            user="alexis", # à modifier
            password="Samsung21C!", # à modifier
            database="BDD_alexis", # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_layout():
    return render_template('layout.html')

#-------------------------------------------------------------------------------#

@app.route('/page/show')
def show_page():
    id = request.args.get('id', 1)
    sql = '''   SELECT * FROM destination
                JOIN page ON destination.page_d = page.id_page
                WHERE page.num_livre=%s
                ORDER BY num_page;
                '''
    pages = cursorSQL(sql, id)
    return render_template('page/page_show.html', pages=pages)

#-------------------------------------------------------------------------------#

@app.route('/livre/show')
def show_livre():
    sql = '''   SELECT * FROM livre
                ORDER BY livre.nom_livre;
                '''
    livres = cursorSQL(sql)

    return render_template('livre/livre_show.html', livres=livres)

#-------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()
