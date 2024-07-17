from pypdf import PdfWriter

try:
    merger = PdfWriter()

    for pdf in ["us Navy encrypted hydrofoil research.pdf", "PPS2022.pdf", "HYDROAEROFOIL BOAT DOCUMENTATION.pdf"]:
        merger.append(pdf)
    rn="merged.pdf"
    merger.write("merged-pdf.pdf")
    merger.close()
    print(f"Successfully merged & created PDF ->{rn} ")
except:
    print("SOMETHING IS WRONG")
finally:
    print("\n Program executed")