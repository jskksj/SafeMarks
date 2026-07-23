# SafeMarks

SafeMarks is a platform-agnostic, command-line-driven bookmark deduplication system built for maximum reliability, transparency, and architectural cleanliness. Designed from the ground up using a strict functional programming style and immutable data structures, SafeMarks completely decouples its core domain logic from any specific hosting environment or user interface.

Core Architecture & Philosophy

SafeMarks is engineered around two foundational pillars:
- Extreme Modularity: The codebase avoids monolithic files entirely. Every distinct logical operation—down to individual transformations—resides in its own isolated file, ensuring maximum code clarity and zero bloat.
- Test-Driven Development (TDD): Integration and unit tests serve as the primary, executable architecture specification. The test suite strictly governs correctness before any implementation code is introduced.

Following a clean Unix philosophy, SafeMarks utilizes a lightweight Python stack with uncompromising boundaries separating pure domain rules, parsing logic, and execution layers.

Hard Rules & Boundaries

SafeMarks enforces strict operational constraints to guarantee user safety and deterministic behavior:

1. No Monolithic Files: Functions are never lumped together into general utility scripts. Each operation lives in its own dedicated module.
2. Explicit User Control: The application operates strictly on a manual, user-triggered lifecycle consisting of Idle, Scan, Interactive Review, and Execution phases. There is no background polling, automatic scanning, or unconfirmed mutation.
3. Atomic Operations & Interruption Safety: Folder tree deletions execute atomically as single transactions. If an operation is interrupted, active transactional units complete fully to prevent orphaned states or partial deletions.
4. Permanent Deletions: SafeMarks features no undo system. Instead, absolute safety is enforced upstream through rigorous safety threshold analysis (defaulting to a 20-group limit) and mandatory human confirmation gates.
5. Deterministic Comparison Rules: Duplicate identification is completely objective, relying on a strict, ordered sequence of URI normalization steps (canonicalizing transport schemes, lowercasing authorities, removing trailing slashes, preserving query parameters) and recursive subtree signature generation.
