from flask import Flask , escape,url_for, request, jsonify
import json
import requests


app = Flask(__name__)

#  head over the http://127.0.0.1:5000/ to see the results

#app.config['SERVER_NAME'] ='localhost:5000'

@app.route('/')
def hello_API():
   return 'You have access to the API service'


#send path data back to website with GET method
with open('data.geojson', 'r') as f:
    distros_dict = json.load(f)

@app.route('/waypoints', methods=['GET'])
def Waypoints():
    return jsonify(distros_dict)




#Read the json data from website with POST method
@app.route('/json_example', methods=['POST'])
def json_example():
    req_data= request.get_json()

    with open('dataforConv-Cao.json', 'w') as outfile:
        json.dump(req_data,outfile)
    return jsonify(req_data)



# URL Building
with app.test_request_context():
    print('The url for the path is ',url_for('Waypoints'))

with open('dataforConv-Cao.json') as json_file:
        data = json.load(json_file)
        for p in data['features']:
            # print(p['geometry']['coordinates'][0][0][0]) for lat
            # print(p['geometry']['coordinates'][0][0][1]) #for lon
            # print(len(p['geometry']['coordinates'][0])) # to calculate the length of the boundaries
            print(p['geometry']['coordinates'])

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    #app.run()



