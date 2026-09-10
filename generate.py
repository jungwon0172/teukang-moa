# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "특강모아"
SITE_DOMAIN = "https://teukgangmoa.vercel.app"  # TODO: 커스텀 도메인 구매 후 교체
ADSENSE_PUB = "ca-pub-2557338953436433"
CONTACT_EMAIL = "yjw2172@naver.com"
NAVER_VERIFY = "c210150a24029e5660d54cb50a0b4fe6cb31aa85"

# 원칙: "내가 직접 가서 들을 수 있는" 오프라인 강연·강좌만 수록.
# 온라인 강의 중심 플랫폼은 제외하고 현장 참석이 기본 형태인 곳만 골랐습니다.

CATEGORIES = {
    "culture": {
        "name": "백화점·마트 문화센터",
        "short": "문화센터",
        "color": "var(--c-culture)",
        "code": "C-01",
        "desc": "전국 지점에서 매 시즌 강좌를 열고, 현장에서 바로 수강하는 가장 대중적인 오프라인 강좌 창구입니다.",
    },
    "public": {
        "name": "도서관·공공 강연",
        "short": "공공강연",
        "color": "var(--c-public)",
        "code": "C-02",
        "desc": "도서관과 지자체가 무료 또는 저비용으로 여는 인문학 강연·평생교육 강좌입니다.",
    },
    "business": {
        "name": "경영자·직무 특강",
        "short": "직무특강",
        "color": "var(--c-business)",
        "code": "C-03",
        "desc": "현장 강의실에 모여 듣는 경영 전략, 리더십, 직무 역량 특강입니다.",
    },
    "salon": {
        "name": "북토크·살롱 모임",
        "short": "북토크",
        "color": "var(--c-salon)",
        "code": "C-04",
        "desc": "책방과 서점, 커뮤니티 공간에서 저자·전문가를 직접 만나는 소규모 모임형 강연입니다.",
    },
    "oneday": {
        "name": "원데이클래스·액티비티",
        "short": "원데이클래스",
        "color": "var(--c-oneday)",
        "code": "C-05",
        "desc": "하루 안에 현장에서 배우고 끝내는 실습형 원데이클래스·체험 모임입니다.",
    },
}

PLATFORMS = [
    # ---------------- 문화센터 ----------------
    {
        "id": "hyundai-culture",
        "name": "현대백화점 문화센터",
        "category": "culture",
        "url": "https://www.ehyundai.com/newCulture/CT/CT010100_L.do",
        "tagline": "전국 현대백화점 점포에서 여는 시즌 강좌",
        "desc": "현대백화점이 전국 점포에서 운영하는 문화센터입니다. 육아, 어학, 취미, 건강 등 생활 밀착 주제의 강좌를 매 시즌 개설하며, 지점 방문 후 강의실에서 직접 수업을 듣는 방식입니다.",
        "audience": "생활 밀착형 강좌를 가까운 지점에서 듣고 싶은 누구나",
        "format": "오프라인 정규 강좌 (시즌제, 지점 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "전국 지점별로 강좌를 검색하고 바로 신청 가능",
            "육아·어학·취미·건강 등 생활 밀착 주제 위주",
            "분기 단위 시즌제 강좌 운영",
        ],
    },
    {
        "id": "lotte-culture",
        "name": "롯데백화점 문화센터",
        "category": "culture",
        "url": "https://culture.lotteshopping.com/",
        "tagline": "전국 롯데백화점 지점의 현장 강좌",
        "desc": "롯데백화점이 전국 지점에서 운영하는 문화센터입니다. 지점별로 강좌 목록이 다르며, 온라인으로 신청한 뒤 정해진 요일에 지점 강의실을 방문해 수강합니다.",
        "audience": "집이나 회사 근처 지점에서 정기적으로 배우고 싶은 성인",
        "format": "오프라인 정규 강좌 (시즌제, 지점 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "인천·분당·부산 등 전국 지점별 강좌 검색",
            "온라인 회원가입 후 강좌별 온라인 신청",
            "시즌마다 새로운 강사·커리큘럼으로 개편",
        ],
    },
    {
        "id": "shinsegae-academy",
        "name": "신세계 아카데미",
        "category": "culture",
        "url": "https://www.shinsegae.com/culture/academy/index.do",
        "tagline": "신세계백화점이 운영하는 문화 아카데미",
        "desc": "신세계백화점 지점에서 운영하는 문화센터형 아카데미입니다. 각 지점 공간에서 강좌를 진행하며, 문화홀에서는 강연·공연도 함께 열립니다.",
        "audience": "백화점 방문과 함께 강좌를 듣고 싶은 성인",
        "format": "오프라인 정규 강좌 (시즌제, 지점 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "지점별 아카데미 강좌 온라인 신청",
            "문화홀 연계 강연·공연 프로그램 운영",
            "생활·취미 중심의 다양한 커리큘럼",
        ],
    },
    {
        "id": "emart-culture",
        "name": "이마트 문화센터",
        "category": "culture",
        "url": "https://culture.emart.com/",
        "tagline": "전국 이마트 매장의 생활 밀착 강좌",
        "desc": "이마트가 전국 매장에서 운영하는 문화센터입니다. 접근성이 높은 매장 특성상 지역 주민 대상의 실용적인 강좌가 많고, 온라인 신청 후 매장 내 강의실에서 수강합니다.",
        "audience": "동네에서 가볍게 다닐 수 있는 강좌를 찾는 성인",
        "format": "오프라인 정규 강좌 (시즌제, 매장 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "전국 매장 단위로 촘촘하게 분포된 강좌망",
            "생활·취미·건강 중심의 실용적 커리큘럼",
            "온라인 회원가입 후 매장별 강좌 신청",
        ],
    },
    {
        "id": "galleria-culture",
        "name": "갤러리아백화점 문화센터",
        "category": "culture",
        "url": "https://culture.galleria.co.kr/",
        "tagline": "타임월드·센터시티 등 지점별 문화센터",
        "desc": "갤러리아백화점이 지점별로 운영하는 문화센터입니다. 지점을 선택해 강좌를 검색하고 신청하는 방식이며, 백화점 회원카드와 연계된 혜택도 함께 안내합니다.",
        "audience": "갤러리아 지점 인근에서 강좌를 찾는 성인",
        "format": "오프라인 정규 강좌 (시즌제, 지점 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "타임월드, 센터시티 등 지점별 강좌 페이지 운영",
            "문화센터 회원카드 연계 백화점 부대시설 혜택",
            "평생교육법에 따른 환불 규정 명시",
        ],
    },
    {
        "id": "akplaza-academy",
        "name": "AK플라자 문화아카데미",
        "category": "culture",
        "url": "http://culture.akplaza.com/main",
        "tagline": "분당·평택 등 AK플라자 지점 아카데미",
        "desc": "AK플라자가 지점별로 운영하는 문화아카데미입니다. 분당점, 평택점 등 지점을 선택해 개설 강좌를 확인하고 신청할 수 있습니다.",
        "audience": "수도권 AK플라자 인근에서 강좌를 찾는 성인",
        "format": "오프라인 정규 강좌 (시즌제, 지점 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "분당점·평택점 등 지점별 강좌 페이지 운영",
            "생활·취미·건강 중심의 시즌제 커리큘럼",
            "온라인 신청 후 지점 방문 수강",
        ],
    },
    {
        "id": "homeplus-culture",
        "name": "홈플러스 문화센터",
        "category": "culture",
        "url": "https://school.homeplus.co.kr/",
        "tagline": "전국 홈플러스 매장의 학기제 강좌",
        "desc": "홈플러스가 전국 매장에서 운영하는 생활 밀착형 배움 공간입니다. 요리·베이킹, 운동·댄스, 어학, 공예 등을 학기 단위로 운영하며, 회원가입 후 매장에서 직접 수강합니다.",
        "audience": "동네 매장에서 부담 없이 취미를 시작하고 싶은 성인",
        "format": "오프라인 정규 강좌 (학기제, 매장 방문)",
        "fee": "유료 (강좌별 상이)",
        "features": [
            "요리·운동·어학·공예 등 생활 밀착 커리큘럼",
            "가족 회원 등록 시 자녀 강좌도 함께 관리",
            "매장 검색 후 학기 단위로 강좌 신청",
        ],
    },
    # ---------------- 도서관·공공 ----------------
    {
        "id": "seoul-library",
        "name": "서울도서관",
        "category": "public",
        "url": "https://lib.seoul.go.kr/",
        "tagline": "서울시청 옆 서울도서관의 시민 강좌",
        "desc": "서울특별시가 운영하는 대표 공공도서관으로, 인문학 강연과 북토크, 시민 강좌를 정기적으로 열고 현장에서 참여할 수 있습니다.",
        "audience": "무료 또는 저비용으로 인문학 강연을 듣고 싶은 시민",
        "format": "오프라인 강좌·강연 (일부 온라인 병행)",
        "fee": "대부분 무료",
        "features": [
            "로그인 후 온라인으로 강좌 신청, 현장 참석",
            "저자 강연, 인문학 강좌 등 정기 프로그램 운영",
            "공석 발생 시 현장 접수도 가능",
        ],
    },
    {
        "id": "nl-library",
        "name": "국립중앙도서관",
        "category": "public",
        "url": "https://www.nl.go.kr/",
        "tagline": "국가 대표 도서관의 강연·세미나 프로그램",
        "desc": "국립중앙도서관 본관에서 강연·세미나, 문화행사를 정기적으로 운영합니다. 도서관 홈페이지의 '강연·세미나' 메뉴를 통해 일정과 신청 방법을 확인할 수 있습니다.",
        "audience": "깊이 있는 인문학·학술 강연을 찾는 성인",
        "format": "오프라인 강연 (본관 현장 참석)",
        "fee": "대부분 무료",
        "features": [
            "학술·인문 분야의 밀도 있는 강연 프로그램",
            "홈페이지 내 '강연·세미나' 메뉴에서 일정 확인",
            "전시·문화행사와 연계해 함께 운영",
        ],
    },
    {
        "id": "sll",
        "name": "서울시평생학습포털 (서울런4050)",
        "category": "public",
        "url": "https://sll.seoul.go.kr/",
        "tagline": "서울시가 운영하는 공공 평생교육 강좌",
        "desc": "서울시민을 위한 생애주기별 평생교육 정보를 제공하는 공공 포털입니다. 지역 50플러스센터 등 오프라인 공간과 연계된 강좌를 함께 운영합니다.",
        "audience": "중장년층, 무료·저비용 공공 강좌를 찾는 시민",
        "format": "오프라인 강좌 (지역 학습관·센터 연계)",
        "fee": "대부분 무료 또는 저비용",
        "features": [
            "중장년 재취업·인생 2막을 위한 강좌 특화",
            "서울시 외 거주자도 회원가입 후 이용 가능",
            "지역 50플러스센터 등 오프라인 공간과 연계",
        ],
    },
    # ---------------- 경영자·직무 특강 ----------------
    {
        "id": "hankyung-academy",
        "name": "한경아카데미",
        "category": "business",
        "url": "https://ac.hankyung.com/",
        "tagline": "한국경제신문이 운영하는 현장 특강",
        "desc": "한경미디어그룹이 전문 강사진과 함께 운영하는 교육 플랫폼입니다. 시의성 있는 이슈를 다루는 1일 특강을 강의실에서 직접 듣는 방식으로 개설합니다.",
        "audience": "직무 역량을 높이려는 실무자, 최신 이슈를 다루는 특강이 필요한 관리자",
        "format": "오프라인 현장 특강",
        "fee": "유료 (과정별 상이)",
        "features": [
            "시의성 있는 이슈를 다루는 1일 특강 수시 개설",
            "언론사 네트워크를 바탕으로 한 전문 강사진",
            "직무별·산업별 세분화된 교육과정",
        ],
    },
    {
        "id": "igm",
        "name": "IGM세계경영연구원",
        "category": "business",
        "url": "https://igm.or.kr/",
        "tagline": "CEO와 임원이 직접 모이는 조찬 강연",
        "desc": "기업 경영진을 대상으로 경영 전략, 리더십 강연과 조찬회를 현장에서 운영하는 교육기관입니다. 국내외 석학과 현직 경영자가 강연자로 참여합니다.",
        "audience": "CEO, 임원, 경영기획 담당자",
        "format": "오프라인 조찬회·세미나 중심",
        "fee": "유료 (회원제·과정별 상이)",
        "features": [
            "국내외 석학, 현직 경영자 강연자 초청",
            "정기 조찬회 형태의 네트워킹형 강연",
            "기업 맞춤형 경영 교육 프로그램 운영",
        ],
    },
    {
        "id": "kpc",
        "name": "한국생산성본부 (KPC)",
        "category": "business",
        "url": "https://www.kpc.or.kr/",
        "tagline": "CEO 경영 아카데미와 최고위 과정",
        "desc": "산업 생산성 향상을 위해 설립된 특별법인으로, CEO 경영 아카데미, AI융합 최고경영자 과정 등 현장 참석형 경영 교육과정을 운영합니다.",
        "audience": "CEO, 경영기획·HRD 담당자",
        "format": "오프라인 정규 과정·특강",
        "fee": "유료 (과정별 상이)",
        "features": [
            "CEO 경영 아카데미, 최고경영자 과정 등 다수 운영",
            "국내 최다 위탁교육 노하우를 바탕으로 한 커리큘럼",
            "전문 교수진과 현장감 있는 실무 중심 강의",
        ],
    },
    {
        "id": "ksa",
        "name": "한국표준협회 (KSA)",
        "category": "business",
        "url": "https://www.ksa.or.kr/",
        "tagline": "기업교육(KSAEDU)이 여는 직무 세미나",
        "desc": "산업표준화법에 근거한 공직유관단체로, 품질경영·표준화 관련 직무 교육과 세미나를 현장에서 운영합니다.",
        "audience": "품질경영·표준화 실무자, 관리자",
        "format": "오프라인 세미나·교육과정",
        "fee": "유료 (과정별 상이)",
        "features": [
            "품질경영·표준화 중심의 전문 교육과정",
            "기업 맞춤형 위탁교육 프로그램 운영",
            "60여 년간 축적된 산업 표준 교육 노하우",
        ],
    },
    # ---------------- 북토크·살롱 ----------------
    {
        "id": "trevari",
        "name": "트레바리",
        "category": "salon",
        "url": "https://trevari.co.kr/",
        "tagline": "매달 한 번, 직접 모여 대화하는 독서 클럽",
        "desc": "월 1권의 책을 읽고 오프라인 아지트에 모여 대화하는 독서모임 커뮤니티입니다. 커리어, 리더십 등 주제별 클럽이 있고, 클럽장이 직접 현장에서 모임을 이끕니다.",
        "audience": "책과 대화를 통해 사람을 만나고 싶은 성인",
        "format": "오프라인 정기 모임 (월 1회, 아지트 방문)",
        "fee": "유료 (클럽·시즌별 회비)",
        "features": [
            "강남·안국 등 오프라인 아지트에서 매달 모임",
            "커리어·리더십 등 주제별 전용 클럽 운영",
            "클럽장이 현장에서 직접 대화를 이끄는 구조",
        ],
    },
    {
        "id": "inabooks",
        "name": "최인아책방",
        "category": "salon",
        "url": "https://inabooks.com/",
        "tagline": "강남의 서점에서 열리는 저자 강연·북토크",
        "desc": "광고인 출신 최인아 대표가 운영하는 독립서점으로, 저자 강연과 북토크, 클래식 렉처 콘서트 등을 책방 공간에서 정기적으로 엽니다.",
        "audience": "책방이라는 공간에서 저자를 직접 만나고 싶은 성인",
        "format": "오프라인 강연·북토크 (책방 현장)",
        "fee": "행사별 상이 (무료 북토크 포함)",
        "features": [
            "저자·전문가를 초청한 정기 북토크",
            "클래식 렉처 콘서트 등 색다른 강연 포맷",
            "3층 유료 회원제 서재 공간과 연계 운영",
        ],
    },
    {
        "id": "kyobo-vora",
        "name": "교보문고 보라(VORA)",
        "category": "salon",
        "url": "https://www.kyobobook.co.kr/",
        "tagline": "광화문 대산홀에서 만나는 저자 강연",
        "desc": "교보문고의 도서 강연 커뮤니티 VORA(보라)가 광화문 교보빌딩 23층 대산홀에서 매달 여는 저자 강연 프로그램입니다. 무료 북토크 '보라토크'와 유료 강연 '명강의 Big10' 등으로 구성됩니다.",
        "audience": "저자를 직접 만나 이야기를 듣고 싶은 독자",
        "format": "오프라인 강연·북토크 (광화문 대산홀 현장)",
        "fee": "프로그램별 상이 (무료 북토크 포함)",
        "features": [
            "매달 다양한 분야 저자를 초청하는 정기 강연",
            "무료 '보라토크', 유료 '명강의 Big10' 등 포맷 다양",
            "교보문고 이벤트 페이지에서 일정·신청 확인",
        ],
    },
    # ---------------- 원데이클래스·액티비티 ----------------
    {
        "id": "taling",
        "name": "탈잉",
        "category": "oneday",
        "url": "https://taling.me/",
        "tagline": "현장에서 배우는 원데이클래스·특강",
        "desc": "일반인 튜터가 직접 개설하는 원데이클래스와 특강을 연결하는 재능 공유 플랫폼입니다. 실무 스킬부터 취미까지 현장에서 만나 배우는 클래스가 많습니다.",
        "audience": "특정 스킬을 짧고 밀도 있게 현장에서 배우고 싶은 성인",
        "format": "오프라인 원데이클래스 (현장 실습 중심)",
        "fee": "유료 (클래스별 상이)",
        "features": [
            "튜터 개인이 직접 개설하는 다양한 커리큘럼",
            "직무 스킬부터 취미까지 폭넓은 카테고리",
            "소규모 정원 중심의 밀착형 현장 클래스",
        ],
    },
    {
        "id": "frip",
        "name": "프립 (Frip)",
        "category": "oneday",
        "url": "https://www.frip.co.kr/",
        "tagline": "액티비티·모임을 현장에서 예약",
        "desc": "액티비티, 원데이클래스, 소셜 모임을 예약할 수 있는 플랫폼입니다. 호스트가 정한 장소와 시간에 직접 모여 진행하는 현장형 모임이 중심입니다.",
        "audience": "새로운 사람과 경험을 통해 배우고 싶은 성인",
        "format": "오프라인 원데이클래스·모임 중심",
        "fee": "유료 (모임별 상이)",
        "features": [
            "호스트가 직접 개설하는 소규모 현장 모임·클래스",
            "지역·관심사 기반 필터링으로 탐색 용이",
            "취미부터 토크형 모임까지 폭넓은 카테고리",
        ],
    },
]

# 등록 순서대로 001, 002 ... 자동 번호 부여
for _i, _p in enumerate(PLATFORMS, start=1):
    _p["num"] = f"{_i:03d}"

def cat_platforms(cat_id):
    return [p for p in PLATFORMS if p["category"] == cat_id]

TOTAL = len(PLATFORMS)

# ---------------------------------------------------------------------------
# shared partials
# ---------------------------------------------------------------------------

def head(title, description, path_depth=0, canonical_path=""):
    prefix = "../" * path_depth
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_DOMAIN}{canonical_path}">
<meta name="naver-site-verification" content="{NAVER_VERIFY}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_DOMAIN}{canonical_path}">
<link rel="stylesheet" href="{prefix}css/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>
</head>
<body>
"""

def header_html(prefix):
    links = "".join(
        f'<a href="{prefix}category/{cid}.html">{c["short"]}</a>' for cid, c in CATEGORIES.items()
    )
    return f"""<header class="site-header">
  <div class="bar wrap">
    <a href="{prefix}index.html" class="brand">{SITE_NAME} <span class="stub">No. 001-{TOTAL:03d}</span></a>
    <button class="nav-toggle" onclick="document.querySelector('.main-nav').classList.toggle('open')">MENU</button>
    <nav class="main-nav">
      {links}
      <a href="{prefix}about.html">사이트 소개</a>
    </nav>
  </div>
</header>
"""

def ad_slot():
    return f"""<div class="ad-slot wrap">
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="{ADSENSE_PUB}"
       data-ad-slot=""
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
"""

def cookie_banner_html(prefix):
    return f"""<div class="cookie-banner" id="cookie-banner">
  <div class="row">
    <p>{SITE_NAME}는 Google AdSense를 통해 광고를 제공하며, 서비스 개선과 맞춤 광고를 위해 쿠키를 사용합니다. 자세한 내용은 <a href="{prefix}privacy.html">개인정보처리방침</a>에서 확인하실 수 있습니다.</p>
    <div class="actions">
      <button class="decline" id="cookie-decline" type="button">거부</button>
      <button class="accept" id="cookie-accept" type="button">동의</button>
    </div>
  </div>
</div>
<script>
(function(){{
  try {{
    var KEY = 'teukgangmoa_cookie_consent';
    var banner = document.getElementById('cookie-banner');
    var stored = localStorage.getItem(KEY);
    if(!stored){{ banner.classList.add('show'); }}
    document.getElementById('cookie-accept').addEventListener('click', function(){{
      localStorage.setItem(KEY, 'accepted');
      banner.classList.remove('show');
    }});
    document.getElementById('cookie-decline').addEventListener('click', function(){{
      localStorage.setItem(KEY, 'declined');
      banner.classList.remove('show');
    }});
  }} catch(e) {{ /* localStorage unavailable — banner simply won't persist */ }}
}})();
</script>
"""

def footer_html(prefix):
    cat_links = "".join(
        f'<a href="{prefix}category/{cid}.html">{c["name"]}</a>' for cid, c in CATEGORIES.items()
    )
    return f"""<footer>
  <div class="wrap">
    <div class="foot-top">
      <div>
        <div class="foot-brand">{SITE_NAME}</div>
        <div class="foot-links" style="margin-top:10px;">{cat_links}</div>
      </div>
      <div class="foot-links">
        <a href="{prefix}about.html">사이트 소개</a>
        <a href="{prefix}contact.html">문의</a>
        <a href="{prefix}privacy.html">개인정보처리방침</a>
        <a href="{prefix}terms.html">이용약관</a>
      </div>
    </div>
    <div class="perforation" style="margin-bottom:18px;"></div>
    <div class="copyright">&copy; 2026 {SITE_NAME}. 본 사이트는 직접 현장에 참석하는 오프라인 강연·강좌 정보를 요약해 안내하는 정보 제공 사이트이며, 신청 및 결제는 각 기관·플랫폼에서 직접 진행됩니다.</div>
  </div>
</footer>
<script>
  document.addEventListener('click', function(e){{
    if(!e.target.closest('.site-header')) document.querySelector('.main-nav')?.classList.remove('open');
  }});
</script>
"""

def page(title, description, body, path_depth=0, canonical_path=""):
    prefix = "../" * path_depth
    return (head(title, description, path_depth, canonical_path)
            + header_html(prefix) + body + footer_html(prefix)
            + ad_slot()
            + cookie_banner_html(prefix) + "</body>\n</html>\n")

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

# ---------------------------------------------------------------------------
# index page
# ---------------------------------------------------------------------------

def stub_card(p, prefix=""):
    c = CATEGORIES[p["category"]]
    return f"""<a href="{prefix}platform/{p['id']}.html" style="display:block;">
      <div class="stub-card">
        <div class="stub-side" style="background:{c['color']}">{c['short']}</div>
        <div class="stub-body">
          <h3>{p['name']}</h3>
          <p>{p['tagline']}</p>
          <div class="meta"><span class="chip">No. {p['num']}</span><span class="chip">{p['format'].split(' ')[0]}</span></div>
          <span class="go">자세히 보기 →</span>
        </div>
      </div>
    </a>"""

def build_index():
    cat_tabs = ""
    for cid, c in CATEGORIES.items():
        cat_tabs += f"""<a href="category/{cid}.html"><span class="tag" style="background:{c['color']}"></span>{c['name']}</a>\n"""

    sections = ""
    for cid, c in CATEGORIES.items():
        cards = ""
        for p in cat_platforms(cid)[:3]:
            cards += stub_card(p, prefix="")
        sections += f"""
    <div class="section-head">
      <div>
        <h2>{c['name']}</h2>
        <p class="section-desc">{c['desc']}</p>
      </div>
      <div class="code">{c['code']}</div>
    </div>
    <div class="card-grid">{cards}</div>
    <div style="margin-top:18px;"><a href="category/{cid}.html" class="stub-card go" style="border:none;">{c['short']} 전체 보기 →</a></div>
"""

    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="eyebrow">On-site Lecture Directory</div>
    <h1>내가 직접 가서<br>듣는 오프라인 강연</h1>
    <p class="lede">화면이 아니라 강의실·서점·조찬 모임에 직접 참석해서 듣는 강연·강좌 창구만 모았습니다. 문화센터부터 도서관 강연, 직무 특강, 북토크, 원데이클래스까지 현장 참석이 기본인 곳들입니다.</p>
    <div class="ticket-display">
      <div class="num">No. {TOTAL:03d}</div>
      <div class="label">현재 {len(CATEGORIES)}개 카테고리, {TOTAL}개 현장 강연처 수록</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cat-tabs">{cat_tabs}</div>
    {sections}
  </div>
</section>
"""
    write("index.html", page(
        f"{SITE_NAME} | 직접 가서 듣는 오프라인 강연·강좌 모음",
        "화면이 아니라 현장에 직접 참석해서 듣는 오프라인 강연·강좌 신청처를 문화센터, 도서관, 직무 특강, 북토크, 원데이클래스로 나눠 정리했습니다.",
        body, path_depth=0, canonical_path="/"
    ))

# ---------------------------------------------------------------------------
# category pages
# ---------------------------------------------------------------------------

def build_categories():
    for cid, c in CATEGORIES.items():
        cards = "".join(stub_card(p, prefix="../") for p in cat_platforms(cid))
        body = f"""
<section class="hero" style="padding:56px 0 40px;">
  <div class="wrap">
    <div class="eyebrow">{c['code']}</div>
    <h1>{c['name']}</h1>
    <p class="lede">{c['desc']}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>수록된 현장 강연처 {len(cat_platforms(cid))}곳</h2>
    </div>
    <div class="card-grid">{cards}</div>
  </div>
</section>
"""
        write(f"category/{cid}.html", page(
            f"{c['name']} 신청처 모음 | {SITE_NAME}",
            c['desc'],
            body, path_depth=1, canonical_path=f"/category/{cid}.html"
        ))

# ---------------------------------------------------------------------------
# platform detail pages
# ---------------------------------------------------------------------------

def build_platforms():
    for p in PLATFORMS:
        c = CATEGORIES[p["category"]]
        features = "".join(f"<li>{f}</li>" for f in p["features"])
        body = f"""
<section class="platform-head">
  <div class="wrap">
    <div class="badge-row">
      <span class="chip" style="border-color:{c['color']};color:{c['color']}">{c['name']}</span>
      <span class="chip">No. {p['num']}</span>
    </div>
    <h1>{p['name']}</h1>
    <p class="sub">{p['tagline']}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="info-grid">
      <div class="cell"><div class="k">진행 방식</div><div class="v">{p['format']}</div></div>
      <div class="cell"><div class="k">주요 대상</div><div class="v">{p['audience']}</div></div>
      <div class="cell"><div class="k">비용</div><div class="v">{p['fee']}</div></div>
    </div>
    <div class="prose">
      <p>{p['desc']}</p>
      <h2>이런 점이 특징이에요</h2>
      <ul>{features}</ul>
    </div>
    <div class="cta-row">
      <a class="btn primary" href="{p['url']}" target="_blank" rel="noopener nofollow">{p['name']} 바로가기</a>
      <a class="btn ghost" href="../category/{p['category']}.html">{c['name']} 더 보기</a>
    </div>
    <div class="disclaimer">본 페이지는 {p['name']}의 공개된 정보를 바탕으로 요약 정리한 안내이며, 실제 강좌 일정·비용·신청 조건은 지점·시즌에 따라 달라질 수 있습니다. 정확한 정보와 신청은 반드시 공식 사이트에서 확인해 주세요.</div>
  </div>
</section>
"""
        write(f"platform/{p['id']}.html", page(
            f"{p['name']} — {p['tagline']} | {SITE_NAME}",
            p['desc'],
            body, path_depth=1, canonical_path=f"/platform/{p['id']}.html"
        ))

# ---------------------------------------------------------------------------
# static pages
# ---------------------------------------------------------------------------

def static_page(slug, title, html_body):
    body = f"""
<section class="page-head">
  <div class="wrap"><h1>{title}</h1></div>
</section>
<section class="static-body wrap">
  {html_body}
</section>
"""
    write(f"{slug}.html", page(f"{title} | {SITE_NAME}", f"{SITE_NAME} {title}", body, path_depth=0, canonical_path=f"/{slug}.html"))

def build_static_pages():
    static_page("about", "사이트 소개", f"""
<p>{SITE_NAME}는 화면이 아니라 강의실, 서점, 도서관, 조찬 모임처럼 실제 장소에 직접 참석해서 듣는 오프라인 강연·강좌를 어디서 신청할 수 있는지 정리해 안내하는 디렉토리 사이트입니다.</p>
<p>강좌를 직접 주최하거나 판매하지 않으며, 각 기관·플랫폼의 공개 정보를 바탕으로 특징을 요약해 소개합니다. 실제 신청과 결제는 각 기관·플랫폼의 공식 채널에서 진행해 주세요.</p>
<h2>수록 기준</h2>
<ul>
  <li>온라인 시청이 아니라 현장 참석이 기본 형태인 강연·강좌</li>
  <li>문화센터, 도서관·공공기관, 직무 특강, 북토크·살롱, 원데이클래스 중 하나 이상에 해당하는 곳</li>
  <li>공식 홈페이지 또는 서비스가 운영 중인 곳</li>
</ul>
<p>온라인 강의가 중심인 플랫폼은 수록 기준에서 제외했습니다. 오프라인 행사를 부정기로만 여는 곳도 우선순위에서 제외하고, 정기적으로 현장 강좌를 여는 곳 위주로 골랐습니다.</p>
<h2>정보 업데이트</h2>
<p>강좌 일정과 정책은 지점·시즌에 따라 자주 바뀔 수 있어, 정기적으로 내용을 점검하고 업데이트하고 있습니다. 잘못된 정보를 발견하셨다면 문의 페이지를 통해 알려주세요.</p>
""")

    static_page("contact", "문의", f"""
<p>{SITE_NAME}에 대한 문의, 정보 수정 요청, 강연처 등록 제안은 아래 이메일로 보내주세요.</p>
<p><strong>이메일</strong>: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
<h2>이런 문의를 환영합니다</h2>
<ul>
  <li>수록된 강연처 정보의 오류 또는 변경 사항 제보</li>
  <li>새로운 오프라인 강연·강좌 창구 등록 제안</li>
  <li>제휴 및 광고 관련 문의</li>
</ul>
""")

    static_page("privacy", "개인정보처리방침", f"""
<p>{SITE_NAME}(이하 '사이트')는 이용자의 개인정보를 중요시하며, 관련 법령을 준수합니다.</p>
<h2>1. 수집하는 개인정보 항목</h2>
<p>본 사이트는 별도의 회원가입 없이 이용 가능하며, 문의 시 입력한 이메일 주소 등 이용자가 자발적으로 제공한 정보만을 수집합니다.</p>
<h2>2. 쿠키 및 광고 서비스 안내</h2>
<p>본 사이트는 Google AdSense를 통해 광고를 게재하며, Google을 비롯한 제3자 공급업체가 쿠키를 사용하여 이용자의 이전 방문 기록을 기반으로 광고를 게재할 수 있습니다.</p>
<ul>
  <li>Google의 광고 쿠키 사용으로 사이트 방문 및 다른 사이트 방문 정보를 기반으로 광고가 게재될 수 있습니다.</li>
  <li>이용자는 <a href="https://adssettings.google.com/" target="_blank" rel="noopener">Google 광고 설정</a>에서 맞춤 광고를 비활성화할 수 있습니다.</li>
  <li>제3자 쿠키 사용에 대한 자세한 내용은 <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">Google 광고 정책</a>을 참고해 주세요.</li>
</ul>
<h2>3. 개인정보의 이용 목적</h2>
<p>수집된 정보는 문의 응대 목적으로만 사용되며, 별도 동의 없이 제3자에게 제공하지 않습니다.</p>
<h2>4. 문의</h2>
<p>개인정보 관련 문의는 <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>로 연락해 주세요.</p>
<p>본 방침은 2026년 8월부터 적용됩니다.</p>
""")

    static_page("terms", "이용약관", f"""
<h2>제1조 (목적)</h2>
<p>본 약관은 {SITE_NAME}(이하 '사이트')가 제공하는 정보 서비스 이용과 관련하여 필요한 사항을 정함을 목적으로 합니다.</p>
<h2>제2조 (서비스의 내용)</h2>
<p>사이트는 오프라인 강연·강좌 신청이 가능한 외부 기관·플랫폼의 정보를 요약해 안내하는 정보 제공 서비스이며, 강좌의 주최, 판매, 예약 대행을 직접 수행하지 않습니다.</p>
<h2>제3조 (정보의 정확성)</h2>
<p>사이트에 게재된 강좌 일정, 비용, 신청 조건 등의 정보는 각 기관·플랫폼의 공개 정보를 바탕으로 작성되며, 실제와 다를 수 있습니다. 정확한 정보는 반드시 해당 기관·플랫폼의 공식 채널에서 확인해야 합니다.</p>
<h2>제4조 (책임의 제한)</h2>
<p>사이트는 외부 기관·플랫폼에서 발생하는 신청, 결제, 서비스 이용과 관련한 분쟁에 대해 책임을 지지 않습니다.</p>
<h2>제5조 (약관의 변경)</h2>
<p>본 약관은 필요 시 사전 고지 없이 변경될 수 있으며, 변경된 약관은 사이트 게시와 동시에 효력을 갖습니다.</p>
<p>본 약관은 2026년 8월부터 적용됩니다.</p>
""")

# ---------------------------------------------------------------------------
# ads.txt / robots.txt / sitemap.xml
# ---------------------------------------------------------------------------

def build_infra_files():
    write("ads.txt", "google.com, pub-2557338953436433, DIRECT, f08c47fec0942fa0\n")

    write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {SITE_DOMAIN}/sitemap.xml
""")

    urls = ["/", "/about.html", "/contact.html", "/privacy.html", "/terms.html"]
    for cid in CATEGORIES:
        urls.append(f"/category/{cid}.html")
    for p in PLATFORMS:
        urls.append(f"/platform/{p['id']}.html")

    items = "".join(f"  <url><loc>{SITE_DOMAIN}{u}</loc></url>\n" for u in urls)
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}</urlset>
""")

if __name__ == "__main__":
    build_index()
    build_categories()
    build_platforms()
    build_static_pages()
    build_infra_files()
    print("DONE —", TOTAL, "platforms across", len(CATEGORIES), "categories")
