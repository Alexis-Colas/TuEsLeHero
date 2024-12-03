from flask import Flask, render_template, redirect, g, request
import pymysql.cursors

app = Flask(__name__)


@app.route('/')
def show_layout():
    return render_template('layout.html')

#-------------------------------------------------------------------------------#

@app.route('/page/show')
def show_page():
    return render_template('page/page_show.html')

#-------------------------------------------------------------------------------#

@app.route('/livre/show')
def show_livre():
    return render_template('livre/livre_show.html')

#-------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()
