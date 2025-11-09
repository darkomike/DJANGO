# Authentication Setup Summary

## ✅ What Was Done

### 1. **Created Authentication Views** (`users/views.py`)
   - **UserRegistrationView**: Sign up with email, username, password (returns token)
   - **UserLoginView**: Login with username/password (returns token)
   - **UserLogoutView**: Logout and delete user's token
   - **ForgotPasswordView**: Request password reset link via email
   - **ResetPasswordView**: Reset password using UID and token
   - **ChangePasswordView**: Change password for authenticated users

### 2. **Updated URL Configuration** (`users/urls.py`)
   Added the following authentication endpoints:
   - `POST /api/users/auth/signup/` - User registration
   - `POST /api/users/auth/login/` - User login
   - `POST /api/users/auth/logout/` - User logout
   - `POST /api/users/auth/forgot-password/` - Request password reset
   - `POST /api/users/auth/reset-password/` - Reset password
   - `POST /api/users/auth/change-password/` - Change password

### 3. **Configured Django Settings** (`bloggie/settings.py`)
   - Added `'rest_framework.authtoken'` to `INSTALLED_APPS`
   - Added `REST_FRAMEWORK` configuration for Token Authentication
   - Set default authentication classes and permissions

### 4. **Ran Migrations**
   - Created database tables for auth tokens
   - Applied all authtoken migrations successfully

### 5. **Created Documentation**
   - `AUTH_ENDPOINTS.md`: Comprehensive authentication API documentation
   - Updated `API_ENDPOINTS.md` with authentication information

---

## 🔑 How Authentication Works

### Token-Based Authentication
1. User signs up or logs in
2. Server returns an authentication token
3. Client stores the token (localStorage, sessionStorage, etc.)
4. Client includes token in `Authorization` header for all requests

### Token Format
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

---

## 🚀 Quick Start Guide

### 1. Create Your First User (Sign Up)
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "email": "admin@example.com",
    "password": "admin123",
    "name": "Admin User"
  }'
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": { ... },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

### 3. Use Token to Access Protected Endpoints
```bash
# Get current user profile
curl -X GET http://127.0.0.1:8000/api/users/me/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"

# Create a post
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "Hello World!",
    "status": "published"
  }'
```

### 4. Logout
```bash
curl -X POST http://127.0.0.1:8000/api/users/auth/logout/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## 📝 Available Endpoints Summary

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/api/users/auth/signup/` | POST | ❌ No | Create new user account |
| `/api/users/auth/login/` | POST | ❌ No | Login and get token |
| `/api/users/auth/logout/` | POST | ✅ Yes | Logout and delete token |
| `/api/users/auth/forgot-password/` | POST | ❌ No | Request password reset |
| `/api/users/auth/reset-password/` | POST | ❌ No | Reset password with token |
| `/api/users/auth/change-password/` | POST | ✅ Yes | Change password |
| `/api/users/me/` | GET | ✅ Yes | Get current user profile |
| `/api/posts/` | GET/POST | ✅ Yes | List/Create posts |
| `/api/comments/` | GET/POST | ✅ Yes | List/Create comments |
| All other endpoints | * | ✅ Yes | Require authentication |

---

## 🔒 Security Features

### ✅ Implemented
- Token-based authentication
- Password hashing (Django default)
- Token deletion on logout
- Token regeneration on password change
- User authentication required for all main endpoints
- Password reset with secure tokens
- Email validation

### 🔧 Recommended Enhancements
1. **Email Configuration**: Set up SMTP for password reset emails
2. **Rate Limiting**: Add throttling to prevent brute force attacks
3. **Token Expiration**: Implement automatic token expiration
4. **Email Verification**: Require email verification for new accounts
5. **Password Strength**: Add password complexity requirements
6. **HTTPS**: Always use HTTPS in production
7. **CORS**: Configure CORS for frontend integration
8. **Refresh Tokens**: Implement refresh token mechanism for better security

---

## 📧 Email Configuration (For Password Reset)

To enable email functionality, add to `settings.py`:

```python
# Email settings for Gmail (example)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-specific-password'
DEFAULT_FROM_EMAIL = 'noreply@bloggie.com'
```

Then uncomment the `send_mail()` call in `ForgotPasswordView` in `users/views.py`.

---

## 🧪 Testing the API

### Using cURL (Command Line)
See examples in the Quick Start Guide above.

### Using Postman or Insomnia
1. Create a POST request to `/api/users/auth/signup/`
2. Set `Content-Type: application/json` header
3. Add request body with username, email, password
4. Copy the token from response
5. For authenticated requests, add header: `Authorization: Token YOUR_TOKEN`

### Using Browser (DRF Browsable API)
1. Go to `http://127.0.0.1:8000/api/users/auth/signup/`
2. Use the form to create an account
3. Copy the token from the response
4. You can't easily use token auth in browser, use session auth instead
5. Or use browser extensions like ModHeader to add Authorization header

### Using Python
```python
import requests

# Sign up
response = requests.post('http://127.0.0.1:8000/api/users/auth/signup/', json={
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'testpass123',
    'name': 'Test User'
})
token = response.json()['token']

# Use token for authenticated request
headers = {'Authorization': f'Token {token}'}
profile = requests.get('http://127.0.0.1:8000/api/users/me/', headers=headers)
print(profile.json())
```

### Using JavaScript (fetch)
```javascript
// Sign up
const signup = async () => {
  const response = await fetch('http://127.0.0.1:8000/api/users/auth/signup/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'testuser',
      email: 'test@example.com',
      password: 'testpass123',
      name: 'Test User'
    })
  });
  const data = await response.json();
  localStorage.setItem('token', data.token);
  return data;
};

// Use token for authenticated request
const getProfile = async () => {
  const token = localStorage.getItem('token');
  const response = await fetch('http://127.0.0.1:8000/api/users/me/', {
    headers: {
      'Authorization': `Token ${token}`
    }
  });
  return await response.json();
};
```

---

## 🎯 Next Steps

1. **Test the endpoints** using the examples above
2. **Configure email** for password reset functionality
3. **Set up CORS** if you have a frontend application
4. **Add rate limiting** for security
5. **Implement token expiration** for better security
6. **Add email verification** for new users
7. **Set up logging** for authentication events
8. **Configure HTTPS** for production deployment

---

## 📚 Additional Documentation

- Full authentication API reference: [AUTH_ENDPOINTS.md](./AUTH_ENDPOINTS.md)
- All API endpoints: [API_ENDPOINTS.md](./API_ENDPOINTS.md)
- Django REST Framework: https://www.django-rest-framework.org/
- Django Authentication: https://docs.djangoproject.com/en/4.2/topics/auth/

---

## 🐛 Troubleshooting

### "Invalid credentials" error
- Check username and password are correct
- Ensure user exists in database
- Check if password was hashed correctly during signup

### "Authentication credentials were not provided"
- Add `Authorization: Token YOUR_TOKEN` header
- Check token is valid and not expired
- Verify token exists in database

### "Invalid token" or "User not found"
- Token may have been deleted (logout)
- User may have been deleted
- Token format incorrect (must be: `Token <token-string>`)

### Email not sending
- Check email configuration in settings.py
- Verify SMTP credentials are correct
- Check firewall/network settings
- Use Gmail App Passwords if using Gmail

---

**Authentication setup is complete and ready to use! 🎉**
