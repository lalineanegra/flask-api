# Basic Flask API

## 3. Basic POST request and database saving

### Local setup

- Download repo with git clone <repo-url>
- Create a virtual environment with called 'env' with: python3 -m env env
- Activate virtual environment with: source env/bin/activate
- Download dependencies with: pip install -r requirements.txt
- Create basic sqlite database: enter the python interpreter with: python3
- Type: from src.main import db
- Type: db.create_all()  (this will create a db file with the columns specified in the defined User model)
- Exit with: exit()

#### Add user

- run the server with: python3 src/main.py
- Make a POST request (using Postman) to http://localhost:5000/user 
- The server should respond with the saved user
