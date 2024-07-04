### API Documentation

**Note:** All endpoints in this documentation are based on the local server running at `http://127.0.0.1` on port `8000`.
### User Authentication and CRUD Endpoints
---
#### Login
- URL: http://127.0.0.1:8000/login
- Method: POST
- Sample Input:

``` json[]
{
    "email": "user4@test.com",
    "password": "test@123"
}
```
#### Logout
- URL: http://127.0.0.1:8000/logout
- Method: POST

---
#### Sign Up
- URL: http://127.0.0.1:8000/sign_up
- Method: POST
- Sample Input:
``` json[]
{
    "email": "user1@test.com",
    "password": "test@123",
    "first_name": "user",
    "last_name": "1"
}
```
---
#### User API
- URL: http://127.0.0.1:8000/user_api
- Use the access token from login as a bearer token; otherwise, an HTTP 401 Unauthorized status is returned.

##### GET:
Retrieve the details of the logged-in user.
##### PUT:
Sample Input
``` json[]
{
    "email": "user88@test.com",
    "first_name": "user",
    "last_name": "1"
}
```
##### PATCH:
Sample Input:
``` json[]
{
    "current_password": "test@123",
    "new_password": "test@123"
}
```
##### DELETE:
The logged-in user and all blogs authored by the user will be deleted.


### Blog Endpoints
---

#### Blog List
##### All Blog List
- URL: http://127.0.0.1:8000/blog_api/list
- Method: GET
- Description: Retrieve the first 10 blogs (first page) from all blogs.

##### Paginated Blog List
- URL: http://127.0.0.1:8000/blog_api/list?page=2
- Method: GET
- Description: Retrieve the second 10 blogs (second page) from all blogs.

##### Blog Search
- URL: http://127.0.0.1:8000/blog_api/list?query=yy
- Method: GET
Description: Retrieve blogs containing "yy" in the title or content on the first page.

##### Paginated Blog Search
- URL: http://127.0.0.1:8000/blog_api/list?query=yy&page=2
- Method: GET
- Description: Retrieve blogs containing "yy" in the title or content on the second page.
---
#### Blog CRUD
##### User's Blogs
- URL: http://127.0.0.1:8000/blog_api/
- Method: GET
- Description: Retrieve all blogs authored by the logged-in user.

##### Create Blog
- URL: http://127.0.0.1:8000/blog_api/
- Method: POST
- Sample Input:
``` json[]
{
    "title": "Evening Serenade", 
    "content": "The sound of a violin floated through the evening air. It was a perfect end to a beautiful day, filled with music and magic."
}
```
##### Update Blog
- URL: http://127.0.0.1:8000/blog_api/
- Method: PUT
- Sample Input:
``` json[]
{
    "id": 27,
    "title": "Evening Serenade edited", 
    "content": "The sound of a violin floated through the evening air. It was a perfect end to a beautiful day, filled with music and magic."
}
```
##### Delete Blog
- URL: http://127.0.0.1:8000/blog_api/
- Method: DELETE
- Sample Input:
``` json[]
{
    "id": 27
}
```

