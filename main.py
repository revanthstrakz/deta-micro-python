# from importlib import import_module
# from deta import Deta
# from datetime import datetime

# deta = Deta("c0gtfkxj_CvBjqd7bj6kL36CAGYHgZA4Y1xmrqAfh")

# users = deta.Base("users")

# users.insert({
#     "name": "datetime",
#     "time": str(datetime.now())
# })

# print(datetime.now())

# def app(event):
#     pass  

from deta import App
from fastapi import FastAPI

app = App(FastAPI())

@app.get("/")
def http():
    return "Hello Deta, I am running with HTTP"

@app.lib.cron()
def cron_job(event):
    return "Hello Deta, I am a cron job"