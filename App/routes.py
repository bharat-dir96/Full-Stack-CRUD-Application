from App import app
from flask import render_template, redirect, url_for, flash, session, request
from App.models import User, Post
from App.forms import RegisterForm, LoginForm, PostForm
from App import db, mail
from flask_login import login_user, logout_user, current_user
from flask_mail import Message
import secrets


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    token = None

    if request.method == 'POST' and form.validate_on_submit():
        user_to_create = User(username = form.username.data,
        full_name = form.full_name.data,
        email_address=form.email_address.data,
        job_title=form.job_title.data,
        password=form.password1.data
        )

        token = generate_verification_token(user_to_create.email_address)
        print(token)
        user_to_create.verification_token=token
        db.session.add(user_to_create)
        db.session.commit()
        verification_link = url_for('verify_email', token=token, _external=True)
        print(verification_link)

        # Mail to send to the registered users fto verify thier account.
        msg = Message('Verify Your Email', sender='bharat.aggarwal@iic.ac.in', recipients=[user_to_create.email_address])
        msg.body = f'Click on the following link to verify your email: {verification_link}'
        mail.send(msg)        

        return redirect(url_for('redirect_page'))

    return render_template('register.html', form=form)

def generate_verification_token(email):
    token = secrets.token_hex(16)                       #To Generate a random token
    return token

@app.route('/redirect')                                         #Redirect route to wait for user to verify their email.
def redirect_page():
    return render_template('redirect.html')


@app.route('/verify')                                           #Route to verify the unique token send to a user to their mail to redirect them to login page.
def verify_email():
    token = request.args.get('token')
    print(token)
    user = User.query.filter_by(verification_token=token).first()

    if user:
        user.is_verified = True
        print(user.is_verified)
        db.session.commit()
        flash('Your email has been verified. You can now log in.', 'success')
        return redirect(url_for('login_page'))

    else:
        flash('Invalid verification token. Please try again.', 'danger')
        return redirect(url_for('register_page'))

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        print(attempted_user)

        if attempted_user and attempted_user.is_verified and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            attempted_user.update_last_login()
            flash(f'Sucess!! Welcome {attempted_user.full_name}', category='success')
            return redirect(url_for('event_page'))

        else:
            flash(f'Username or password are not matched! or Email Verification is not done. Please try again', category='danger')


    return render_template('login.html', form=form)

@app.route("/logout")                                           #logout Route to end the cuurent session.
def logout_page():
    logout_user()
    session.clear()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page')) 

@app.route("/event-page")                   #route for redirecting the authenticated users to the main event page.
def event_page():
    current_posts = Post.query.all()
    return render_template('event_page.html', current_posts=current_posts)

@app.route("/create-post", methods=['GET','POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post_created = Post(post_title=form.title.data,
                            post_description=form.description.data)
        db.session.add(post_created)
        db.session.commit()
        flash('Post is successfully created', category='success')

        return redirect(url_for('event_page'))

    return render_template('create_post.html', form=form)

@app.route("/update-post/<int:post_id>", methods=['GET','POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)  
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.post_title = form.title.data
        post.post_description = form.description.data
        db.session.commit()
        flash('Post Updated successfully', category='success')
        return redirect(url_for('event_page'))
    
    return render_template('update_post.html', form=form, post=post)

@app.route("/delete-post/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)  
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully', category='success')
    return redirect(url_for('event_page'))

