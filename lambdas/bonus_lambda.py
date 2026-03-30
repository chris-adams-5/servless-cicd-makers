import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    now = datetime.now(timezone.utc)
    time_str = now.strftime("%H:%M:%S UTC")
    date_str = now.strftime("%A, %d %B %Y")

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "skill": "tell_time",
            "message": f"The current time is {time_str} on {date_str}."
        })
    }