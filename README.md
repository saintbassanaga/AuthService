# **Django Authentication System**

This project is a Django-based authentication system that includes user login, signup, password reset, and profile management functionality.

## **Features**

1. **User Authentication**
   - Login using email or username and password.
   - Password reset functionality with email-based reset link.
   - Secure password storage using Django's authentication system.

2. **Pages**
   - Login
   - Signup
   - Forgot Password
   - Change Password (authenticated users only)
   - Dashboard (accessible only to authenticated users)
   - Profile (view and update user details)

3. **Validation**
   - Password and email validations included during signup and password reset.
   - Proper error handling and user-friendly messages for invalid inputs.

---

## **Implementation Details**

### **Custom User Model**
- The project uses a custom user model (`accounts.User`) to allow email-based authentication and better flexibility for future extensions.
- `AbstractUser` is inherited to retain compatibility with Django's built-in authentication framework.

**Reason for choice:** Django recommends using a custom user model for projects that require email as the primary identifier. This avoids refactoring issues in the future.

---

### **Views**
1. **Signup View**
   - Validates password length and ensures password confirmation.
   - Sends a welcome email upon successful registration.

2. **Login View**
   - Supports both email and username-based login using a custom authentication backend.

3. **Password Reset**
   - Uses Django's built-in `PasswordResetView` and `PasswordResetConfirmView`.
   - Sends a secure password reset link to the user’s email.

**Reason for choice:** Django's built-in views are secure and follow best practices, minimizing the need for custom implementations.

---

### **Templates**
- Templates are organized in the `accounts/templates/accounts/` directory for clarity and modularity.
- Custom styling is applied through a CSS file located in `static/accounts/css/style.css`.

**Note:** Inline styles have been avoided to ensure scalability and easier maintenance.

---

### **Static Files**
- Static files (CSS, JS, images) are managed using Django's static files system.
- Ensure you run `python manage.py collectstatic` before deploying to production.

---

### **Security Considerations**
- CSRF protection is enabled for all forms (`{% csrf_token %}` included).
- User passwords are hashed using Django's default `PBKDF2` algorithm.
- Sensitive pages like the dashboard and profile require user authentication.

**Reason for choice:** Following security best practices ensures the application is robust against common vulnerabilities like CSRF, XSS, and brute-force attacks.

---

### **Testing**
- Basic tests for signup, login, and password reset functionality are implemented in `accounts/tests.py`.

**How to run tests:**
```bash
python manage.py test accounts
