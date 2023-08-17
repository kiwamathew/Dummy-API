from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/courses')
def get_courses():
    courses = [
    {
       "course_name" : "a",
       "rating" : "b",
       "department" : "c",
       "duration" : "d"
    },
    {

       "course_name" : "e",
       "rating" : "f",
       "department" : "g",
       "duration" : "h"
    },
    {

       "course_name" : "i",
       "rating" : "j",
       "department" : "k",
       "duration" : "l"
    },
    {

       "course_name" : "m",
       "rating" : "n",
       "department" : "o",
       "duration" : "p"
    },
    {

       "course_name" : "q",
       "rating" : "r",
       "department" : "s",
       "duration" : "t"
    }

]
    return jsonify(courses)

if __name__== "__main__":
    app.run(debug=True)
