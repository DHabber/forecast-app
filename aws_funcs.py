import boto3
from datetime import date



def test(forecast_data):
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table('web_app_NoSQL')
    dynamoTable.put_item(
        Item={
            "location": forecast_data["location"],
            "cast_time": str(date.today()),
            "country": forecast_data["country"],
            "days": [
            {
                "date": day["date"],
                "day_temp": str(day["day_temp"]),
                "night_temp": str(day["night_temp"]),
                "humidity": str(day["humidity"]),
                "icon": day["icon"]
            }
            for day in forecast_data["days"]
        ],
        }
    )

        
"""    try:
        response = client.put_item(
            TableName='web_app_NoSQL',
            Item = forecast_data
        )
    except boto3.ClientError as err:
        logger.error("Error %s: %s", err.response['Error']['Code'], err.response['Error']['Message'])
"""
"""
    print(forecast_data["country"])
    for day in forecast_data["days"]:
        print(day["date"])
        print(day["day_temp"])
        print(day["humidity"])
        print(day["icon"])
        print(day["night_temp"])
"""
