from app import app
from app.master.views import app_bp

app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
