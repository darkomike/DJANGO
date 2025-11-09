# Bloggie API Endpoints

Base URL: `http://localhost:8000/api/`

## Authentication

All API endpoints now require authentication using Token Authentication.

### Authentication Endpoints
- `POST /api/users/auth/signup/` - User registration (returns token)
- `POST /api/users/auth/login/` - User login (returns token)
- `POST /api/users/auth/logout/` - User logout (requires auth)
- `POST /api/users/auth/forgot-password/` - Request password reset
- `POST /api/users/auth/reset-password/` - Reset password with token
- `POST /api/users/auth/change-password/` - Change password (requires auth)

### Using Token Authentication
Include the token in the Authorization header:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

For detailed authentication documentation, see [AUTH_ENDPOINTS.md](./AUTH_ENDPOINTS.md)

---

## Users (`/api/users/`)

### Standard REST Endpoints
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `PATCH /api/users/{id}/` - Partial update user
- `DELETE /api/users/{id}/` - Delete user

### Custom Endpoints
- `GET /api/users/me/` - Get current user's profile
- `GET /api/users/{id}/profile/` - Get user profile
- `GET /api/users/{id}/posts/` - Get all posts by user
- `GET /api/users/{id}/followers/` - Get user's followers
- `GET /api/users/{id}/following/` - Get users that this user follows

---

## Posts (`/api/posts/`)

### Standard REST Endpoints
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{slug}/` - Get post by slug
- `PUT /api/posts/{slug}/` - Update post
- `PATCH /api/posts/{slug}/` - Partial update post
- `DELETE /api/posts/{slug}/` - Delete post

### Query Parameters
- `?category=tech` - Filter by category
- `?status=published` - Filter by status
- `?published=true` - Filter by published flag
- `?tags=django,python` - Filter by tags
- `?search=keyword` - Search in title, content, excerpt
- `?ordering=-createdAt` - Order results

### Custom Endpoints
- `GET /api/posts/{slug}/comments/` - Get all comments for post
- `GET /api/posts/{slug}/likes/` - Get all likes for post
- `GET /api/posts/{slug}/shares/` - Get all shares for post
- `GET /api/posts/{slug}/views_count/` - Get view count for post
- `POST /api/posts/{slug}/publish/` - Publish a post
- `POST /api/posts/{slug}/unpublish/` - Unpublish a post

---

## Comments (`/api/comments/`)

### Standard REST Endpoints
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create a new comment (supports anonymous)
- `GET /api/comments/{id}/` - Get comment details
- `PUT /api/comments/{id}/` - Update comment
- `PATCH /api/comments/{id}/` - Partial update comment
- `DELETE /api/comments/{id}/` - Delete comment

### Query Parameters
- `?post={post_id}` - Filter by post
- `?postId={post_id}` - Filter by post ID
- `?user={user_id}` - Filter by user

### Custom Endpoints
- `GET /api/comments/my_comments/` - Get comments by current user

---

## Contacts (`/api/contacts/`)

### Standard REST Endpoints
- `GET /api/contacts/` - List all contacts (Admin only)
- `POST /api/contacts/` - Submit contact form (Public)
- `GET /api/contacts/{id}/` - Get contact details (Admin only)
- `DELETE /api/contacts/{id}/` - Delete contact (Admin only)

### Custom Endpoints
- `POST /api/contacts/submit/` - Submit contact form (Public)

---

## Follows (`/api/follows/`)

### Standard REST Endpoints
- `GET /api/follows/` - List all follow relationships
- `POST /api/follows/` - Create a follow relationship
- `GET /api/follows/{id}/` - Get follow details
- `DELETE /api/follows/{id}/` - Delete follow relationship

### Query Parameters
- `?followerId={user_id}` - Filter by follower
- `?followingId={user_id}` - Filter by following

### Custom Endpoints
- `POST /api/follows/follow_user/` - Follow a user
  - Body: `{"followingId": user_id}`
- `POST /api/follows/unfollow_user/` - Unfollow a user
  - Body: `{"followingId": user_id}`
- `GET /api/follows/my_followers/` - Get current user's followers
- `GET /api/follows/my_following/` - Get users current user follows

---

## Likes (`/api/likes/`)

### Standard REST Endpoints
- `GET /api/likes/` - List all likes
- `POST /api/likes/` - Create a like (supports guests)
- `GET /api/likes/{id}/` - Get like details
- `DELETE /api/likes/{id}/` - Delete like

### Query Parameters
- `?post={post_id}` - Filter by post
- `?postId={post_id}` - Filter by post ID
- `?user={user_id}` - Filter by user
- `?isGuest=true` - Filter by guest likes

### Custom Endpoints
- `POST /api/likes/toggle_like/` - Toggle like on a post
  - Body: `{"postId": post_id}`
- `GET /api/likes/my_likes/` - Get likes by current user

---

## Newsletters (`/api/newsletters/`)

### Standard REST Endpoints
- `GET /api/newsletters/` - List all subscriptions (Admin only)
- `POST /api/newsletters/` - Subscribe to newsletter (Public)
- `GET /api/newsletters/{id}/` - Get subscription details (Admin only)
- `DELETE /api/newsletters/{id}/` - Delete subscription (Admin only)

### Custom Endpoints
- `POST /api/newsletters/subscribe/` - Subscribe to newsletter (Public)
  - Body: `{"email": "user@example.com"}`
- `POST /api/newsletters/unsubscribe/` - Unsubscribe from newsletter (Public)
  - Body: `{"email": "user@example.com"}`

---

## Shares (`/api/shares/`)

### Standard REST Endpoints
- `GET /api/shares/` - List all shares
- `POST /api/shares/` - Create a share (supports guests)
- `GET /api/shares/{id}/` - Get share details
- `DELETE /api/shares/{id}/` - Delete share

### Query Parameters
- `?post={post_id}` - Filter by post
- `?postId={post_id}` - Filter by post ID
- `?platform=facebook` - Filter by platform
- `?user={user_id}` - Filter by user
- `?isGuest=true` - Filter by guest shares

### Custom Endpoints
- `GET /api/shares/my_shares/` - Get shares by current user
- `GET /api/shares/platform_stats/` - Get share statistics by platform

---

## Views (`/api/views/`)

### Standard REST Endpoints
- `GET /api/views/` - List all views (Admin only)
- `POST /api/views/` - Record a view (Public)
- `GET /api/views/{id}/` - Get view details (Admin only)
- `DELETE /api/views/{id}/` - Delete view (Admin only)

### Query Parameters
- `?post={post_id}` - Filter by post
- `?postId={post_id}` - Filter by post ID
- `?userId={user_id}` - Filter by user
- `?isGuest=true` - Filter by guest views

### Custom Endpoints
- `POST /api/views/record_view/` - Record a view on a post (Public)
  - Body: `{"postId": post_id}`
- `GET /api/views/my_views/` - Get views by current user
- `GET /api/views/post_views_count/?post={post_id}` - Get view statistics for a post
  - Returns: `{"total_views": int, "unique_users": int, "guest_views": int}`

---

## Platform Choices for Shares
- `unknown` - Unknown
- `facebook` - Facebook
- `twitter` - Twitter
- `linkedin` - LinkedIn
- `whatsapp` - WhatsApp
- `telegram` - Telegram
- `reddit` - Reddit
- `email` - Email
- `copy_link` - Copy Link
- `other` - Other

## User Roles
- `user` - Regular User
- `admin` - Administrator
- `moderator` - Moderator
- `editor` - Editor

## User Status
- `active` - Active
- `inactive` - Inactive
- `banned` - Banned
- `suspended` - Suspended

## Post Status
- `draft` - Draft
- `published` - Published
- `archived` - Archived
