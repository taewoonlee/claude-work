# 할 일 (Todo)

> 작업 시작 시 이 파일을 확인하세요.
> 완료한 항목은 `[x]`로 표시하고, `progress.md`에 기록하세요.

---

## 오늘 할 일

- [ ] 작업 환경 구축 완료 확인
- [ ] `.env` 파일에 필요한 환경변수 채워넣기
- [ ] CLAUDE.md의 이름/직업 항목 채워넣기

---

## 대기 중

### MDC-OpenStack-AI-Platform 구성도 페이지 (2026-10-18)

참고: `참고자료/OpenStack_개발서버_설계문서.xlsx` → "OpenStack+GPUaaS+CMP-Demo구성도" 시트

- [x] 1. `mdc-openstack.html` 새 파일 생성 (메인 다크/틸 톤앤매너, 같은 상단 메뉴)
  - 상단: 제목 "OpenStack + GPUaaS + CMP 데모 환경 구성도" + 요약 배지
  - 구성도: 엑셀 그림을 HTML/CSS 블록으로 다시 그림 (이미지 복사 X)
    - Internet → Fortigate 60E → L2 Switch → VIP(HA)
    - OpenStack Cluster (Kolla-Ansible/OVN): Controller 01~03 + GPU Compute Node(H200×4)
    - OVN(SDN)/OVS Bridge → VM Network: Bastion, CMP, K8s Master/Worker×2, GPU VM×2, LB/Ingress
    - FC SAN Storage (FC Switch A/B, Cinder 백엔드)
    - 네트워크 대역 / 범례 / 주요 특징 / 서비스 라우팅
  - 모바일 화면에서도 깨지지 않게 (세로 배치)
- [x] 2. `index.html` 프로젝트 하위 메뉴에 "MDC-OpenStack-AI-Platform" 추가 → `mdc-openstack.html`
- [x] 3. `portfolio.html`을 `index.html`과 동기화
- [x] 4. 브라우저로 열어 확인 → `progress.md` 기록

### 설명회 섹션 추가 (2026-10-18)

참고: `참고자료/설명회 매뉴구성.txt` (6개 항목) — 사용자 결정: 새 파일 대신 `mdc-openstack.html` 안에 추가, 공인 IP 마스킹

- [x] 0. `mdc-openstack.html.bak` 백업
- [x] 1. 상단에 "설명회 순서" 목차(STEP 1~6) 섹션 추가 — STEP 1 = 기존 구성도 섹션(#diagram)
- [x] 2. 기존 섹션 뒤에 STEP 2~6 섹션 추가 (같은 톤앤매너)
  - STEP 2 CMP 설명 → https://cmp.i-data.ai/ 링크
  - STEP 3 VM 초기 실행 → 명령어 블록 + 복사 버튼
  - STEP 4 Horizon / STEP 5 Grafana(MDC는 VPN 필요) / STEP 6 ELK
  - 🔒 비밀번호·VPN 계정 미표기, 공인 IP는 `x.x.x.215` 형태
- [x] 3. 상단 메뉴에 "설명회" 링크 추가
- [x] 4. Edge 헤드리스로 데스크톱/모바일 확인 → `progress.md` 기록

### STEP 1 구성도 패킷 흐름 애니메이션 (2026-10-18)

- [x] 0. `mdc-openstack.html.bak` 새로 백업 (현재 버전 기준)
- [x] 1. 세로 연결선(`.vline`): 선은 은은하게, 그 위로 빛나는 점(패킷)이 위→아래로 반복 이동
  - 선 색상 그대로 (공인=파랑, 내부=초록, SAN=빨강), 선마다 출발 시간을 살짝 다르게
- [x] 2. 가로 화살표(`→`, Internet→FW→Switch / 서비스 라우팅): 점이 왼쪽→오른쪽으로 이동 (모바일은 세로 방향)
- [x] 3. 가로 막대(VIP · OVN · VM Network): 빛이 좌→우로 훑고 지나가는 효과
- [x] 4. "움직임 줄이기" 설정한 사용자는 애니메이션 끔 (접근성)
- [x] 5. HTML 구조는 그대로, CSS만 추가 → 데스크톱/모바일 확인 → progress.md 기록

---

## 완료

_없음_
