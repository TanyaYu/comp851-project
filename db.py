from lead import Lead

def get_leads():
    f = open("user_data.json", "r")
    return f.read()
