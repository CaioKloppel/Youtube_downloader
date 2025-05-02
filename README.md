# YouTube Downloader - Vídeo e Áudio em Alta Qualidade

Este é um script em Python que permite baixar vídeos e áudios do YouTube com foco na **melhor qualidade disponível**. Utilizando as bibliotecas `pytubefix` e `moviepy`, o programa garante que o vídeo e o áudio sejam baixados separadamente e combinados posteriormente para oferecer o melhor resultado final.

## 📌 Funcionalidades

- Baixa vídeos do YouTube com qualidade máxima (vídeo e áudio separados e recombinados).
- Baixa apenas o áudio, se desejado.
- Permite ao usuário escolher o diretório de destino.
- Interface simples via terminal.

## ⚙️ Requisitos

Antes de rodar o script, você precisa instalar os seguintes pacotes Python:

```bash
pip install pytubefix moviepy
```

## ▶️ Como usar

1. Execute o script:
    ```bash
    python nome_do_script.py
    ```
2. Informe o caminho da pasta onde deseja salvar os arquivos.
3. Escolha o formato do download: `audio` ou `video`.
4. Cole o link do vídeo do YouTube quando solicitado.

## 💡 Detalhes Técnicos

- Para downloads de vídeo:
  - O script seleciona a melhor qualidade de vídeo e áudio disponíveis separadamente.
  - Após o download, os arquivos são combinados usando `moviepy` para gerar um arquivo `.mp4` final de alta qualidade.
- Para downloads de áudio:
  - Apenas a faixa de áudio é baixada diretamente no formato `.mp3`.

## 🧹 Limpeza Automática

Após gerar o arquivo final do vídeo, os arquivos temporários de vídeo e áudio são automaticamente removidos da pasta para manter tudo organizado.

## 📎 Exemplo de uso

```
Endereço da pasta a qual você gostaria que o vídeo ou áudio seja baixado.
Exemplo: C:\Users\Usernick\OneDrive\Youtube_downloads
Endereço: C:\MeusVideos
Download audio ou video: video
Video url: https://www.youtube.com/watch?v=EXEMPLO
Downloading video...
Downloading audio...
[...]
```

## ❗ Observações

- Apenas os formatos `video` e `audio` são aceitos como entrada.
- O nome do vídeo final será baseado no título do vídeo original do YouTube (formatado para evitar caracteres inválidos).
- ⏱️ **O tempo de download pode variar dependendo do tamanho e da qualidade do vídeo selecionado.**
