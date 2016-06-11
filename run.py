#!flask/bin/python
from app import app

# helps flask know which environment its in
import OS
app.config.from_object(os.environ['APP_SETTING'])

if __name__ == '__main__':
	unittest.main()

    app.run()

from app import views


