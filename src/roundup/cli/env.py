"""Environment configuration display command."""

from __future__ import annotations

import click

from roundup.settings import print_config

__all__ = ["env"]


@click.command(
    short_help="Show environment variable settings.",
    help="Display environment variables for configuring Roundup behavior.",
)
def env():
    print_config()
