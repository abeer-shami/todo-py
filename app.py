from flask import Flask, render_template, flash, redirect, url_for, request, logging
from wtforms import Form, StringField, TextAreaField, validators
from flask_mysqldb import MySQL

app = Flask (__name__)

# init MYSQL
mysql = MySQL(app)

# Config MySQL
app.config['MYSQL_HOST'] = 'mysql6001.site4now.net'
app.config['MYSQL_USER'] = 'a34cb1_todo'
app.config['MYSQL_PASSWORD'] = 'aroma123'
app.config['MYSQL_DB'] = 'db_a34cb1_todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key = 'UPDATETHISPART'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def task():
    return render_template('add.html')

# Task Form Class
class TaskForm(Form):
    name = StringField('Name')
    description = TextAreaField('Description')

# Add Article
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm(request.form)
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        name = form.name.data
        description = form.description.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO todotask(name, description) VALUES(%s, %s)",(name, description))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('the task created ', 'success')

        return redirect(url_for('add'))

    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug = True)
