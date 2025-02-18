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

from datetime import datetime, timezone

from restalchemy.dm import filters
from restalchemy.dm import models
from restalchemy.dm import properties
from restalchemy.dm import relationships
from restalchemy.dm import types
from restalchemy.storage.sql import orm


# class ExampleModel(models.ModelWithUUID, orm.SQLStorableMixin):
#     __tablename__ = "table_name"
#     name = properties.property(types.String(max_length=255), default="")
