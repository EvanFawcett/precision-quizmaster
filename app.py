from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# A list to store quiz questions and answers
quiz_data = {}


@app.route('/')
def index(): 
    return render_template('index.html', quiz_data=quiz_data)  

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
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

                # For now, just print the data and modify later
                print(f"Answer {i}: {answer} - Follow-up Question: {follow_up_question}")

                # Check if a follow-up question is provided and create answer fields for it
                if follow_up_question:
                    for j in range(1, 10):
                        follow_up_answer_key = f'answer_{i}_follow_up_{j}'
                        follow_up_answer = request.form.get(follow_up_answer_key)

                        if follow_up_answer:
                            quiz_data[follow_up_question]['answers'][follow_up_answer] = {'next_question': ''}


    return render_template('index.html', quiz_data=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
