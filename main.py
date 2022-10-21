from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.routes import user, automobile
from config import engine
import uvicorn
from api.models import models
from settings import get_settings


# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=user.router, prefix="/test-ordago", tags=["Test"])
app.include_router(router=automobile.router, prefix="/test-ordago", tags=["Automobile"])

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/info")
async def info():
    return {"app_name": get_settings().database_url}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
