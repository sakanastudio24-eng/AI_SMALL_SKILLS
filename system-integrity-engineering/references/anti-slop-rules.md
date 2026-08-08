# Anti-Slop Rules

Use this reference before accepting AI-generated architecture, generated tests, broad refactors, or code that appears complete but may not preserve real behavior.

## Reject Unless Justified

- giant service classes
- generic manager classes
- repositories that expose every table operation
- duplicated policy across frontend, backend, and SQL
- magic strings scattered across layers
- broad `catch` blocks that erase error meaning
- UI components containing business authority
- hidden network calls
- hidden writes in read endpoints
- unbounded retries
- automatic mutation retry after an uncertain result
- temporary unsafe bypasses without expiry or removal plan
- tests that assert implementation text but are described as runtime proof
- speculative abstractions with one use
- massive refactors mixed with unrelated feature work
- comments that explain avoidable complexity instead of removing it
- interfaces larger than their consumers need
- new code that copies an existing state controller instead of reusing or adapting its proven pattern

## Reject Blind SOLID Ceremony

- Do not create a class when a pure function is clearer.
- Do not add an interface for every concrete implementation.
- Do not split coherent code only to reduce line count.
- Do not add layers that merely forward calls.
- Require abstraction to reduce coupling or preserve a meaningful contract.

## Reality Check

Before closeout, ask:

- What real behavior did this preserve?
- Which source of truth is authoritative?
- Which boundary is actually tested?
- What can fail at runtime and how is it diagnosed?
- Did this change require rewriting previously working systems?
- Is there any new business rule duplicated across layers?
