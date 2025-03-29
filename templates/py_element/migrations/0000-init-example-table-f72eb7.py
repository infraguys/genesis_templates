#    Copyright 2016 Eugene Frolov <eugene@frolov.net.ru>
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

from restalchemy.storage.sql import migrations


class MigrationStep(migrations.AbstarctMigrationStep):

    def __init__(self):
        self._depends = []

    @property
    def migration_id(self):
        return "f72eb746-75cc-4a75-87c1-143091726f78"

    @property
    def is_manual(self):
        return False

    def upgrade(self, session):
        expressions = [
            """
            CREATE TABLE IF NOT EXISTS "examples" (
                "uuid" UUID PRIMARY KEY,
                status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE')),
                "name" VARCHAR(256) NOT NULL,
                "description" VARCHAR(256) NOT NULL,
                "project_id" UUID NOT NULL,
                "created_at" TIMESTAMP(6) NOT NULL DEFAULT NOW(),
                "updated_at" TIMESTAMP(6) NOT NULL DEFAULT NOW()
            );
            """,
            """
            CREATE INDEX "examples_name_idx" ON "examples" ("name");
            """,
            """
            CREATE INDEX "examples_project_id_idx" ON "examples" (
                "project_id"
            );
            """,
        ]

        for expression in expressions:
            session.execute(expression)

    def downgrade(self, session):
        tables = ["examples"]

        for table in tables:
            self._delete_table_if_exists(session, table)


migration_step = MigrationStep()
