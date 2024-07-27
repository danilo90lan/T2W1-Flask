from flask import Flask, request

app = Flask(__name__)


#defining a route
@app.route("/")     # "/" means the main page
def welcome():
    return "Hello, welcome to testing API using Flask"

@app.route("/")
def welcome_again():
    return "ciao"

@app.route("/about")
def about():
    return "about page"

@app.route("/contact")
def contact():
    return "My contact details are ........."

courses = [
    {
        "code":101,
        "name":"diploma of IT",
        "duration":"1.5 years"
    },

    {
        "code":101,
        "name":"diploma of IT",
        "duration":"1.5 years"
    },

    {
        "code":101,
        "name":"diploma of IT",
        "duration":"1.5 years"
    }
]

# @app.route("/courses")
# def list_courses():
#     return courses

@app.route("/courses/101")
def get_course_101():
    return courses[0]

@app.route("/courses/200")
def error_route():
    return {"error":404}

@app.route("/courses")
def list_courses():
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)]
    return courses

# POST Request
# add a new course
@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json()
    courses.append(body)
    return courses

# DELETE Request
# Delete a course
@app.route("/courses/107", methods=["DELETE"])
def delete_course_107():
    del courses[-1]
    return {"message":"deleted succesfully"}

# PUT Request
# Updating an entire course
@app.route("/courses/107", methods=["PUT"])
def update_course_107():
    body = request.get_json()
    courses[-1] = body
    return courses[-1] 

#PATCH request
@app.route("/courses/101", methods=["PATCH"])
def update_101():
    body = request.get_json()
    courses[0]["duration"] = body.get("duration") or courses[0]["duration"]
    return courses[0]

if __name__=="__main__":
    app.run(debug=True)