# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging
from os import getenv

from validation.tests.github import GithubTests
from validation.tests.gitlab import GitlabTests

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    if getenv("GITLAB_TOKEN"):
        logging.info("Running validation for GitLab.")
        GitlabTests().run()
    else:
        logging.info("GITLAB_TOKEN not set, skipping the validation for GitLab.")

    if getenv("GITLAB_GNOME_TOKEN"):
        logging.info("Running validation for GitLab (gitlab.gnome.org instance).")
        GitlabTests(
            instance_url="https://gitlab.gnome.org/",
            namespace="packit-validation",
            token_name="GITLAB_GNOME_TOKEN",
        ).run()
    else:
        logging.info(
            "GITLAB_GNOME_TOKEN not set, "
            "skipping the validation for GitLab (gitlab.gnome.org instance).",
        )

    if getenv("GITLAB_FREEDESKTOP_TOKEN"):
        logging.info("Running validation for GitLab (gitlab.freedesktop.org instance).")
        GitlabTests(
            instance_url="https://gitlab.freedesktop.org/",
            namespace="packit-service",
            token_name="GITLAB_FREEDESKTOP_TOKEN",
        ).run()
    else:
        logging.info(
            "GITLAB_FREEDESKTOP_TOKEN not set, "
            "skipping the validation for GitLab (gitlab.freedesktop.org instance).",
        )

    if getenv("SALSA_DEBIAN_TOKEN"):
        logging.info("Running validation for GitLab (salsa.debian.org instance).")
        GitlabTests(
            instance_url="https://salsa.debian.org/",
            namespace="packit-validation",
            token_name="SALSA_DEBIAN_TOKEN",
        ).run()
    else:
        logging.info(
            "SALSA_DEBIAN_TOKEN not set, "
            "skipping the validation for GitLab (salsa.debian.org instance).",
        )

    if getenv("GITHUB_TOKEN"):
        logging.info("Running validation for GitHub.")
        GithubTests().run()
    else:
        logging.info("GITHUB_TOKEN not set, skipping the validation for GitHub.")
