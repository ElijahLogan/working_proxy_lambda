import json
import requests

def handler(event, context):
    # TODO implement
    a = event["queryStringParameters"]['description']

# Define the attributes
    attributes = {
        "userId": "3f957e60-aae2-48aa-8c91-fd48be2471dc",
        "noteId": "a8098c1a-f86e-11dafrf-bd1a-00112444be1e",
        "part": "hand",
        "description": "left hip",
        "tod": "2024-07-04T22:27:23Z"
    }
    
    # Target IP address (replace with the actual IP address)
    target_ip = "3"
    
    # Create the JSON body
    json_body = attributes
    
    # Send the POST request
    try:
        response = requests.post(f"http://{target_ip}/add", json=json_body)
        if response.status_code == 200:
            print("Request sent successfully!")
    except:
        print("An exception occurred")
    return {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'},
    'body': a
}
