from flask import Flask, jsonify
from controllers.employee_controller import employee_bp

app = Flask(__name__)
app.secret_key = "lab2_employee_secret_key_2026"
app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return '<h2>Aplikasi Employee</h2><p><a href="/employees/new">Buka pengelolaan employee</a></p>'

if __name__ == "__main__":
    app.run(debug=True)
