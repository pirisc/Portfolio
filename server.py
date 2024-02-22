from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/") #This is a decorator 
def my_home():
    return render_template ('index.html')

@app.route("/<string:page_name>") #With this syntax we can dinamically accept different url parametehres
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open ('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data ['subject']
        message = data ['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open ('database.csv', newline='', mode = 'a') as database2:
        email = data['email']
        subject = data ['subject']
        message = data ['message']
        csv_writer = csv.writer(database2, delimiter = ',', quotechar ='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() #We are going to get the data as a dictionary
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong. Try again! "
