# Authentication Endpoints

This document describes the authentication endpoints available in the Bloggie API.

## Base URL
All endpoints are prefixed with: `http://127.0.0.1:8000/api/users/`

---

## Authentication Endpoints

### 1. Sign Up (User Registration)
**Endpoint:** `POST /api/users/auth/signup/`

**Permission:** Public (AllowAny)

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securePassword123",
  "name": "John Doe",
  "bio": "Software developer and blogger"
}
```

**Response (201 Created):**
```json
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "uid": "550e8400-e29b-41d4-a716-446655440000",
    "username": "johndoe",
    "email": "john@example.com",
    "name": "John Doe",
    "displayName": "John Doe",
    "avatar": null,
    "photoURL": null,
    "bio": "Software developer and blogger",
    "github": null,
    "linkedin": null,
    "twitter": null,
    "website": null,
    "role": "user",
    "status": "active",
    "createdAt": "2025-11-09T10:30:00Z",
    "updatedAt": "2025-11-09T10:30:00Z"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

---

### 2. Login
**Endpoint:** `POST /api/users/auth/login/`

**Permission:** Public (AllowAny)

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "user": {
    "id": 1,
    "uid": "550e8400-e29b-41d4-a716-446655440000",
    "username": "johndoe",
    "email": "john@example.com",
    "name": "John Doe",
    "displayName": "John Doe",
    "avatar": null,
    "photoURL": null,
    "bio": "Software developer and blogger",
    "role": "user",
    "status": "active"
  }
}
```

**Error Response (401 Unauthorized):**
```json
{
  "error": "Invalid credentials"
}
```

---

### 3. Logout
**Endpoint:** `POST /api/users/auth/logout/`

**Permission:** Authenticated users only

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Request Body:** None

**Response (200 OK):**
```json
{
  "message": "Logout successful"
}
```

---

### 4. Forgot Password
**Endpoint:** `POST /api/users/auth/forgot-password/`

**Permission:** Public (AllowAny)

**Request Body:**
```json
{
  "email": "john@example.com"
}
```

**Response (200 OK):**
```json
{
  "message": "Password reset link has been sent to your email",
  "reset_link": "http://127.0.0.1:8000/reset-password/MQ/abc123-token/",
  "uid": "MQ",
  "token": "abc123-token"
}
```

**Note:** In production, only the message should be returned. The `reset_link`, `uid`, and `token` are included here for development/testing purposes.

---

### 5. Reset Password
**Endpoint:** `POST /api/users/auth/reset-password/`

**Permission:** Public (AllowAny)

**Request Body:**
```json
{
  "uid": "MQ",
  "token": "abc123-token",
  "new_password": "newSecurePassword456",
  "confirm_password": "newSecurePassword456"
}
```

**Response (200 OK):**
```json
{
  "message": "Password reset successful"
}
```

**Error Responses:**
- **400 Bad Request** (Passwords don't match):
```json
{
  "error": "Passwords do not match"
}
```

- **400 Bad Request** (Invalid/expired token):
```json
{
  "error": "Invalid or expired reset token"
}
```

---

### 6. Change Password
**Endpoint:** `POST /api/users/auth/change-password/`

**Permission:** Authenticated users only

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Request Body:**
```json
{
  "old_password": "currentPassword123",
  "new_password": "newSecurePassword456",
  "confirm_password": "newSecurePassword456"
}
```

**Response (200 OK):**
```json
{
  "message": "Password changed successfully",
  "token": "new-token-here-after-password-change"
}
```

**Error Responses:**
- **400 Bad Request** (Passwords don't match):
```json
{
  "error": "New passwords do not match"
}
```

- **400 Bad Request** (Incorrect old password):
```json
{
  "error": "Old password is incorrect"
}
```

---

## Using Authentication Token

After login or signup, you'll receive an authentication token. Include this token in the `Authorization` header for all authenticated requests:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Example with cURL:
```bash
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
     http://127.0.0.1:8000/api/users/me/
```

### Example with JavaScript (fetch):
```javascript
fetch('http://127.0.0.1:8000/api/users/me/', {
  headers: {
    'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

### Example with Python (requests):
```python
import requests

headers = {
    'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
}

response = requests.get('http://127.0.0.1:8000/api/users/me/', headers=headers)
print(response.json())
```

---

## Testing the Endpoints

### 1. Sign Up a New User
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "name": "Test User"
  }'
```

### 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### 3. Get Current User Profile (requires token)
```bash
curl -X GET http://127.0.0.1:8000/api/users/me/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### 4. Logout (requires token)
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/logout/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### 5. Forgot Password
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/forgot-password/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com"
  }'
```

### 6. Reset Password
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/reset-password/ \
  -H "Content-Type: application/json" \
  -d '{
    "uid": "MQ",
    "token": "abc123-token",
    "new_password": "newpass456",
    "confirm_password": "newpass456"
  }'
```

### 7. Change Password (requires token)
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/change-password/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "old_password": "testpass123",
    "new_password": "newpass456",
    "confirm_password": "newpass456"
  }'
```

---

## Email Configuration (For Password Reset)

To enable email sending for the forgot password feature, add the following to your `settings.py`:

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or your email provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
```

Then uncomment the `send_mail()` function in `users/views.py` in the `ForgotPasswordView`.

---

## Security Notes

1. **Always use HTTPS in production** to protect tokens and passwords in transit
2. **Store tokens securely** on the client side (e.g., httpOnly cookies, secure storage)
3. **Implement rate limiting** on login and password reset endpoints to prevent brute force attacks
4. **Set up proper email configuration** for password reset functionality
5. **Consider adding email verification** for new user registrations
6. **Implement token expiration** for enhanced security
7. **Use strong password requirements** (minimum length, complexity, etc.)
