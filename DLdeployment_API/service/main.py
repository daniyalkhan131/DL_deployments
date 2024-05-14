from fastapi import FastAPI
from service.api.api import main_router

app = FastAPI (project_name='Diabetic-Retinopathy-Detection')
app.include_router(main_router)
 

@app.get("/")
def root():
    return {'welcome to diabetic retinopathy diagnosis, images': 'grading' }


# class InputItem(BaseModel):
#     name: str 
#     price: int
#     discount: int

# class OutputItem(BaseModel):
#     name: str 
#     selling_price: int 

# @app.get("/") #using get method, and / for home page
# def read():
#     return {"Hello": "World"} #it will return dict
# #then write uvicorn main:app for executing this on server
# #use --reload 

# @app.get("/items/{item id}")
# def read_item(item_id: int, q: Union[str, None] = None) :
#     return {"item id": item_id, "q": q}


# @app.post ("/items/", response_model=OutputItem) #for keeping check on output way
# def add_item(item: InputItem) :
#     selling_price= item.price-item.discount #computation like this should be in core,
#     #like processing data, model predictn etc
#     return {"name": item.name, "selling_price": selling_price}

