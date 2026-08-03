"""
Write programs to parse text files, CSV, HTML, XML and JSON documents and
extract relevant data. After retrieving data check any anomalies in the data, missing
values etc.
"""
import re
import csv
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class SimpleHtmlParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.extractedData = []
        self.inTableRow = False
        self.currentCell = ""
        self.currentRow = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.inTableRow = True
            self.currentRow = []
        elif tag in ["td", "th"] and self.inTableRow:
            self.currentCell = ""

    def handle_data(self, data):
        if self.inTableRow:
            self.currentCell += data.strip()

    def handle_endtag(self, tag):
        if tag in ["td", "th"] and self.inTableRow:
            self.currentRow.append(self.currentCell)
            self.currentCell = ""
        elif tag == "tr":
            self.inTableRow = False
            if self.currentRow:
                self.extractedData.append(self.currentRow)

def checkAnomalies(dataRecords, expectedKeys):
    anomaliesFound = []
    for index, record in enumerate(dataRecords):
        recordAnomalies = []
        for key in expectedKeys:
            if key not in record:
                recordAnomalies.append(f"Missing key: {key}")
            elif record[key] is None or str(record[key]).strip() == "":
                recordAnomalies.append(f"Empty value for key: {key}")
        if recordAnomalies:
            anomaliesFound.append({"recordIndex": index, "issues": recordAnomalies})
    return anomaliesFound

def parseTextFile(filePath):
    extractedData = []
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                match = re.match(r"id:(\w+),\s*name:([^,]*),\s*score:(\d*)", line)
                if match:
                    extractedData.append({
                        "id": match.group(1),
                        "name": match.group(2).strip(),
                        "score": match.group(3)
                    })
                else:
                    extractedData.append({"rawLine": line, "parseError": True})
    return extractedData

def parseCsvFile(filePath):
    extractedData = []
    with open(filePath, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            extractedData.append(dict(row))
    return extractedData

def parseHtmlFile(filePath):
    with open(filePath, "r") as file:
        content = file.read()
    parser = SimpleHtmlParser()
    parser.feed(content)
    parsedRows = parser.extractedData
    if not parsedRows:
        return []
    headers = [h.lower() for h in parsedRows[0]]
    structuredData = []
    for row in parsedRows[1:]:
        record = {}
        for idx, header in enumerate(headers):
            record[header] = row[idx] if idx < len(row) else ""
        structuredData.append(record)
    return structuredData

def parseXmlFile(filePath):
    tree = ET.parse(filePath)
    root = tree.getroot()
    extractedData = []
    for item in root.findall("item"):
        record = {
            "id": item.findtext("id"),
            "name": item.findtext("name"),
            "score": item.findtext("score")
        }
        extractedData.append(record)
    return extractedData

def parseJsonFile(filePath):
    with open(filePath, "r") as file:
        data = json.load(file)
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and "items" in data:
        return data["items"]
    return [data]

def main():
    expectedKeys = ["id", "name", "score"]

    textData = parseTextFile("sample.txt")
    print("Text Data Anomalies:", checkAnomalies(textData, expectedKeys))
    print()

    csvData = parseCsvFile("sample.csv")
    print("CSV Data Anomalies:", checkAnomalies(csvData, expectedKeys))
    print()

    htmlData = parseHtmlFile("sample.html")
    print("HTML Data Anomalies:", checkAnomalies(htmlData, expectedKeys))
    print()

    xmlData = parseXmlFile("sample.xml")
    print("XML Data Anomalies:", checkAnomalies(xmlData, expectedKeys))
    print()

    jsonData = parseJsonFile("sample.json")
    print("JSON Data Anomalies:", checkAnomalies(jsonData, expectedKeys))

if __name__ == "__main__":
    main()