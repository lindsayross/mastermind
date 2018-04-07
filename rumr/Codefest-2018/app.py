from flask import Flask, request, jsonify, render_template
import cf_deployment_tracker
import os, json
from cloudant import Cloudant
import db_controller

cf_deployment_tracker.track()

app = Flask(__name__)

db_name = 'rumr'
client = None
db = None

port = int(os.getenv('PORT', 8000))

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found vcap services')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local vcap_services')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

@app.route('/rumr/api/users', methods=['GET'])
def get_users():
    if client:
        return jsonify(db_controller.get_users(db))
    else:
        print('No database')
        return jsonify([])

@app.route('/rumr/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    if client:
        return jsonify(db_controller.get_user(db, user_id))
    else:
        print('No database')
        return jsonify([])

@app.route('/rumr/api/users', methods=['POST'])
def put_user():
    user = request.json
    return db_controller.put_user(db, user)
    #  if client:
    #      db.create_document(data)
    #  else:
    #      print('No database')
    #      return jsonify([])

@app.route('/rumr/api/match/<string:user_id>', methods=['GET'])
def get_matches(user_id):
    matches = db_controller.get_matches(db, user_id)
    return jsonify(matches)

#  @app.route('/rumr/api/users/<int:user_id>', methods=['PUT'])
#  def update_user(user_id):
#      update = request.json
#      db_controller.update_user(db, user_id, update)
#      return get_user(user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)












