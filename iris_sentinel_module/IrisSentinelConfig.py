"""
  IRIS sentinel Source Code
  Copyright (C) 2023 - RedNoodles
  sam@rednoodles.bid
  Created by RedNoodles - 2023-12-17

  License MIT
"""
module_name = "IrisSentinel"
module_description = "Pipeline for Sentinel Logs"
interface_version = "1.2.0"
module_version = "0.1.0"

pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "sentinel_pipeline",
    "pipeline_human_name": "Sentinel Pipeline",
    "pipeline_args": ["testarg1"],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}


module_configuration: list[dict] = []
