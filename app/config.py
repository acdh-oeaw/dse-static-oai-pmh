ENDPOINTS = {
    "schnitzler-briefe": {
        "title": "Arthur Schnitzler: Briefwechsel mit Autorinnen und Autoren (1888–1931).",
        "url": "https://schnitzler-briefe.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B3-8",
    },
    "schnitzler-tagebuch": {
        "title": "Arthur Schnitzler: Tagebuch (1879–1931).",
        "url": "https://schnitzler-tagebuch.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84BB-0",
    },
    "b-vg": {
        "title": "Die Entstehung des Bundes-Verfassungsgesetzes 1920.",
        "url": "https://b-vg.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B4-7",
    },
    "akademieprotokolle": {
        "title": "Sitzungsprotokolle der Österreichischen Akademie der Wissenschaften.",
        "url": "https://akademieprotokolle.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B5-6",
    },
    "grazer-nuntiatur": {
        "title": "Grazer Nuntiatur: Korrespondenz (1580–1602).",
        "url": "https://grazer-nuntiatur.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "ita",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B6-5",
    },
    "nuntiatur-pius-xi": {
        "title": "Nuntiatur Pius XI: Korrespondenz (1923–1936)",
        "url": "https://nuntiatur-pius-xi.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "ita",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B7-4",
    },
    "tillich-lectures": {
        "title": "A digital edition of Paul Tillich's Lecture 'Religion and Culture', Harvard 1955-1956.",
        "url": "https://tillichcorrespondence.github.io/tillich-lectures-static/oai-pmh/",
        "default_lang": "eng",
    },
    "familiensache": {
        "title": "Familiensache. Dynastische Handlungsspielräume in der Korrespondenz von Kaiserin Eleonora Magdalena von Pfalz-Neuburg (1655-1720).",  # noqa: 501
        "url": "https://kaiserin-eleonora.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B8-3",
    },
    "wmp1": {
        "title": "Das erste Wiener Merkantilprotokoll.",
        "url": "https://wmp1.acdh.oeaw.ac.at/oai-pmh/",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84B9-2",
    },
    "amp": {
        "title": "Auden Musulin Papers: A Digital Edition of W. H. Auden's Letters to Stella Musulin.",
        "url": "https://csae8092.github.io/amp-app/oai-pmh/",
        "default_lang": "eng",
    },
    "gtrans": {
        "title": "Die große Transformation: Staat und kommunaler öffentlicher Dienst in Wien (1918–1920).",
        "url": "https://gtrans.acdh.oeaw.ac.at/oai-pmh/",
        "fulltext_xpath": "//tei:profileDesc/tei:abstract/.//text()",
        "default_lang": "deu",
        "pid": "https://hdl.handle.net/21.11115/0000-0016-84BA-1",
    },
}

VERB_MAPPING = {
    "Identify": "Identify.xml",
    "ListRecords": "ListRecords.xml",
    "ListIdentifiers": "ListIdentifiers.xml",
    "ListMetadataFormats": "ListMetadataFormats.xml",
    "GetRecord": "",
}

FULLTEXT_BLACK_LIST = ["tei:note", "tei:abbr", "tei:am", "tei:del"]
