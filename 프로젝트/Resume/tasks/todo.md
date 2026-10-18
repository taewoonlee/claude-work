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

---

## 완료

_없음_
