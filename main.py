from flask import Flask, render_template, request
import pandas as pd
import geopandas as gpd
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/output')
def es1():
    gdfMilano = gpd.read_file("ds964_nil_wm.zip")
    df = pd.read_csv("colonnine_ricarica_geo.csv")
    table = gdfMilano.to_html()
    return render_template('output.html', table = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)