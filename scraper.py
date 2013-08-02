import csv
import urllib
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
	# It's just a plain vanilla form. Just return it.
	return render_template('index.html')

@app.route("/scrapr", methods=['POST'])
def parse():
	# Get the URL submitted, open the connection, get results, and start
	# parsing the object.
	url_to_fetch = request.form['url']
	connection = urllib.urlopen(url_to_fetch)
	text = connection.read()
	page_soup = BeautifulSoup(text)

	# Open the CSV file for writing. We will end up returning this.
	csvFilename = "output_" + str(int(time.time())) + ".csv"
	csvFile = open("static/" + csvFilename, "w")
	csvWriter = csv.writer(csvFile, delimiter=',')

	# For every table, create a soup to process all of its individual parts.
	for table in page_soup.find_all("table"):
		table_soup = BeautifulSoup(str(table))

		for body in table_soup:
			body = BeautifulSoup(str(body))
			rows = body.find_all("tr")

			for tr in rows:
				cols = tr.find_all(["td", "th"])
				colsArr = []

				for td in cols:
					data_set = unicode(td.string).strip()
					
					# Expand any headers that might span more than 1 column.
					if "colspan" in td.attrs:
						times_to_repeat = int(td["colspan"])
					else:
						times_to_repeat = 1

					# Append to accumulated array as appropriate.
					if data_set.isdigit():
						data_set = int(data_set)

					for i in range(times_to_repeat):
						colsArr.append(data_set)

				csvWriter.writerow(colsArr)

			# Write an empty row just to give some space.
			csvWriter.writerow([])
	csvFile.close()

	return redirect(url_for("tools/static", filename=csvFilename))


if __name__ == "__main__":
	app.run(debug = True, port=8080)