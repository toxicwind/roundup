"""
Constraint argument schemas for benchmark configuration.
"""

from roundup.schemas.scheduler.constraints.args import (
    ConstraintArgs,
    ErrorRate,
    ErrorRateOrList,
    PositiveNum,
    PositiveNumOrList,
)
from roundup.schemas.scheduler.constraints.error import (
    MaxErrorRateConstraintArgs,
    MaxErrorsConstraintArgs,
    MaxGlobalErrorRateConstraintArgs,
)
from roundup.schemas.scheduler.constraints.request import (
    MaxDurationConstraintArgs,
    MaxRequestsConstraintArgs,
    MinRequestsConstraintArgs,
)
from roundup.schemas.scheduler.constraints.saturation import (
    OverSaturationConstraintArgs,
)

__all__ = [
    "ConstraintArgs",
    "ErrorRate",
    "ErrorRateOrList",
    "MaxDurationConstraintArgs",
    "MaxErrorRateConstraintArgs",
    "MaxErrorsConstraintArgs",
    "MaxGlobalErrorRateConstraintArgs",
    "MaxRequestsConstraintArgs",
    "MinRequestsConstraintArgs",
    "OverSaturationConstraintArgs",
    "PositiveNum",
    "PositiveNumOrList",
]
