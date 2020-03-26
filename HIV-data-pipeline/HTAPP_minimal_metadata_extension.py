import os
import json
  
from schema_explorer import SchemaExplorer

def get_class(class_name, description = None, subclass_of = ["Thing"], requires_dependencies = None, requires_value = None, display_name = None):

    class_attributes = {
                    '@id': 'bts:'+class_name,
                    '@type': 'rdfs:Class',
                    'rdfs:comment': description if description else "",
                    'rdfs:label': class_name,
                    'schema:isPartOf': {'@id': 'http://schema.biothings.io'}
    }

    if subclass_of:
        parent = {'rdfs:subClassOf':[{'@id':'bts:' + sub} for sub in subclass_of]}
        class_attributes.update(parent)

    if requires_dependencies:
        requirement = {'rdfs:requiresDependency':[{'@id':'sms:' + dep} for dep in requires_dependencies]}
        class_attributes.update(requirement)

    if requires_value != None:
        value_constraint = {'rdfs:requiresChildAsValue':{'@id':'sms:' +  str(requires_value)}}
        class_attributes.update(value_constraint)
    
    if display_name:
        class_attributes.update({'sms:displayName':display_name})

    return class_attributes



# path to schema metadata (output or input)
schema_path = "./schemas"
output_schema_name = "HTAPP"


# instantiate schema explorer
se = SchemaExplorer()


"""
######################################################
# first add the classes w/o dependencies to the schema
######################################################
"""
class_req_add = get_class("HTAPP",\
                              description = "HTAPP minimal metadata extension",\
                              subclass_of = ["Thing"]
)
se.update_class(class_req_add)

display_name = "HTAN Participant ID"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "HTAN patient ID",\
                              subclass_of = ["Case"],\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "HTAN Sample ID"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Unique identifier for the biosample source material",\
                              subclass_of = ["Biosample"],\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "Cancer Type"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Cancer diagnosis",\
                              subclass_of = ["Disease"],
                              requires_value = True,\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "Breast Carcinoma"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Breast cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "Colon Carcinoma"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Colon cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)


display_name = "Lung Carcinoma"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Lung cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)


display_name = "Malignant Ovarian Neoplasm"
class_name = se.get_class_label_from_display_name(display_name)

class_req_add = get_class(class_name,\
                              description = "Ovarian cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "Malignant Brain Neoplasm"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Brain cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)

display_name = "Malignant Adrenal Gland Neoplasm"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Adrenal gland cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)


display_name = "Malignant Neoplasm Connective Soft Tissue"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Soft tissue cancer",\
                              subclass_of = ["CancerType"],\
                              display_name = display_name
)
se.update_class(class_req_add)


'''
adding a generic category assay
'''
class_req_add = get_class("Assay",\
                              description = "A planned process with the objective to produce information about the material entity that is the evaluant, by physically examining it or its proxies.<OBI_0000070>"
)
se.update_class(class_req_add) # note: use update_class to add a new class


'''
adding a subcategory sequencing assay (as a subclass of assay)
'''
class_req_add = get_class("SequencingAssay",\
                              description = "The determination of the sequence of component residues in a macromolecule, e.g. amino acids in a protein or nucleotide bases in DNA/RNA or the computational analysis performed to determine the similarities between nonidentical proteins or molecules of DNA or RNA.<NCIT_C17565>",\
                              subclass_of = ["Assay"]
)
se.update_class(class_req_add) # note: use update_class to add a new class


display_name = "Library Construction Method"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Process which results in the creation of a library from fragments of DNA using cloning vectors or oligonucleotides with the role of adaptors <OBI_0000711>",\
                              subclass_of = ["SequencingAssay"],
                              requires_value = True,\
                              display_name = display_name
)
se.update_class(class_req_add) # note: use update_class to add a new class

'''
adding children of library construction method
'''

display_name = "10x"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "10X is a 'synthetic long-read' technology and works by capturing a barcoded oligo-coated gel-bead and 0.3x genome copies into a single emulsion droplet, processing the equivalent of 1 million pipetting steps. Successive versions of the 10x chemistry use different barcode locations to improve the sequencing yield and quality of 10x experiments.<EFO_0008995>",\
                              subclass_of = ["LibraryConstructionMethod"],\
                              display_name = display_name
)
se.update_class(class_req_add) # note: use update_class to add a new class

display_name = "Smart-seq2"
class_name = se.get_class_label_from_display_name(display_name)
class_req_add = get_class(class_name,\
                              description = "Switch mechanism at the 5’ end of RNA templates (Smart).<EFO_0008930>",\
                              subclass_of = ["LibraryConstructionMethod"],
                              display_name = display_name
)
se.update_class(class_req_add) # note: use update_class to add a new class



"""
######################################################
# add dependencies and requirements to classes
######################################################
"""

class_info = se.explore_class("HTAPP")
class_req_edit = get_class("HTAPP",\
                              description = class_info["description"],\
                              subclass_of = class_info["subClassOf"],\
                              requires_dependencies = ["HtanParticipantId","HtanSampleId","CancerType", "LibraryConstructionMethod"]
)
se.edit_class(class_req_edit) 
# note: use class_edit to edit a current class; you can explore existing class properties
# and reuse them in the edited class (e.g. here via class_info)



"""
######################################################
# DONE adding requirements to schema
######################################################
"""

# saving updated schema.org schema
se.export_schema(os.path.join(schema_path, output_schema_name + ".jsonld"))

"""
######################################################
# Generating JSONSchema schema from schema.org schema
######################################################
"""

'''
To generate JSONSchema schema for validation based on this schema.org schema
run ./schema_generator.py; just point it to the output schema above or invoke 
directly the JSONSchema generation method as show below
'''

from schema_generator import get_JSONSchema_requirements 

# see schema_generator.py for more details on parameters

#JSONSchema name 
json_schema_name = "minimalHTAPPJSONSchema"

json_schema = get_JSONSchema_requirements(se, "HTAPP", schema_name = json_schema_name)

# store the JSONSchema schema
with open(os.path.join(schema_path, json_schema_name + ".json"), "w") as s_f:
    json.dump(json_schema, s_f, indent = 3) # adjust indent - lower for more compact schemas
