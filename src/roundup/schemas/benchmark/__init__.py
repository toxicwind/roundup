"""
Centralized benchmark argument schemas for Roundup.
"""

from roundup.schemas.benchmark.entrypoints import (
    BenchmarkArgs,
    BenchmarkMetadata,
    BenchmarkScenario,
    GenerativeMetricsArgs,
    MetricsArgs,
    args_model_config,
    default_kind,
    default_kind_list,
)
from roundup.schemas.benchmark.goodput import GoodputSLO
from roundup.schemas.benchmark.outputs import (
    BenchmarkOutputArgs,
    ConsoleBenchmarkOutputArgs,
    CSVBenchmarkOutputArgs,
    HTMLBenchmarkOutputArgs,
    JSONBenchmarkOutputArgs,
    PlotBenchmarkOutputArgs,
    YAMLBenchmarkOutputArgs,
)
from roundup.schemas.benchmark.profiles import (
    AsyncProfileArgs,
    ConcurrentProfileArgs,
    GoodputProfileArgs,
    ProfileArgs,
    ReplayProfileArgs,
    SweepProfileArgs,
    SynchronousProfileArgs,
    ThroughputProfileArgs,
)
from roundup.schemas.benchmark.random import RandomArgs, StaticRandomArgs
from roundup.schemas.benchmark.scenarios import SCENARIO_DIR, get_builtin_scenarios
from roundup.schemas.benchmark.transient import TransientPhaseConfig

__all__ = [
    "SCENARIO_DIR",
    "AsyncProfileArgs",
    "BenchmarkArgs",
    "BenchmarkMetadata",
    "BenchmarkOutputArgs",
    "BenchmarkScenario",
    "CSVBenchmarkOutputArgs",
    "ConcurrentProfileArgs",
    "ConsoleBenchmarkOutputArgs",
    "GenerativeMetricsArgs",
    "GoodputProfileArgs",
    "GoodputSLO",
    "HTMLBenchmarkOutputArgs",
    "JSONBenchmarkOutputArgs",
    "MetricsArgs",
    "PlotBenchmarkOutputArgs",
    "ProfileArgs",
    "RandomArgs",
    "ReplayProfileArgs",
    "StaticRandomArgs",
    "SweepProfileArgs",
    "SynchronousProfileArgs",
    "ThroughputProfileArgs",
    "TransientPhaseConfig",
    "YAMLBenchmarkOutputArgs",
    "args_model_config",
    "default_kind",
    "default_kind_list",
    "get_builtin_scenarios",
]
