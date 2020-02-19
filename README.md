# Quality over quantity (qoq)
Quality over Quantity, provides an easy way to link and overview Github projects with Circle CI builds. With such stats we review the quality state over time per branch.

Further data agreggation between Github and CircleCi could show estimates of time and effort spent across projects/repositories within an organisation.

# Pre-requisites
* Active Github account and personal access token: For more information ```https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line#creating-a-token``` 
* Active Circle Ci account and token available, for more information ```https://circleci.com/docs/2.0/managing-api-tokens/#creating-a-personal-api-token``` 
* Python 3.7 / pip
* pyenv (optional, recommended).

# Build pipeline
By default the service uses Circle Ci to run builds for every commit pushed to the repository on any branch. 
Review the file located in ```.circleci/config.yml``` 

Given the repository is public you can also review the build pipeline here ```https://circleci.com/gh/griojas/quality-over-quantity```


# Set up the project

Its recommended to use virtual environments to avoid polluting your local machine.

1. Create virtual environment ```python -m venv venv```
2. Activate the virtual environment ```source venv/bin/activate``` 
3. Install dependencies ```pip install -r requirements.txt```
4. Run the service ```FLASK_APP='qoq' FLASK_ENV='development' flask run```

The service provides a few links:
1. API Documentation: http://127.0.0.1:5000/api
2. Home page: http://127.0.0.1:5000

# Tests

There are a few basic functional tests, unit test are not included in this challenge.
In order to run your tests locally make sure the environment variables ```VCS_TOKEN``` and ```CI_TOKEN``` are available in your host and contain valid tokens. For more details see the "Pre-requisites" section.

Once you are ready run the command: ```coverage run -m pytest -v``` 







