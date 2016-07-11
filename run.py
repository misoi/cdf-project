
from app import app
import models
PORT = 5000

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=PORT)