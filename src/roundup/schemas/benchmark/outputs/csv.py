from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field

from roundup.schemas.benchmark.outputs.output import BenchmarkOutputArgs
from roundup.settings import settings

__all__ = ["CSVBenchmarkOutputArgs"]


@BenchmarkOutputArgs.register("csv")
class CSVBenchmarkOutputArgs(BenchmarkOutputArgs):
    """Model for CSV benchmark output arguments."""

    kind: Literal["csv"] = Field(
        default="csv",
        description="The kind of output.",
    )
    path: Path = Field(
        default_factory=lambda: settings.default_results_dir / "benchmarks.csv",
        description="The file to save the output to.",
    )
