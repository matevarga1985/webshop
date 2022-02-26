from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return "juppee"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional [str] = None):
    # http://127.0.0.1:8000/items/5?q=sas
    return {"item_id": item_id, "q":q}



#     //main.py
# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)