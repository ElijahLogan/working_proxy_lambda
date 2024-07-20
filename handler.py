import json
import requests

def handler(event, context):
    # TODO implement
    d = event["queryStringParameters"]['description']
    p = event["queryStringParameters"]['part']
    u = event["queryStringParameters"]['userId']
    n  = event["queryStringParameters"]['noteId']
    t = event['queryStringParameters']['tod']
    

# Define the attributes
    attributes = {
        "userId": u,
        "noteId": n,
        "part": p,
        "description": d,
        "tod": t
    }
    
    # Target IP address (replace with the actual IP address)
    target_ip = "3."
    
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
    'body': t
}
