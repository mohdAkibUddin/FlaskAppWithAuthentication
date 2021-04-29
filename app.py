from flask import Flask, redirect, url_for
from flask import render_template
from forms import NewForm, EditForm

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
@app.route("/index/")
@app.route("/home/")
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


@app.route("/actors/edit/<int:actor_id>", methods=["GET", "POST"])
def edit_actor(actor_id):
    form = EditForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template(
        "edit.jinja2",
        title="Edit Actor",
        description="Complete this form to update actor information",
        form=form,
        template="form-template"
    )


@app.route("/actors/view/<int:actor_id>", methods=["GET"])
def view_actor(actor_id):
    return render_template(
        "view.jinja2",
        title="View Actor Information",
        description="View of single actor and their oscar information"
    )


@app.route("/api/actors/", methods=["GET"])
def api_view_all_records() -> str:
    pass


@app.route("/api/actors/<int:actor_id>/", methods=["GET"])
def api_view_record(actor_id) -> str:
    pass


@app.route("/api/actors/", methods=["POST"])
def api_add_record() -> str:
    pass


@app.route("/api/actors/<int:actor_id>/", methods=["PUT"])
def api_update_record(actor_id) -> str:
    pass


@app.route("/api/actors/<int:actor_id>/", methods=["DELETE"])
def api_delete_record(actor_id) -> str:
    pass


if __name__ == '__main__':
    app.run()
