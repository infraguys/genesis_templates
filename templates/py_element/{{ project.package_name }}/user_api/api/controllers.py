#    Copyright {{ functions.now().strftime('%Y') }} {{ author.name }}.
#
#    All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from gcl_iam import controllers as iam_controllers
from restalchemy.api import controllers as ra_controllers
from restalchemy.api import resources as ra_resources

from {{ project.package_name }}.user_api.api import versions
from {{ project.package_name }}.user_api.dm import models


class ApiEndpointController(ra_controllers.RoutesListController):
    """Controller for /v1/ endpoint"""

    __TARGET_PATH__ = f"/{versions.API_VERSION_1_0}/"


class ExampleController(
    iam_controllers.PolicyBasedControllerMixin,
    ra_controllers.BaseResourceControllerPaginated,
):
    __policy_service_name__ = "{{ project.package_name }}"
    __policy_name__ = "example"

    __resource__ = ra_resources.ResourceByRAModel(
        model_class=models.ExampleModel,
        convert_underscore=False,
    )
