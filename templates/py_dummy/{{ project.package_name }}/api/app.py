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

from restalchemy.api import applications
from restalchemy.api.middlewares import contexts
from restalchemy.api.middlewares import logging
from restalchemy.api.middlewares import errors
from restalchemy.api.middlewares import retry_on_error
from restalchemy.api import routes
from restalchemy.storage import exceptions as storage_exc

from {{ project.package_name }}.api import controllers
from {{ project.package_name }}.api import routes as app_routes
from {{ project.package_name }}.api import versions


class UserApiApp(routes.Route):
    __controller__ = controllers.RootController
    __allow_methods__ = [routes.FILTER]


# Route to /1.0.0/ endpoint.
setattr(UserApiApp, versions.API_VERSION_1_0, routes.route(app_routes.ApiEndpointRoute))


def get_user_api_application():
    return UserApiApp


def attach_middlewares(app, middlewares_list):
    for middleware in middlewares_list:
        app = middleware(application=app)
    return app


def configure_middleware(middleware_class, *args, **kwargs):
    def build_middleware(application):
        return middleware_class(application=application, *args, **kwargs)

    return build_middleware


def build_wsgi_application():
    return attach_middlewares(
        applications.Application(get_user_api_application()),
        (
            contexts.ContextMiddleware,
            configure_middleware(
                middleware_class=retry_on_error.RetryOnErrorsMiddleware,
                exceptions=storage_exc.DeadLock,
            ),
            errors.ErrorsHandlerMiddleware,
            logging.LoggingMiddleware,
        ),
    )
