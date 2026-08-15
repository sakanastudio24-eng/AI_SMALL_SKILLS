# InkTaste Core Laws

Read this file for every InkTaste screen or section audit.

## First-Time User Questions

Within ten seconds, the screen should answer:

1. Where am I?
2. What person, object, or group am I viewing?
3. What state is it in?
4. What matters most?
5. What is the primary action?
6. What else is interactive?
7. What will happen if I tap?
8. What happened after I tapped?

## Ten-Second Screen Test

Ask:

1. Where am I?
2. What object, person, or group am I seeing?
3. What is its current state?
4. What information matters most?
5. What is the primary action?
6. What else is pressable?
7. Is status distinct from action?
8. Is navigation distinct from settings and toggles?
9. If something is unavailable, is the reason understandable?
10. After an action, will the user know what happened?

## Laws

### 1. Location Must Be Explicit

Make the header the normal primary location and hierarchy surface. Avoid duplicating the title in the body.

### 2. Major Navigation Uses Icon and Label

Favor recognition over icon memory for important destinations, including bottom navigation. Back, Search, Settings, Close, and More may remain unlabeled only when context is unmistakable.

### 3. Users Do Not Scroll Back to Escape

Keep Back or another escape affordance predictably reachable on detail screens.

### 4. Hierarchy Outranks Decoration

Order content intentionally:

```text
location/header
-> subject/state
-> important information
-> primary action
-> secondary information/actions
```

A clear structure may pass V1 before final visual polish.

### 5. Every Interactive Object Looks Interactive

Clearly distinguish information, status, navigation, action, selection, boolean, More, and destructive controls.

### 6. Same Appearance Means Same Behavior

Do not reuse one pill or card treatment for unrelated interaction types.

### 7. Different Behavior Needs Different Treatment

Do not make badges, navigation rows, buttons, toggles, selections, or destructive actions visually interchangeable.

### 8. Use the Interaction Grammar

Follow the grammar defined in `SKILL.md`. Depart only when a stronger familiar platform pattern is demonstrably clearer.

### 9. Tags Communicate Meaning Families

Make related semantics feel related and different classification systems distinguishable. Never rely on color alone.

### 10. Recognition Beats Memory

Label InkVein-specific concepts such as Artifacts, Pulls, special Group actions, and moderation/admin actions until their meaning is sufficiently obvious.

### 11. One Concept Gets One Primary Home

Challenge duplication such as Group Progress versus Task Progress, repeated legal/community surfaces, redundant Account Status, or repeated Task identity. If two modules cannot be differentiated in one sentence, question whether both should exist.

### 12. Containers Communicate Grouping, Not Decoration

Avoid `page -> card -> card -> row card -> pill`. Prefer spacing, typography, alignment, separators, and section structure before adding another container.

### 13. Foreground and Background Depth Is Legible

Make active or pressable foreground layers stronger and passive structural layers quieter. Do not hard-code a final color system into InkTaste.

### 14. Quiet Surfaces Can Signal Seriousness

Consider quieter or white surfaces for Settings, Privacy/Data, Legal, Reporting, Disputes/Appeals, and safety-sensitive administration. Treat this as direction, not a universal white-background mandate.

### 15. One Obvious Primary Action

Do not let secondary actions compete equally with the main action.

### 16. Status Is Not Action

State communicates what something is. Action communicates what the user can do. Keep them distinct.

### 17. Current State Is Visible

Make selections, toggles, and tabs clearly expose their current state.

### 18. Actions Need Immediate Feedback

Use this hierarchy:

```text
inline/local feedback -> object-specific state or error
toast/bottom notification -> lightweight success, error, or background completion
blocking modal/screen -> only when progress cannot safely continue
```

### 19. Errors Are Local and Specific

Do not repeat a generic service failure across an entire page.

### 20. Prevent Predictable Invalid Actions

Keep the backend authoritative while avoiding controls the client already knows will predictably fail.

### 21. Never Fake a Button or Value

Allow no dead buttons, silent placeholders, fake metrics, fake build/version data, or fake View All. Remove unavailable behavior, disable it with an honest useful reason, or implement the smallest real behavior.

### 22. Loading Preserves Context

Prefer local loading over unnecessary full-screen blocking. When authority permits creation or publishing, consider immediate local preview at the destination with honest processing state and background upload/processing.

### 23. Preserve Unfinished Work

Consider bounded account/object-scoped local drafts for meaningful Create, Report, Appeal, Moderator, Admin, and long-text flows. Never imply local-only state is remotely saved. Do not persist secrets unnecessarily.

### 24. Empty States Explain the Space

When useful, explain what belongs here and how the user gets something here.

### 25. Labels Describe User Goals

Prefer concrete verbs and nouns: Create project, Add critique, View artifacts, Edit profile, Remove video. Avoid vague labels such as Manage or Continue when context does not make them clear.

### 26. Preserve Navigation Context

Back should normally restore the prior view, tab, and location.

### 27. Use Forgiving Touch Targets

Target approximately 44–48 logical pixels for common mobile interactions.

### 28. Limit Simultaneous Choices

Use progressive disclosure instead of many equally weighted controls.

### 29. Real Data Survives the UI

Give names, Groups, Tasks, Quills, Events, Projects, and headers bounded width, appropriate line rules, and ellipsis where needed. Prevent uncontrolled wrapping from breaking hierarchy.

### 30. Hide Internal Implementation Language

Avoid UUIDs, unnecessary safe refs, backend status keys, internal source refs, and raw backend errors. Translate them to product language.

### 31. Destructive Actions Are Distinct

Delete, Remove, Leave, Reset, Withdraw, and Block must not look like ordinary navigation.

### 32. Use Progressive Disclosure

Keep common actions visible. Put rare or advanced controls behind More, Settings, or dedicated screens.

### 33. Accessibility Is UX

Evaluate text scaling, screen-reader labels and order, touch targets, selected/disabled state, contrast, non-color state cues, and labels for unfamiliar icons.
