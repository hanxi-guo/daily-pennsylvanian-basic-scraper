# GitHub Actions errors

If you're running into Python errors during your GitHub Actions workflow—especially stuff like "ModuleNotFoundError: No module named 'requests'"—this guide is for you. I ran into a bunch of frustrating issues with Pipenv and deployment, so here's what happened (I think!) and how to fix it step-by-step.

---

## ❗️Problem 0: `requests` (or any dependency) missing in GitHub Actions

### 🔍 The error:
```
ModuleNotFoundError: No module named 'requests'
```

### 🔍 GitHub Actions log:
```bash
Run pipenv run python ./script.py
Traceback (most recent call last):
  File "./script.py", line 9, in <module>
    import daily_event_monitor
  File "./daily_event_monitor.py", line 8, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```


### Fix:
1. Make sure Pipfile and Pipfile.lock are both committed and pushed.
2. **Delete** any `touch Pipfile` lines in your workflow file.
3. **Install dependencies properly in your workflow:**

```yaml
- name: Install dependencies
  run: pipenv install --deploy --dev
```


---

## ❗️Problem 1: Pipfile.lock is out of date

### 🔍 The error:
```
Your Pipfile.lock (...) is out of date. Expected: (...)
ERROR:: Aborting deploy
```

### 🤔 What’s happening:
This means the Pipfile and Pipfile.lock aren’t in sync. `pipenv install --deploy` checks for a **perfect match** and fails if it finds a difference.

### Fix:
```bash
pipenv lock
git add Pipfile.lock
```

Then commit and push again to see if it running well now.

---

## ❗️Problem 2: Pipenv lock fails locally (`FileNotFoundError`, broken virtualenv)

### 🔍 The error:
```
FileNotFoundError: No such file or directory: .../.venv/bin/python
ERROR: Failed to lock Pipfile.lock!
```

### 🤔 What’s happening:
Your local pipenv virtualenv might be broken or missing. This often happens if something went wrong during a previous install

### Fix:

1. **Remove and reset environment:**

```bash
pipenv --rm
```

2. **Reinstall and lock:**

```bash
pipenv install --dev
pipenv lock
```

The following step us same as what it originallly like in problem 1.


---

Hope this helps you (or future me (｡•̀ᴗ-)✧) fix the issue faster. If you run into any more weird Pipenv + CI bugs, feel free to update this file!
```
