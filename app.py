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


@app.route("/actors/new/", methods=["GET", "POST"])
def insert_actor():
    form = NewForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template(
        "new.jinja2",
        title="New Actor",
        description="Insert an actor into the database",
        form=form,
        template="form-template"
    )


if __name__ == '__main__':
    app.run(debug=True)
