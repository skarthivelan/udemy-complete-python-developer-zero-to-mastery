from flask import Flask,render_template, url_for ,request,redirect

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/<string:pageName>")
def html(pageName):
    return render_template(pageName)

def write_to_file(data):
    with open('ContactedData.txt', mode='a') as database:
        file = database.write(f"\n{data['email']} | {data['subject']} | {data['message']}")
@app.route("/submit_form", methods=['POST', 'GET'])
def formSubmit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return "Something went wrong. Try again!"

