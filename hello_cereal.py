import requests
import csv
from dagster import pipeline, solid


@solid
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")

@pipeline
def hello_cereal_pipeline():
    hello_cereal()  # pylint:disable=no-value-for-parameter
