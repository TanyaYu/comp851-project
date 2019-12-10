import csv, io, json
import boto3


def download_leads():
    s3 = boto3.client('s3')
    s3.download_file('comp851-m1-f19', 'userdata2.csv', 'ud2.csv')
    with open('userdata2.csv', 'wb') as f:
        s3.download_fileobj('comp851-m1-f19', 'userdata2.csv', f)
    return parse_leads()


def parse_leads():
    csvfile = open('userdata2.csv', 'r')
    reader = csv.DictReader(io.StringIO(csvfile.read()))
    json_data = json.dumps(list(reader))
    return json_data
