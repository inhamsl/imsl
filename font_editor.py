import os
import re

def force_update_h2_style(target_dir='.'):
    # 1. 패턴: <h2 style="...#003a71;..."> 형태를 찾음
    # 속성 내부의 띄어쓰기가 달라도 찾을 수 있도록 \s* 활용
    h2_regex = re.compile(r'(<h2\s+style=")([^"]*#003a71;?[^"]*)(")', re.IGNORECASE)
    
    updated_files = 0
    
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            if filename.lower().endswith(('.html', '.htm')):
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    def replacement_func(match):
                        prefix = match.group(1)   # <h2 style="
                        style_content = match.group(2).strip() # 기존 스타일 내용
                        suffix = match.group(3)   # "
                        
                        # 이미 font-weight가 설정되어 있다면 수정하지 않음
                        if 'font-weight' in style_content.lower():
                            return match.group(0)
                        
                        # 마지막에 세미콜론이 없으면 붙여줌
                        if not style_content.endswith(';'):
                            style_content += ';'
                            
                        # font-weight: 900; 주입
                        return f'{prefix}{style_content} font-weight: 900;{suffix}'

                    new_content = h2_regex.sub(replacement_func, content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"[수정 완료] {file_path}")
                        updated_files += 1
                        
                except Exception as e:
                    print(f"[오류] {file_path}: {e}")

    print(f"\n총 {updated_files}개의 파일이 객관적으로 수정되었습니다.")

if __name__ == "__main__":
    force_update_h2_style()