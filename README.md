# MSL 연구실 홈페이지 관리 가이드

인하대학교 재료합성연구실(MSL) 홈페이지 저장소예요.
홈페이지 주소: https://inhamsl.github.io/imsl/

**글·사진·논문·구성원은 코드를 열지 않고 웹 화면(Pages CMS)에서 바꿔요.**
저장하면 1~2분 뒤 홈페이지에 자동으로 반영됩니다.

> ⚠️ 이 저장소는 **공개(Public)** 예요. 비밀번호, 깃허브 복구 코드, 개인 연락처 같은 파일은 절대 올리지 마세요.

문의: 이진석 (enfwowlstjr@naver.com)

---

## 1. 편집하는 곳: Pages CMS

1. https://app.pagescms.org 에 접속해서 로그인해요.
   - 연구실 깃허브 계정을 가진 사람 → **Sign in with GitHub**
   - 이메일로 초대받은 사람 → 초대 메일의 링크로 들어가서 이메일 인증
2. 저장소 `inhamsl/imsl` → 브랜치 `main`을 고르면 왼쪽에 메뉴가 보여요.

| 메뉴 | 하는 일 |
|---|---|
| 게시판 › 공지사항 | 공지 글 쓰기·수정 (사진은 본문에 바로 넣기) |
| 게시판 › 갤러리 | 사진 한 장 + 설명 올리기 |
| 연구 실적 › 논문 / 특허 / 학회 발표 | 목록에 한 줄 추가 |
| 구성원 › 현재 구성원 / 졸업생 | 새 학생 추가, 졸업 처리 |
| 메인 화면 - 대표 논문 | 메인 맨 위 "LATEST PUBLICATION" 상자 바꾸기 |
| 사진 보관함 | 업로드한 사진 모아보기 |

### 자주 하는 일

**공지 올리기** — 공지사항 → `Add an entry` → 제목·날짜·본문 입력(사진은 이미지 버튼) → `Save`.
공지 목록과 메인 화면 NOTICE에 자동으로 올라가요.

**갤러리 올리기** — 갤러리 → `Add an entry` → 제목·날짜·사진·설명 → `Save`.
여러 날 행사면 "날짜"에 마지막 날, "시작 날짜"에 첫날을 넣어요. 메인 화면 GALLERY에는 가장 최근 글이 보여요.

**논문 추가** — 연구 실적 → 논문 → 맨 아래 `Add an item` → 연도·제목·저자·저널·권호페이지(·DOI) → `Save`.
목록 맨 아래에 추가해도 홈페이지에서는 연도별 최신순으로 자동 정렬돼요. DOI를 넣으면 제목이 논문 링크가 돼요.
메인 화면 대표 논문도 바꾸려면 "메인 화면 - 대표 논문"에서 따로 수정해요.

**새 학생** — 구성원 → 현재 구성원 → 맨 아래 `Add an item` → 구분·이름·사진·연구 분야·이메일 → `Save`.

**졸업 처리** — 현재 구성원에서 그 학생 항목을 지우고(휴지통 아이콘), 졸업생 → 맨 아래 `Add an item`으로 추가.
졸업생 표에서는 맨 아래에 추가한 사람이 맨 위에 보여요.

**사진 팁** — 휴대폰 원본(5~10MB)보다 카톡으로 한 번 보낸 사진(1~2MB)이 적당해요. 홈페이지가 빨라져요.
올릴 수 있는 형식은 jpg·png·gif·webp예요. 아이폰 HEIC 사진도 카톡으로 한 번 보내면 jpg가 돼요.
업로드한 사진 파일 이름은 자동으로 겹치지 않는 이름으로 바뀌어요.

### 후배 초대하기 (연구실 깃허브 계정으로 로그인한 사람만)

Pages CMS 왼쪽 메뉴의 **Collaborators** → **Invite** → 후배 이메일 입력 → **Send invite**.
후배는 깃허브 계정이나 연구실 계정 비밀번호 없이 이메일만으로 편집할 수 있어요.

### 반영이 안 될 때

저장 후 2~3분이 지나도 안 바뀌면 github.com/inhamsl/imsl → **Actions** 탭에서
`pages build and deployment`가 빨간색(실패)인지 확인하세요.
실패해도 홈페이지는 직전 상태 그대로 유지돼요. 방금 바꾼 내용을 다시 확인하거나 문의해 주세요.

---

## 2. 처음 한 번만: Pages CMS 연결 (관리자)

1. https://app.pagescms.org → **Sign in with GitHub** (연구실 계정 `inhamsl`)
2. GitHub App 설치 화면에서 **Only select repositories** → `inhamsl/imsl` 선택 → Install
3. 저장소 목록에서 `inhamsl/imsl` 선택 → 메뉴가 보이면 끝

메뉴 구성은 저장소의 `.pages.yml` 파일에 있어요.

---

## 3. 구조 (코드를 고칠 사람용)

이 사이트는 GitHub Pages에 내장된 **Jekyll**로 만들어져요. 저장(push)하면 GitHub가 알아서 HTML을 만들어 올립니다.

```
_config.yml            사이트 설정 (컬렉션, 주소 규칙)
.pages.yml             Pages CMS 메뉴 설정
_layouts/default.html  모든 페이지 공통 틀 (<head>, 헤더, 푸터)
_layouts/notice.html   공지 글 화면
_layouts/gallery.html  갤러리 글 화면
_includes/header.html  상단 메뉴   ← 메뉴는 여기 한 곳만 고치면 전 페이지에 반영
_includes/footer.html  하단 정보   ← 주소·전화번호도 여기 한 곳
_notices/              공지 글 (글 하나 = 파일 하나) → notice_view/파일이름.html
_gallery/              갤러리 글 → gallery_view/파일이름.html
_data/papers.yml       논문 목록        _data/patents.yml        특허 목록
_data/presentations.yml 학회 발표       _data/members.yml        현재 구성원
_data/alumni.yml       졸업생           _data/home.yml           메인 대표 논문
css/                   페이지별 스타일 (공통 스타일은 style.css)
images/                사진 (notice/, gallery/, people/)
*.html (최상위)         각 페이지. professor·research·contact는 내용이 그대로 들어 있어요.
```

- 링크·사진 주소는 `{{ '/images/x.jpg' | relative_url }}`처럼 써야 주소(/imsl)가 바뀌어도 안 깨져요.
- `sitemap.xml`은 자동으로 만들어져요(jekyll-sitemap).
- 예전 주소(`notice_view/notice_view_13.html` 등)는 그대로 유지돼요.

### 학교 도메인(imsl.inha.ac.kr)을 직접 연결하려면

1. 학교 전산 담당에 `imsl.inha.ac.kr` → `inhamsl.github.io` **CNAME** 레코드를 요청
2. 저장소 Settings → Pages → Custom domain에 `imsl.inha.ac.kr` 입력 → Enforce HTTPS 체크

`_config.yml`은 고칠 필요 없어요. 사이트 주소는 GitHub Pages가 자동으로 맞춰요.
