from flask import Blueprint, render_template, redirect, url_for
import Application.forms as forms

routes_blueprint = Blueprint(
    "routes_blueprint",
    __name__,
    template_folder="templates"
)


@routes_blueprint.route("/")
@routes_blueprint.route("/index/")
@routes_blueprint.route("/home/")
def home():
    return render_template(
        "home.jinja2",
        title="Actor's and their Oscars",
        description="Details about actors and what age they were awarded an Oscar."
    )


@routes_blueprint.route("/actors/new/", methods=["GET", "POST"])
def insert_actor():
    form = forms.NewForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template(
        "new.jinja2",
        title="New Actor",
        description="Insert an actor into the database",
        form=form,
        template="form-template"
    )


@routes_blueprint.route("/actors/edit/<int:actor_id>", methods=["GET", "POST"])
def edit_actor(actor_id):
    form = forms.EditForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template(
        "edit.jinja2",
        title="Edit Actor",
        description="Complete this form to update actor information",
        form=form,
        template="form-template"
    )


@routes_blueprint.route("/actors/view/<int:actor_id>", methods=["GET"])
def view_actor(actor_id):
    return render_template(
        "view.jinja2",
        title="View Actor Information",
        description="View of single actor and their oscar information"
    )
