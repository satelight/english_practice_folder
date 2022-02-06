from models import session, English
from sqlalchemy import desc
from flask import Flask,render_template,request,redirect,url_for,Response
from sqlalchemy.sql.expression import func,select
app = Flask(__name__)

@app.route('/')
def index():
    items = session.query(English).all()
    session.close()
    return render_template('index.html',items=items)

@app.route('/input',methods=["GET","POST"])
def input():
    items = session.query(English).order_by(desc(English.id)).all()
    if request.method == "POST":
        insert_data = English()
        insert_data.english_sentence = request.form["english_sentence"]
        insert_data.japanese_sentence = request.form["japanese_sentence"]
        insert_data.master_check = False
        session.add(insert_data)
        session.commit()
        session.close()
        return redirect(url_for('input'))
    return render_template('question_insert.html',items=items)


@app.route('/update/<int:id>',methods=["GET","POST"])
def update(id):
    english_data = session.query(English).get(id)
    if request.method == "POST":
        english_data.english_sentence = request.form["english_sentence"]
        english_data.japanese_sentence = request.form["japanese_sentence"]
        session.add(english_data)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    return render_template('update.html',item=english_data)

@app.route('/confirm_test', methods=["GET", "POST"])
def confirm_test():
    english_data = session.query(English).order_by(func.random()).all()
    return render_template('confirm_test.html', items=english_data)


@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    english_data = session.query(English).get(id)
    if request.method == "POST":
        session.delete(english_data)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    return render_template('delete.html',item=english_data)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=60003)
