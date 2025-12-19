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

## Step 2: 문서 구조화

다음 템플릿에 맞춰 문서를 작성해주세요:

```markdown
# {summary}

**작성일**: {오늘 날짜}<br>
**목적**: {이 대화를 왜 저장하는지 1줄}<br>
**Primary Tag**: #{primary_tag}<br>
**Tags**: #{tag1} #{tag2} #{tag3}<br>

## 핵심 내용

{summary를 2-3문단으로 확장한 내용}

## 주요 포인트

**배경:**<br>
- 핵심 배경 1<br>
- 핵심 배경 2<br>

**해결 방법:**<br>
- 방법 1<br>
- 방법 2<br>

**결과:**<br>
- 결과 1<br>
- 결과 2<br>

## 대화 내용

### User
첫 번째 질문...

### Assistant
첫 번째 답변...

### User
두 번째 질문...

### Assistant
두 번째 답변...
```

**🚨 마크다운 포맷팅 규칙 (필수):**

**CRITICAL RULE 1: 코드 블록 전 반드시 2칸 줄바꿈**<br>
- 코드 블록 앞에 빈 줄 2개(`\n\n`) 필수<br>
- 예: `이전 문단\n\n```python\ncode\n```\n\n다음 문단`<br>

**CRITICAL RULE 2: 모든 리스트 항목 끝에 `<br>` 태그**<br>
- 리스트 항목(-, *, 1.) 끝에 반드시 `<br>` 추가<br>
- 예: `- 항목 1<br>\n- 항목 2<br>`<br>

**CRITICAL RULE 3: 리스트 제목 끝에도 `<br>` 태그**<br>
- 굵은 글씨 제목 끝에도 `<br>` 추가<br>
- 예: `**장점:**<br>\n- 항목 1<br>`<br>

**CRITICAL RULE 4: 기술 용어는 반드시 백틱(`)**<br>
- 변수명, 함수명, 파일 경로 등은 백틱으로 감싸기<br>
- 특히 언더스코어(_) 포함된 용어 필수<br>
- 예: `` `primary_tag` ``, `` `list[str]` ``, `` `save_to_helix()` ``<br>

**중요:**<br>
- User/Assistant 구분 명확히<br>
- 코드 블록은 원본 그대로 유지하되 위 규칙 적용<br>
- 줄바꿈은 `\n`으로 표현<br>

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
python /Users/1111622/study/helix/local-client/save-helix.py --mode simple << 'EOF'
{위에서 생성한 JSON}
EOF
```

**실행 예시:**

```bash
python /Users/1111622/study/helix/local-client/save-helix.py --mode simple << 'EOF'
{"summary":"Docker Compose를 Kubernetes로 마이그레이션하는 전략 수립","primary_tag":"인프라","tags":["docker","kubernetes","migration","k8s"],"conversation":"### User\nDocker Compose를 K8s로 옮기고 싶어요\n\n### Assistant\n좋습니다. 단계별로 진행해보겠습니다..."}
EOF
```

**heredoc 방식 설명:**
- `<< 'EOF'`로 시작해서 `EOF`로 끝나는 부분이 JSON 입력
- 작은따옴표, 특수문자 걱정 없이 안전하게 전달
- 여러 줄도 문제없이 처리됨
- 파일은 `~/study/helix/temp/helix_simple_YYYY-MM-DD_HHMMSS.md` 형식으로 저장
