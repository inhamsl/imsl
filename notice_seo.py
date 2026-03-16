import os

# 1. 대상 폴더와 기준 주소 설정
target_dir = 'notice_view'
base_url = "https://imsl.inha.ac.kr/notice_view/"

def update_notice_seo(folder):
    if not os.path.exists(folder):
        print(f"오류: {folder} 폴더를 찾을 수 없습니다.")
        return

    for filename in os.listdir(folder):
        if filename.endswith('.html'):
            path = os.path.join(folder, filename)
            
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 기존에 있던 캐노니컬 태그가 있다면 삭제 (필터링)
            new_lines = [line for line in lines if 'rel="canonical"' not in line]

            # 파일명에 맞춘 고유 주소 생성
            # 예: notice_view_13.html -> https://imsl.inha.ac.kr/notice_view/notice_view_13.html
            specific_url = f'<link rel="canonical" href="{base_url}{filename}">\n'

            # <head> 태그 다음에 삽입
            final_content = []
            inserted = False
            for line in new_lines:
                final_content.append(line)
                if '<head>' in line and not inserted:
                    final_content.append(f"    {specific_url}")
                    inserted = True
            
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(final_content)
            print(f"[Done] {filename} -> {base_url}{filename}")

if __name__ == "__main__":
    update_notice_seo(target_dir)