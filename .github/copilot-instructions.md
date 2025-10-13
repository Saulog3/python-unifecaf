## Repo: python-unifecaf — quick agent guide

This repository contains classroom examples and exercises organized by lesson (aulaXX). The goal of an AI coding agent here is to be immediately useful editing, adding examples, fixing lightweight bugs, and producing small learning artifacts.

Keep the instructions short and specific. Prefer edits inside the `aula*/exemplos` and `aula*/exercicios` folders unless the user asks to change global files.

Important pointers
- Project layout: top-level folders `aula01_*` .. `aula06_*` each contain `exemplos/` and `exercicios/` subfolders with standalone Python scripts. Treat each script as a small, runnable example rather than a library module.
- When referencing examples, use these canonical files:
  - `aula05_API_Flask_e_FastAPI/exemplos/a05e01_flask.py` — simple Flask CRUD example, uses `app.run(debug=True, port=3344)` for local run.
  - `aula05_API_Flask_e_FastAPI/exemplos/a05e02_fastAPI.py` — FastAPI CRUD example, uses `uvicorn.run('a5e02_fastAPI:app', port=3344, reload=True)`.
  - `aula02_tipagem_e_typing/exemplos/a02e01_typing.py` — shows typing conventions used across exercises.

Running and debugging
- Local runs are expected using plain Python interpreters and small virtualenvs. Examples include the shebang comments at top of `a05e01_flask.py` and `a05e02_fastAPI.py` describing venv + pip install steps. Use the same pattern when adding new examples.
- Common commands (PowerShell on Windows):
  - Create venv: `python -m venv .venv`
  - Activate: `.\.venv\Scripts\Activate.ps1`
  - Install deps: `pip install fastapi[all]` or `pip install flask flask-cors`
  - Run FastAPI example directly: `python aula05_API_Flask_e_FastAPI/exemplos/a05e02_fastAPI.py`
  - Or run with uvicorn: `python -m uvicorn aula05_API_Flask_e_FastAPI/exemplos.a05e02_fastAPI:app --reload --port 3344`

Conventions found in code
- Examples prefer explicit UTF-8 JSON responses:
  - Flask: `app.config["JSON_AS_ASCII"] = False` and a custom `json_response` helper in `a05e01_flask.py`.
  - FastAPI: `utf8_json_response` helper and `media_type="application/json; charset=utf-8"`.
- In-memory data stores are used for examples (lists of dicts or Pydantic models). If you need persistent storage, add a new `aula06_banco_de_dados_com_python` example that follows the existing naming (there is already an aula06 folder with examples showing SQLAlchemy/SQLite).
- File naming: example scripts begin with `aNNex_name.py`; exercises `aNNex_name.py` under `exercicios/`.

What agents should do first
- Small edits and fixes only: correct typos in docstrings, update run instructions at the top of example files, fix obvious bugs in single-file examples, and add short comments showing expected HTTP endpoints for API examples.
- When adding tests: create minimal unit scripts alongside examples (e.g., `test_a05_fastapi_minimal.py`) that run quick smoke checks (import the app and assert endpoints exist). Keep tests simple and independent of external services.

Integration and external dependencies
- Primary external libs used in examples: `flask`, `flask-cors`, `fastapi`, `uvicorn`, `pydantic`, `sqlalchemy` (in aula06). Avoid adding heavy infra; prefer small dependencies.

Files to reference when making behavioral changes
- `aula05_API_Flask_e_FastAPI/exemplos/a05e02_fastAPI.py` — endpoint design, CORS, response helpers.
- `aula05_API_Flask_e_FastAPI/exemplos/a05e01_flask.py` — JSON/UTF-8 conventions and request/response helpers.
- `aula02_tipagem_e_typing/exemplos/a02e01_typing.py` — typing style used throughout exercises.

Commit and PR style
- Keep commits small and focused (one exercise, one example). Use Portuguese commit messages if repository history uses Portuguese (existing commits used Portuguese earlier).

Limitations & Do nots
- Do not modify student-submitted files under `Exercicio concluídos/` unless asked — these are past submissions.
- Avoid adding global tooling (CI, formatters) without asking — this is a teaching repo and changes should be minimally invasive.

If anything is unclear, ask the user a short question (Portuguese is fine) and prefer to make a small, reversible change first.

---
If you'd like, I can now add this file to `.github/` and commit it. Want me to proceed?
