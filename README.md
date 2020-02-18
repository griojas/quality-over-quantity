# Quality over quantity (qoq)
Quality over Quantity, provides a 360 overview of the design and development effort

# Pre-requisites
* python 3.7 / pip
* sqlite
* pyenv (optional, recommended).

* Build pipeline
By default the service uses Circle Ci to run builds for every commit pushed to the repository.

# Using the service locally

Its recommended to use virtual environments to avoid polluting your local machine.

1. Create virtual environment ```python -m venv venv```
2. Activate the virtual environment ```source venv/bin/activate``` 
3. Install dependencies ```pip install -r requirements.txt```
4. Run the service ```FLASK_APP='qoq' FLASK_ENV='development' flask run```

By default the service provides:
1. API Documentation: http://127.0.0.1:5000/api
2. Home page: http://127.0.0.1:5000








