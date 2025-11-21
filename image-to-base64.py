"""
🎨 CONVERSOR DE IMAGEM PARA BASE64
BS Developer - Ferramenta Auxiliar

Este script converte qualquer imagem (PNG, JPG, GIF, WebP) 
para formato Base64 inline, permitindo embedar a imagem 
diretamente no HTML sem depender de arquivos externos.

USO:
    python image-to-base64.py caminho/da/imagem.png

EXEMPLO:
    python image-to-base64.py logo.png

OUTPUT:
    - base64-output.txt (código base64 puro)
    - base64-html-ready.txt (pronto para colar no HTML)
"""

import base64
import sys
import os
from pathlib import Path

def get_mime_type(file_path):
    """Detecta o tipo MIME baseado na extensão do arquivo"""
    extension = Path(file_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon'
    }
    return mime_types.get(extension, 'image/png')

def convert_image_to_base64(image_path):
    """Converte uma imagem para Base64"""
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(image_path):
            print(f"❌ ERRO: Arquivo não encontrado: {image_path}")
            return None
        
        # Lê o arquivo em modo binário
        with open(image_path, 'rb') as image_file:
            # Converte para base64
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Detecta tipo MIME
        mime_type = get_mime_type(image_path)
        
        # Tamanho do arquivo
        file_size = os.path.getsize(image_path)
        file_size_kb = file_size / 1024
        
        # Data URI completo
        data_uri = f"data:{mime_type};base64,{encoded_string}"
        
        print("✅ CONVERSÃO BEM-SUCEDIDA!")
        print(f"📁 Arquivo: {os.path.basename(image_path)}")
        print(f"📊 Tamanho: {file_size_kb:.2f} KB")
        print(f"🎨 Tipo: {mime_type}")
        print(f"📏 Base64 length: {len(encoded_string)} caracteres")
        
        # Salva o base64 puro
        with open('base64-output.txt', 'w', encoding='utf-8') as f:
            f.write(encoded_string)
        print(f"\n💾 Base64 puro salvo em: base64-output.txt")
        
        # Salva o data URI completo
        with open('base64-html-ready.txt', 'w', encoding='utf-8') as f:
            f.write(data_uri)
        print(f"💾 Data URI completo salvo em: base64-html-ready.txt")
        
        # Salva exemplo de uso em HTML
        html_example = f'''<!-- EXEMPLO DE USO NO HTML -->

<!-- Opção 1: Tag <img> -->
<img src="{data_uri}" alt="Logo BS Developer" class="w-32 h-auto">

<!-- Opção 2: Background CSS -->
<div style="background-image: url('{data_uri}'); width: 150px; height: 150px;"></div>

<!-- Opção 3: JavaScript -->
<script>
const logoImg = document.getElementById('logoImg');
logoImg.src = "{data_uri}";
</script>

<!-- DICA: Cole o data URI completo no lugar da URL da imagem -->
'''
        
        with open('base64-html-example.html', 'w', encoding='utf-8') as f:
            f.write(html_example)
        print(f"💾 Exemplo HTML salvo em: base64-html-example.html")
        
        # Aviso sobre tamanho
        if file_size_kb > 100:
            print(f"\n⚠️  AVISO: Imagem grande ({file_size_kb:.2f} KB)")
            print("   Considere otimizar a imagem antes de embedar")
            print("   Recomendado: < 50 KB para performance ideal")
        
        return data_uri
        
    except Exception as e:
        print(f"❌ ERRO na conversão: {str(e)}")
        return None

def main():
    print("=" * 60)
    print("🎨 CONVERSOR DE IMAGEM PARA BASE64")
    print("   BS Developer - Ferramenta Auxiliar")
    print("=" * 60)
    print()
    
    # Verifica argumentos
    if len(sys.argv) < 2:
        print("❌ USO INCORRETO!")
        print()
        print("📝 Como usar:")
        print("   python image-to-base64.py caminho/da/imagem.png")
        print()
        print("📝 Exemplos:")
        print("   python image-to-base64.py logo.png")
        print("   python image-to-base64.py assets/logo-bs-dev.png")
        print("   python image-to-base64.py C:\\Users\\Bruno\\Desktop\\logo.jpg")
        print()
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Converte
    print(f"🔄 Convertendo: {image_path}")
    print()
    
    data_uri = convert_image_to_base64(image_path)
    
    if data_uri:
        print()
        print("=" * 60)
        print("✨ CONVERSÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print()
        print("📋 PRÓXIMOS PASSOS:")
        print("1. Abra 'base64-html-ready.txt'")
        print("2. Copie o conteúdo completo")
        print("3. Cole no HTML no lugar da URL da imagem")
        print()
        print("💡 DICA: Use 'base64-html-example.html' como referência")
        print()
    else:
        print()
        print("=" * 60)
        print("❌ CONVERSÃO FALHOU!")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
