pyinstaller --onefile Test_Script.py && rmdir /s /q build && rmdir /s /q __pycache__ && del Test_Script.spec && move dist\* . && rmdir /s /q dist
