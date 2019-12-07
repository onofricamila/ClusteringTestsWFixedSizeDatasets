import json

paths = None
algoNames = None

def _getPaths():
    return paths


def _getAlgoNames():
    return algoNames


def _fetchConfig():
    # we use the global key word to being able to change the values of the variables declared outside the function
    global paths
    global algoNames

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    paths = data.get("paths")
    algoNames = data.get("algoNames")


def _fetchElementIfNull(_getter):
    element = _getter()
    if (element != None):
        return element
    # else
    _fetchConfig()
    return _getter()


def _getElementFromDict(key, _getter):
    dict = _fetchElementIfNull(_getter)
    return dict.get(key)


def getNonTimeSeriesDatasetsPath():
    return _getElementFromDict(key="nonTimeSeriesDatasetsPath", _getter=_getPaths)


def getClusteringResultsPath():
    return _getElementFromDict(key="clusteringResultsPath", _getter=_getPaths)


def getmKMeansName():
    return _getElementFromDict(key="kmeans", _getter=_getAlgoNames)


def getDbscanName():
    return _getElementFromDict(key="dbscan", _getter=_getAlgoNames)
