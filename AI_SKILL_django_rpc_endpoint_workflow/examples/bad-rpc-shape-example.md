# Bad RPC Shape Example

## Problem
A single endpoint named `POST /api/team/action/` accepts a `type` field and performs unrelated operations.

## Why It Fails
Validation, permission rules, and service boundaries become unclear.

## Better Shape
Split into explicit endpoints such as `send-invite`, `remove-member`, and `archive-team`.
