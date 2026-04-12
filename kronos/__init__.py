"""Kronos - Time Series Prediction Library

A fork of shiyu-coder/Kronos providing tools for time series forecasting,
particularly suited for financial market data.

Modules:
    model: Core Kronos prediction model
    utils: Utility functions for data preparation and visualization
    data: Data loading and preprocessing tools

Personal fork notes:
    - Using this for experimenting with stock price forecasting
    - See examples/ directory for usage notebooks
    - Added plot_forecast to default imports for convenience
"""

__version__ = "0.1.0"
__author__ = "Kronos Contributors"
__license__ = "MIT"

from kronos.model import KronosModel
from kronos.utils import (
    prepare_time_series,
    normalize_series,
    denormalize_series,
    plot_forecast,  # frequently needed, so importing by default
)

__all__ = [
    "KronosModel",
    "prepare_time_series",
    "normalize_series",
    "denormalize_series",
    "plot_forecast",
]
