from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    # Log the data (you can replace this with DB save or WhatsApp API etc.)
    print(f"New Contact: {name}, {phone}, {message}")

    flash("Thank you! We'll contact you shortly.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
