# Module Boundary Map Example

## Current Problem

The billing page imports pricing rules, payment transport formatting, and invoice rendering utilities from three separate feature areas, making every billing change cross-cut multiple owners.

## Better Shape

- `billing-domain`: pricing rules, invoice rules, state transitions
- `billing-api`: request/response contracts
- `billing-ui`: screens and components
- `billing-infra`: provider integrations and persistence adapters
