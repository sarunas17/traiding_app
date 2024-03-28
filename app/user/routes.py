from flask import render_template
from app.user import bp



@login_manager.user_loader
def load_user(vartotojo_id):
    return User.query.get(int(vartotojo_id))

@bp.route("/login")
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

@bp.route("/register")
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


@bp.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")

