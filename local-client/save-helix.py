#!/usr/bin/env python3
"""Helix 저장 스크립트 - Slash Command에서 직접 실행 (테스트용)"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

def save_to_helix(summary: str, primary_tag: str, tags: list[str], conversation: str, mode: str = "simple"):
    """대화를 Helix에 저장 (테스트: 파일로 저장)"""

    print("=" * 80)
    print("📝 Helix 저장 테스트")
    print("=" * 80)
    print()
    print(f"📌 Summary: {summary}")
    print(f"🏷️  Primary Tag: {primary_tag}")
    print(f"🔖 Tags: {', '.join(tags)}")
    print(f"📁 Mode: {mode}")
    print()

    # temp 디렉토리 생성
    temp_dir = Path.home() / "study" / "helix" / "temp"
    temp_dir.mkdir(parents=True, exist_ok=True)

    # 파일명 생성: helix_simple_2025-12-18_123456.md
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"helix_{mode}_{timestamp}.md"
    filepath = temp_dir / filename

    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(conversation)

    print(f"💾 저장 완료: {filepath}")
    print()
    print("💬 Conversation Preview:")
    print("-" * 80)
    # 처음 500자만 미리보기
    preview = conversation[:500] + "..." if len(conversation) > 500 else conversation
    print(preview)
    print("-" * 80)
    print()
    print(f"✅ 테스트 완료! 파일 저장됨: {filepath}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Helix 대화 저장")
    parser.add_argument("--mode", choices=["simple", "detailed"], default="simple",
                        help="저장 모드: simple 또는 detailed")
    args = parser.parse_args()

    # stdin에서 JSON 읽기
    try:
        data = json.loads(sys.stdin.read())
        save_to_helix(
            summary=data['summary'],
            primary_tag=data['primary_tag'],
            tags=data['tags'],
            conversation=data['conversation'],
            mode=args.mode
        )
    except json.JSONDecodeError:
        print("ERROR: 올바른 JSON 형식이 아닙니다.")
        sys.exit(1)
    except KeyError as e:
        print(f"ERROR: 필수 필드 누락: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
