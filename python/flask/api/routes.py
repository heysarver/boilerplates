from . import api_blueprint

@api_blueprint.route('/endpoint1')
def api_endpoint1():
    return jsonify({"message": "API Endpoint 1"})
