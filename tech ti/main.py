from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlit:///eticket.db'
db=SQLAlchemy(app)

class eticket(db.model):
    name=db.coloumn(db.spring(100), nullable=False)
    admission_no=db.coloumn(db.spring(100), primary_key=False)
    destination=db.coloumn(db.spring(100), nullable=False)
    way=db.coloumn(db.integer,default=0)

db.create_all()    


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    admission_no=request.form['admission no.']
    destination=request.form['destination']
    way=request.form['way']
    new_ticket=ticket(name=name,admission_no=admission_no,destination=destination,way=way)
    db.session.add(new_ticket)
    db.session.commit()
    return 'ticket added successfully'


if __name__=="__main__":
    app.run(debug=True)