<h1 align="center">

  <a href="https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3">
    <img  src="readme/DigitalOcean.png" alt="digitalocean" width="200">
  </a>

  <br>
   Simple blog
  <br>

</h1>

<h4 align="center">
    <br>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3"
      target="_blank">
      How To Make a Web Application Using Flask in Python 3
    </a>
</h4>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![DigitalOcean](https://img.shields.io/badge/DigitalOcean-tutorual-green)](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)

</div>
<hr>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-use">How To Use</a>
</p>


## Features
* Simple blog 
  - add, update and viewing posts in blog


## Tech stack
- [Flask](https://flask.palletsprojects.com/en/latest/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/index.html)


## How To Use
To clone and run this project, you'll need:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)


<details>
<summary>Step-by-step commands</summary>

1. Firstly clone repo
   ```bash
   git clone https://github.com/Kazzila/flask_blog
   ```

2. Move to working dir
   ```bash
   cd flask_blog
   ```
3. Settings Poetry
   ```bash
   poetry config virtualenvs.in-project true
   ```

4. Activate venv
   ```bash
   poetry shell
   ```

5. Install packages
   ```bash
   poetry install --no-dev
   ```

6. Add the FLASK_APP environment variable:
    ```bash
   export FLASK_APP=app
   ```

7. Add the FLASK_DEBUG environment variable for development mode:
    ```bash
   export FLASK_DEBUG=true
   ```

8. Init database:
    ```bash
   python main.py -idb
   ```

9. Run the Flask application:
    ```bash
   python main.py
   ```

10. Open url [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

</details>


<br>
<br>
<p align="center">
  <a href="https://github.com/Kazzila">GitHub</a> •
  <a href="https://kazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
