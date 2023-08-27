import re

with open("calmcarthur_emerging_assignment.docx", "r") as file:
    text = file.read()

citations = re.findall(r'\[\d+\]', text)

prev_citation = 0
for citation in citations:
    num = int(citation[1:-1])
    if num < prev_citation:
        print("Error: citation", citation, "is out of order")
    else:
        prev_citation = num
