from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate username and password
        if len(password) >= 8 and password.isalnum():
            # In a real app, you'd save these details to a database.
            return redirect(url_for('success', username=username))
        else:
            return "Password must be at least 8 alphanumeric characters."

    return render_template('register.html')

# Route for the success page
@app.route('/success/<username>')
def success(username):
    return f"Welcome, {username}! You have successfully registered."

if __name__ == '__main__':
    app.run(debug=True)
