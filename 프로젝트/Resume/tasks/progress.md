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
- [완료] STEP 1 구성도 연결선에 패킷 흐름 애니메이션 추가 (CSS만, HTML 구조 변경 없음)
  - 백업: `mdc-openstack.before-packet.html.bak`
  - 세로선: 빛나는 점이 위→아래 이동(선 색상별), 나란한 선은 0.4초씩 엇갈림
  - 가로 화살표: 점이 좌→우 이동 / 가로 막대(VIP·OVN·VM Network): 빛이 훑고 지나감
  - 움직임 줄이기(prefers-reduced-motion) 설정 시 애니메이션 끔
  - Edge 헤드리스로 시점 2개 캡처해 움직임 확인, 모바일 가로 넘침 없음 확인
- [수정] 패킷 흐름을 무한 반복 → 트래픽 순서대로 1회 재생 (사용자 피드백: 계속 흘러서 눈이 피곤함)
  - 백업: `mdc-openstack.before-sequence.html.bak`
  - Internet → FW → L2 → VIP → Controller/GPU → OVN → VM Network → VM (약 6.4초), SAN A→B→Storage 동시 진행
  - 구성도·서비스 라우팅이 화면에 보일 때 시작(IntersectionObserver), "▶ 패킷 흐름 다시 보기" 버튼 추가
  - 애니메이션을 특정 시점(1.3/2.7/4.7초)에 멈춰 캡처해 순서 확인, 9초 후 정지 확인
