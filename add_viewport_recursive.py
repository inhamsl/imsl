import os

def insert_viewport_tag_recursively(target_directory='.'):
    """
    지정한 디렉토리 및 모든 하위 폴더의 HTML 파일을 찾아
    viewport 메타 태그가 없는 경우 <head> 섹션에 삽입합니다.
    """
    # 삽입할 뷰포트 태그 (표준 반응형 설정)
    viewport_tag = '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    
    updated_count = 0
    skipped_count = 0

    # os.walk는 (현재 경로, 하위 폴더 목록, 파일 목록)을 반환하며 하위 폴더를 모두 탐색합니다.
    for root, dirs, files in os.walk(target_directory):
        for filename in files:
            # HTML 파일 확장자 확인 (대소문자 구분 없이)
            if filename.lower().endswith(('.html', '.htm')):
                file_path = os.path.join(root, filename)
                
                try:
                    # 파일 내용 읽기
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # 이미 viewport 태그가 있는지 확인 (대소문자 무시 검색)
                    full_text = "".join(lines).lower()
                    if 'name="viewport"' not in full_text:
                        new_content = []
                        inserted = False
                        
                        for line in lines:
                            new_content.append(line)
                            # <head> 태그를 찾으면 바로 다음 줄에 삽입
                            if not inserted and '<head>' in line.lower():
                                new_content.append(viewport_tag)
                                inserted = True
                        
                        if inserted:
                            # 변경된 내용을 다시 쓰기
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.writelines(new_content)
                            print(f"[성공] {file_path}")
                            updated_count += 1
                        else:
                            print(f"[경고] {file_path}: <head> 태그를 찾을 수 없어 건너뜁니다.")
                            skipped_count += 1
                    else:
                        # 이미 존재하면 건너뜀
                        skipped_count += 1
                        
                except Exception as e:
                    print(f"[오류] {file_path} 처리 중 문제 발생: {e}")

    print("\n" + "="*40)
    print(f"작업 완료: {updated_count}개 파일 수정됨, {skipped_count}개 파일 건너뜀")

if __name__ == "__main__":
    insert_viewport_tag_recursively()