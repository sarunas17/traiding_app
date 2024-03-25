from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(vartotojo_id):
    return User.query.get(int(vartotojo_id))

@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login failed. Check email and password', 'danger')
    return render_template("login.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/register")
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        encrypted_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.nem.data, email=form.email.data, password=encrypted_pass)
        db.session.add(user)
        db.session.commit()
        flash('Registration successfull. You can login now.', 'success')
        return redirect(url_for('index'))
    return render_template("register.html")


@app.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")


@app.route("/404")
def page_not_found():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')