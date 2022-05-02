from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

my_email = "feodorateferi@gmail.com"
# to-do list:
# make email in contact page work
# fix footer section
# erase reference to Sean Halpin...
# add profile pic in bio area ( i'm 16...)
# add pretty backgrounds to pages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/redirecting")
def success():
    return render_template("success.html")

@app.route("/contact-me", methods=['GET', 'POST'])
def contact_me():
    if request.method == "POST":
        data = request.form
        return redirect(url_for("success"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
