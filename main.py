import GeoIP
import requests
import json

from flask import Flask, render_template
from flask import request

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

app = Flask(__name__)


@app.route('/ad')
def ad():
    country_code = gi.country_code_by_addr(request.remote_addr)
    user = str(request.remote_addr).replace(".", "")
    params = {"country_code": country_code, "user_id": user, "sub_id": "Pretio Interview"}
    post_req = requests.post("https://offers.pretio.in/publishers/c00d0814f0b548c68817473b1605a375/api/", data=params)
    if post_req.status_code == 200:
        json_data = json.loads(post_req.text)
        return render_template("index.html", url=json_data['url'])
    elif post_req.status_code == 204:
        return render_template("index.html", error="No reward available.")
    else:
        return render_template("index.html", error="Something has gone wrong")

if __name__ == "__main__":
    app.run()
