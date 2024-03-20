pyinstaller --onefile Test_Script.py && rm -rf build && rm -rf __pycache__ && rm Test_Script.spec && mv dist/* . && rm -rf dist
