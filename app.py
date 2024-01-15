from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# A list to store quiz questions and answers
quiz_data = []


@app.route('/')
def index(): 
    return render_template('index.html', quiz_data=quiz_data)  

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    if request.method =='POST':
        #Retrieve data from the form
        question = request.form.get('question')
        
        # Use a list comprehension to gather all answers dynamically
        answers = [request.form.get(f'answer{i}') for i in range(1, 10) if request.form.get(f'answer{i}')]

        # Store the quiz data
        quiz_data.append({
            'question': question,
            'answers': answers
        })

        # For now, just print the data and modify later
        print(f"Question: {question}")
        for i, answer in enumerate(answers):
            print(f"Answer {i + 1}: {answer}")


    return render_template('index.html', quiz_data=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
