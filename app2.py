from PIL import Image
import os

pasta = r"C:\Users\Bruno\Downloads\livro tombo 1"
pasta_pdf = r"C:\Users\Bruno\Downloads\livro tombo 1 PDF"

arquivos = sorted(
    [f for f in os.listdir(pasta) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
)

for arquivo in arquivos:
    caminho_imagem = os.path.join(pasta, arquivo)

    img = Image.open(caminho_imagem).convert("RGB")

    nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
    caminho_pdf = os.path.join(pasta_pdf, nome_pdf)

    img.save(caminho_pdf, "PDF")

    print(f"PDF criado: {nome_pdf}")

print("Todos os PDFs foram criados!")