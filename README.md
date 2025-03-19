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
- Now run this command -                                                      python run.py

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
        
        1.2 Verify Email
        - Endpoint: /verify
        - Method: GET
        - Query Parameter:
          /auth/verify?token=your_verification_token
        - Response (Success - 200 OK):
          {
            "message": "Email verified successfully. You can now log in."
          }
          
        1.3 User Login
          - Endpoint: /login
          - Method: POST
          - Request Body(JSON):
            {
              "email_address":"bharataggatrwal2k2@gmail.com"
              "password":"SecurePass123"
            }  
          - Response (Success - 200 OK):
          {
            "message": "Success!! Welcome Bharat Aggarwal"
          }
         - Response (Error - 400 Bad Request):
          {
            "error": "Username or password are not matched! or Email Verification is not done. Please try again."
          }
    2. Post Management
       
       2.1 Fetch All Posts
         - Endpoint: /event-page
         - method: POST
         - Response (Success - 200 OK):
           [
             {
                 "id": 1,
                 "post_title": "First Post",
                 "post_description": "This is my first post.",
                 "created_at": "2025-03-19 20:26:07.973093"
                 "updated_at": "2025-03-19 20:26:07.973093"
             }
   
       2.2 Create a New Post
         - Endpoint: /create-post
         - method: POST
         - Request Body (JSON):
            {
              "title": "My Second Post",
              "content": "This is an amazing post about APIs!"
            }
         - Response (Success - 201 Created):
            {
              "message": "Post is created successfully."
            }
   
          
       2.3 Update a Post
         - Endpoint: /update-post/{id}
         - method: PUT
         - Request Body (JSON):
            {
              "title": "Updated Title",
              "content": "Updated content...."
            }
         - Response (Success - 201 Created):
            {
              "message": "Post Updated Successfully."
            }

       2.4 Delete a Post
          - Endpoint: /delete-post{id}
          - method: DELETE
          - Response (Success - 201 Created):
            {
              "message": "Post deleted Successfully."
            }

    3. Error Handling
       If something goes wrong, the API will return an error response like this:

          - Status Code: 400 Bad Request
          Response (Example):
          {
            "error": "Username Already exists."
          }
        
    4. Authentication & Security
        - Users must register and verify their email before logging in.
        - Authenticated users get a JWT token for authorization.

  

  
  
