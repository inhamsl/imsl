import os
import glob

def update_lab_phone_number():
    # 1. 대상 파일 및 번호 설정
    old_number = "7114"
    new_number = "8769"
    
    # 2. 현재 폴더 내의 모든 html 파일 목록 가져오기
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("수정할 HTML 파일이 폴더에 없습니다.")
        return

    print(f"총 {len(html_files)}개의 파일에서 번호 수정을 시작합니다: {old_number} -> {new_number}")

    for file_path in html_files:
        try:
            # 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 텍스트 교체 (7114 -> 8769)
            if old_number in content:
                new_content = content.replace(old_number, new_number)
                
                # 파일 쓰기
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"[완료] {file_path}")
            else:
                print(f"[건너뜀] {file_path} (번호 없음)")

        except Exception as e:
            print(f"[오류] {file_path}: {e}")

    print("\n모든 작업이 완료되었습니다.")

if __name__ == "__main__":
    update_lab_phone_number()