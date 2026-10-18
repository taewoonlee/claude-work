# 작업 기록 (Progress)

> 완료한 작업을 아래에 추가(append)하세요. 삭제하지 마세요.

---

## 2026-09-14

- [완료] 작업 환경 초기 구축
  - `tasks/todo.md` 생성
  - `tasks/progress.md` 생성
  - `.env` 템플릿 생성
  - `SECURITY.md` 비상 매뉴얼 생성

## 2026-10-10

- [완료] 상단 메뉴 "프로젝트"에 하위 메뉴 추가 (`index.html`)
  - "SORA 프로젝트" → https://aiosec.makenet.co.kr/ (새 탭)

## 2026-10-18

- [완료] MDC-OpenStack-AI-Platform 구성도 페이지 추가
  - 새 파일 `mdc-openstack.html` (메인 다크/틸 톤, 엑셀 "OpenStack+GPUaaS+CMP-Demo구성도" 시트 기반 HTML/CSS 구성도)
  - 공인 IP는 `x.x.x.211` 형태로 마스킹, 내부 IP(10.10.10.0/24)는 그대로
  - `index.html` 프로젝트 하위 메뉴에 "MDC-OpenStack-AI-Platform" 추가, `portfolio.html` 동기화
  - Edge 헤드리스로 데스크톱/모바일 화면 확인
- [수정] Ingress LB 공인 IP를 x.x.x.220으로 변경 (기존 .215=VIP, .218=CPU VM 01과 중복되던 문제 해소)
- [수정] `vercel.json` builds src를 `index.html` → `*.html`로 변경 (mdc-openstack.html·portfolio.html 404 해결)
- [완료] `mdc-openstack.html`에 설명회 섹션 추가 (`참고자료/설명회 매뉴구성.txt` 기반)
  - 백업: `mdc-openstack.html.bak`
  - 히어로 아래 "설명회 순서" 목차(STEP 1~6) 추가, 기존 구성도 = STEP 1
  - STEP 2 CMP(링크) / 3 VM 초기 실행(명령어 + 복사 버튼) / 4 Horizon / 5 Grafana(MDC는 VPN 안내) / 6 ELK
  - 🔒 비밀번호·VPN 계정은 표기 안 함(●●●●●●), 공인 IP는 x.x.x.NNN 마스킹 → 원본 값 0건 grep 확인
  - 상단 메뉴에 "설명회"(#agenda) 추가
  - [수정] 모바일에서 긴 명령어 때문에 페이지가 839px로 넘치던 문제 → `.cmd-steps > li { min-width: 0 }`
  - Edge 헤드리스로 데스크톱(1366) / 모바일(504, 헤드리스 최소 폭) 확인
