# Quality over quantity (qoq)
Quality over Quantity, provides an easy way to link and overview Github projects with Circle CI builds. With such stats we review the quality state over time per branch.

Further data agreggation between Github and CircleCi could show estimates of time and effort spent across projects/repositories within an organisation.

# Pre-requisites
* Active Github account / Active CircleCI account
* python 3.7 / pip
* pyenv (optional, recommended).

* Build pipeline
By default the service uses Circle Ci to run builds for every commit pushed to the repository on any branch.

# Using the service locally

Its recommended to use virtual environments to avoid polluting your local machine.

1. Create virtual environment ```python -m venv venv```
2. Activate the virtual environment ```source venv/bin/activate``` 
3. Install dependencies ```pip install -r requirements.txt```
4. Run the service ```FLASK_APP='qoq' FLASK_ENV='development' flask run```

The service provides a few links:
1. API Documentation: http://127.0.0.1:5000/api
2. Home page: http://127.0.0.1:5000








