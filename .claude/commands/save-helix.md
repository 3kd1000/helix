현재 대화를 Helix 지식 그래프에 저장합니다.

## Step 1: 대화 요약 및 태그 생성

현재까지의 대화 내용을 분석하여 다음 형식으로 요약 및 태그를 생성해주세요.

**태그 생성 규칙:**
- primary_tag: "개발", "인프라", "AI", "데이터" 중 정확히 1개 선택
- tags: 구체적인 기술/주제 키워드 3~5개 (소문자, 하이픈 사용)

**예시 (Few-shot):**

1. Docker Compose를 Kubernetes로 마이그레이션하는 대화
   → primary_tag: "인프라"
   → tags: ["docker", "kubernetes", "migration", "k8s"]

2. FastAPI로 RAG 시스템 구축하는 대화
   → primary_tag: "AI"
   → tags: ["rag", "fastapi", "chromadb", "embedding"]

3. React에서 useEffect 최적화하는 대화
   → primary_tag: "개발"
   → tags: ["react", "hooks", "useeffect", "optimization"]

4. PostgreSQL 백업 자동화 스크립트 작성
   → primary_tag: "인프라"
   → tags: ["postgresql", "backup", "automation", "cron"]

5. Qwen 모델 파인튜닝으로 주식 뉴스 분석
   → primary_tag: "AI"
   → tags: ["fine-tuning", "qwen", "nlp", "finance"]

## Step 2: Conversation 포맷팅

전체 대화 내용을 다음 형식으로 정리해주세요:

```
### User
사용자 첫 번째 질문 내용...

### Assistant
어시스턴트 첫 번째 답변 내용...

### User
사용자 두 번째 질문 내용...

### Assistant
어시스턴트 두 번째 답변 내용...
```

**중요:**
- User/Assistant 구분 명확히
- 코드 블록은 원본 그대로 유지
- 줄바꿈은 `\n`으로 표현

## Step 3: JSON 생성

위 내용을 다음 JSON 형식으로 조립해주세요:

```json
{
  "summary": "대화의 핵심 내용을 1-2문장으로 간결하게 요약",
  "primary_tag": "인프라",
  "tags": ["docker", "kubernetes", "migration"],
  "conversation": "### User\n질문 내용...\n\n### Assistant\n답변 내용..."
}
```

## Step 4: save-helix.py 실행

위에서 생성한 JSON을 다음 명령어로 실행해주세요:

```bash
echo '위에서 생성한 JSON' | python /Users/1111622/study/helix/local-client/save-helix.py
```

**실행 예시:**

```bash
echo '{"summary":"Docker Compose를 Kubernetes로 마이그레이션하는 전략 수립","primary_tag":"인프라","tags":["docker","kubernetes","migration","k8s"],"conversation":"### User\nDocker Compose를 K8s로 옮기고 싶어요\n\n### Assistant\n좋습니다. 단계별로 진행해보겠습니다..."}' | python /Users/1111622/study/helix/local-client/save-helix.py
```

**주의사항:**
- JSON 내부 따옴표는 큰따옴표(") 사용
- echo는 작은따옴표(') 사용
- Python 스크립트 경로는 절대 경로
