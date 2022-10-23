from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.routes import user, automobile, login
from config import engine
from api.models import models
from fastapi.responses import RedirectResponse
from settings import get_settings

# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=user.router, tags=["Login"])
app.include_router(router=login.router, tags=["Auth"])
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
async def docs_redirect():
    return RedirectResponse(url="/docs")
