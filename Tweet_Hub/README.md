# TweetHub: A Django-Based Twitter 

Overview
TweetHub is a Twitter-like social media application built with Django. This platform allows users to create accounts, post tweets with images, and interact with other users' content.

Features
- User authentication (register, login, logout)
- Create, read, update, and delete tweets
- Image upload functionality for tweets
- Responsive design using Bootstrap
- User profile management

Technology Stack
- **Backend**: Django 5.1
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default)
- **Image Storage**: Django's built-in media handling

Installation

Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

Setup Instructions
1. Clone the repository
   ```
   git clone https://github.com/your-username/tweethub.git
   cd tweethub
   ```

2. Install required packages
   ```
   pip install django pillow
   ```

3. Run migrations
   ```
   python manage.py migrate
   ```

4. Create a superuser (admin)
   ```
   python manage.py createsuperuser
   ```

5. Start the development server
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/tweet/`

Project Structure
- `chaiheadq/` - Project configuration files
- `twitter/` - Main application
  - `models.py` - Data models for tweets and user interactions
  - `views.py` - View functions/classes for rendering templates
  - `urls.py` - URL routing
  - `templates/` - HTML templates
- `media/` - User-uploaded images
- `static/` - CSS, JavaScript, and other static files

Usage

User Registration
1. Navigate to `/accounts/register/`
2. Fill out the registration form
3. Log in with your new credentials

Creating Tweets
1. Log in to your account
2. Navigate to the tweet creation page
3. Enter your tweet text (up to 500 characters)
4. Optionally upload an image
5. Submit the form

Managing Tweets
- **View**: All tweets are displayed on the main page
- **Edit**: Users can edit their own tweets by clicking the "Edit" button
- **Delete**: Users can delete their own tweets by clicking the "Delete" button

Admin Interface
Access the Django admin interface at `/admin/` to:
- Manage user accounts
- Moderate tweet content
- Configure application settings

Future Enhancements
- Like/unlike functionality
- Comment system
- User following/followers
- Hashtag support
- Notification system

Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
- Django documentation
- Bootstrap framework
- All contributors who have helped improve this project

