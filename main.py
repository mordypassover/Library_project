from fastapi import FastAPI
import uvicorn
from routes import member_routes, book_routes, report_routes

app = FastAPI()
app.include_router(book_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
