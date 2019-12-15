# Full Stack API - CRUD APP
## Trivia API

A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game.
The application does the following:

1) Display questions - both all questions and by category. Questions show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 


## About the Stack
* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **React.js** for our website's frontend


## Project Structure

### Backend
The `./backend` directory contains a Flask and SQLAlchemy server. Endpoints have been defined in app.py, models for database and SQLAlchemy setup can be found in models.py. 

### Frontend
The `./frontend` directory contains a complete React frontend to consume the data from the Flask server.


## Development Setup
To start and run the app please do the following:


#### Backend

- Please make sure that you installed all above-mentioned dependencies
- Cd into the backend folder and run:
  ```
  $ pip install -r requirements.txt
  ```
- Run the development server:
  ```
  $ export FLASK_APP=flaskr
  $ export FLASK_ENV=development # enables debug mode
  $ flask run
  ```
- Test your endpoints and/or curl via [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  


#### Frontend

- Again, make sure that you have all the dependencies installed ([Node.js](https://nodejs.org/en/download/))
- Cd into frontend folder with your command line tool of choice
- Run npm install and npm run subsequently
- Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```
- Navigate to Home page [http://localhost:5000](http://localhost:5000)


## API Endpoints

### GET '/categories'
#### General:
- Returns a list of categories, the total number of categories and a success message
- Sample: curl http://127.0.0.1:5000/categories

```json
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "success": true,
    "total_categories": 6
}
```

### GET '/questions'
#### General:
    - Returns a list of questions, categories, success value, success message, and a total number of questions
    - Results are paginated
    - Sample: curl http://127.0.0.1:5000/questions
```json
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
        ],
    "current_category": null,
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
            {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        }
    ],
    "success": true,
    "total_questions": 17
}
```
### DELETE '/questions/{id}'
#### General:
    - Returns a new list of paginated questions minus the deleted one, a success message, the id of the deleted item, and a total number of questions
    - Sample: curl -X DELETE http://127.0.0.1:5000/questions/1

### POST '/questions'
### General:
    - Returns a filtered list of questions based on search term, a success message, and the total number of questions.
    - Results are paginated
    - Sample: curl http://localhost:5000/questions -H "Content-Type: application/json" -d "{'search_term': 'title'}" -X POST
```json
{
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```
### POST '/questions/add'
### General:
    - Returns a filtered list of questions plus new question, a success message, the total number of questions, and the new question id.
    - Results are paginated
    - Sample: curl -X POST http://127.0.0.1:5000/questions/add -H "Content-Type: application/json" -d '{"question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", "answer": "Edward Scissorhands", "difficulty": 3, "category": 5}'
```json
{
  "created": 195,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 17
}
```

    
### GET '/categories/{id}/questions'
### General:
    - Returns a list of questions based on selected category, a success message, and the id of the category
    - Results are paginated
    - Sample: curl http://127.0.0.1:5000/categories/2/questions
```json
{
  "current_category": 3,
  "questions": [
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true
}
```
    
### POST '/quizzes'
### General:
    - Returns a random question from the selected category, a success message, and the id of the category
    - Sample: curl -X POST http://localhost:5000/quizzes -H "Content-Type: application/json" -d '{ "previous_questions": [], "quiz_category": {"type": "Sports", "id": 5 }}'
```json
{

}
```



## Source
This repository has been downloaded and locally worked on from [Udacity](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter). 