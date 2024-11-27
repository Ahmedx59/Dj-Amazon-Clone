# Dj-Amazon-Clone

![GitHub stars][]![GitHub watchers][]![GitHub forks][]

## Description
Dj-Amazon-Clone is a Django Rest API designed to power your e-commerce platform. It provides a comprehensive set of features and functionalities to build and manage your online store. This project aims to replicate the core functionality and user experience of the popular e-commerce platform Amazon.

## Tech Stack
The Dj-Amazon-Clone project utilizes the following technologies:
- Python: The backend of the project is developed using Python, a versatile and powerful programming language.
- Django: Django is a high-level Python web framework that provides a clean and efficient way to build web applications.
- Django Rest Framework: Django Rest Framework is a powerful and flexible toolkit for building Web APIs.
- Docker: Docker is used for containerization, allowing for easy deployment and scalability.
- Redis: Redis is an in-memory data structure store used for caching and session management.
- SQLite/PostgreSQL: The project supports both SQLite and PostgreSQL as database options.
- Stripe: Stripe is integrated for payment processing and handling transactions.
- Ajax: Ajax is used to create dynamic and interactive user interfaces.
- Celery: Celery is used for task scheduling and distributed message passing.
- Postman: Postman is utilized for testing and documenting the API endpoints.
- HTML/CSS/SCSS: HTML, CSS, and SCSS are used for designing and styling the frontend components.
- JavaScript: JavaScript is used for adding interactivity and enhancing user experience.

## Installation and Usage
To set up and run the Dj-Amazon-Clone project locally, please follow the instructions below:
1. Clone the repository:
   ```bash
   git clone https://github.com/Omarmoatz/Dj-Amazon-Clone.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Dj-Amazon-Clone
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - If using SQLite:
     ```bash
     python manage.py migrate
     ```
   - If using PostgreSQL:
     ```bash
     # Update the database settings in settings.py to match your PostgreSQL configuration
     python manage.py migrate
     ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the API endpoints at `http://localhost:8000/api/`.

## Contributing
Contributions are welcome! If you would like to contribute to Dj-Amazon-Clone, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit your code.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Preview
![](screenshot.png)



