Django CRUD Practise - Student Registration 

Overview

This Django project demonstrates a simple CRUD (Create, Read, Update, Delete) application for managing student registrations. The system allows users to add, view, update, and delete student records dynamically. It is implemented with a user-friendly interface using Bootstrap for styling.

Features

1. Student Registration Form
	•	A Bootstrap-styled form is provided to register new students.
	•	Form fields include:
	•	Name
	•	Email
	•	Mobile
	•	Course

2. Student Records Table
	•	A dynamic table adjacent to the registration form displays all registered students.
	•	Each record includes:
	•	Student ID
	•	Name
	•	Email
	•	Mobile
	•	Course
	•	Action Buttons: Update and Delete

3. Dynamic Operations
	•	Add Student:
	•	Upon form submission, a new student record is added to the database and dynamically reflected in the table.
	•	Update Student:
	•	Clicking the Update button for a specific student redirects to update.html, where the form is pre-filled with the student’s current details.
	•	After submitting the updated form, changes are saved to the database and reflected in the table.
	•	Delete Student:
	•	Clicking the Delete button removes the corresponding student record dynamically from the table and database.

Technical Details

Frameworks & Tools
	•	Backend: Django
	•	Frontend: HTML, CSS, Bootstrap
	•	Database: SQLite 

student_crud_project/
├── manage.py
├── student_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── update.html
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
├── db.sqlite3
└── static/
    ├── css/
    └── js/
    
Key Files
	1.	views.py
	•	Handles logic for creating, updating, reading, and deleting student records.
	2.	models.py
	•	Defines the Student model with fields for name, email, mobile, and course.
	3.	home.html
	•	Displays the registration form and the dynamic table of student records.
	4.	update.html
	•	Contains the update form pre-filled with selected student details.

Installation & Setup
 
 1.	Clone the repository:
 
   	    git clone <repository_url>
        cd practise


	2.	Install dependencies:

            pip install django


	3.	Run migrations:

            python manage.py makemigrations
            python manage.py migrate


	4.	Start the development server:

            python manage.py runserver


	5.	Open the application in your browser:

            http://127.0.0.1:8000/

Usage
	1.	Add a student by filling in the registration form and clicking the Enroll button.
	2.	View all registered students in the dynamic table.
	3.	Update a student’s details:
	•	Click the Update button for a specific student.
	•	Modify the details in the pre-filled form on the update page.
	•	Submit the updated form to save changes.
	4.	Delete a student:
	•	Click the Delete button for a specific student to remove their record.

Screenshots
	1.	Home Page with Form and Table
<img width="1440" alt="Screenshot 2024-12-19 at 2 56 32 PM" src="https://github.com/user-attachments/assets/94ca3ef9-8565-48a5-9c72-165d51017404" />
	2.	Update Page
 <img width="1439" alt="Screenshot 2024-12-19 at 2 57 44 PM" src="https://github.com/user-attachments/assets/4f1b8c11-a462-45d0-a73d-acc96df16f2a" />


Future Enhancements
	•	Add search functionality for filtering student records.
	•	Implement pagination for large datasets.
	•	Include a confirmation prompt before deleting a record.

License

This project is licensed under the MIT License.

Let me know if you need further refinements!
