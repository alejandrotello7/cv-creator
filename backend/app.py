from urllib.parse import unquote

from flask import Flask, request, send_file
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from werkzeug.utils import quote
import html
app = Flask(__name__)

@app.route('/generate_pdf', methods=['POST'])
@app.route('/backend/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json(force=True)
    app.logger.info("Received data: %s", data)

    # Decode HTML entities
    data = {key: unquote(value) for key, value in data.items()}

    # Generate PDF using ReportLab
    pdf_content = generate_pdf_content(data)

    # Create a BytesIO buffer to store the PDF content
    pdf_buffer = BytesIO(pdf_content)

    # Return the PDF as a file attachment
    return send_file(pdf_buffer, as_attachment=True, mimetype='application/pdf', download_name='generated.pdf')


def generate_pdf_content(data):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    content = []

    # Personal Information
    personal_info_table = [['Personal Information'],
                           [f"Name: {quote(data['name'])}"],
                           [f"Last Name: {quote(data['last_name'])}"],
                           [f"Email: {quote(data['email'])}"],
                           # Add more personal information as needed
                           ]

    # Working Experience
    experience_table = [['Work Experience'],
                        [f"Company: {quote(data['company'])}"],
                        [f"Position: {quote(data['position'])}"],
                        [f"Duration: {quote(data['duration'])}"],
                        # Add more work experience details
                        ]

    # Combine personal information and working experience into a two-column table
    data_table = [[Table(personal_info_table), Table(experience_table)]]

    # Define styles for the table
    table_style = TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black),
                              ('LEFTPADDING', (0, 0), (-1, -1), 10),
                              ('RIGHTPADDING', (0, 0), (-1, -1), 10)])
    table_style.add('TEXTCOLOR', (0, 0), (-1, -1), 'black')
    table_style.add('FONTNAME', (0, 0), (-1, -1), 'Helvetica')
    content.append(Table(data_table, style=table_style))

    doc.build(content)
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
