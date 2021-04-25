from flask import Flask, redirect, url_for
from flask import render_template
from forms import NewForm, EditForm

app = Flask(__name__)
SECRET_KEY = "notSoSecretKey"
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    return render_template(
        "home.jinja2",
        title="Actor's and their Oscars",
        description="Details about actors and what age they were awarded an Oscar."
    )


if __name__ == '__main__':
    app.run(debug=True)
