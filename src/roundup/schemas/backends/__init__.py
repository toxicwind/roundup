"""
Backend Args schemas for Roundup backend configuration.
"""

from __future__ import annotations

from roundup.schemas.backends.backend import BackendArgs
from roundup.schemas.backends.openai_http import OpenAIHTTPBackendArgs
from roundup.schemas.backends.openai_websocket import OpenAIWebSocketBackendArgs
from roundup.schemas.backends.vllm_python import VLLMPythonAsyncBackendArgs
from roundup.schemas.backends.vllm_python_batch import VLLMPythonBatchBackendArgs

__all__ = [
    "BackendArgs",
    "OpenAIHTTPBackendArgs",
    "OpenAIWebSocketBackendArgs",
    "VLLMPythonAsyncBackendArgs",
    "VLLMPythonBatchBackendArgs",
]
