from flask import Flask
from threading import Thread
import subprocess
app = Flask('')

@app.route('/')
def main():
  return "alive 200"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()

command1 = subprocess.Popen(['node', 'main.js'])
keep_alive()
