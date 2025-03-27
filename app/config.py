ENDPOINTS = {
    "schnitzler-briefe": {
        "title": "Arthur Schnitzler: Briefwechsel mit Autorinnen und Autoren (1888–1931).",
        "url": "https://schnitzler-briefe.acdh.oeaw.ac.at/oai-pmh/",
    },
    "b-vg": {
        "title": "Die Entstehung des Bundes-Verfassungsgesetzes 1920.",
        "url": "https://b-vg.acdh.oeaw.ac.at/oai-pmh/",
    },
    "akademieprotokolle": {
        "title": "Sitzungsprotokolle der Österreichischen Akademie der Wissenschaften.",
        "url": "https://akademieprotokolle.acdh.oeaw.ac.at/oai-pmh/",
    },
    "grazer-nuntiatur": {
        "title": "Grazer Nuntiatur: Korrespondenz (1580–1602).",
        "url": "https://grazer-nuntiatur.acdh.oeaw.ac.at/oai-pmh/",
    },
    "nuntiatur-pius-xi": {
        "title": "Nuntiatur Pius XI: Korrespondenz (1923–1936)",
        "url": "https://nuntiatur-pius-xi.acdh.oeaw.ac.at/oai-pmh/",
    },
    "tillich-lectures": {
        "title": "A digital edition of Paul Tillich's Lecture 'Religion and Culture', Harvard 1955-1956.",
        "url": "https://tillichcorrespondence.github.io/tillich-lectures-static/oai-pmh/",
    },
    "familiensache": {
        "title": "Familiensache. Dynastische Handlungsspielräume in der Korrespondenz von Kaiserin Eleonora Magdalena von Pfalz-Neuburg (1655-1720).",  # noqa: 501
        "url": "https://kaiserin-eleonora.oeaw.ac.at/oai-pmh/",
    },
    "wmp1": {
        "title": "Das erste Wiener Merkantilprotokoll.",
        "url": "https://wmp1.acdh.oeaw.ac.at/oai-pmh/",
    },
    "amp": {
        "title": "Auden Musulin Papers: A Digital Edition of W. H. Auden's Letters to Stella Musulin.",
        "url": "https://csae8092.github.io/amp-app/oai-pmh/",
    },
    "gtrans": {
        "title": "Die große Transformation: Staat und kommunaler öffentlicher Dienst in Wien (1918–1920).",
        "url": "https://gtrans.acdh.oeaw.ac.at/oai-pmh/",
        "fulltext_xpath": "//tei:profileDesc/tei:abstract/.//text()"
    },
}

VERB_MAPPING = {
    "Identify": "Identify.xml",
    "ListRecords": "ListRecords.xml",
    "ListIdentifiers": "ListIdentifiers.xml",
    "ListMetadataFormats": "ListMetadataFormats.xml",
    "GetRecord": "",
}

FULLTEXT_BLACK_LIST = [
    "tei:note",
    "tei:abbr",
    "tei:am",
    "tei:del"
]
