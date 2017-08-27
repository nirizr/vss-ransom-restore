@for /f "delims=" %%i in ('python -c "import platform; print(platform.architecture()[0])"') do set bits=%%i

@echo Note: You're building a %bits% executable, it will only be able to run on a %bits% architecture machine.
@echo To build an execuable for a different architecture, please use a cpython environment of the same architecture (make sure you're not running a 32bit python with a 64bit machine!)
@pause

pip install -r requirements.txt

pyinstaller vss-ransom-restore/main.py --onefile --name vss-ransom-restore