#!/usr/bin/env python3
"""
Google Ads Management System - Ads Module
=========================================

This module contains the core components for managing Google Ads campaigns
with safety guardrails, phase progression, and baseline configuration.

Modules:
- guardrails: Enforces change safety for Performance Max campaigns
- phase_manager: Manages campaign progression through different phases
- ensure_baseline_config: Validates and repairs baseline configuration
"""

from .guardrails import PerformanceMaxGuardrails, GuardrailVerdict, ChangeType
from .phase_manager import CampaignPhaseManager, PhaseEligibilityResult, PhaseProgressResult, CampaignPhase
from .ensure_baseline_config import BaselineConfigValidator, BaselineConfigResult
from .notifications import NotificationManager, NotificationConfig, NotificationType

__version__ = "1.0.0"
__author__ = "AI-Powered Google Ads Management System"

__all__ = [
    'PerformanceMaxGuardrails',
    'GuardrailVerdict', 
    'ChangeType',
    'CampaignPhaseManager',
    'PhaseEligibilityResult',
    'PhaseProgressResult',
    'CampaignPhase',
    'BaselineConfigValidator',
    'BaselineConfigResult',
    'NotificationManager',
    'NotificationConfig',
    'NotificationType'
]
