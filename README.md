# PDF Parsing and Management (P2M)

P2M is a Python and AWS CDK project designed to upload PDF files, intelligently parse their content, preview the extracted data, and export it as JSON. The architecture is defined using the AWS Cloud Development Kit (CDK) in Python, while Lambda handlers manage the runtime logic.

## Features

- **PDF Upload:** Upload PDF documents from a local device or via URL.
- **Intelligent Parsing:** Detects and parses tables or structured data using large language models to decide on the best strategy for each document.
- **Data Preview:** Presents extracted data in tabular form before exporting.
- **JSON Export:** Allows export of parsed content as JSON for other applications.
- **Table Detection:** Utilizes generative AI to locate tables within documents for efficient extraction.

## UI/UX Guidelines

- **Layout:** Clear sections for upload, preview, and export.
- **Typography:** Uses the sans-serif **Inter** font for headings and body text.
- **Iconography:** Minimalist line-style icons in a soft blue accent.
- **Animation:** Subtle transitions for loading states and data transformation.

## Repository Structure

```
cdk/                 # Infrastructure as code using AWS CDK
  app.py            # CDK application entry point
  requirements.txt  # CDK Python dependencies
  src/
    stacks/
      pdf_processor_stack.py  # Defines AWS resources
handlers/            # AWS Lambda handler code
  __init__.py
  pdf_upload_handler.py
  parse_pdf_handler.py
  preview_handler.py
  export_handler.py
requirements.txt     # Runtime dependencies for Lambda functions
```

## Getting Started

1. **Install Dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install -r cdk/requirements.txt
   ```

2. **Bootstrap CDK** (once per AWS environment)

   ```bash
   cd cdk
   cdk bootstrap
   ```

3. **Deploy**

   ```bash
   cdk deploy
   ```

4. **Testing Locally**

   Use your preferred testing framework (e.g., `pytest`) to test individual handlers.

## Contributing

Feel free to open issues or pull requests to improve P2M. This project is provided as a starting point for a PDF parsing pipeline on AWS.

