# claude-work

Claude Code 작업 공간입니다.

## 폴더 구조

```
claude-work/
├── CLAUDE.md              # Claude Code 행동 지침
├── SECURITY.md            # 🚨 보안 비상 매뉴얼
├── .gitignore             # git 제외 목록 (.env, test/ 등)
├── README.md              # 이 파일
├── portfolio.html         # 포트폴리오 페이지
├── weather_fetch.py       # 날씨 데이터 수집 스크립트
├── weather.txt            # 날씨 데이터 출력 결과
└── tasks/
    ├── todo.md            # 할 일 체크리스트
    └── progress.md        # 작업 기록 (append-only)
```

> `.env` 및 `test/` 폴더는 보안상 git에서 제외됩니다.

## 시작하기

1. `.env` 파일에 필요한 API 키·환경변수를 입력하세요.
2. `tasks/todo.md`에서 오늘 할 일을 확인하세요.
3. 작업이 끝나면 `tasks/progress.md`에 기록하세요.

## 보안 주의사항

- `.env` 파일은 절대 git에 올리지 마세요.
- 키 노출이 의심되면 `SECURITY.md`를 즉시 확인하세요.
