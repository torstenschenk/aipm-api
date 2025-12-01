# API Fundamentals and Design Labs

Practice core API concepts and design principles in three small Jupyter notebooks.

## Contents
- [01_API_Fundamentals.ipynb](01_API_Fundamentals.ipynb) : Introduction to APIs, HTTP methods (GET, POST), status codes, and consuming APIs with `requests`.
- [02_FastAPI_Intro.ipynb](02_FastAPI_Intro.ipynb) : Introduction to FastAPI, creating your first API, Path/Query parameters, and Swagger UI.
- [03_FastAPI_CRUD.ipynb](03_FastAPI_CRUD.ipynb) : Building a complete CRUD API (Create, Read, Update, Delete) with FastAPI and Pydantic models.
- [main.py](main.py) : A ready-to-run FastAPI app that mirrors the CRUD notebook (root health check, create/read/update/delete/search tasks). Start it with `uvicorn main:app --reload` from this folder and open `http://127.0.0.1:8000/docs` to explore the endpoints.

## Why we ship a dedicated `main.py`

Running an API requires a long-lived server process that can be invoked by an ASGI server such as `uvicorn`. While the notebooks walk through the concepts step by step, they are not an ideal place to keep a production-ready app: cells run in isolation, state is lost between executions, and there is no stable entry point for tooling, deployment, or automated tests. The standalone `main.py` file solves this by collecting the FastAPI app, routes, and data models in one importable module so that any environment (local dev, Docker, CI) can start the service with a single command (`uvicorn main:app --reload`). Keeping the app in a Python file also forces us to respect Python packaging conventions, ensures type-checkers and linters can analyze the code, and mirrors how APIs are structured in real-world projects.

### Key Terms
- **ASGI (Asynchronous Server Gateway Interface)**: A standard interface between web servers and Python web applications or frameworks. It allows for asynchronous capabilities (like handling many connections at once), which is essential for modern, high-performance APIs like those built with FastAPI.
- **Uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`. It is the program that actually runs your FastAPI application, listening for incoming HTTP requests and passing them to your code.
- **CI (Continuous Integration)**: A software development practice where code changes are automatically built, tested, and prepared for release. In a CI pipeline, automated scripts need to be able to start your API and run tests against it without human intervention, which is much easier with a standard python file than a notebook.

## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. For this purpose you can use the following commands:

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the hands-on ml notebooks.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file. M1/Apple Silicon issues.*

### **`macOS`** or `Linux` type the following commands : 

- Install the virtual environment and the required packages by following commands:

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
### **`Windows`** type the following commands :

- Install the virtual environment and the required packages by following commands.

For `PowerShell` CLI :

```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For `Git-bash` CLI :
  
```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
**`Note:`**
If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

```Bash
python.exe -m pip install --upgrade pip
```
