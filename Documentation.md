# Blog API

##  Overview

The **Blog API** is a RESTful backend built with **Django** and **Django REST Framework (DRF)**.

It provides a complete blogging system with authentication, posts, comments, and likes — following modern backend best practices.

---

## Features

*  JWT Authentication (Login, Signup, Logout)
*  CRUD for Blog Posts
*  Comment System
*  Like/Unlike System
*  Permission-Based Access Control


---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** SimpleJWT
* **Documentation:** DRF Spectacular
* **Database:** SupaBase

---

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/blog-api.git

# Navigate into project
cd blog-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

##  Authentication

Uses **JWT (JSON Web Tokens)**.

### Signup

`POST /api/auth/signup/`

```json
{
  "username": "jennifer",
  "password": "securepassword"
}
```

---

### Login

`POST /api/auth/login/`

```json
{
  "username": "jennifer",
  "password": "securepassword"
}
```

**Response**

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

### Logout

`POST /api/auth/logout/`

```json
{
  "refresh": "jwt_refresh_token"
}
```

---

## API Endpoints

### Posts

| Method | Endpoint             | Description            |
| ------ | -------------------- | ---------------------- |
| GET    | `/api/posts/`        | List all posts         |
| POST   | `/api/posts/`        | Create a post          |
| GET    | `/api/posts/{id}/` | Retrieve a single post |
| PATCH  | `/api/posts/{id}/` | Update a post          |
| DELETE | `/api/posts/{id}/` | Delete a post          |

---

### Comments

| Method | Endpoint              | Description    |
| ------ | --------------------- | -------------- |
| GET    | `/api/comments/`      | List comments  |
| POST   | `/api/comments/`      | Create comment |
| PATCH  | `/api/comments/{id}/` | Update comment |
| DELETE | `/api/comments/{id}/` | Delete comment |

---

### Likes

| Method | Endpoint                  | Description   |
| ------ | ------------------------- | ------------- |
| POST   | `/api/posts/{id}/like/`   | Like a post   |

---

## Permissions

* `IsAuthenticatedOrReadOnly`
* Custom `IsAuthorOrReadOnly`

### Rules

*  Anyone can view content
*  Only authenticated users can create
*  Only authors can edit/delete

---

---

## API Documentation

Swagger/OpenAPI docs available via:

```
/api/schema/
/api/docs/
```

---

## Features Yet to Be Added


### User Profile System

* User profile model (avatar, social links, followers, followings)
* Profile view and update endpoints

---

### Notifications System

* Real-time or async notifications for:
  
  * New comments on posts
  * Likes on posts
* Email or in-app notification support

---

### Search & Filtering

* Search posts by title and content
* Filter posts by:

  * Author
  * Date created
  * Status (draft/published)

---

### Nested Comments (Replies)

* Enable replies to comments
* Support threaded discussions

---

### Follow System

* Users can follow/unfollow other users
* Personalized feed based on followed users

---

### Analytics

* Track post views
* Monitor user engagement (likes, comments)



---
