from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel

from Eyes.api.database.database import create_tables, delete_tables
from Eyes.api.repository.repository import MailRepository

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")

app = FastAPI(lifespan=lifespan)

class MailAdd(BaseModel):

   email: str

@app.post("/")
async def add_mail(new_mail: MailAdd):
   mail = await MailRepository.add_mail(new_mail.email)
   return mail

@app.get("/")
async def get_mails():
   mails = await MailRepository.get_mails()
   return mails