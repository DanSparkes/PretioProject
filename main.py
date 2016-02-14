import GeoIP
from flask import Flask
from flask import request

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

app = Flask(__name__)

@app.route('/ad')
def ad():
    country_code = gi.country_code_by_addr(request.remote_addr)
    return country_code if country_code else "No Country Code Found."

if __name__ == "__main__":
    app.run(debug=True)