from __future__ import annotations

from cache_key_audit.models import Rule

PROJECT_NAME = 'cache-key-audit'
SUMMARY = 'Find tenant and user isolation risks in cache key designs.'
SAMPLE_RISK = 'cache key /account/settings tenant missing user missing shared true'
SAMPLE_CLEAN = 'cache key tenant:{tenant_id}:user:{user_id}:settings shared false ttl 300'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-tenant',
        severity='high',
        pattern='\\btenant\\s*(missing|none|null)\\b',
        message='tenant dimension is missing',
        recommendation='Include tenant or workspace ID in the cache key.',
    ),
    Rule(
        code='missing-user',
        severity='medium',
        pattern='\\buser\\s*(missing|none|null)\\b',
        message='user dimension may be missing',
        recommendation='Include user ID for personalized responses.',
    ),
    Rule(
        code='shared-cache',
        severity='low',
        pattern='\\bshared\\s*true\\b',
        message='shared cache is enabled',
        recommendation='Confirm response is safe for shared caching.',
    ),
)
