import PyPDF2

def extract_pages_with_text(input_pdf, output_pdf, target_text):
    pdf_writer = PyPDF2.PdfWriter()
    
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            if target_text in text:
                pdf_writer.add_page(page)
                # Add the next two pages if available
                if page_num + 1 < len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num + 1])
                if page_num + 2 < len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num + 2])
    
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

input_pdf = 'textbook_stats.pdf'
output_pdf = 'chapter_summaries.pdf'
target_text = 'Chapter Summary'

extract_pages_with_text(input_pdf, output_pdf, target_text)
