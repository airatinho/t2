from flask import Flask,render_template
import json

import asyncio
import os

loop=asyncio.get_event_loop()
app = Flask(__name__)
path="jsons/"
num_f=len(os.listdir(path))

async def m_funct(num_f:int)->list:
    """Сортирует айдишники из json от трех источников"""
    results=[]
    for i in range(num_f):
        try:
            data =  json.load(
                    open(f"jsons/source_{i+1}.json",encoding="utf-8")
                )#ошибка таймаута 2 секунды, после которых падаем в ошибку asyncio.TimeoutError
            results.extend( data.get(str(i+1)))
        except Exception:
            continue
    return  sorted(results, key=lambda k: k['id'])

@app.route('/')
def hello_world():
    # loop.run_until_complete(m_funct(num_f))
    res=loop.run_until_complete(m_funct(num_f))
    return render_template("test.html",res=res)

if __name__ == '__main__':
    app.run(debug=False,use_reloader=False)