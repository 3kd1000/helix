#!/usr/bin/env python3
"""Helix 저장 스크립트 - Slash Command에서 직접 실행"""

import sys
import json
import os
import requests

def save_to_helix(summary: str, primary_tag: str, tags: list[str], conversation: str):
    """대화를 Helix에 저장"""

    # 환경변수에서 설정 읽기
    webhook_url = os.getenv('HELIX_WEBHOOK_URL', 'http://localhost:8000/webhook/save')
    token = os.getenv('HELIX_TOKEN')

    if not token and webhook_url != 'http://localhost:8000/webhook/save':
        print("ERROR: HELIX_TOKEN 환경변수가 설정되지 않았습니다.")
        sys.exit(1)

    # Webhook 호출
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.post(
        webhook_url,
        json={
            "summary": summary,
            "primary_tag": primary_tag,
            "tags": tags,
            "conversation": conversation
        },
        headers=headers
    )

    if response.status_code == 200:
        print("✅ Helix에 저장 완료!")
        result = response.json()
        print(f"📄 생성된 문서: {result.get('filename', 'N/A')}")
        related_docs = result.get('related_docs', [])
        print(f"🔗 연관 문서: {len(related_docs)}개")
        for i, doc in enumerate(related_docs[:3], 1):
            print(f"   {i}. {doc.get('title', 'N/A')} (유사도: {doc.get('score', 0):.2f})")
    else:
        print(f"❌ 저장 실패: {response.status_code}")
        print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    # stdin에서 JSON 읽기
    try:
        data = json.loads(sys.stdin.read())
        save_to_helix(
            summary=data['summary'],
            primary_tag=data['primary_tag'],
            tags=data['tags'],
            conversation=data['conversation']
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
