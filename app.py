from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure your MySQL connection
db = mysql.connector.connect(
    host=" sql8.freesqldatabase.com ",
    user=" sql8673726",
    password="xWplLT4LMV",
    database="sql8673726"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    typegroup = request.form.get('typegroup')
    gender = request.form.get('gender')

    # Insert data into the database
    sql = "INSERT INTO users (Name, Email, Mobile, Typegroup, Gender) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, mobile, typegroup, gender)
    cursor.execute(sql, values)

    # Commit the changes
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    return render_template('submit.html')

if __name__ == '__main__':
    app.run(port=5000)
