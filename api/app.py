from sqlmodel import SQLModel, create_engine, Session, Field
from typing import Optional, List, Dict
from uuid import UUID, uuid4
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from pydantic import EmailStr, validator
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse
from uvicorn import run
from starlette.middleware.cors import CORSMiddleware
from shutil import copyfileobj
import os

load_dotenv()

def getId():
    return str(uuid4())

def getDate():
    return str(datetime.now())

class User(SQLModel, table=True):
    id: str = Field(default_factory=getId, primary_key=True)
    fullname:str = Field()
    email:EmailStr = Field(...)
    role:str = Field(default="user")
    picture:str = Field(default="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp")
    created_at:str = Field(default_factory=getDate)
    updated_at:str = Field(default_factory=getDate)

class Product(SQLModel, table=True):
    id: str = Field(default_factory=getId, primary_key=True)
    name:str = Field(...)
    price:float = Field(...)
    description:str = Field(...)
    summary: Optional[str] = Field()
    pictures:List[str] = Field(...)
    categories: List[str] = Field(...)
    stock: int = Field(...)
    created_at:str = Field(default_factory=getDate)
    updated_at:str = Field(default_factory=getDate)

class Quotation(SQLModel, table=True):
    id: str = Field(default_factory=getId, primary_key=True)
    user_id: str = Field(foreign_key=User.id)
    product_id: str = Field(foreign_key=Product.id)
    quantity: int = Field(...)
    created_at:str = Field(default_factory=getDate)
    updated_at:str = Field(default_factory=getDate)

class Order(SQLModel, table=True):
    id: str = Field(default_factory=getId, primary_key=True)
    user_id: str = Field(foreign_key=User.id)
    quotations: List[str] = Field(foreign_key=Quotation.id)
    created_at:str = Field(default_factory=getDate)
    updated_at:str = Field(default_factory=getDate)
    status: str = Field(default="pending")
    total: float = Field(...)

class Files():
    id: str = Field(default_factory=getId, primary_key=True)
    userid: str = Field(foreign_key=User.id)
    filename: str = Field()
    filetype: str = Field()
    created_at:str = Field(default_factory=getDate)


DB_URI = getenv("DB_URI")
PORT = int(getenv("PORT"))
HOST = getenv("HOST")

engine = create_engine(DB_URI)
session = Session(engine)
SQLModel.metadata.create_all(engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get('/api/products')
def get_products(request: Request):
    products = session.query(Product).all()
    return JSONResponse(content=products)

@app.get('/api/products/:id')
def get_product(request: Request, id: str):
    product = session.query(Product).filter_by(id=id).first()
    return JSONResponse(content=product)

@app.post('/api/products')
def create_product(request: Request, product: Product):
    session.add(product)
    session.commit()
    return JSONResponse(content=product)

@app.put('/api/products/:id')
def update_product(request: Request, id: str, product: Product):
    product.id = id
    session.add(product)
    session.commit()
    return JSONResponse(content=product)

@app.delete('/api/products/:id')
def delete_product(request: Request, id: str):
    product = session.query(Product).filter_by(id=id).first()
    session.delete(product)
    session.commit()
    return JSONResponse(content=product)

@app.get('/api/users')
def get_users(request: Request):
    users = session.query(User).all()
    return JSONResponse(content=users)

@app.get('/api/users/:id')
def get_user(request: Request, id: str):
    user = session.query(User).filter_by(id=id).first()
    return JSONResponse(content=user)

@app.post('/api/users')
def create_user(request: Request, user: User):
    session.add(user)
    session.commit()
    return JSONResponse(content=user)

@app.put('/api/users/:id')
def update_user(request: Request, id: str, user: User):
    user.id = id
    session.add(user)
    session.commit()
    return JSONResponse(content=user)

@app.delete('/api/users/:id')
def delete_user(request: Request, id: str):
    user = session.query(User).filter_by(id=id).first()
    session.delete(user)
    session.commit()
    return JSONResponse(content=user)

@app.get('/api/quotations')
def get_quotations(request: Request):
    quotations = session.query(Quotation).all()
    return JSONResponse(content=quotations)

@app.get('/api/quotations/:id')
def get_quotation(request: Request, id: str):
    quotation = session.query(Quotation).filter_by(id=id).first()
    return JSONResponse(content=quotation)

@app.post('/api/quotations')
def create_quotation(request: Request, quotation: Quotation):
    session.add(quotation)
    session.commit()
    return JSONResponse(content=quotation)

@app.put('/api/quotations/:id')
def update_quotation(request: Request, id: str, quotation: Quotation):
    quotation.id = id
    session.add(quotation)
    session.commit()
    return JSONResponse(content=quotation)

@app.delete('/api/quotations/:id')
def delete_quotation(request: Request, id: str):
    quotation = session.query(Quotation).filter_by(id=id).first()
    session.delete(quotation)
    session.commit()
    return JSONResponse(content=quotation)

@app.get('/api/orders')
def get_orders(request: Request):
    orders = session.query(Order).all()
    return JSONResponse(content=orders)

@app.get('/api/orders/:id')
def get_order(request: Request, id: str):
    order = session.query(Order).filter_by(id=id).first()
    return JSONResponse(content=order)

@app.post('/api/orders')
def create_order(request: Request, order: Order):
    session.add(order)
    session.commit()
    return JSONResponse(content=order)

@app.put('/api/orders/:id')
def update_order(request: Request, id: str, order: Order):
    order.id = id
    session.add(order)
    session.commit()
    return JSONResponse(content=order)

@app.delete('/api/orders/:id')
def delete_order(request: Request, id: str):
    order = session.query(Order).filter_by(id=id).first()
    session.delete(order)
    session.commit()
    return JSONResponse(content=order)

templates = Jinja2Templates(directory="templates")
app.mount('/assets', StaticFiles(directory="templates/assets"), name="assets")
app.mount('/uploads', StaticFiles(directory="uploads"), name="uploads")


@app.post("api/:id/upload/")
async def create_upload_files(id:str, files: List[UploadFile]):
    res = []
    for file in files:
       with open(f'uploads/{id}/{file.filename}', 'wb') as f:
           fl = file.file
           await copyfileobj(fl, f)
           fileObj = {
                "id": getId(),
                "userid": id,
                "filename": file.filename,
                "filetype": file.content_type,
                "created_at": getDate(),
                "filesize":file.size,
                "url": f"http://{HOST}:{PORT}/uploads/{id}/{file.filename}"
            }
           res.append(fileObj)
    return JSONResponse(content=res)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT)