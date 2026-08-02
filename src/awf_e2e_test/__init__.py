"""Minimal package used to validate the Adaptive Agent Workflow."""

from .calculator import add, divide
from .statistics import mean
from .summary import StatisticsSummary, describe

__all__ = ["StatisticsSummary", "add", "describe", "divide", "mean"]
