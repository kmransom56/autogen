# filename: /home/keransom/autogen/python/packages/autogen-magentic-one/examples/uploads/network_config_parserv1.py

import os
import logging
import pandas as pd
import re
import PyPDF2
from docx import Document
from flask import Flask, request, render_template, flash, redirect, url_for, send_file
from werkzeug.utils import secure_filename

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/keransom/autogen/python/packages/autogen-magentic-one/examples/uploads'
app.secret_key = 'your_secret_key'


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def read_pdf_file(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text


def read_word_file(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def parse_network_requirements(content):
    # Example parsing: This needs to be customized as per actual content
    # Extract detailed network information relevant to FortiGate configuration
    return {
        "interfaces": [],
        "policies": [],
        "services": [],
        "addresses": []
    }


def write_to_excel(parsed_details, output_file):
    # Example write: This needs customization
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    pd.DataFrame(parsed_details['interfaces']).to_excel(writer, sheet_name='Interfaces')
    pd.DataFrame(parsed_details['policies']).to_excel(writer, sheet_name='Policies')
    pd.DataFrame(parsed_details['services']).to_excel(writer, sheet_name='Services')
    pd.DataFrame(parsed_details['addresses']).to_excel(writer, sheet_name='Addresses')
    writer.save()


def generate_fortigate_config(parsed_details):
    # Debugging output to verify configuration generation
    logging.debug("Generating FortiGate configuration...")
    try:
        commands = [f"config system interface {detail}" for detail in parsed_details["interfaces"]]
        if not commands:
            logging.warning("No configuration commands generated. Check parsing logic or input data.")
        return commands
    except Exception as e:
        logging.error(f"Error generating configuration: {e}")
        return []


@app.route('/')
def upload_page():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.endswith('.pdf'):
            text_data = read_pdf_file(file_path)
        elif filename.endswith('.docx'):
            text_data = read_word_file(file_path)
        elif filename.endswith('.txt'):
            text_data = read_text_file(file_path)
        else:
            flash("Unsupported file format", "danger")
            return redirect(url_for('upload_page'))

        parsed_details = parse_network_requirements(text_data)
        request.session['parsed_details'] = parsed_details

        return render_template('preview_policy.html', policy=parsed_details)

    flash("File upload failed", "danger")
    return redirect(url_for('upload_page'))


@app.route('/create_policy', methods=['POST'])
def create_policy():
    parsed_details = request.session.get('parsed_details')
    if not parsed_details:
        flash("No policy data available. Please upload a file first.", "danger")
        return redirect(url_for('upload_page'))

    output_excel_file = os.path.join(app.config['UPLOAD_FOLDER'], "network_requirements.xlsx")
    write_to_excel(parsed_details, output_excel_file)

    config_commands = generate_fortigate_config(parsed_details)
    config_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "fortigate_config.txt")
    try:
        with open(config_file_path, "w") as config_file:
            config_file.write("\n".join(config_commands))
        logging.debug("Configuration file written successfully.")
    except Exception as e:
        logging.error(f"Failed to write configuration file: {e}")

    flash("Configuration file and Excel have been generated", "success")
    return redirect(url_for('upload_page'))


@app.route('/download_excel', methods=['GET'])
def download_excel():
    output_excel_file = os.path.join(app.config['UPLOAD_FOLDER'], "network_requirements.xlsx")
    return send_file(output_excel_file, as_attachment=True)


@app.route('/download_config', methods=['GET'])
def download_config():
    config_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "fortigate_config.txt")
    return send_file(config_file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)