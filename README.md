# UNDER DEVELOPMENT

# Install Requirements
```
pip3 install -r requirements.txt
pip3 install -r rti_python/requirements.txt
```
#Compile QT5 .UI files
OSX
```javascript
pyuic5 -x file.ui -o file.py
```

Windows
```javascript
python -m PyQt5.uic.pyuic -x filename.ui -o filename.py

C:\Users\XXX\AppData\Local\Programs\Python\Python35\Scripts\pyuic5.exe -x file.ui -o file.py
```

#Compile QT5 .qrc files
Add all the images included in the .qrc file.  Then compile it.
Also add the images to the spec file.