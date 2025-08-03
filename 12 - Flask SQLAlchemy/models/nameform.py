# Importa a classe principal da extensão Flask-WTF, que integra a biblioteca wtforms.
from flask_wtf import FlaskForm
# Importa os tipos de campo `StringField` (para texto) e `SubmitField` (para botão de envio) do WTForms.
from wtforms import StringField, SubmitField
# Importa o validador `DataRequired`, que garante que um campo não seja enviado vazio.
from wtforms.validators import DataRequired
# Importa a classe datetime do módulo padrão do Python para trabalhar com datas e horas.

# Define uma classe de formulário `NameForm` que herda de `FlaskForm`.
class NameForm(FlaskForm):
    # Cria um campo de texto com o rótulo 'Qual é o seu nome?' e um validador que exige preenchimento.
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    # Cria um botão de envio com o rótulo 'Enviar'.
    submit = SubmitField('Enviar')