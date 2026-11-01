# backend/app/ingestion/pdf_extractor.py

import fitz


def extract_pdf_text(file_path):

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        pages.append(
            {
                "page": page_number + 1,
                "text": page.get_text("text")
            }
        )

    return pages