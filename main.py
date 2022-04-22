import smtplib
import sqlite3
from flask import Flask, session, render_template
from fpdf import FPDF, XPos, YPos
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from functions import results_compare_items, results_reasoning, login_required, results_reasoning_pdf, \
    results_compare_items_pdf
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
    answers_reasoning = results_reasoning_pdf()
    answers_compare_items = results_compare_items_pdf()

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
    pdf.set_font('DejaVu', size=10)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 5
    pdf.cell(0, 0, 'TEST ROZUMOWANIE', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.ln(line_height)
    heading = ['Nr testu', 'Twierdzenie', 'Pytanie', 'Poprawna odp.', 'Twoja odp.']
    for item in heading:
        pdf.multi_cell(col_width, line_height, item,
                       new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
    pdf.ln(line_height)
    for item in answers_reasoning:
        for el in item:
            el = str(el)
            pdf.multi_cell(col_width, line_height, el, border=1,
                           new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
        pdf.ln(line_height)
    pdf.ln(line_height)
    pdf.ln(line_height)

    pdf.cell(0, 0, 'TEST PORÓWNYWANIE ELEMENTÓW', align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.ln(line_height)
    heading = ['Nr testu', 'Litery 1', 'Litery 2', 'Poprawna odp.', 'Twoja odp.']
    for item in heading:
        pdf.multi_cell(col_width, line_height, item,
                       new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
    pdf.ln(line_height)
    for item in answers_compare_items:
        for el in item:
            el = str(el)
            pdf.multi_cell(col_width, line_height, el, border=1,
                           new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
        pdf.ln(line_height)

    pdf.output('pdf_results.pdf')

    msg = MIMEMultipart()
    msg['Subject'] = 'Wynik testu'
    msg['From'] = 'Testy GIA'
    msg['To'] = session['email_address']

    content = '''Witaj

    W załączniku przesyłamy wyniki testów.

    Miłego dnia,
    Testy GIA'''
    body = MIMEText(content, 'plain')
    msg.attach(body)

    compare_items_file = 'pdf_results.pdf'
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
