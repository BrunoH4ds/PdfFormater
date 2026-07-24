from PIL import Image
import os

pasta = r"C:\Users\Bruno\Downloads\livro tombo 1"

arquivos = sorted([f for f in os.listdir(pasta) if f.lower().endswith((".jpg", ".jpeg", ".png"))])

images = []

for arquivo in arquivos:
    img = Image.open(os.path.join(pasta, arquivo)).convert("RGB")
    images.append(img)
images[0].save(
    os.path.join(pasta, "Arquivo_Final.pdf"),
    save_all= True,
    append_images=images[1:]
)

print("PDF CRIADO")