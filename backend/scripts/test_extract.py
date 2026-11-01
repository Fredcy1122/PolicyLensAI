from app.ingestion.pdf_extractor import extract_pdf_text

pages = extract_pdf_text(
    "../data/raw/legislation/customs_act.pdf"
)

print(f"Pages: {len(pages)}")

print("\nFIRST PAGE PREVIEW\n")
print("-" * 50)

print(pages[0]["text"][:1000])

print("-" * 50)