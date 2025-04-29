
# Orapy Back End

## Getting started

To make it easy for you to get started with GitHub, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files


```
cd existing_repo
git remote add origin https://github.com/osas-vn/orapy.git
git branch -M <branch>
git push -uf origin <branch>
```

## OraPy RESTful API

Setting for Debug with VSCode
_launch.json_

```
 {
  "version": "0.2.0",
 "configurations": [
 {
 "name": "FastAPI Debug",
 "type": "python",
 "request": "launch",
 "module": "uvicorn",
 "args": [
  "your_main_module:main",
  "--port", "5000",
  "--reload"
  ],
   "jinja": true,
  "justMyCode": true,
  "console": "integratedTerminal",
  "env": {
  "PYTHONPATH": "${workspaceFolder}",
   },
   }
  ]
  }
```

---

**Explaination**

- name: A descriptive name for the debug configuration (e.g., "FastAPI Debug").
- type: Set to "python" for Python debugging.
- request: Set to "launch" to start the application.
- module: Use uvicorn to run the FastAPI application.
- args: Arguments passed to uvicorn:
  - "your_main_module:app": Replace your_main_module with the name of your Python file (without .py) and app with the FastAPI instance (e.g., main:app if your file is main.py and the FastAPI instance is named app).
  - "--port": port of application want to use. (e.x: "--port", "5000" that is application use port 5000 )
  - "--reload": Enables auto-reloading when code changes (optional but useful during development).
- jinja: Set to true if you're using Jinja2 templates.
- justMyCode: Set to true to exclude library code from debugging.
- console: Set to "integratedTerminal" to run the application in the VSCode terminal.
- env: Optional environment variables. PYTHONPATH ensures the workspace folder is included in the Python path.

---

**Starting to run system**

```
uvicorn app:app --reload
```

**Access document of OraPy RESTful API system**

```
http://localhost:5000/docs
```
