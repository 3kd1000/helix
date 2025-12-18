# Project Helix

**AI와의 대화를 지식 그래프로 자산화하는 개인용 파이프라인**

## 🧬 Project Helix란?

Helix = 나선형 (DNA 이중나선)
- 💬 대화 하나하나가 나선의 한 단계
- 📈 반복할수록 위로 올라가는 상승 나선 (Upward Spiral)
- 🧠 과거 경험이 쌓여 미래의 나를 돕는 지식의 자산화

## 📁 프로젝트 구조

```
helix/
├── local-client/           # 로컬 CLI 스크립트
│   ├── save-helix.py       # Webhook 호출 스크립트
│   └── requirements.txt
│
├── .claude/                # Claude Slash Command
│   └── commands/
│       └── save-helix.md   # /save-helix 정의
│
├── oracle-server/          # Oracle Cloud 배포 서비스 (FastAPI)
│   ├── api/
│   ├── schemas/
│   └── search-ui/
│
├── k8s/                    # Kubernetes Manifests
│
├── chrome-extension/       # (향후) 웹 브라우저용
│
└── docs/                   # (submodule) 프로젝트 문서
    └── side-projects/helix/
        ├── architecture-design.md
        └── development-roadmap.md
```

## 🚀 Quick Start (Phase 1 - 로컬 개발)

### 1. 의존성 설치

```bash
cd local-client
pip install -r requirements.txt
```

### 2. Claude Slash Command 테스트

```bash
# Claude Code에서 실행
/save-helix
```

### 3. Docker Compose로 로컬 테스트 (향후)

```bash
docker compose -f docker-compose.dev.yml up
```

## 📚 문서

자세한 내용은 `docs/side-projects/helix/` 참조:
- `architecture-design.md`: 아키텍처 설계
- `development-roadmap.md`: 개발 로드맵 및 의사결정 과정

## 🛠️ 개발 상태

**Phase 1: 로컬 프로토타입 (진행 중)**
- [x] 프로젝트 구조 생성
- [x] save-helix.py 작성
- [x] Slash Command 정의
- [ ] FastAPI 백엔드 구현
- [ ] ChromaDB 연동
- [ ] End-to-End 테스트

**Phase 2: Oracle 배포 (예정)**
**Phase 3: 확장 기능 (예정)**
**Phase 4: 오픈소스 공개 (예정)**

## 🔧 환경변수 설정

```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export HELIX_WEBHOOK_URL="http://localhost:8000/webhook/save"  # 로컬 개발용
export HELIX_TOKEN=""  # 로컬은 필요 없음, 프로덕션 시 설정
```

## 📝 License

개인 프로젝트 (향후 오픈소스 공개 예정)

---

**작성일**: 2025-12-18
**작성자**: 정주상 (jsjung)
