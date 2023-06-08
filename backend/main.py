from fastapi import FastAPI, HTTPException
import uvicorn
from routes.books import book_router
from routes.users import user_router


app = FastAPI()
app.include_router(book_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)