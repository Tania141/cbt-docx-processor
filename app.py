from flask import Flask, request, send_file, jsonify
from docx import Document
import io
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'online',
        'message': 'CBT DOCX Processor API',
        'endpoints': {
            '/process-docx': 'POST - Process DOCX with replacements'
        }
    })

@app.route('/process-docx', methods=['POST'])
def process_docx():
    try:
        # Get file and replacements from request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        docx_file = request.files['file']
        replacements = request.form.get('replacements')
        
        if not replacements:
            return jsonify({'error': 'No replacements provided'}), 400
        
        # Parse replacements JSON
        import json
        replacements_dict = json.loads(replacements)
        
        # Load DOCX
        doc = Document(docx_file)
        
        # Replace text in paragraphs
        for paragraph in doc.paragraphs:
            for key, value in replacements_dict.items():
                if key in paragraph.text:
                    # Replace in runs to preserve formatting
                    for run in paragraph.runs:
                        if key in run.text:
                            run.text = run.text.replace(key, str(value))
        
        # Replace text in tables
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        for key, value in replacements_dict.items():
                            if key in paragraph.text:
                                for run in paragraph.runs:
                                    if key in run.text:
                                        run.text = run.text.replace(key, str(value))
        
        # Save to BytesIO
        output = io.BytesIO()
        doc.save(output)
        output.seek(0)
        
        # Return processed file
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            as_attachment=True,
            download_name='processed.docx'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
