import os
import webbrowser

port = 4545
webbrowser.open('http://localhost:' + str(port))
os.system('python -m http.server ' + str(port))