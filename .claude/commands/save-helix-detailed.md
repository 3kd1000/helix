현재 대화를 Helix 지식 그래프에 저장합니다. (상세 버전)

**📚 이 명령어는 @docs/guides/documentation-guide.md의 모든 규칙을 적용하여 고품질 문서를 생성합니다.**

## Step 1: 대화 요약 및 태그 생성

현재까지의 대화 내용을 분석하여 다음 형식으로 요약 및 태그를 생성해주세요.

**태그 생성 규칙:**<br>
- primary_tag: "개발", "인프라", "AI", "데이터" 중 정확히 1개 선택<br>
- tags: 구체적인 기술/주제 키워드 3~5개 (소문자, 하이픈 사용)<br>

**예시 (Few-shot):**<br>

1. Docker Compose를 Kubernetes로 마이그레이션하는 대화<br>
   → primary_tag: "인프라"<br>
   → tags: ["docker", "kubernetes", "migration", "k8s"]<br>

2. FastAPI로 RAG 시스템 구축하는 대화<br>
   → primary_tag: "AI"<br>
   → tags: ["rag", "fastapi", "chromadb", "embedding"]<br>

3. React에서 useEffect 최적화하는 대화<br>
   → primary_tag: "개발"<br>
   → tags: ["react", "hooks", "useeffect", "optimization"]<br>

## Step 2: 문서 구조화 (@docs/guides/documentation-guide.md 참조)

**@docs/guides/documentation-guide.md 파일을 참조하여 다음 사항을 준수해주세요:**<br>

### 📋 문서 필수 구조

```markdown
# {summary}

**작성일**: {오늘 날짜}<br>
**목적**: {이 대화를 왜 저장하는지}<br>
**Primary Tag**: #{primary_tag}<br>
**Tags**: #{tag1} #{tag2} #{tag3}<br>

## 문제 상황 / 배경

{무엇이 문제였는지, 왜 이 대화를 했는지}

## 해결 방법 / 구현 내용

**핵심 접근:**<br>
- 접근법 1<br>
- 접근법 2<br>

**구현 단계:**<br>
1. 단계 1<br>
2. 단계 2<br>
3. 단계 3<br>

## 실행 예제

```bash
# 실제로 실행 가능한 코드
command --option value
```

## 주요 포인트

**배울 점:**<br>
- 핵심 1<br>
- 핵심 2<br>

**주의사항:**<br>
- 주의 1<br>
- 주의 2<br>

## 대화 내용

### User
질문...

### Assistant
답변...
```

### 🚨 마크다운 포맷팅 규칙 (필수)

**@docs/guides/documentation-guide.md의 모든 CRITICAL RULE을 반드시 준수하세요:**<br>

**CRITICAL RULE 1: 코드 블록 전 반드시 2칸 줄바꿈**<br>
- 코드 블록 앞뒤에 빈 줄 2개(`\n\n`) 필수<br>
- MacDown, Obsidian, GitHub에서 제대로 렌더링되도록<br>

**CRITICAL RULE 2: 모든 리스트 항목 끝에 `<br>` 태그**<br>
- 리스트 항목(-, *, 1.) 끝에 반드시 `<br>` 추가<br>
- 가독성 확보 및 줄바꿈 정상 표시<br>

**CRITICAL RULE 3: 리스트 제목 끝에도 `<br>` 태그**<br>
- 굵은 글씨 제목 끝에도 `<br>` 추가<br>
- 패턴: `**제목:**<br>`<br>

**CRITICAL RULE 4: 기술 용어는 반드시 백틱(`)**<br>
- 변수명, 함수명, 파일 경로는 백틱으로 감싸기<br>
- 특히 언더스코어(_) 포함 용어는 필수<br>
- 예: `` `primary_tag` ``, `` `list[str]` ``, `` `save_to_helix()` ``<br>

**추가 규칙:**<br>
- 표 전후에 빈 줄<br>
- 제목과 본문 사이에 빈 줄<br>
- 인라인 코드 사용 (`` `kubectl` `` 명령어)<br>

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

**중요:**<br>
- `conversation` 필드에는 위 Step 2에서 작성한 **전체 구조화된 문서**를 포함<br>
- 모든 마크다운 포맷팅 규칙이 적용된 상태로 전달<br>
- 줄바꿈은 `\n`으로 표현<br>

## Step 4: save-helix.py 실행

위에서 생성한 JSON을 다음 명령어로 실행해주세요:

```bash
python /Users/1111622/study/helix/local-client/save-helix.py --mode detailed << 'EOF'
{위에서 생성한 JSON}
EOF
```

**실행 예시:**<br>

```bash
python /Users/1111622/study/helix/local-client/save-helix.py --mode detailed << 'EOF'
{"summary":"Docker Compose를 Kubernetes로 마이그레이션하는 전략 수립","primary_tag":"인프라","tags":["docker","kubernetes","migration","k8s"],"conversation":"# Docker Compose를 Kubernetes로 마이그레이션\n\n**작성일**: 2025-12-18<br>\n**목적**: 단일 호스트 제한 극복<br>..."}
EOF
```

**heredoc 방식 설명:**<br>
- `<< 'EOF'`로 시작해서 `EOF`로 끝나는 부분이 JSON 입력<br>
- 작은따옴표, 특수문자 걱정 없이 안전하게 전달<br>
- 여러 줄, 코드 블록도 문제없이 처리됨<br>
- `conversation` 필드에 모든 구조화된 내용 포함 가능<br>
- 파일은 `~/study/helix/temp/helix_detailed_YYYY-MM-DD_HHMMSS.md` 형식으로 저장<br>
