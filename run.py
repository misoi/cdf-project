#!flask/bin/python
from app import app


# helps flask know which environment its in
#p.config.from_object(os.environ['APP_SETTING'])

if __name__ == '__main__':
	

	app.run(debug=True)

    

from app import views


