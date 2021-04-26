from flask import Blueprint

api_blueprint = Blueprint(
    "api_blueprint",
    __name__
)


@api_blueprint.route("/api/actors/", methods=["GET"])
def api_view_all_records() -> str:
    pass


@api_blueprint.route("/api/actors/<int:actor_id>/", methods=["GET"])
def api_view_record(actor_id) -> str:
    pass


@api_blueprint.route("/api/actors/", methods=["POST"])
def api_add_record() -> str:
    pass


@api_blueprint.route("/api/actors/<int:actor_id>/", methods=["PUT"])
def api_update_record(actor_id) -> str:
    pass


@api_blueprint.route("/api/actors/<int:actor_id>/", methods=["DELETE"])
def api_delete_record(actor_id) -> str:
    pass
