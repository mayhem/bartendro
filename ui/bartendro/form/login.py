from wtforms import Form, StringField, PasswordField, SubmitField, SelectField, validators


class LoginForm(Form):
    user = StringField("Name", [validators.Length(min=3, max=255)])
    password = PasswordField("Password", [validators.Length(min=3, max=255)])

    login = SubmitField("login")


form = LoginForm()
