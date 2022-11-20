import os
import json

from flask import Flask, request, abort, redirect

app = Flask(__name__)

config = {
    'DATABASE_URI': os.environ.get('DATABASE_URI', ''),
    'HOSTNAME': os.environ['HOSTNAME'],
    'GREETING': os.environ.get('GREETING', 'Hello'),
}

from sqlalchemy import create_engine
engine = create_engine(config['DATABASE_URI'], echo=True)

@app.route("/user", methods=["POST"])
def add_user():
    request_data = request.get_json()
    user_name = request_data['userName']
    first_name = request_data['firstName']
    last_name = request_data['lastName']
    email = request_data['email']
    phone = request_data['phone']
    
    try:
        with engine.connect() as connection:
            result = connection.execute(
                """
                insert into users (user_name, first_name, last_name, email, phone)
                values ('{}', '{}', '{}', '{}', '{}') returning id;
                """.format(user_name, first_name, last_name, email, phone)).first()
            id_ = result['id']
        return {"id": id_}
    except Exception as ex:
        abort(400, "Endpoint: /user, Method: get. Error:{}".format(str(ex)))

def get_user_from_db(user_id):
    rows = []
    try:
        with engine.connect() as connection:
            result = connection.execute(
                """
                select id, user_name, first_name, last_name, email, phone from users 
                where id={} limit 1;
                """.format(user_id))
            rows = [dict(r.items()) for r in result]
        return rows
    except Exception as ex:
        abort(400, "Get user from DB with id = {str(user_id)}. Error:{str(ex)}")

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    rows = get_user_from_db(user_id)

    data = {}
    if rows:
        data['id'] = rows[0]['id']
        data['userName'] = rows[0]['user_name']
        data['firstName'] = rows[0]['first_name']
        data['lastName'] = rows[0]['last_name']
        data['email'] = rows[0]['email']
        data['phone'] = rows[0]['phone']

    return data

@app.route("/user/<user_id>", methods=["PUT"])
def put_user(user_id):
    request_data = request.get_json()
    rows = get_user_from_db(user_id)

    user_name = request_data.get('userName', rows[0]['user_name'])
    first_name = request_data.get('firstName', rows[0]['first_name'])
    last_name = request_data.get('lastName', rows[0]['last_name'])
    email = request_data.get('email', rows[0]['email'])
    phone = request_data.get('phone', rows[0]['phone'])

    try:
        with engine.connect() as connection:
            sql_request = """
                update users set user_name = '{}', first_name = '{}', last_name = '{}', email = '{}', phone = '{}' 
                where id = {} returning *;
                """.format(user_name, first_name, last_name, email, phone, user_id)
            result = connection.execute(sql_request).first()
    except Exception as ex:
        abort(400, "Endpoint: /user/user_id, Method: put. Error: {}".format(str(ex)))

    return "User updated"

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        with engine.connect() as connection:
            result = connection.execute("delete from users where id = {}".format(user_id))

        return "User deleted"
    except Exception as ex:
        abort(400, "Endpoint: /user/user_id, Method: delete. Error:{}".format(str(ex)))

@app.route('/db')
def db():
    rows = []
    with engine.connect() as connection:
        result = connection.execute("select id, user_name, first_name, last_name, email, phone from users;")
        rows = [dict(r.items()) for r in result]
    return json.dumps(rows)

@app.route("/")
def hello():
    return config['GREETING'] + ' from ' + config['HOSTNAME'] + '!'

@app.route("/config")
def configuration():
    return json.dumps(config)


@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', debug=True)
