from flask import (
    Flask,
    render_template)


# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create URL route in our application for "/"
@app.route("/")
def home():

    """
    This function just responds to browser URL localhost:5000/

    :return         the render template 'home.html'
    """
    return render_template('home.html')


# If we'r running on the standalone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
