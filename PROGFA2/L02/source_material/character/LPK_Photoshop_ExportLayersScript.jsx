#target photoshop

var doc = app.activeDocument;
var outputFolder = Folder.selectDialog("Select the folder to export PNGs to");

if (outputFolder) {
    exportLayers(doc, outputFolder);
}

function exportLayers(doc, outputFolder) {
    for (var i = 0; i < doc.layers.length; i++) {
        var layer = doc.layers[i];
        if (layer.typename == "LayerSet") {
            var folder = new Folder(outputFolder + "/" + layer.name);
            if (!folder.exists) folder.create();
            exportLayers(layer, folder);
        } else {
            exportLayer(layer, outputFolder);
        }
    }
}

function exportLayer(layer, outputFolder) {
    var layerName = layer.name;
    var file = new File(outputFolder + "/" + layerName + ".png");

    var tempDoc = app.documents.add(doc.width, doc.height, doc.resolution, "tempDoc", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
    app.activeDocument = doc;
    layer.duplicate(tempDoc, ElementPlacement.PLACEATBEGINNING);
    app.activeDocument = tempDoc;

    var options = new ExportOptionsSaveForWeb();
    options.format = SaveDocumentType.PNG;
    options.PNG8 = false;
    options.transparency = true;
    options.interlaced = false;
    options.quality = 100;

    tempDoc.exportDocument(file, ExportType.SAVEFORWEB, options);
    tempDoc.close(SaveOptions.DONOTSAVECHANGES);
}
