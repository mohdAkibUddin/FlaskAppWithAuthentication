from flask import Flask, request, Response, redirect, url_for
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import simplejson as json


app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)
app.config['SECRET_KEY'] = "XXXXXXXXXXXXXX"
app.config['MYSQL_DATABASE_HOST'] = "db"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "password"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = "oscarsData"
mysql.init_app(app)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/actors', methods=['GET'])
@app.route('/index/', methods=['GET'])
@app.route('/home/', methods=['GET'])
@app.route('/actors/', methods=['GET'])
def home():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM oscar_winning_actors")
    result = cursor.fetchall()
    return render_template(
        "home.jinja2",
        title="Actor's and their Oscars",
        description="Details about actors and what age they were awarded an Oscar.",
        actors=result
    )


@app.route("/actors/view/<int:actor_id>", methods=["GET"])
@app.route("/actors/view/<int:actor_id>/", methods=["GET"])
def view_actor(actor_id):
    cursor = mysql.get_db().cursor()
    sql_select_query = """SELECT * FROM oscar_winning_actors WHERE actorID = %s"""
    cursor.execute(sql_select_query, actor_id)
    result = cursor.fetchall()[0]
    return render_template(
        "view.jinja2",
        title="View Actor Information",
        description="View of single actor and their oscar information",
        actor=result
    )


@app.route('/actors/new', methods=['GET'])
@app.route('/actors/new/', methods=['GET'])
def insert_actor_form():
    return render_template('new.jinja2', title='New Actors Form')


@app.route("/actors/new", methods=["POST"])
@app.route("/actors/new/", methods=["POST"])
def insert_actor():
    cursor = mysql.get_db().cursor()
    input_data = (request.form.get('name'), request.form.get("movie"), request.form.get("age"), request.form.get("year"))
    sql_insert_query = """INSERT INTO oscar_winning_actors (name, movie, age, year) VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, input_data)
    mysql.get_db().commit()
    return redirect(url_for("home"), code=302)


@app.route('/actors/edit/<int:actor_id>', methods=['GET'])
@app.route('/actors/edit/<int:actor_id>/', methods=['GET'])
def edit_actor_form(actor_id):
    cursor = mysql.get_db().cursor()
    sql_select_query = "SELECT * FROM oscar_winning_actors WHERE actorID=%s"
    cursor.execute(sql_select_query, actor_id)
    result = cursor.fetchall()
    return render_template('edit.jinja2', title='View Form', actor=result[0])


@app.route('/actors/edit/<int:actor_id>', methods=['POST'])
@app.route('/actors/edit/<int:actor_id>/', methods=['POST'])
def edit_actor(actor_id):
    cursor = mysql.get_db().cursor()
    input_data = (request.form.get('name'), request.form.get("movie"), request.form.get("age"), request.form.get("year"), actor_id)
    sql_update_query = """UPDATE oscar_winning_actors SET name = %s, movie = %s, age = %s, year = %s WHERE actorID = %s"""
    cursor.execute(sql_update_query, input_data)
    mysql.get_db().commit()
    return redirect(url_for("home"), code=302)


@app.route('/actors/delete/<int:actor_id>/', methods=['POST'])
@app.route('/actors/delete/<int:actor_id>/', methods=['POST'])
def delete_actor(actor_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM oscar_winning_actors WHERE actorID = %s """
    cursor.execute(sql_delete_query, actor_id)
    mysql.get_db().commit()
    return redirect(url_for("home"), code=302)


@app.route('/api/actors', methods=['GET'])
@app.route('/api/actors/', methods=['GET'])
def api_view_all_records() -> Response:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM oscar_winning_actors')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    response = Response(json_result, status=200, mimetype='application/json')
    return response


@app.route('/api/actors/<int:actor_id>', methods=['GET'])
@app.route('/api/actors/<int:actor_id>/', methods=['GET'])
def api_view_record(actor_id) -> Response:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM oscar_winning_actors WHERE actorID =%s', actor_id)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    response = Response(json_result, status=200, mimetype='application/json')
    return response


@app.route('/api/actors', methods=['POST'])
@app.route('/api/actors/', methods=['POST'])
def api_add_record() -> Response:
    content = request.json
    cursor = mysql.get_db().cursor()
    input_data = (content['name'], content['movie'], content['age'], content['year'])
    sql_insert_query = """INSERT INTO oscar_winning_actors (name, movie, age, year) VALUES (%s, %s,%s, %s)"""
    cursor.execute(sql_insert_query, input_data)
    mysql.get_db().commit()
    response = Response(status=201, mimetype='application/json')
    return response


@app.route('/api/actors/<int:actor_id>', methods=['PUT'])
@app.route('/api/actors/<int:actor_id>/', methods=['PUT'])
def api_update_record(actor_id) -> Response:
    content = request.json
    cursor = mysql.get_db().cursor()
    input_data = (content['Name'], content['Movie'], content['Age'], content['Year'], content['Index'])
    sql_update_query = """UPDATE oscar_winning_actors SET name = %s, movie = %s, age = %s, year = %s WHERE actorID = %s"""
    cursor.execute(sql_update_query, input_data)
    mysql.get_db().commit()
    response = Response(status=201, mimetype='application/json')
    return response


@app.route('/api/actors/<int:actor_id>', methods=['DELETE'])
@app.route('/api/actors/<int:actor_id>/', methods=['DELETE'])
def api_delete_record(actor_id) -> Response:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM oscar_winning_actors WHERE actorID = %s"""
    cursor.execute(sql_delete_query, actor_id)
    mysql.get_db().commit()
    response = Response(status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
