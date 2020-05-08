# import flask
from flask import Flask, render_template, escape, request,session,redirect  # import Flask class from flask module
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
# from werkzeug import secure_filename
import os
import math

import pymysql



with open("config.json","r") as c:
    params=json.load(c)["params"]
local_server=True
app = Flask(__name__)
app.secret_key="super-secrete-key"
app.config['UPLOAD_FOLDER']=params["upload_location"]
app.config.update(
    Mail_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL='True',
    MAIL_USERNAME=params['mail_user'],
    MAIL_PASSWORD=params['mail_password']
)
mail=Mail(app)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI']=params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/doanything'

db=SQLAlchemy(app)

class Contact(db.Model):
    # sno, name, email, phone_num, msg, date
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String (50), nullable=False)
    email=db.Column(db.String (30), nullable=False)
    phone_num=db.Column(db.String (12), nullable=False)
    msg=db.Column(db.String (120), nullable=False)
    date=db.Column(db.String (12), nullable=True)

class Posts(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String (50), nullable=False)
    slug=db.Column(db.String (30), nullable=False)
    content=db.Column(db.String (120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date=db.Column(db.String (12), nullable=True)
    img_file=db.Column(db.String (12), nullable=True)


@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['no_of_posts']))
    # Pagination logic
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page=int(page)

    posts = posts[(page-1) * int(params['no_of_posts']):(page-1) * int(params['no_of_posts']) + int(params['no_of_posts'])]

    if (page==1):
        prev='#'
        next="/?page="+str(page+1)

    elif (page == last):
        next='#'
        prev="/?page="+str(page-1)
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)



    #posts=Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template("index.html",params=params,posts=posts,prev=prev,next=next)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():

    if ('user' in session and session['user']==params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params,posts=posts)

    if request.method=='POST':
        username=request.form.get('uname')
        password = request.form.get('password')
        if (params['admin_user'] == username and params['admin_password'] == password):
            # Redirect to admin pannel
            # set the session variable
            session['user'] = username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params,posts=posts)


    else:
        return render_template("login.html", params=params)


@app.route('/about')
def about():

    return render_template("about.html",params=params)

@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params=params,post=post)



@app.route('/contact', methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        # add entry to the database
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry=Contact(name=name,email=email,phone_num=phone,msg=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        # to send mail
        '''mail.send_message("New Message From "+name.upper(),
                          sender=email,
                          recipients=[params['mail_user']],
                          body=message+"\n Phone : "+phone)
        '''


    return render_template("contact.html",params=params)


@app.route('/edit/<string:sno>', methods = [ 'GET', 'POST'] )
def edit(sno):
    print("You are in edit method")
    if ('user' in session and session['user'] == params['admin_user']):
        print("User in session ",request.method)
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            tagline = request.form.get('tagline')
            date = datetime.now()
            img_file = request.form.get('img_file')

            if (sno=='0'):
                post=Posts(title=title,slug=slug,content=content,tagline=tagline,date=date,img_file=img_file)
                db.session.add(post)
                db.session.commit()
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html",params=params,post=post)

    # return render_template("index.html", params=params, sno=sno)




            # title tagline slug content image

    #return render_template("index.html",params=params,posts=posts)

# edit is under construction...
'''


@app.route('/edit/<string:sno>', methods = ['GET','POST'])
def edit(sno):
    print("Hi 1",request.method)
    if ('user' in session and session['user']==params['admin_user']):
        print("Hi 2 : ",sno + request.method)
        if (request.method == 'POST'):
            print("Hi 3")
            title=request.form.get('title')
            tagline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date=datetime.now()

            if sno=='0':
                print("here")
                post=Posts(title=title,slug=slug,content=content,tagline=tagline,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post=Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html", params=params,sno=sno,post=post)


            # title tagline slug content image

    #return render_template("index.html",params=params,posts=posts)
'''

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    print("1")
    if ('user' in session and session['user'] == params['admin_user']):
        print("1")
        #if request.method=='POST':
        if (request.method == 'POST'):
            print("1")
            f=request.files['file1']
            print(f)
            f.save(os.path.join(app.config['UPLOAD_FOLDER']))#,secure_filename(f.filename))
            return "Uploaded successfully...!!!"




    return render_template("about.html",params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:sno>',methods=['GET','POST'])
def delete(sno):

    if ('user' in session and session['user']==params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')






app.run(debug=True)
