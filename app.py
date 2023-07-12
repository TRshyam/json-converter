from flask import Flask,render_template,request


# class q_BANK:
#     def __init__(self,id,question,mark,difficulty,type,answer):
#         self.id=id
#         self.question=question
#         self.mark=mark
#         self.difficulty=difficulty
#         self.type=type
#         self.answer=answer
#     def __repr__(self):
#         return f'<q_BANK:{}'
#         pass



app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@ app.route("/login",methods=['POST','GET'])
def login():
    question=request.form["question"]
    mark=request.form["mark"]
    difficulty=request.form["difficulty"]
    type=request.form["type"]
    answer=request.form["answer"]
    print(answer,type,difficulty,mark,question)
    return render_template('d.html',que=question)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)