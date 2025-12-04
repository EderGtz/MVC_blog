from flask import Blueprint, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash
from .models import get_all_blogs, get_user_by_username, create_blog_entry
#Connecting URL's

blog_bp = Blueprint("blog", __name__)

@blog_bp.route('/')
def home():
    blogs = get_all_blogs()
    return render_template('indexBlog.html', blogs=blogs)

@blog_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = get_user_by_username(username)

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('blog.post_blog_page'))
        else:
            return "Credenciales invalidas"
    return render_template('login.html')

@blog_bp.route('/post', methods=['GET','POST'])
def post_blog_page():

    if 'username' not in session:
        return redirect(url_for('blog.login'))
    
    if request.method == "POST":
        title = request.form.get('title')
        date = request.form.get('date')
        body = request.form.get('body_text')
        
        if create_blog_entry(title, date, body):
            return redirect(url_for('blog.home'))
        else:
            return "Error al guardar"
    return render_template('postblog.html')

@blog_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.home'))