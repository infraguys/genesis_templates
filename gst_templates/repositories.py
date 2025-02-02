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

import git


class GitRepository:

    def __init__(self, repository_path):
        super().__init__()
        self._repository_path = os.path.abspath(repository_path)

    def _init_directory(self):
        """
        Checks if the repository directory exists and if it is a directory.
        If not, raise a ValueError.
        If yes, create the directory if it does not exist.

        :return: None
        """
        os.makedirs(self._repository_path, exist_ok=True)
        if not os.path.isdir(self._repository_path):
            raise ValueError(
                f"{self._repository_path} is a file, but expected a directory"
            )

    def is_repo_initialized(self):
        """
        Checks if the repository is initialized.

        This method checks if the repository is properly initialized by trying
        to create a Git repository object.

        :return: True if the repository is initialized, False otherwise.
        :rtype: bool
        """
        try:
            git.Repo(self._repository_path)
            return True
        except git.InvalidGitRepositoryError:
            return False

    def has_uncommitted_changes(self):
        """
        Checks if there are uncommitted changes in the repository.

        This method checks if the repository has any uncommitted changes,
        including untracked files.

        :return: True if there are uncommitted changes, False otherwise.
        :rtype: bool
        """

        repo = git.Repo(self._repository_path)
        return repo.is_dirty(untracked_files=True)

    def initialize_repository(self):
        """
        Initializes a new Git repository.

        This method creates a new Git repository in the
        `_repository_path` directory. If the directory does not exist,
        it will be created.

        :return: None
        """
        self._init_directory()
        if not self.is_repo_initialized():
            git.Repo.init(self._repository_path)

    @property
    def path(self):
        """
        The absolute path of the repository.

        :return: The absolute path of the repository as a string.
        :rtype: str
        """
        return self._repository_path

    def add_file(self, file_path):
        repo = git.Repo(self._repository_path)
        repo.git.add(file_path)

    def commit(self, message=None):
        message = message or "Automated commit"
        repo = git.Repo(self._repository_path)
        repo.git.commit(m=message)
