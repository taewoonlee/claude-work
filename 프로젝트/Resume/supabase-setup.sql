-- =============================================
-- 방명록 테이블 생성 및 RLS 설정
-- Supabase SQL Editor에서 실행하세요
-- =============================================

-- 1. 테이블 생성
create table if not exists messages (
  id         bigint generated always as identity primary key,
  name       text        not null check (char_length(name) between 1 and 50),
  content    text        not null check (char_length(content) between 1 and 500),
  created_at timestamptz not null default now()
);

-- 2. 최신순 조회 인덱스
create index if not exists messages_created_at_idx on messages (created_at desc);

-- 3. RLS 활성화
alter table messages enable row level security;

-- 4. 누구나 읽기 가능
create policy "누구나 읽기"
  on messages for select
  using (true);

-- 5. 누구나 작성 가능
create policy "누구나 작성"
  on messages for insert
  with check (true);
