##FIZZBUZZ
### Prerequisites for linux
1. Make sure your system has Python 2.7.14. Setup instruction is [here](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)
1. Install pip and virtualenv from [here](https://docs.python.org/2/installing/index.html)

### Setup for Developers running linux
1. Clone the project `git clone https://github.com/Anjali05/fizz-buzz.git`.
1. cd into fizz-buzz
1. Activate virtualenv and install flask:
    1. virtualenv <virtual_env_name>. eg virtualenv venv
    1. . venv/bin/activate (if virtual_env_name = venv)
    1. pip install Flask
1. Run the project `flask run --host=0.0.0.0 --port=34232`. Navigate to http://localhost:34232/fizzbuzz/<num> to try it out.
1. Deactivate your virtual env by running `deactivate`.
