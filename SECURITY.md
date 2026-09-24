# 🚨 보안 비상 매뉴얼

> 키 노출이 의심될 때 즉시 이 순서대로 따라하세요.

---

## 1단계 — 노출된 키 파악

어떤 서비스의 키인지 확인:

| 서비스 | 키 접두사 예시 | 관리 콘솔 |
|--------|---------------|-----------|
| OpenRouter | `sk-or-v1-...` | https://openrouter.ai/keys |
| Oracle Cloud | IAM 키 | Oracle Cloud 콘솔 → IAM |
| WordPress | 앱 비밀번호 | 사이트 관리자 → 사용자 |

---

## 2단계 — 즉시 폐기

- **OpenRouter:** 콘솔에서 해당 키 삭제(Revoke)
- **Oracle:** IAM → API Keys → 삭제
- **SSH 키:** `~/.ssh/oracle-server.key` 교체, 서버에서 `authorized_keys` 수정

---

## 3단계 — 새 키 발급

각 서비스 콘솔에서 새 키 생성 후 `.env` 파일에만 저장.

---

## 4단계 — 환경변수 교체

```bash
# .env 파일 수정
# (절대 터미널에 키를 직접 붙여넣지 마세요)
```

---

## 5단계 — 사용 이력 확인

- **OpenRouter:** 콘솔 → Usage 탭에서 비정상 사용 확인
- **Oracle:** 감사 로그(Audit) 확인
- 의심스러운 사용이 있으면 즉시 서비스 제공사에 신고

---

## 예방 수칙

1. `.env` 파일은 절대 `git add` 하지 않기
2. `.gitignore`에 `.env` 항목 유지
3. 터미널에서 키를 직접 출력하지 않기 (`echo $API_KEY` 금지)
4. 화면 공유 시 `.env` 창 닫기

---

*최종 수정: 2026-09-14*
