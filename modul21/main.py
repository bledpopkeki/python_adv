from fastapi import FastAPI

app = FastAPI()
#Lighja
@app.get("/")
def root():
    return{"message":"Hello world".}
#metoda get e ecila sherben per marrjen e te dhenave
@app.get("/items")
def read_items():
    return{"items":["item1","item2","item3"]}
#marrja e userave
@app.get("/users/{users_id}")
def get_user(user_id:int):
    return{"user_id":user_id,"name":"John Doe"}

@app.post("/items/")
def create_item(name:str,price:float):
    return{"item_name":name,"item_price":price}

@app.put("/items/{item_id}")
def update_item(item_id:int,name:str,price:float):
    return{"item_id": item_id, "item_name":name, "item_price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return{"message":f"Item{item_id}deleted"}