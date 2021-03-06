"""use the class IDF"""

from io import StringIO
from eppy3000.modelmaker import IDF
from pprint import pprint

txt = """{
    "epJSON_schema_version": "8.9.0",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "required": [
        "Building",
        "GlobalGeometryRules"
    ],
    "properties": {
        "Building": {
            "name": {
                "default": "NONE",
                "retaincase": true,
                "type": "string"
            },
            "memo": "Describes parameters that are used during the simulation of the building. There are necessary correlations between the entries for this object and some entries in the Site:WeatherStation and Site:HeightVariation objects, specifically the Terrain field.",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "solar_distribution": {
                            "note": "MinimalShadowing | FullExterior | FullInteriorAndExterior | FullExteriorWithReflections | FullInteriorAndExteriorWithReflections",
                            "default": "FullExterior",
                            "enum": [
                                "",
                                "FullExterior",
                                "FullExteriorWithReflections",
                                "FullInteriorAndExterior",
                                "FullInteriorAndExteriorWithReflections",
                                "MinimalShadowing"
                            ],
                            "type": "string"
                        },
                        "terrain": {
                            "note": "Country=FlatOpenCountry | Suburbs=CountryTownsSuburbs | City=CityCenter | Ocean=body of water (5km) | Urban=Urban-Industrial-Forest",
                            "default": "Suburbs",
                            "enum": [
                                "",
                                "City",
                                "Country",
                                "Ocean",
                                "Suburbs",
                                "Urban"
                            ],
                            "type": "string"
                        },
                        "north_axis": {
                            "note": "degrees from true North",
                            "units": "deg",
                            "default": 0.0,
                            "type": "number"
                        },
                        "maximum_number_of_warmup_days": {
                            "note": "EnergyPlus will only use as many warmup days as needed to reach convergence tolerance. This field's value should NOT be set less than 25.",
                            "exclusiveMinimum": true,
                            "default": 25.0,
                            "minimum": 0.0,
                            "type": "number"
                        },
                        "loads_convergence_tolerance_value": {
                            "default": 0.04,
                            "type": "number",
                            "maximum": 0.5,
                            "note": "Loads Convergence Tolerance Value is a fraction of load",
                            "minimum": 0.0,
                            "exclusiveMinimum": true
                        },
                        "temperature_convergence_tolerance_value": {
                            "default": 0.4,
                            "type": "number",
                            "maximum": 0.5,
                            "minimum": 0.0,
                            "units": "deltaC",
                            "exclusiveMinimum": true
                        },
                        "minimum_number_of_warmup_days": {
                            "note": "The minimum number of warmup days that produce enough temperature and flux history to start EnergyPlus simulation for all reference buildings was suggested to be 6. When this field is greater than the maximum warmup days defined previous field the maximum number of warmup days will be reset to the minimum value entered here. Warmup days will be set to be the value you entered when it is less than the default 6.",
                            "exclusiveMinimum": true,
                            "default": 6.0,
                            "minimum": 0.0,
                            "type": "number"
                        }
                    }
                }
            },
            "legacy_idd": {
                "numerics": {
                    "fields": [
                        "north_axis",
                        "loads_convergence_tolerance_value",
                        "temperature_convergence_tolerance_value",
                        "maximum_number_of_warmup_days",
                        "minimum_number_of_warmup_days"
                    ]
                },
                "field_info": {
                    "name": {
                        "field_type": "a",
                        "field_name": "Name"
                    },
                    "solar_distribution": {
                        "field_type": "a",
                        "field_name": "Solar Distribution"
                    },
                    "terrain": {
                        "field_type": "a",
                        "field_name": "Terrain"
                    },
                    "north_axis": {
                        "field_type": "n",
                        "field_name": "North Axis"
                    },
                    "maximum_number_of_warmup_days": {
                        "field_type": "n",
                        "field_name": "Maximum Number of Warmup Days"
                    },
                    "loads_convergence_tolerance_value": {
                        "field_type": "n",
                        "field_name": "Loads Convergence Tolerance Value"
                    },
                    "temperature_convergence_tolerance_value": {
                        "field_type": "n",
                        "field_name": "Temperature Convergence Tolerance Value"
                    },
                    "minimum_number_of_warmup_days": {
                        "field_type": "n",
                        "field_name": "Minimum Number of Warmup Days"
                    }
                },
                "alphas": {
                    "fields": [
                        "name",
                        "terrain",
                        "solar_distribution"
                    ]
                },
                "fields": [
                    "name",
                    "north_axis",
                    "terrain",
                    "loads_convergence_tolerance_value",
                    "temperature_convergence_tolerance_value",
                    "solar_distribution",
                    "maximum_number_of_warmup_days",
                    "minimum_number_of_warmup_days"
                ]
            },
            "maxProperties": 1,
            "minProperties": 1,
            "type": "object",
            "min_fields": 8.0
        }
    },
    "epJSON_schema_build": "40101eaafd"
}"""

idftxt = """
{
    "Building": {
        "Bldg": {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 3,
            "loads_convergence_tolerance_value": 0.05,
            "maximum_number_of_warmup_days": 30,
            "minimum_number_of_warmup_days": 6,
            "north_axis": 0.0,
            "solar_distribution": "MinimalShadowing",
            "temperature_convergence_tolerance_value": 0.05,
            "terrain": "Suburbs"
        }
    }
}
"""

fhandle = StringIO(txt)
idfhandle = StringIO(idftxt)
iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"

idf = IDF(idfname=fname, iddname=iddfname)
print(idf)


# idf = IDF(idfname=fname)

# pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldproperty('branch_list_name'))
# print(idf.idfobjects['AirLoopHVAC'][0])
# for fname in idf.idd.iddobjects['AirLoopHVAC'].fieldnames():
#     print(fname)
# pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldnames())



# print(idf)

# idf.saveas('karamba.txt')
# idfobjects = {key:[val1 for val1 in val.values()] for key, val in idf.idf.items()}

# cracsystem = idf.idfobjects['AirLoopHVAC'][0]
# pprint(cracsystem.eppy_objidd.fieldnames())
# print()
# pprint(cracsystem.eppy_objidd.fieldproperty('demand_side_inlet_node_names'))
# print(crac)