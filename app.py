from QuestionAnsweringFinal import *
from SummarizerFinal import *
from flask import Flask, render_template, request
from markupsafe import Markup
import mysql.connector
mydb =  mysql.connector.connect(host="localhost", user="root", passwd="samul54321",database="summarizerandqamodel",auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
sql = "INSERT INTO data (Article,Summary,Question,Answer,Probability) VALUES(%s,%s,%s,%s,%s)"
app = Flask(__name__)
headings = ("Article","Summary","Question","Answer","Probability")
@app.route('/')
def home():
    return render_template('index.html') 
@app.route('/summerizer_and_qa',methods=['GET','POST'])
def summerizer_and_qa():
    article=request.form['article']
    question=request.form['question']
    sumArticle=summarizer(article)
    answer, probability=questionAnswering(article,question)
    val = (article,sumArticle,question,answer,probability)
    mycursor.execute(sql,val)
    mydb.commit()
    value1 = Markup('<p>{0}</p>').format(sumArticle)
    value2 = Markup('<h2>Summarized Article</h2>')
    value4 = Markup('<span>OUTPUT</span>')
    value3 = Markup('<h2>The answer of the question is:- {0}. And the probability of the answer being correct is {1}%</h2>').format(answer,probability)
    return render_template('index.html',summary=value1,tag=value2, answer=value3, tag2=value4)
@app.route('/db_dump', methods=['GET','POST'])
def db_dump():
    mycursor.execute("SELECT * FROM data")
    result= mycursor.fetchall()
    return render_template('db_show.html',data = result,headings=headings)
