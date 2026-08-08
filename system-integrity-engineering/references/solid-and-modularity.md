# SOLID And Modularity

Use this reference when changing classes, modules, service boundaries, extension points, or large functions.

## Single Responsibility

A function, component, class, or module should have one coherent responsibility and one principal reason to change.

Split when responsibilities change for different reasons. Do not split coherent code just to reduce line count.

Identify the role before editing:

- policy
- orchestration
- adapter
- parser
- renderer
- diagnostic mapper
- storage

## Open/Closed

Stable code should allow new capabilities through extension without rewriting proven behavior.

Use strategies, registries, handlers, adapters, discriminated unions, or composable policies when real variation exists.

An extension seam must be justified by multiple implementations, predictable future variants, a volatile integration boundary, or repeated modification pressure.

Do not create a speculative plugin system for one implementation.

## Liskov Substitution

Subtypes and implementations must preserve declared promises.

A replacement must not:

- weaken required outputs
- introduce unexpected side effects
- change error meaning
- reject promised inputs
- require callers to know concrete implementation details

Require contract tests when multiple implementations exist.

## Interface Segregation

Use narrow capability-focused interfaces. A dependency should receive only the methods it needs.

Avoid broad names such as:

```text
EverythingRepository
ApplicationService
GlobalApiClient
Manager
```

Prefer focused names appropriate to the project:

```text
CaseReader
DecisionWriter
NotificationPublisher
DiagnosticRecorder
TokenIssuer
```

## Dependency Inversion

High-level policy depends on abstractions. Low-level adapters implement those abstractions.

Do not let high-level business logic depend directly on HTTP response libraries, SQL client details, environment variables, UI framework state, or vendor-specific error bodies.

## Modularity Test

Before accepting the structure, ask:

- Can this behavior be changed without editing unrelated working flows?
- Can the core decision be tested without infrastructure?
- Does this abstraction remove coupling or only forward calls?
- Does the module name describe one responsibility?
