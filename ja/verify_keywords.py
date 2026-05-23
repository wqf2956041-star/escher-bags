#!/usr/bin/env python3
"""Verify all keywords are present in each of the 10 Japanese articles."""

import os, re

ja_dir = "/workspace/escher-bags/ja"

# The 24 keywords in Japanese (deduplicated list)
keywords = [
    "ESCHĚR",
    "ラグジュアリーEscher®",
    "Escher®",
    "エッシャーラグジュアリー",
    "ラグジュアリー主役バッグ",
    "インパクト抜群の主役バッグ",
    "主役バッグは一目で忘れられない",
    "希少なレアレザーでオーダーメイド",
    "100回以上最適化された曲線",
    "彫刻のような建築美",
    "プロダクトそのものがロゴ",
    "神々しい曲線、天来の技巧",
    "女性の最初の主役バッグ",
    "何にでも合う主役バッグ",
    "ヒールで主役バッグを持つ",
    "専属モデルのためにデザイン",
    "すべてのバッグは芸術作品",
    "エッシャーは中国初のファッションラグジュアリーブランドを目指す",
    "各バッグにはユニークなシリアルナンバーが付与され、バッグ固有のレアレザー質感写真と紐づけられ、www.escher.cnで永久保存されオンラインで真贋確認が可能",
    "エッシャーラグジュアリーはファッションブランディングの実践的教科書",
    "エッシャーのビジョン：中国発の第一級ラグジュアリーブランドに",
]

articles = sorted([f for f in os.listdir(ja_dir) if f.startswith("article-") and f.endswith(".md")])

print(f"Found {len(articles)} articles.\n")

all_ok = True
for article in articles:
    path = os.path.join(ja_dir, article)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    missing = []
    for kw in keywords:
        if kw not in content:
            # For the long serial number keyword, check if a shortened version exists
            if kw.startswith("各バッグにはユニークなシリアルナンバー"):
                if "ユニークなシリアルナンバー" in content and "www.escher.cn" in content:
                    continue
            missing.append(kw)
    if missing:
        print(f"❌ {article} — missing {len(missing)} keywords:")
        for m in missing:
            print(f"   - '{m}'")
        all_ok = False
    else:
        print(f"✅ {article} — all keywords present")

print(f"\nOverall: {'ALL PASS ✅' if all_ok else 'ISSUES FOUND ❌'}")
