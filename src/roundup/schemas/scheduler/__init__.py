"""
Scheduler-related argument schemas.
"""

from roundup.schemas.scheduler.constraints import (
    ConstraintArgs,
    ErrorRate,
    ErrorRateOrList,
    MaxDurationConstraintArgs,
    MaxErrorRateConstraintArgs,
    MaxErrorsConstraintArgs,
    MaxGlobalErrorRateConstraintArgs,
    MaxRequestsConstraintArgs,
    MinRequestsConstraintArgs,
    OverSaturationConstraintArgs,
    PositiveNum,
    PositiveNumOrList,
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
