# Blog Application System
This repository contains a Django-based blog application system with JWT authentication. The application provides features for user authentication (sign up, login, logout), and CRUD operations for blogs.

### Features
- User Authentication (Sign Up, Login, Logout)
- JWT Authentication for secure access
- Create, Read, Update, and Delete (CRUD) operations for blogs
- Pagination for listing blogs
- Detailed logging of errors

### Installation
Clone the repository:
```
git clone https://github.com/varshamohan08/blog_application_system.git
```
Navigate to the project directory:
```
cd blog_application_system
```
Install the required packages:
```
pip install -r requirements.txt
```
Run the development server:
```
python manage.py runserver
```
### Dockerization
To run the application using Docker, follow these steps:

Build the Docker image:
```
docker build -t blog_app .
```
Run the Docker container:
```
docker run -p 8000:8000 blog_app
```
### Logging
Errors are logged to log/error.log. This can be configured in the ins_logger module.

### Pagination
Pagination for the blog list is handled by the BlogPagination class, which sets the page size to 10.

### Authentication
JWT authentication is used to secure the endpoints. Ensure to include the JWT token in the Authorization header as Bearer <token>.

### API Endpoints
The detailed description of the API endpoints can be found in the [api_documentation.md](api_documentation.md) file.
