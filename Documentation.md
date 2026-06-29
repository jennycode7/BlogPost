# Blog API Documentation

---

## Authentication - Signup

* **URL:** `/api/auth/signup/`
* **Method:** `POST`
* **Content-Type:** `application/json`

### **Request Body:**

| Field Name | Type   | Required | Description     |
| ---------- | ------ | -------- | --------------- |
| username   | string | Yes      | Unique username |
| password   | string | Yes      | User password   |

* **Example Request:**

```json
{
  "username": "jennifer",
  "password": "securepassword"
}
```

---

### **Response**

**Status Code:** `201 Created`

```json
{
  "message": "User created successfully"
}
```

---

### **Error Responses**

**400 Bad Request**

```json
{
  "error": "Username already exists"
}
```

---

### **Notes**

* No authentication required

---

## Authentication - Login

* **URL:** `/api/auth/login/`
* **Method:** `POST`
* **Content-Type:** `application/json`

### **Request Body:**

| Field Name | Type   | Required | Description |
| ---------- | ------ | -------- | ----------- |
| username   | string | Yes      | Username    |
| password   | string | Yes      | Password    |

* **Example Request:**

```json
{
  "username": "jennifer",
  "password": "securepassword"
}
```

---

### **Response**

**Status Code:** `200 OK`

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

### **Error Responses**

**401 Unauthorized**

```json
{
  "error": "Invalid credentials"
}
```

---

### **Notes**

* Returns JWT tokens

---

## Authentication - Logout

* **URL:** `/api/auth/logout/`
* **Method:** `POST`
* **Content-Type:** `application/json`

### **Request Body:**

| Field Name | Type   | Required | Description   |
| ---------- | ------ | -------- | ------------- |
| refresh    | string | Yes      | Refresh token |

* **Example Request:**

```json
{
  "refresh": "your_refresh_token"
}
```

---

### **Response**

**Status Code:** `200 OK`

```json
{
  "message": "Logged out successfully"
}
```

---

### **Notes**

* Requires authentication

---

## Posts - List & Create

* **URL:** `/api/posts/`
* **Method:** `GET | POST`
* **Content-Type:** `application/json`

### **Request Body (POST):**

| Field Name | Type   | Required | Description        |
| ---------- | ------ | -------- | ------------------ |
| title      | string | Yes      | Post title         |
| content    | string | Yes      | Post content       |
| status     | string | Yes      | draft or published |

---

### **Response**

**GET - 200 OK**

```json
[
  {
    "id": 1,
    "title": "My First Blog",
    "slug": "my-first-blog",
    "content": "This is my first post",
    "status": "published",
    "author": {
      "id": 1,
      "username": "jennifer"
    },
    "likes_count": 2,
    "comments_count": 1,
    "created_at": "2026-06-28T12:00:00Z",
    "published_at": "2026-06-28T12:30:00Z"
  }
]
```

---

**POST - 201 Created**

```json
{
  "message": "Post created successfully"
}
```

---

### **Notes**

* GET is public
* POST requires authentication
* Author is auto-assigned

---

## Posts - Detail / Update / Delete

* **URL:** `/api/posts/{id}/`
* **Method:** `GET | PATCH | DELETE`
* **Content-Type:** `application/json`

---

### **Response**

**GET - 200 OK**

```json
{
  "id": 1,
  "title": "My First Blog",
  "slug": "my-first-blog",
  "content": "This is my first post"
}
```

---

**PATCH - 200 OK**

```json
{
  "message": "Post updated successfully"
}
```

---

**DELETE - 204 No Content**

---

### **Notes**

* Only author can update/delete

---

## Comments

* **URL:** `/api/comments/`
* **Method:** `GET | POST`
* **Content-Type:** `application/json`

---

### **Request Body (POST):**

| Field Name | Type   | Required | Description  |
| ---------- | ------ | -------- | ------------ |
| post       | int    | Yes      | Post ID      |
| content    | string | Yes      | Comment text |

---

### **Response**

**200 OK**

```json
[
  {
    "id": 1,
    "content": "Nice post!",
    "author": "jennifer"
  }
]
```

---

### **Notes**

* Requires authentication to create

---

## Likes

* **URL:** `/api/posts/{id}/like/`
* **Method:** `POST`

---

### **Response**

```json
{
  "message": "Post liked"
}
```

---


### **Notes**

* Requires authentication
* Prevent duplicate likes

---

## General Notes

* All protected routes require:

```
Authorization: Bearer <access_token>
```

* Permissions:

  * Read → Public
  * Write → Authenticated users
  * Edit/Delete → Owner only

---
