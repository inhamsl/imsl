import os
from datetime import datetime

# 1. 설정: 우리 연구실 주소와 검색할 폴더들
base_url = "https://imsl.inha.ac.kr/"
target_folders = ['', 'notice_view', 'gallery_view'] # 메인, 공지, 갤러리 폴더
sitemap_filename = "sitemap.xml"

# 2. 사이트맵 헤더 작성
xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml_footer = '</urlset>'

def generate_sitemap():
    url_entries = []
    today = datetime.now().strftime('%Y-%m-%d')

    for folder in target_folders:
        # 폴더 경로 설정 (메인은 현재 폴더)
        current_path = folder if folder else "."
        if not os.path.exists(current_path):
            continue

        for filename in os.listdir(current_path):
            if filename.endswith(".html"):
                # URL 경로 생성
                if folder:
                    page_path = f"{folder}/{filename}"
                else:
                    # index.html은 루트(/)로 표시하는 것이 깔끔함
                    page_path = "" if filename == "index.html" else filename
                
                full_url = f"{base_url}{page_path}"
                
                # 우선순위 설정 (메인은 1.0, 나머지는 0.5)
                priority = "1.0" if filename == "index.html" and not folder else "0.5"
                
                entry = f"  <url>\n    <loc>{full_url}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>"
                url_entries.append(entry)

    # 3. 파일 쓰기
    with open(sitemap_filename, "w", encoding="utf-8") as f:
        f.write(xml_header)
        f.write("\n".join(url_entries))
        f.write("\n" + xml_footer)
    
    print(f"성공: {len(url_entries)}개의 페이지를 담은 {sitemap_filename}가 생성되었습니다.")

if __name__ == "__main__":
    generate_sitemap()