import os
import requests
import json
import datetime

from dotenv import load_dotenv

load_dotenv()
__weatherapi_url = "https://api.weatherapi.com/v1/forecast.json"


def handle_weatherapi_request(location: str):
    try:
        response = requests.get(
            __weatherapi_url,
            {
                "q": location,
                "aqi": 'no',
                "key": os.environ.get("WEATHER_API_KEY"),
                "units": "metric",
                "days": 7
            }
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        # return render_template("index.html", message="Failed to connect to weatherapi")
        pass
    except requests.RequestException as e:
        # return render_template("index.html", message=e.response.json()["error"]["message"])
        pass
    else:
        return parse_response_to_week_dict(response.json())


def parse_response_to_week_dict(response_json: dict):
    week_dict = {
        "location": response_json["location"]["name"],
        "country": response_json["location"]["country"],
        "days": [
            {
                "date": day["date"],
                "day_temp": average_temp([hour["temp_c"] for hour in day["hour"] if hour["is_day"] == 1]),
                "night_temp": average_temp([hour["temp_c"] for hour in day["hour"] if hour["is_day"] == 0]),
                "humidity": day["day"]["avghumidity"],
                "icon": day["day"]["condition"]["icon"],
            }
            for day in response_json["forecast"]["forecastday"]
        ],
    }
    save_history(week_dict)
    return week_dict


def average_temp(temperatures: list):
    return round((sum(temperatures) / len(temperatures)), 2)


def save_history(week_dict):
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    filename = "history/" + date + "-" + week_dict["location"] + ".json"
    data = {"date": date, "city": week_dict}
    with open(filename, "a") as f:
        json.dump(data, f, indent=4, separators=(", ", ": "))


def load_history():
    file_names = os.listdir("history/")
    # for file_name in file_names:
    # Do something with the file name
    #     print(file_name)

    print(file_names)
    return {"file_names": file_names}
    # print(json.dumps(file_names_json))


if __name__ == "__main__":
    load_history()
