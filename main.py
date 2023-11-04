import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

USERNAME = "rizal"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
DATE = dt.datetime.now().strftime("%Y%m%d")


def create_new_user():
    params = {
        "token": os.environ.get("PIXELA_KEY"),
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=params)
    print(response.text)


def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai",

    }

    headers = {
        "X-USER-TOKEN": os.environ.get("PIXELA_KEY")
    }
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def paint_the_graph():
    headers = {
        "X-USER-TOKEN": os.environ.get("PIXELA_KEY")
    }

    graph_config = {
        "date": DATE,
        "quantity": "4.0"
    }

    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def update_graph():
    headers = {
        "X-USER-TOKEN": os.environ.get("PIXELA_KEY")
    }

    graph_config = {
        "quantity": "10.8"
    }

    endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

    response = requests.put(url=endpoint, json=graph_config, headers=headers)
    print(response.text)
