.PHONY: build

build:
	pyinstaller --hidden-import travian4api -F main.py

