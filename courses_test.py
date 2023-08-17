from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/courses')
def get_courses():
    courses = [
    {
       "course_name" : "Introduction to python programming",
       "rating" : "2/10",
       "department" : "Computer science",
       "duration" : "80 minutes"
    },
    {

       "course_name" : "Web development fundamentals",
       "rating" : "4/10",
       "department" : "Information technology",
       "duration" : "100 minutes"
    },
    {

       "course_name" : "User experience designer",
       "rating" : "7/10",
       "department" : "Development",
       "duration" : "100 minutes"
    },
    {

       "course_name" : "Data scientist",
       "rating" : "6/10",
       "department" : "Information technology",
       "duration" : "120 minutes"
    },
    {

       "course_name" : "Web administration",
       "rating" : "1/10",
       "department" : "Administration",
       "duration" : "200 minutes"
    }

]
    return jsonify(courses)

if __name__== "__main__":
    app.run(debug=True)
