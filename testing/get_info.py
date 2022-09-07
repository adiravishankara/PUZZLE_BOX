import urequests

def get_time():
    result = urequests.get("http://api.timezonedb.com/v2.1/get-time-zone?key="
        "IEEE2W7V3CXW&format=json&by=zone&zone=Asia/Tokyo").json()

    print(result)

get_time()
