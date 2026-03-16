import os

def batch_replace_urls():
    # 설정값
    target_dir = "."  # 현재 폴더 및 하위 폴더 전체 대상
    old_url = "https://imsl.inha.ac.kr/"
    new_url = "https://inhamsl.github.io/imsl/"

    updated_count = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # HTML 파일만 대상으로 함
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if old_url in content:
                        # 주소 치환
                        new_content = content.replace(old_url, new_url)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"수정 완료: {file_path}")
                        updated_count += 1
                except Exception as e:
                    print(f"에러 발생 ({file_path}): {e}")
    
    print(f"\n총 {updated_count}개의 파일이 성공적으로 수정되었습니다.")

if __name__ == "__main__":
    batch_replace_urls()