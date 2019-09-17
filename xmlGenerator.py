from xml.dom.minidom import Document

def createXML(boundingBox, fileName, destinyDirectory):
	#fileName = filePath.split("/")
	#fileName = fileName[-1]
	#fileName = fileName[:-4]

	#print(boundingBox)
	#print(destinyDirectory)

	#criar XML
	doc = Document()

	MD_Metadata = doc.createElement('gmd:MD_Metadata')
	MD_Metadata.setAttribute('xmlns:gmd', 'http://www.isotc211.org/2005/gmd')
	MD_Metadata.setAttribute('xmlns:gco', 'http://www.isotc211.org/2005/gco')

	output = open(destinyDirectory + "/" + fileName, "w")
	#doc.appendChild(EX_GeographicBoundingBox)
	doc.appendChild(MD_Metadata)

	EX_GeographicBoundingBox = doc.createElement('gmd:EX_GeographicBoundingBox')

	westBoundLongitude = doc.createElement('gmd:westBoundLongitude')
	Decimal = doc.createElement('gco:Decimal')
	Decimal.appendChild(doc.createTextNode(str(boundingBox[0][1])))
	westBoundLongitude.appendChild(Decimal)
	EX_GeographicBoundingBox.appendChild(westBoundLongitude)

	eastBoundLongitude = doc.createElement('gmd:eastBoundLongitude')
	Decimal = doc.createElement('gco:Decimal')
	Decimal.appendChild(doc.createTextNode(str(boundingBox[1][1])))
	eastBoundLongitude.appendChild(Decimal)
	EX_GeographicBoundingBox.appendChild(eastBoundLongitude)

	southBoundLatitude = doc.createElement('gmd:southBoundLatitude')
	Decimal = doc.createElement('gco:Decimal')
	Decimal.appendChild(doc.createTextNode(str(boundingBox[2][1])))
	southBoundLatitude.appendChild(Decimal)
	EX_GeographicBoundingBox.appendChild(southBoundLatitude)

	northBoundLatitude = doc.createElement('gmd:northBoundLatitude')
	Decimal = doc.createElement('gco:Decimal')
	Decimal.appendChild(doc.createTextNode(str(boundingBox[3][1])))
	northBoundLatitude.appendChild(Decimal)
	EX_GeographicBoundingBox.appendChild(northBoundLatitude)

	MD_Metadata.appendChild(EX_GeographicBoundingBox)

	doc.writexml(output," "," ", "\n", "UTF-8")

	output.close()