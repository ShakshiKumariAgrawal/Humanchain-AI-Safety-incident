from flask import Flask, request, jsonify, abort
from flask import send_from_directory
from models import Incident
from database import db

ALLOWED_SEVERITIES = ["Low", "Medium", "High"]

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    @app.route('/', methods=['GET'])
    def serve_home():
        return send_from_directory('static', 'index.html')
    def home():
        return jsonify({"message": "Welcome to the HumanChain AI Safety Incident API"}), 200

    with app.app_context():
        db.create_all()
        # Optional: Prepopulate database if empty
        if not Incident.query.first():
            sample_incidents = [
                Incident(title="AI Chatbot went rogue", description="The chatbot started generating offensive content.", severity="High"),
                Incident(title="Self-driving car hesitation", description="Car froze unexpectedly at a green light.", severity="Medium"),
                Incident(title="Recommendation system bias", description="Product recommendations were heavily biased.", severity="Low"),
            ]
            db.session.bulk_save_objects(sample_incidents)
            db.session.commit()

    @app.route('/incidents', methods=['GET'])
    def get_incidents():
        incidents = Incident.query.all()
        return jsonify([incident.to_dict() for incident in incidents]), 200

    @app.route('/incidents', methods=['POST'])
    def create_incident():
        data = request.get_json()

        if not data:
            abort(400, description="Request must be JSON.")

        title = data.get('title')
        description = data.get('description')
        severity = data.get('severity')

        if not title or not description or not severity:
            abort(400, description="Missing required fields: title, description, severity.")

        if severity not in ALLOWED_SEVERITIES:
            abort(400, description=f"Severity must be one of {ALLOWED_SEVERITIES}.")

        new_incident = Incident(title=title, description=description, severity=severity)
        db.session.add(new_incident)
        db.session.commit()

        return jsonify(new_incident.to_dict()), 201

    @app.route('/incidents/<int:incident_id>', methods=['GET'])
    def get_incident(incident_id):
        incident = Incident.query.get(incident_id)
        if not incident:
            abort(404, description="Incident not found.")
        return jsonify(incident.to_dict()), 200

    @app.route('/incidents/<int:incident_id>', methods=['DELETE'])
    def delete_incident(incident_id):
        incident = Incident.query.get(incident_id)
        if not incident:
            abort(404, description="Incident not found.")

        db.session.delete(incident)
        db.session.commit()
        return jsonify({"message": f"Incident {incident_id} deleted successfully."}), 200

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(error=str(error)), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error=str(error)), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
