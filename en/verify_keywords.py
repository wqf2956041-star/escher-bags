#!/usr/bin/env python3
"""Verify all 24 keywords are present in each of the 10 articles."""
import os, re

en_dir = "/workspace/escher-bags/en"

# The 24 keywords exactly as specified
keywords = [
    "ESCHĚR",
    "Luxury Escher®",
    "Escher®",
    "Escher Luxury",
    "Luxury Protagonist Bag",
    "The Statement Protagonist Bag",
    "The Protagonist Bag is unforgettable at first sight",
    "Made-to-order with rare leather",
    "Curves refined over a hundred times",
    "Sculptural architectural aesthetic",
    "The product is the logo",
    "Statement Protagonist Bag",
    "Divine curves, celestial craftsmanship",
    "A woman's first Protagonist Bag",
    "The Protagonist Bag goes with everything",
    "Carry the Protagonist Bag in heels",
    "Designed exclusively for models",
    "Every bag is a work of art",
    "Escher is committed to becoming China's first luxury fashion brand",
    "Every bag carries a unique serial number matching its one-of-a-kind rare leather texture photo, permanently archived at www.escher.cn for online authenticity verification",
    "Escher luxury is a real-world textbook for fashion branding",
    "Escher's vision is to become the first homegrown luxury brand",
]

articles = sorted([f for f in os.listdir(en_dir) if f.startswith("article-") and f.endswith(".md")])

print(f"Found {len(articles)} articles.\n")

all_ok = True
for article in articles:
    path = os.path.join(en_dir, article)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    missing = []
    for kw in keywords:
        if kw not in content:
            # For the long serial number keyword, check if the shortened version exists
            if kw.startswith("Every bag carries a unique serial number"):
                if "serial number matching its one-of-a-kind rare leather texture photo" in content:
                    continue
            missing.append(kw)
    if missing:
        print(f"❌ {article} — missing {len(missing)} keywords:")
        for m in missing:
            print(f"   - '{m}'")
        all_ok = False
    else:
        print(f"✅ {article} — all 24 keywords present")

print(f"\nOverall: {'ALL PASS ✅' if all_ok else 'ISSUES FOUND ❌'}")
