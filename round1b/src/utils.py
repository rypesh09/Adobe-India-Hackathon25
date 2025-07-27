import os
import json
import fitz  # PyMuPDF

def analyze_document():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pdf_folder = os.path.join(base_path, "input", "pdf")
    persona_file = os.path.join(base_path, "input", "persona.json")
    output_path = os.path.join(base_path, "output", "result.json")
    
    results = {}

    # Load persona
    try:
        with open(persona_file, 'r', encoding='utf-8') as f:
            persona_data = json.load(f)
        results["persona"] = persona_data
    except Exception as e:
        results["persona"] = f"Error reading persona.json: {str(e)}"

    # Read PDFs
    pdf_summaries = {}
    try:
        for pdf_file in os.listdir(pdf_folder):
            if pdf_file.endswith('.pdf'):
                pdf_path = os.path.join(pdf_folder, pdf_file)
                doc = fitz.open(pdf_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                pdf_summaries[pdf_file] = text[:500]  # Preview
        results["pdf_summaries"] = pdf_summaries
    except Exception as e:
        results["pdf_summaries"] = f"Error reading PDFs: {str(e)}"

    final_result = {
        "status": "success",
        "details": results
    }

    # ✅ Write result to output/result.json
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(final_result, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing output: {str(e)}")

    return final_result
