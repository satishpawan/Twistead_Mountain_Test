                 Jr. Software Engineer (Backend)– Coding Test
Scenario
You are building a lightweight backend service for managing personal tasks. Each task is tied to a
user and only visible to that user.
This app will expose both:
• REST APIs
• GraphQL listing for tasks

Rest APIs: 
1) create users using admin dashboard
   url :  http://127.0.0.1:8000/admin/
   username : admin
   password : admin
   
2)login to generate token at
  url : http://127.0.0.1:8000/signin/
  reuest data: 
  {
    "username": "Test1",
    "password": "Admin@123"
  }
  response :
  {
    "token": "0bf51db47d45816613ed672e9834fcd2138f96e8"
  }

3) auth user token at
 url : http://127.0.0.1:8000/api-token-auth/

request data : {
    "username" : "Test1",
    "password" : "Admin@123"
}
response : {
    "token": "0bf51db47d45816613ed672e9834fcd2138f96e8",
    "username": "Test1",
    "email": ""
}

4) get all the tasks assign to loged user only
    url : http://127.0.0.1:8000/api-task/
    method : GET
    in header autherization token must be set
    response :[
    {
        "u_id": "c2ba167a-594f-4fa8-8c4d-172db58771d8",
        "title": "Task4",
        "status": "todo",
        "assigned_to": 2,
        "created_at": "2025-09-18T19:14:22.370038Z",
        "updated_at": "2025-09-18T19:14:22.370082Z"
    }, 
]
5) create task 
    url : http://127.0.0.1:8000/api-task/
    method : POST
    in header autherization token must be set
    request data :
     {
      "title" : "Task9"
     }
   response data :
     {
    "u_id": "8f36a206-3de2-48ec-9b3b-b7cd7a6868c5",
    "title": "Task9",
    "status": "todo",
    "assigned_to": 2,
    "created_at": "2025-09-19T06:32:32.583796Z",
    "updated_at": "2025-09-19T06:32:32.583863Z"
   }
7) update task
    url : http://127.0.0.1:8000/api-task/
    method : POST
    in header autherization token must be set
    request data :
     {
      "status" : "in_progress"
     }
    response data:
   {
    "u_id": "c2ba167a-594f-4fa8-8c4d-172db58771d8",
    "title": "Task4",
    "status": "in_progress",
    "assigned_to": 2,
    "created_at": "2025-09-18T19:14:22.370038Z",
    "updated_at": "2025-09-19T06:36:12.477032Z"
}
8)  delete task
    url : http://127.0.0.1:8000/api-task/
    method : POST
    in header autherization token must be set
    query param : u_id
    response :
    {
    "message": "Task deleted successfully"
    }

 • GraphQL listing for tasks
 url : http://127.0.0.1:8000/graphql/
 method : POST
 in header autherization token must be set
 request : 
 {
  "query": "query { personalTasks {uId,title, status, createdAt, updatedAt, assignedTo {id, username, email}}}"
}
 resposne : 
 {
    "data": {
        "personalTasks": [
            {
                "uId": "c2ba167a-594f-4fa8-8c4d-172db58771d8",
                "title": "Task4",
                "status": "IN_PROGRESS",
                "createdAt": "2025-09-18T19:14:22.370038+00:00",
                "updatedAt": "2025-09-19T06:36:12.477032+00:00",
                "assignedTo": {
                    "id": "2",
                    "username": "Test1",
                    "email": ""
                }
            }
        ]
    }
}
 
