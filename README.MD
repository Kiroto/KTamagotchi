# Ana's Tamagotchi
## Executing
To execute the program locally, you can build it and run the executable, or run `main.py` with python 3.
## Getting Started
## Building
To build the app, the `PyInstaller` package is required.
Run `python -m PyInstaller main.py -F --add-data "./src/resources;./src/resources"` to package the app. The resulting file will reside in the newly created [dist](/dist/) folder.