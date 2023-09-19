from flask import Flask, render_template, request, session, Response
from dotenv import load_dotenv

import forecast
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("aws_access_key_id")
color = os.environ.get("BG_COLOR")


@app.get('/')
def index():
    print(color)
    return render_template("index.html", color=color)


@app.post("/search")
def search():
    search_term = request.form["search"]
    forecast_data = forecast.handle_weatherapi_request(search_term)
    session['forecast_data'] = forecast_data
    return render_template("render_weatherapi.html", forecast_data=forecast_data, color=color)


@app.route("/get_file")
def get_file():
    file_name = "history/" + request.args.get("file_name")
    response_value = "attachment; filename=" + file_name
    with open(file_name) as fp:
        json = fp.read()
    return Response(
        json,
        mimetype="text/json",
        headers={"Content-disposition": response_value})


@app.post("/history")
def history():
    print("test")
    files = forecast.load_history()
    return render_template("render_search_history.html", files=files, color=color)


if __name__ == "__main__":
    app.run(debug=True)
