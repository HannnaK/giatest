import smtplib
from flask import Flask, session, render_template
from fpdf import FPDF
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from functions import results_compare_items, results_reasoning, login_required
from registration_login import auth_bp
from solving_tests import solving_tests_bp
from api_gia import api_gia_bp
from login_mail import user, password

app = Flask(__name__)
app.secret_key = 'secret-key-1103'
app.register_blueprint(auth_bp)
app.register_blueprint(solving_tests_bp)
app.register_blueprint(api_gia_bp)


@app.route('/')
def welcome():
    if session:

        user = session['username']
    else:
        user = None
    return render_template('welcome.html', user=user)


@app.route('/results', endpoint='results')
@login_required
def results():
    answers_reasoning = results_reasoning()
    answers_compare_items = results_compare_items()

    return render_template('results.html', answers_reasoning=answers_reasoning,
                           answers_compare_items=answers_compare_items)


@app.route('/send_email', endpoint='send_email')
@login_required
def send_email():
    answers_compare_items = results_compare_items()

    pdf_compare_items = FPDF()
    pdf_compare_items.add_page()
    pdf_compare_items.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
    pdf_compare_items.set_font('DejaVu', size=14)
    print(answers_compare_items)
    pdf_compare_items.cell(200, 10, txt='TO jest', ln=1)
    for aci in answers_compare_items:
        aci = str(aci)
        pdf_compare_items.cell(200, 10, txt=aci, ln=2)
    pdf_compare_items.output("pdf_compare_items.pdf")

    msg = MIMEMultipart()
    msg['Subject'] = 'Wynik testu'
    msg['From'] = 'Testy GIA'
    msg['To'] = 'hankakokocinska@wp.pl'

    content = '''Witaj

    W załączniku przesyłamy wyniki testów.

    Miłego dnia,
    Testy GIA'''
    body = MIMEText(content, 'plain')
    msg.attach(body)

    compare_items_file = 'pdf_compare_items.pdf'
    with open(compare_items_file, mode='rb') as f:
        part = MIMEApplication(f.read(), Name=basename(compare_items_file))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(compare_items_file))
    msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)

    return ('wysłany mail')


if __name__ == '__main__':
    app.run(debug=True)
