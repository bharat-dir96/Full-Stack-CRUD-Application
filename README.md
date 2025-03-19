Here’s a brief description about this project:  

- Developed a **Full Stack CRUD Application** with user authentication and post management.  
- New users can **register** and get **verified via email** before logging in.  
- After verification, users can **log in** to access the **main event page** where all posts are displayed.  
- Users can **create new posts** using the **"Create New Post"** button.  
- Users can **update or delete their posts**, with changes **instantly reflecting** on the live posts page.  

Steps to setup and run the project successfully:
- First clone this git repo using following command in your terminal - git clone https://github.com/bharat-dir96/Full-Stack-CRUD-Application.git
- Then Head over to the repo folder

- Now, First Install the requirements file with this command -                pip install -r requirements.txt
- Now run this command python -                                               python run.py

  This will run this application into your browser and you can interact with it efficiently.
  You can do the following operations -
  - Register as a New User
  - Login using your credentials
  - Create New Post
  - Read All Posts
  - Update Your Post
  - Delete Your Post
 
    Base URL:
    http://127.0.0.1:5000/

    1. User Authentication
       1.1 Register a New User
       - Endpoint: /register
       - method: POST
       - Request Body(JSON):
         {
         "username":"Bharat9647"
         "full_name":"Bharat Aggarwal"
         "email_address":"bharataggarwal2k2@gmail.com"
         "job_title":"Software Developer"
         "password":"SecurePass123"
           }

      - Response (Success - 201 Created):
        {
          "message": "User registered successfully. Please check your email for verification."
        }
      - Response (Error - 400 Bad Request):
        {
          "error": "Email already exists."
        }


        
  

  

  
  
