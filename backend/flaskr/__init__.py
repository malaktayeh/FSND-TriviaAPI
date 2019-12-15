import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after
    completing the TODOs
    '''
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type,Authorization,true'
          )
        response.headers.add(
          'Access-Control-Allow-Methods',
          'GET,PUT,POST,DELETE,OPTIONS'
          )
        return response

    '''
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    '''
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories_data = Category.query.all()
        categories = []

        for category in categories_data:
            categories.append(category.type)

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': categories,
            'total_categories': len(categories)
        })

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the
    screen for three pages.
    Clicking on the page numbers should update the questions.
    '''
    @app.route('/questions', methods=['GET'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories_data = Category.query.all()
        categories = []

        for category in categories_data:
            categories.append(category.type)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'current_category': None,
            'categories': categories
        })

    '''
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to
    a question, the question will be removed.
    This removal will persist in the database
    and when you refresh the page.
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.\
                filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except Exception:
            abort(422)
    '''
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    '''

    @app.route('/questions', methods=['POST'])
    def return_search_result():
        body = request.get_json()
        search_str = body.get('searchTerm', None)

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)

        if (body is {}):
            abort(400)
        elif (search_str is not ''):
            selection = Question.query.\
                filter(Question.question.ilike(f'%{search_str}%')).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(selection),
                'current_category': None
            })

    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at
    the end of the last page of the questions list in
    the "List" tab.
    '''
    @app.route('/questions/add', methods=['POST'])
    def add_new_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)

        if (body is {}):
            abort(400)
        else:
            try:
                question = Question(
                    question=new_question,
                    answer=new_answer,
                    difficulty=new_difficulty,
                    category=new_category
                )

                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify({
                    'success': True,
                    'created': question.id,
                    'questions': current_questions,
                    'total_questions': len(selection)
                })
            except Exception:
                abort(404)

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    '''
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def filter_questions(category_id):
        selection = Question.query.\
            filter(Question.category == str(category_id+1)).\
            order_by(Question.id).all()

        current_questions = paginate_questions(request, selection)

        if len(selection) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'current_category': category_id+1
        })

    '''
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question
    parameters and return a random questions within the given
    category, if provided, and that is not one of the previous
    questions.

    TEST: In the "Play" tab, after a user selects "All" or a
    category, one question at a time is displayed, the user
    is allowed to answer and shown whether they were correct
    or not.
    '''
    @app.route('/quizzes', methods=['POST'])
    def play_trivia():
        body = request.get_json()
        category = int(body['quiz_category']['id'])
        category_type = body['quiz_category']['type']
        previous_questions = body['previous_questions']

        if (previous_questions is None and category_type is None):
            abort(405)

        # if 'All' category has been selected
        if category_type is 'click':
            category = None
            query_by_category = Question.query.all()
        # if a specific category has been selected, get its questions
        else:
            # since ids start with one in the db, always add 1 to id
            category += 1
            query_by_category = Question.query.\
                filter(Question.category == category)

        query = [question.format() for question in query_by_category]

        # flag for while loop
        play = True
        # get random question
        question = random.choice(query)

        while (play):
            if (question.get('id') not in previous_questions):
                return jsonify({
                    'success': True,
                    'question': question,
                    'category': category+1
                })
            else:
                if (len(question) > len(previous_questions)):
                    question = random.choice(query)
                else:
                    play = False
            return jsonify({
                  'success': True,
                  'question': question,
                  'category': category+1
                })

    # '''
    # @TODO:
    # Create error handlers for all expected errors
    # including 404 and 422.
    # '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    return app
