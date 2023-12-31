#!/usr/bin/env python3
#
#
#  IRIS sentinel Source Code
#  Copyright (C) 2023 - RedNoodles
#  sam@rednoodles.bid
#  Created by RedNoodles - 2023-12-17
#
#  License MIT

import traceback
from pathlib import Path

import iris_interface.IrisInterfaceStatus as InterfaceStatus
from iris_interface.IrisModuleInterface import IrisPipelineTypes, IrisModuleInterface, IrisModuleTypes

import iris_sentinel_module.IrisSentinelConfig as interface_conf
from iris_sentinel_module.sentinel_handler.sentinel_handler import SentinelHandler


class IrisSentinelInterface(IrisModuleInterface):
    """
    Provide the interface between Iris and sentinelHandler
    """
    name = "IrisSentinelInterface"
    _module_name = interface_conf.module_name
    _module_description = interface_conf.module_description
    _interface_version = interface_conf.interface_version
    _module_version = interface_conf.module_version
    _pipeline_support = interface_conf.pipeline_support
    _pipeline_info = interface_conf.pipeline_info
    _module_configuration = interface_conf.module_configuration
    
    _module_type = IrisModuleTypes.module_pipeline
    
    
    def pipeline_handler(self, pipeline_type, pipeline_data):
        """
        Receive data from the main pipeline and dispatch to sentinel handler
        :param pipeline_type:
        :param pipeline_data:
        :return:
        """

        if pipeline_type == IrisPipelineTypes.pipeline_type_import:
            #  Call the import chain as task chain
            return self.task_files_import(input_data=pipeline_data)

        elif pipeline_type == IrisPipelineTypes.pipeline_type_update:
            # Call the update chain as task chain
            return self.task_files_import(input_data=pipeline_data)

        else:
            return InterfaceStatus.I2Error('Unrecognized pipeline type')

    def pipeline_files_upload(self, base_path, file_handle, case_customer, case_name, is_update):
        """
        Handle the files for a specific
        :return:
        """

        if base_path and Path(base_path).is_dir:
            file_handle.save(Path(base_path, file_handle.filename))
            return InterfaceStatus.I2Success("Successfully saved file {} to {}".format(file_handle.filename, base_path))

        else:
            return InterfaceStatus.I2Error("Directory {} not found. Can't save file".format(base_path))

    def task_files_import(self, input_data):

        try:
            configuration = self.get_configuration_dict()
            if self._evidence_storage:

                if configuration.is_success():

                    sentinel_handler = SentinelHandler(mod_config=self.module_dict_conf,
                                                       server_config=self.server_dict_conf,
                                                       evidence_storage=self._evidence_storage,
                                                       input_data=input_data,
                                                       logger=self.log)

                    ret = sentinel_handler.import_evidence()
                    if not ret:
                        return InterfaceStatus.I2Error(logs=list(self.message_queue))

                    return InterfaceStatus.I2Success(logs=list(self.message_queue))

                else:
                    self.log.error(logs=[configuration.get_message()])
                    logs = [configuration.get_message()]
            else:
                self.log.error('Evidence storage not available')
                logs = ['Evidence storage not available']

            return InterfaceStatus.I2Error(logs=logs)

        except Exception as e:
            traceback.print_exc()
            return InterfaceStatus.I2Error(logs=[traceback.print_exc()])
     
