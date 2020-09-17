# import json
# import os
from schematic.models.metadata import MetadataModel
from schematic.manifest.generator import ManifestGenerator

#inputMModelLocation = "./schemas/exampleSchemaReq.jsonld"
#inputMModelLocation = "./HIV-data-pipeline/schemas/scRNASeq.jsonld"
# inputMModelLocation = "./HIV-data-pipeline/schemas/HTAPP.jsonld"
inputMModelLocation = "./data/schema_org_schemas/HIV_v1.1.jsonld"
inputMModelLocationType = "local"
# datasetType = "scRNASeq"
# modelType = "TableA"

metadata_model = MetadataModel(inputMModelLocation, inputMModelLocationType)
### function for getting model Manifest
#  mm.getModelManifest(modelType, additionalMetadata = {"Filename":["MantonCB1_HiSeq_1_S1_L001_R1_001.fastq.gz"]} )
# getModelManifest = mm.getModelManifest

### function for validating manifest
# mm.validateModelManifest(manifest_path, datasetType)
# validateModelManifest = mm.validateModelManifest

### populates manifest with path to csv
# populateModelManifest = mm.populateModelManifest

### gets dependencies
# "Generating dependency graph and ordering dependencies")
# dependencies = mm.getOrderedModelNodes(component, "requiresDependency")
# getDependencies = mm.getOrderedModelNodes
