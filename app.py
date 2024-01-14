from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index(): 
    return render_template('index.html')  

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    if request.method =='POST':
        #Retrieve data from the form
        question = request.form.get('question')
        answer1 = request.form.get('answer1')
        answer2 = request.form.get('answer2')

        # For now, just print the data and modify later
        print(f"Question: {question}")
        print(f"Answer 1: {answer1}")
        print(f"Answer 2: {answer2}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
