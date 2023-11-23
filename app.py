import smtplib
import random
import ssl
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, email_message)


@app.route('/', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        sender_email = "oceanly204@gmail.com"
        sender_password = "lyihkkozuiqofazp"
        recipient_email = request.form['email']
        subject = 'OTP FOR OCEANLY NETWORKS'
        otp = random.randint(100000, 999999)
        message = "YOUR ONE TIME PASSWORD IS {}".format(otp)
        
        send_email(sender_email, sender_password, recipient_email, subject, message)
        
        # Store the OTP and recipient email in session for verification
        session['otp'] = otp
        session['recipient_email'] = recipient_email
        
        return redirect('/verification')
    
    return render_template('forgot_password.html')


@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        
        if session['otp'] == int(entered_otp):
            # OTP verification successful, redirect to home page 
            return redirect('/home')
        else:
            error = "Invalid OTP. Please try again."
            return render_template('verification.html', error=error)
    
    return render_template('verification.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/aboutus.html')
def about_us():
    return render_template('aboutus.html')

@app.route('/Confirmm.html')
def update():
    return render_template('Confirmm.html')

@app.route('/help.html')
def help():
    return render_template('help.html')
if __name__ == '__main__':
    app.secret_key = 'abc'  # Add a secret key for session management
    app.run()
