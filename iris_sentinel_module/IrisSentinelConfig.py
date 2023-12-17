#!/usr/bin/env python3
#
#
#  IRIS sentinel Source Code
#  Copyright (C) 2023 - RedNoodles
#  sam@rednoodles.bid
#  Created by RedNoodles - 2023-12-17
#
#  License MIT

module_name = "IrisSentinel"
module_description = ""
interface_version = 1.1
module_version = 1.0

pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "sentinel_pipeline",
    "pipeline_human_name": "sentinel Pipeline",
    "pipeline_args": [
        ['sentinel_arg', 'optional']
    ],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}


module_configuration = [
    {
        "param_name": "sentinel_url",
        "param_human_name": "sentinel URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "sentinel_key",
        "param_human_name": "sentinel key",
        "param_description": "sentinel API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    },
    
]