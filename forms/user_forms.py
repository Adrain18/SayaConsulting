# user_forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from models.users import User, Position, Role
from flask_wtf.file import FileField, FileRequired, FileAllowed

class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    name = StringField('Nombre', validators=[DataRequired()])
    ape_pat = StringField('Apellido Paterno', validators=[DataRequired()])
    ape_mat = StringField('Apellido Materno', validators=[DataRequired()])
    direction = StringField('Dirección', validators=[DataRequired()])
    id_position = SelectField('Posición', coerce=int, validators=[DataRequired()], choices=[])
    id_role = SelectField('Rol', coerce=int, validators=[DataRequired()], choices=[])
    image = FileField('Imagen', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes en formato JPG o PNG')])
    submit = SubmitField('Registrar')

    # Validar Correo Unico
    def validate_email(self, field):
        if User.check_email(field.data):
            raise ValidationError('El correo ya existe')

    # Validar Username Unico
    def validate_username(self, field):
        if User.check_username(field.data):
            raise ValidationError('El username ya existe')

################# Formulario de Login ##################
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class UpdateProfileForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    name = StringField('Nombre', validators=[DataRequired()])
    ape_pat = StringField('Apellido Paterno', validators=[DataRequired()])
    ape_mat = StringField('Apellido Materno', validators=[DataRequired()])
    direction = StringField('Dirección', validators=[DataRequired()])
    id_position = SelectField('Posición', coerce=int, validators=[DataRequired()], choices=[])
    id_role = SelectField('Rol', coerce=int, validators=[DataRequired()], choices=[])
    submit = SubmitField('Actualizar')

