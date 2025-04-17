import json
import re
import codecs
from bs4 import BeautifulSoup

def parse_attendance_data(data):

    html_snippet = data

    soup = BeautifulSoup(html_snippet, 'lxml') 

    target_script_content = None
    target_td = soup.find('td', id='zc-viewcontainer_My_Attendance')
    if target_td:
        script_in_td = target_td.find('script')
        if script_in_td and script_in_td.string and 'pageSanitizer.sanitize' in script_in_td.string:
            target_script_content = script_in_td.string

    if not target_script_content:
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'pageSanitizer.sanitize' in script.string:
                 target_script_content = script.string
                 break

    if not target_script_content:
        return json.dumps({"error": "Could not find the <script> tag containing 'pageSanitizer.sanitize'. Cannot proceed."}, indent=2)

    match = re.search(r"pageSanitizer\.sanitize\s*\(\s*'(.*?)'\s*\)", target_script_content, re.DOTALL)

    if not match:
        script_preview = target_script_content[:500] + ('...' if len(target_script_content) > 500 else '')
        return json.dumps({
            "error": "Could not extract the escaped HTML string from the script content using regex.",
            "script_preview": script_preview
        }, indent=2)

    escaped_html = match.group(1)

    try:
        unescaped_html = codecs.decode(escaped_html, 'unicode_escape')
    except Exception as e:
        escaped_preview = escaped_html[:500] + ('...' if len(escaped_html) > 500 else '')
        return json.dumps({
            "error": f"Failed to unescape the HTML string: {e}",
            "escaped_html_preview": escaped_preview
        }, indent=2)

    inner_soup = BeautifulSoup(unescaped_html, 'lxml')

    rows = inner_soup.find_all('tr')

    if not rows:
        unescaped_preview = inner_soup.prettify()[:500] + ('...' if len(inner_soup.prettify()) > 500 else '')
        return json.dumps({
            "error": "No 'tr' (table row) elements found in the unescaped HTML content.",
            "unescaped_html_preview": unescaped_preview
        }, indent=2)

    parsed_data = []

    MIN_EXPECTED_COLUMNS = 7

    for i, row in enumerate(rows):
        
        cells = row.find_all(['td', 'th'], recursive=False)
        num_cells = len(cells)

        
        if num_cells < MIN_EXPECTED_COLUMNS or cells[0].name == 'th':
            continue

        first_cell_text = cells[0].get_text(strip=True)

        if first_cell_text in ["Course Code", "Sl. No."]:
            continue

        try:

            course_code_cell = cells[0]
            course_code = ""
            course_type = "N/A" 

            if course_code_cell.contents:

                 if isinstance(course_code_cell.contents[0], str):
                      potential_code = course_code_cell.contents[0].strip()
                      if '<' not in potential_code and len(potential_code) > 2: 
                           course_code = potential_code

                 course_type_tag = course_code_cell.find('font')
                 if course_type_tag:
                     course_type_text = course_type_tag.get_text(strip=True)
                     if course_type_text: 
                         course_type = course_type_text

                 if not course_code:
                      full_text = course_code_cell.get_text(strip=True)
                      if course_type != "N/A" and full_text.endswith(course_type):
                          course_code = full_text[:-len(course_type)].strip()
                      elif course_type != "N/A" and course_type in full_text:
                           course_code = full_text.replace(course_type, '').strip()
                      else:
                           course_code = full_text 


            if not course_code or course_code.lower() == 'course code':
                 continue 


            course_name = cells[1].get_text(strip=True) if num_cells > 1 else "N/A"
            theory_lab = cells[2].get_text(strip=True) if num_cells > 2 else "N/A"
            faculty = cells[3].get_text(strip=True) if num_cells > 3 else "N/A"
            section = cells[4].get_text(strip=True) if num_cells > 4 else "N/A"
            registered = cells[5].get_text(strip=True) if num_cells > 5 else "N/A"
            absent = cells[6].get_text(strip=True) if num_cells > 6 else "N/A"

            percentage = "N/A"
            if num_cells > 7:
                percentage_cell = cells[7]
                percentage_tag = percentage_cell.find('strong')
                percentage = percentage_tag.get_text(strip=True) if percentage_tag else percentage_cell.get_text(strip=True)


            misc = cells[8].get_text(strip=True) if num_cells > 8 else "N/A"

            data_row = {
                "Course Code": course_code,
                "Type": course_type,
                "Course Name": course_name,
                "Theory/Lab": theory_lab, 
                "Faculty": faculty,
                "Section": section,
                "Registered": registered,
                "Absent": absent,
                "Percentage": percentage,
                "Misc": misc
            }
            parsed_data.append(data_row)

        except IndexError:
            print(f"Warning: Row {i} with {num_cells} cells caused an unexpected IndexError. Skipping.")
        except Exception as e:
            row_preview = str(row)[:150].replace('\n', ' ') + '...'
            print(f"\nWarning: Could not extract data reliably from row {i}. Error: {e}")
            print(f"         Problematic row preview: {row_preview}\n")



    if parsed_data:
        return json.dumps(parsed_data, indent=2)
    else:
        return json.dumps({
            "error": "No data rows were successfully parsed.",
            "message": "Check input file, HTML structure, and potential warnings printed during execution."
            }, indent=2)

if __name__ == "__main__":
    result_json = parse_attendance_data("attendance.txt")
    print(result_json)