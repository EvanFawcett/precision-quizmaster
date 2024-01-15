from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# A list to store quiz questions and answers
quiz_data = {}


@app.route('/')
def index(): 
    return render_template('index.html', quiz_data=quiz_data)  

@app.route('/submit_set', methods=['POST'])
def submit_set():
    if request.method =='POST':
        #Retrieve data from the form
        question = request.form.get('question')

        # Store the quiz data using a nested dictionary structure
        if question not in quiz_data:
            quiz_data[question] = {'answers': {}}

        # Loop through the submitted form data to gather answers and follow-up questions
        for i in range(1, 10):
            answer_key = f'answer{i}'
            follow_up_key = f'follow_up_question{i}'

            answer = request.form.get(answer_key)
            follow_up_question = request.form.get(follow_up_key)

            # Check if the answer is not empty
            if answer:
                quiz_data[question]['answers'][answer] = {'next_question': follow_up_question}

    return render_template('index.html', quiz_data=quiz_data)

@app.route('/follow_up_question', methods=['POST'])
def follow_up_question():
    if request.method == 'POST':
        # Retrieve data from the form
        parent_question = request.form.get('parent_question')
        parent_answer = request.form.get('parent_answer')

        return render_template('follow_up_question.html', parent_question=parent_question, parent_answer=parent_answer)

if __name__ == '__main__':
    app.run(debug=True)
