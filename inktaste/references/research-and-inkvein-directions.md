# Research and InkVein Directions

Read this file for InkVein-specific audits and Mobbin research.

## Mobbin Research Law

Use Mobbin as research, never as a copying engine.

For each major screen or section:

1. Understand the InkVein screen's actual purpose.
2. Identify the specific UX problem.
3. Search Mobbin by screen purpose, interaction type, information hierarchy, or an approved reference app name.
4. Visually inspect the returned screens.
5. Extract interaction and hierarchy principles.
6. Decide what applies to InkVein.
7. Reject patterns that conflict with InkVein's product model.
8. Implement an InkVein-native structure.

Do not search vague phrases such as "beautiful modern UI" and copy the first result. Do not claim Mobbin research without visual inspection. If access is unavailable, mark research evidence unavailable and continue only when the task can be completed from source and supplied evidence.

## Approved References

### Glassdoor

Use for named global navigation, community structure, location hierarchy, and reducing unnecessary container nesting.

### Mimo

Strong Settings reference. Study section hierarchy, switches for booleans, clear navigation rows, a distinct destructive section, low container dependence, and simple information architecture.

### YouTube

Strongest Profile reference. Study identity-to-controls-to-content hierarchy, creator content prominence, local content tabs, and labeled global navigation. Do not copy YouTube styling blindly.

### Strava

Use for global-to-screen-to-local navigation hierarchy, local tabs, clear location, and background/cover imagery where identity or context benefits. Zech specifically favors the cover-image treatment.

### GroupMe

Use selectively for Group information/settings, secondary Group navigation, and simple group identity plus quick action plus navigation-row structure. Do not use it as the visual direction for main Group Home or Group management/admin UI.

## Current InkVein Directions

### Profile

- Future stats: Artifacts / Pulls / Impact.
- Do not put Bio in a decorative container without grouping need.
- Add real media preview for videos when scoped.
- Give Projects a clear Create affordance.
- Make Groups-tab navigation correct.
- Make Artifact View All real before exposing it.
- Hide unnecessary internal refs in Artifact rows.
- Reduce nested containers.
- Prefer YouTube as the leading reference.

### Settings

- Prefer Mimo as the leading reference.
- Challenge duplicated Account Status.
- Restructure Legal, Privacy & Data, Community Guidelines, and Help & Support.
- Add trustworthy app/build metadata later; never use fake values.

### Notifications

- Current categories: All, Unresolved, Needs Action.
- Current source definition: Unresolved means `status != archived`.
- Known UX debt: follower and Group-invite items can remain Unresolved after being viewed.
- Investigate notification-type-specific resolution semantics during InkTaste/polish; do not merely style the current behavior or invent lifecycle authority.

### Needs Action

- Restore three strike circles.
- Place Appeal on the right later.

### Create

- Improve photo support/presentation, preview, publish feedback, and bounded local drafts/recovery.
- Prefer background processing only where authority supports honest local preview and processing state.

### Groups

- Reduce excess containers and use a stronger full-width structure.
- Add media preview to Group Assets when scoped.
- Briefs are currently hidden.
- Move Posts toward the correct Asset-backed source direction.
- Add user/group media removal when scoped.
- Clarify Task Progress versus Group Progress semantically.

### Group Home

Do not use GroupMe as the main visual reference. Research stronger purpose-matched references.

### Home

- Improve Explore visibility.
- Prevent custom names from creating uncontrolled two-line headers.

### Events

- Remove the odd card/bottom-element artifact when scoped.
- Preserve existing Event lifecycle and product meaning.

### Explore and Search

- Structurally distinguish active and inactive typing states.
- Use authoritative profile photos.
- Strengthen hierarchy.

### Moderator and Admin Mobile

Prioritize usability and performance over broad visual redesign.

### Console

Consider UI later while preserving staff/admin purpose and strict contracts.

## Explicitly Deferred Product Scope

Do not create Calendar as part of an InkTaste section pass unless explicitly requested.

- Calendar V1: manual personal Calendar, manual Group Calendar, freeform Calendar Items.
- Calendar V2: copy a Group Calendar Item to personal Calendar as an independent snapshot with no synchronization.

## Final-Polish Boundary

After structural acceptance, leave only final color, fine spacing, typography refinement, shadows/surface treatment, motion, animation, micro-interactions, icon refinement, and bounded remaining performance optimization.

If major restructuring remains, the section has not passed InkTaste.
