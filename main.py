from fastapi import FastAPI
from routers.notes import router as notes_router
from routers.users import router as user_router
from routers.auth import router as auth_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(notes_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Notes app!"}
