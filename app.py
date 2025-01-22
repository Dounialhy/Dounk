from flask import Flask, request, render_template

# Initialize Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<username>', methods=['GET', 'POST'])
def user_profile(username):
    if request.method == 'POST':
        return f'Hello, {username}! Your profile has been updated.'
    else:
        return f'Hello, {username}! This is your profile page.'

if __name__ == '__main__':
    app.run(debug=True)