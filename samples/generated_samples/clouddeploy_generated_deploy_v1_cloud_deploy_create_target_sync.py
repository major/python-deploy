# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateTarget
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-deploy


# [START clouddeploy_generated_deploy_v1_CloudDeploy_CreateTarget_sync]
from google.cloud import deploy_v1


def sample_create_target():
    # Create a client
    client = deploy_v1.CloudDeployClient()

    # Initialize request argument(s)
    request = deploy_v1.CreateTargetRequest(
        parent="parent_value",
        target_id="target_id_value",
    )

    # Make the request
    operation = client.create_target(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END clouddeploy_generated_deploy_v1_CloudDeploy_CreateTarget_sync]