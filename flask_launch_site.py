# Import the necessary libraries
from flask import Flask, render_template, request, redirect
import sqlite3, re

# Create the Flask application
app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the countdown timer page
@app.route('/timer')
def timer():
    return render_template('timer.html')


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# Define the email subscription page
@app.route('/subscribe', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if validate_email(email):
            conn = sqlite3.connect('emails.db')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS emails (email text)')
            c.execute('INSERT INTO emails (email) VALUES (?)', (email,))
            conn.commit()
            conn.close()
            return 'Email added successfully!'
        else:
            return 'Email address is required.'
    else:
        return render_template('index.html')


# Start the application
if __name__ == '__main__':
    app.run(debug=True)
