# Popup vs Content Script Breakdown

## Popup

Use the popup for user-triggered actions, status display, and lightweight controls.

## Content Script

Use the content script for page observation, inline overlays, DOM interaction, and page-context UI.

## Rule

Do not treat the popup as if it can directly own page state without a messaging layer or shared state source.
