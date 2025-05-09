# Edreate Blog Project

A comprehensive Django blog application with admin capabilities.

## Features

- Responsive home page with a list of blog posts
- Admin interface for adding, editing, and deleting blog posts
- Individual post pages with full content
- Modern and clean UI design
- Mobile-friendly layout

## Requirements

- Python 3.10 or higher
- Django 5.0 or higher
- Pillow (for image handling)

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd edreate-blog
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations blog
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:
   ```
   python manage.py createsuperuser
   ```

6. Copy the Edreate logo to the static/images folder as `edreate_logo.png`

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the site at http://127.0.0.1:8000/
   - The admin interface is available at http://127.0.0.1:8000/admin/

## Project Structure

```
project_root/
├── edreate_blog_app/            # Main project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py
├── blog/                        # Blog app folder
│   ├── __init__.py
│   ├── admin.py                 # Admin configuration
│   ├── apps.py
│   ├── migrations/
│   ├── models.py                # Database models
│   ├── tests.py
│   ├── urls.py                  # Blog app URLs
│   └── views.py                 # View functions
├── static/                      # Static files
│   ├── css/
│   │   └── style.css            # Enhanced styling
│   ├── js/
│   └── images/
│       └── edreate_logo.png     # Edreate logo
├── templates/                   # Templates
│   ├── base.html                # Base template
│   ├── blog/                    # Blog templates
│   │   ├── home.html            # Home page with blog list
│   │   └── post_detail.html     # Individual post page
│   └── includes/
│       ├── header.html          # Header with logo
│       └── footer.html          # Footer with logo
├── manage.py
└── requirements.txt             # Project dependencies
```

## Usage

1. Log in to the admin interface using your superuser credentials.
2. Create, edit, or delete blog posts from the admin panel.
3. View the list of posts on the home page.
4. Click on a post title to view the full content on a dedicated page.

## Customization

- Modify the CSS in `static/css/style.css` to change the appearance
- Edit#
