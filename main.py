from fastapi import FastAPI
import uvicorn
from routes import member_routes, book_routes, report_routes
from database.db_connection import create_books_and_members_tables

create_books_and_members_tables()

app = FastAPI()
app.include_router(book_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
