import sys
import requests
import json

def update_caller_id(username, callerid):
    # Define the API endpoint
    url = "https://spoofwave.com/api/call"

    # Define the payload data
    data = {
        "username": username,
        "callerid": callerid
    }

    # Set the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success"):
            print("Caller ID updated successfully.")
            print(f"Balance: {response_data.get('balance')}")
        else:
            print("Failed to update Caller ID.")
            print("Message:", response_data.get("message"))
    else:
        print("Failed to connect to the API.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 spoofcall.py YOUR_USERNAME CALLER_ID")
        sys.exit(1)

    # Get the command-line arguments
    username = sys.argv[1]
    callerid = sys.argv[2]

    # Call the function to update the caller ID
    update_caller_id(username, callerid)