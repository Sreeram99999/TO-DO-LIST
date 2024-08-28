# Django To-Do List Application

Project Description:
This project is a simple To-Do List application built using the Django framework. It allows users to add tasks with descriptions, view a list of all tasks, and manage completed tasks by moving them to a history section where they can be deleted. The project leverages Django's built-in admin interface to store and manage data in the database.

Features:
    ->Add Tasks: Input fields for task name and description.
    ->View Task List: Navigate to a list of all tasks.
    ->Mark as Completed: Completed tasks are moved to a history section.
    ->Delete Tasks: Delete tasks from the history section.
    ->Admin Interface: Manage tasks and other data through Django's admin panel.

Installation:
Clone the Repository:
  git clone https://github.com/Sreeram99999/TO-DO-LIST.git
  cd TO-DO-LIST
  
Create a Virtual Environment:
  python3 -m venv venv
  source venv/bin/activate
  
Create a Superuser (for Django Admin):
  python manage.py createsuperuser
  
Run the Development Server:
  python manage.py runserver

Access the Application:
    Visit http://127.0.0.1:8000/ in your web browser to access the To-Do List application.
    Visit http://127.0.0.1:8000/admin/ to access the Django admin panel.
    
Usage:
    Adding Tasks:
        Navigate to the task creation page.
        Enter the task name and description.
        Submit to add the task to your list.
    Viewing Tasks:
        Navigate to the task list page to see all your tasks.
    Completing and Managing Tasks:
        Mark tasks as completed, which will move them to the history section.
        Delete tasks from the history if they are no longer needed.

Technologies Used:
    Django: Web framework for building the application.
    Python: Programming language used in development.
    SQLite: Default database used by Django (can be switched to other databases).
