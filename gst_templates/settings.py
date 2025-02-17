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
#

import os
import json

from gst_templates import jinja_functions


class TemplateSetting:

    TEMPLATE_INFO_SECTION = "template_info"
    FUNCTIONS_SECTION = "functions"

    def __init__(self, template_setting_path):
        self._template_setting_path = template_setting_path
        self._settings_vars = self._load_template_settings(
            template_setting_path
        )
        self._fill_template_parameters(self._settings_vars)
        super().__init__()

    def _load_template_settings(self, template_setting_path):
        """
        Load the template settings from a JSON file.

        This method takes the path to a JSON file representing the template
        settings and loads the settings from the file.

        :param template_setting_path: The path to the JSON file containing the
            template settings.
        :type template_setting_path: str
        :return: The loaded template settings.
        :rtype: dict
        """
        with open(template_setting_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _fill_template_parameters(self, settings_vars):
        """
        Fill in the template parameters based on the given template settings.

        This method takes the template settings dictionary and fills in the
        template parameters such as the name, version and path of the template.

        :param settings_vars: The template settings dictionary.
        :type settings_vars: dict
        """
        template_settings = settings_vars.pop(self.TEMPLATE_INFO_SECTION)
        self._name = template_settings.pop("name")
        self._version = template_settings.pop("version")
        self._path = self._get_template_path(template_settings.pop("path"))

    def initialize(self):
        tmp_settings = self.settings_vars
        for section_name, settings in self.settings_vars.items():
            if section_name in [
                self.TEMPLATE_INFO_SECTION,
                self.FUNCTIONS_SECTION,
            ]:
                continue

            print(f"Initializing {section_name} settings...")
            for param_name, param_value in settings.items():
                print(
                    f"Initializing parameter '{param_name}' [{param_value}]: ",
                    end="",
                )
                tmp_settings[section_name][param_name] = input() or param_value

        self._settings_vars = tmp_settings

    def save(self, new_project_settings_path):
        """
        Save the project settings to the specified path.

        This method takes the path to the new project settings file and saves
        the current project settings to the file.

        :param new_project_settings_path: The path to the new project settings
            file.
        :type new_project_settings_path: str
        """
        settings_vars = self.settings_vars
        settings_vars.pop(self.FUNCTIONS_SECTION)
        settings_vars.update(
            {
                self.TEMPLATE_INFO_SECTION: {
                    "name": self.name,
                    "version": self.version,
                    "template_file_name": self.file_name,
                }
            }
        )
        with open(new_project_settings_path, "w", encoding="utf-8") as fp:
            json.dump(settings_vars, fp, indent=4)

    def _get_template_path(self, path_from_settings):
        """
        Resolve the absolute path of the template using the given path from the
        settings.

        This method first changes the current working directory to the parent
        directory of the template setting path, then it resolves the absolute
        path of the template using the given path and finally it changes the
        current working directory back to the original current working
        directory.

        :param path_from_settings: The path of the template from the settings.
        :type path_from_settings: str
        :return: The absolute path of the template.
        :rtype: str
        """
        current_dir = os.getcwd()
        os.chdir(os.path.dirname(self._template_setting_path))
        template_path = os.path.abspath(path_from_settings)
        os.chdir(current_dir)
        return template_path

    @property
    def settings_vars(self):
        """
        The original template settings.

        :return: The original template settings.
        :rtype: dict
        """
        copy_settings = self._settings_vars.copy()
        copy_settings[self.FUNCTIONS_SECTION] = (
            jinja_functions.get_jinja_functions()
        )
        return copy_settings

    @property
    def name(self):
        """
        The name of the template setting.

        :return: The name of the template setting.
        :rtype: str
        """
        return self._name

    @property
    def version(self):
        """
        The version of the template setting.

        :return: The version of the template setting.
        :rtype: str
        """
        return self._version

    @property
    def path(self):
        """
        The path of the template setting.

        :return: The path of the template setting.
        :rtype: str
        """
        return self._path

    @property
    def template_files(self):
        """
        Retrieve all file paths within the template directory.

        This property method traverses the template directory specified by the
        `path` attribute, collecting all directory and file paths.

        :return: A list of directory and file paths within the template
                 directory.
        :rtype: list
        """

        all_paths = []
        for dirpath, _, filenames in os.walk(self.path):
            all_paths.append(dirpath)
            for filename in filenames:
                full_file_path = os.path.join(dirpath, filename)
                all_paths.append(full_file_path)

        return all_paths

    @property
    def file_name(self):
        """
        The file name of the template setting.

        :return: The file name of the template setting.
        :rtype: str
        """
        return os.path.basename(self._template_setting_path)
