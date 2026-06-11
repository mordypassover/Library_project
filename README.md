# library project

## basic project explanation

the program handles a library of books and members as 2 data tables,
books and members. the tables are handled by python classes BookDB
and MemberDB. the classes are called in main.py. main runs methods
via routes using fastapi. uvicorn runs main. books and users can
be added, books can be borrowed and returned, and book reports 
can be added updated and red.  

## Technologies Used

- Python
- FastAPI
- uvicorn
- logging
- MySQL
- Docker

file build

library_project
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

## doker

docker run --name mysql-lib-pjt \
-e MYSQL_ROOT_PASSWORD=***** \
-e MYSQL_DATABASE=library_db \
-p 3306:3306 \
-d mysql:8

docker exec -it mysql-lib-pjt mysql -uroot -proot1

## Database Information
db name : library_db

## Database Tables

### Table: `books`

|-------------|-----------|-------------|-------------|
| column Name |   data    | Constraints | Description |
| Description |           |             |             |
|-------------|-----------|-------------|-------------|
|    id       |    int    | not Null    | primary key |
|-------------|-----------|-------------|-------------|
|   title     |  varchar  | not Null    | book name   |
|             |           | 50 chars    |             |
|-------------|-----------|-------------|-------------|
|  author     |  varchar  |  not Null   | author name |
|             |           |  50 chars   |             |
|-------------|-----------|-------------|-------------|
|   genre     | varchar   |   not Null  |  Fiction    |
|             |           |     ENUM    |  Non-Fiction|
|             |           |             |  Science    |
|             |           |             |  History    |
|             |           |             |  Other      |
|-------------|-----------|-------------|-------------|
|is_available |` boll     |   not Null  |availability | 
|-------------|-----------|-------------|-------------|
| id_member_  | int|Noll  |             | id of member|
| by_borrowed |           |             | or Null     |
|-------------|-----------|-------------|-------------|

### Table: `members`

|-------------|-----------|-------------|-------------|
| column Name |   data    | Constraints | Description |
| Description |           |             |             |
|-------------|-----------|-------------|-------------|
|    id       |    int    | not Null    | primary key |
|-------------|-----------|-------------|-------------|
|   name      |  varchar  | not Null    | member      |
|             |           | 50 chars    | name        |
|-------------|-----------|-------------|-------------|
|   email     |  varchar  |  not Null   | member      |
|             |           |  50 chars   | email       |
|             |           |  unique     |             |
|-------------|-----------|-------------|-------------|
|   is_active | bool      |  not Null   | active check|
|-------------|-----------|-------------|-------------|
|total_borrows|` boll     |   not Null  |availability | 
|-------------|-----------|-------------|-------------|


## System Rules

1. when creating a book must enter book name, author and genre.
then after validation, book is added to books table. 
2. genre allowed are  Fiction | Non-Fiction | Science | History | Other.
3. when creating a member user must enter name and unique email. 
after validation, member is added to members table.
4. inactive members cant borrow books.
5. borrowed books cant be reborrowed.
6. members cant borrow more then 3 books.
7. only member can return his borrowed books.


## API Endpoints

# Books Endpoints
|---------------|-------------------|------------------|-----------------|-----------------|
|Method         |   Endpoint        |  Description     | Request Body    |     Response    |
|---------------|-------------------|------------------|-----------------|-----------------|
     POST               /books       INSERT TO BOOKS     book_name,              201
                                                         author, genre.          400
|---------------|-------------------|------------------|-----------------|-----------------|
     GET                /books        gets all books            --               200
|---------------|-------------------|------------------|-----------------|-----------------|
     GET              /books/{id}      get book by id           --             200, 404
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT              /books/{id}      update book           dict              200, 404
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT         /books/{id}/return     return book        book_name           200, 400
                  /{member_id}          
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT         /books/{id}/borrow     borrow book        book_name          200, 400
                  /{member_id}
|---------------|-------------------|------------------|-----------------|-----------------|

# Books Endpoints

|---------------|-------------------|------------------|-----------------|-----------------|
|Method         |   Endpoint        |  Description     | Request Body    |     Response    |
|---------------|-------------------|------------------|-----------------|-----------------|
     POST           /members           INSERT member      name, email           201, 400
|---------------|-------------------|------------------|-----------------|-----------------|
     GET            /members           gets all member          --                 200
|---------------|-------------------|------------------|-----------------|-----------------|
     GET            /members/{id}     gets member by id         --             200, 400
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT            /members/{id}     update member            dict            200, 404
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT            /members/{id}       deactivate            --               200, 400
                    /deactivate           member
|---------------|-------------------|------------------|-----------------|-----------------|
     PUT            /members/{id}      activate member         --              200, 400
                    /activate 
|---------------|-------------------|------------------|-----------------|-----------------|

# Reports Endpoints

|---------------|-------------------|------------------|-----------------|-----------------|
     GET          /reports/summary     gets report              --               200
|---------------|-------------------|------------------|-----------------|-----------------|
     GET           /reports/books      gets reports             --               200
                    -by-genre           by genre
|---------------|-------------------|------------------|-----------------|-----------------|
     GET         /reports/top             gets most             --               200
                       -member          active member
|---------------|-------------------|------------------|-----------------|-----------------|


## System Flow

1. Server Startup:
   
   the server connects to mysql creates tables if they don't 
   exist and creates an instance of MemberDB and BooksDB, then 
   starts FastAPI server.

2. Creating a Member:
   
   user sends POST request to /members with name and email, the 
   system validates that the email is unique. the system creates 
   member with is_active=True and total_borrows=0 and returns the
   created members id.

3. Borrowing a Book:

   User sends put request to /books/{id}/borrow/{member_id}, the
   system checks if book exists then checks if the member
   exists and is active. the system checks if book is available
   then checks if member has less than 3 books if not, updates
   book: is_available=False, borrowed_by_member_id=member_id
   and increments member's total_borrows by 1 and returns
   success message to user.


   