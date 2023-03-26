from flask import Flask, render_template

app = Flask('UniqueStudio')


# Index/Home Page
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', title='Unique Studio')


# Clients Page
@app.route('/clients/')
def clients():
    return render_template('clients.html', title='Clients')


# Calendar Page
@app.route('/calendar/')
def calendar():
    return render_template('calendar.html', title='Calendar')

@app.errorhandler(404)
def page_not_found(e):
    """Catch inexistent routes"""
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
