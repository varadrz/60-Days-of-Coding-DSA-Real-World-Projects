from flask import Flask, render_template, request, redirect
from url_shortener import URLShortener

app = Flask(__name__)
shortener = URLShortener()


@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    original_url = None

    if request.method == "POST":
        long_url = request.form.get("long_url")
        if long_url:
            short_url = shortener.shorten_url(long_url)

    return render_template("index.html", short_url=short_url)


@app.route("/<code>")
def redirect_url(code):
    long_url = shortener.expand_url(code)
    if long_url:
        return redirect(long_url)
    return "Invalid or expired URL", 404


if __name__ == "__main__":
    app.run(debug=True)
