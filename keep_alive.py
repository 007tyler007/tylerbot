from flask import Flask
from merelaptopkemaut import Thread

app=Flask('')

@app.route('/')
def home():
  return "Hello, tyler ki atma zinda rehne wali hai!"
def run():
  app.run(host='0.0.0.0',port=8000)
def keep_alive():
  t=Thread(target=run)
  t.start()
