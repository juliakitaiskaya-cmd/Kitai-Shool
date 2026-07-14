---
name: kitai-school-design
description: Use this skill to generate well-branded interfaces and assets for Kitai School (онлайн-школа китайского языка, Москва), either for production or throwaway prototypes/mocks/decks. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the `README.md` file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc.), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask a few questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick reference
- **Tokens & fonts:** `colors_and_type.css` — CSS variables for palette, type scale, radii, shadows, spacing, plus semantic classes (`.ks-display`, `.ks-h2`, `.ks-body`, `.ks-eyebrow`, …). Import it first.
- **Brand essence:** warm "paper" cream background `#FAF7F2` (never plain white) · deep crimson-red accent `#A41E3A` (hover `#841630`) · warm near-black ink `#2C2420` · elegant high-contrast serif (Cormorant Garamond) with **one italic accent word** in headings · friendly emoji icons inside the platform · proof-by-numbers tone · Russian copy ("вы" in marketing, "ты" in the platform).
- **Logo:** `assets/kitai-logo.svg`.
- **Imagery:** `assets/` holds team portraits, students, camp, exhibition photos (warm, candid, documentary).
- **UI kits:** `ui_kits/website/` (marketing landing) and `ui_kits/platform/` (student learning platform). Reuse their JSX components and CSS patterns — don't reinvent the look.

## Rules of thumb
- Headings: serif + a single italicized accent word (`<span class="italic">`/`.ks-accent`). Body & UI: Inter.
- Buttons = soft rounded rectangle (`--r-btn`, 14px). Chips, badges & tags = full pill radius. Cards = 16–22px radius, soft warm shadow, optional 4px colored left border (brick for lessons, green for feedback).
- One accent red — don't go multicolor. Use cream `#FCF6E2` for callout highlights, green `#27B260` for success.
- Platform icons stay as emoji (intentional). Marketing "icons" are roman numerals (I–IV) and Chinese seal glyphs (启 始 奖 速).
- Avoid: bluish/purple gradients, glassmorphism, cold grey shadows, generic stock glamour photography.
- Fonts are Google Fonts best-match substitutions — confirm with the user if exact brand webfonts are available.
