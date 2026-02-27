# Python coding test practice setup

## 1) One-time macOS fix (required first)
Your current `python3` is blocked by the Apple Xcode license state.
Run this in a normal Terminal app:

```bash
sudo xcodebuild -license
```

Read and agree to the license.

## 2) Create virtual environment in this project
After step 1, run:

```bash
cd /Users/jinmun/Desktop/python_practice
python3 -m venv .venv
```

## 3) Open this folder in VS Code
Install recommended extensions when prompted.

## 4) Run files with `python <filename>.py`
Open a VS Code terminal in this workspace and run:

```bash
source .venv/bin/activate
python your_file.py
```

Because this project uses `.vscode/settings.json`, VS Code should also auto-activate `.venv` in the integrated terminal.

## Quick test

```bash
echo 'print("hello")' > hello.py
python hello.py
```
