#    Copyright 2025 Genesis Corporation.
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

import os

import jinja2


class JinjaTemplateRender:

    def __init__(self, template_settings, repository):
        super().__init__()
        self._template_settings = template_settings
        self._repository = repository

    def initialize_project_settings(self):
        """
        Initialize the project settings using the given template settings and
        repository.

        This method takes the template settings and repository, and uses them
        to initialize the project settings. It then saves the project settings
        to a file in the repository and commits the changes.

        :return: None
        """
        self._template_settings.initialize()

        template_path = os.path.join(
            self._repository.path, "project_settings.json"
        )

        self._template_settings.save(template_path)
        self._repository.add_file(template_path)
        self._repository.commit("Initialize project settings")

    def render_template(self):
        template_files = self._template_settings.template_files

        target_files = (
            jinja2.Template("\n".join(template_files))
            .render(**self._template_settings.settings_vars)
            .split("\n")
        )

        # Replace template path prefix to repository path prefix
        target_files = [
            (
                self._repository.path
                + target_file[len(self._template_settings.path) :]
            )
            for target_file in target_files
        ]

        for source_path, target_path in zip(template_files, target_files):
            # create directory if it does not exist
            if os.path.isdir(source_path):
                os.makedirs(target_path, exist_ok=True)
                continue

            # Render and copy files
            with open(source_path, "r", encoding="utf-8") as fp1:
                with open(target_path, "w", encoding="utf-8") as fp2:
                    fp2.write(
                        jinja2.Template(fp1.read()).render(
                            **self._template_settings.settings_vars
                        )
                    )
