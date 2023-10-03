from flask import Flask, request, send_file
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from werkzeug.utils import quote
app = Flask(__name__)

@app.route('/backend/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.json

    # Generate PDF using ReportLab
    pdf_content = generate_pdf_content(data)

    # Create a BytesIO buffer to store the PDF content
    pdf_buffer = BytesIO(pdf_content)

    # Return the PDF as a file attachment
    return send_file(pdf_buffer, as_attachment=True, attachment_filename='generated.pdf')

def generate_pdf_content(data):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    content = []

    # Create content here based on data received from frontend
    content.append(Paragraph(f"Name: {quote(data['name'])}", getSampleStyleSheet()['Normal']))
    content.append(Paragraph(f"Email: {quote(data['email'])}", getSampleStyleSheet()['Normal']))
    # Add more content here

    doc.build(content)
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
