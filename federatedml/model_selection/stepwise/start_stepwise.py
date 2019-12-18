#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from arch.api.utils import log_utils
from federatedml.model_selection.stepwise.stepwise import Stepwise

LOGGER = log_utils.getLogger()


def _get_stepwise_param(model):
    model.model_param.stepwise_param.role = model.role
    model.model_param.stepwise_param.mode = model.mode
    return model.model_param.cv_param


def run(model, train_data, test_data):
    if not model.need_run:
        return train_data
    step_obj = Stepwise()
    stepwise_param = _get_stepwise_param(model)
    step_obj.run(stepwise_param, train_data, test_data, model)
    LOGGER.info("Finish Stepwise run")
    return train_data
