import os

# 1. 환경 설정
target_dir = 'gallery_view'
# 학교 공식 도메인과 갤러리 폴더 경로
base_url = "https://imsl.inha.ac.kr/gallery_view/"

def apply_gallery_seo():
    # 폴더 존재 여부 확인
    if not os.path.exists(target_dir):
        print(f"오류: {target_dir} 폴더를 찾을 수 없습니다.")
        return

    count = 0
    for filename in os.listdir(target_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(target_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 원리: 이미 캐노니컬 태그가 있으면 중복 삽입 방지를 위해 건너뜀
            if any('rel="canonical"' in line for line in lines):
                continue

            new_lines = []
            inserted = False
            # 각 파일명(filename)을 활용해 고유한 주소 생성
            # 예: photo1.html -> https://imsl.inha.ac.kr/gallery_view/photo1.html
            specific_url = f'<link rel="canonical" href="{base_url}{filename}">\n'

            for line in lines:
                new_lines.append(line)
                # <head> 태그를 찾아 바로 아랫줄에 삽입
                if '<head>' in line and not inserted:
                    new_lines.append(f"    {specific_url}")
                    inserted = True
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            
            print(f"[신규 적용] {filename}")
            count += 1

    if count == 0:
        print("새로 적용할 파일이 없습니다.")
    else:
        print(f"총 {count}개의 신규 파일에 SEO 태그를 삽입했습니다.")

if __name__ == "__main__":
    apply_gallery_seo()