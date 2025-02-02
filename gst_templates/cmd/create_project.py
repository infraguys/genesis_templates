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

import logging
import sys

from oslo_config import cfg

from gst_templates.common import config
from gst_templates.common import log as infra_log
from gst_templates import renders
from gst_templates import repositories
from gst_templates import settings


cli_opts = [
    cfg.StrOpt(
        "template_settings",
        default="./templates/py_dummy.settings.json",
        help="The path to the template settings file.",
    ),
    cfg.StrOpt(
        "target_directory",
        help="The path to the target directory.",
    ),
]


CONF = cfg.CONF
CONF.register_cli_opts(cli_opts)


def main():
    # Parse config
    config.parse(sys.argv[1:])

    # Configure logging
    infra_log.configure()
    log = logging.getLogger(__name__)

    template_setting = settings.TemplateSetting(CONF.template_settings)

    repository = repositories.GitRepository(CONF.target_directory)
    repository.initialize_repository()
    if repository.has_uncommitted_changes():
        log.error("The target directory contains uncommitted changes.")
        sys.exit(-1)

    template_render = renders.JinjaTemplateRender(
        template_setting,
        repository,
    )
    template_render.initialize_project_settings()
    template_render.render_template()

    log.info("Bye!!!")


if __name__ == "__main__":
    main()
