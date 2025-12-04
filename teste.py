from flask import Flask, render_template_string, url_for
import os

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Te amo para todo sempre</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600;800&display=swap" rel="stylesheet">
  <style>
    :root{--text-color: #fff}
    html,body{height:100%;margin:0;font-family:'Poppins',system-ui,Segoe UI,Roboto,Arial}
    body{background:#000;display:grid;place-items:center;color:var(--text-color);overflow:hidden}

    /* camada de imagem de fundo (opacidade aplicada só à imagem) */
    .bg {
      position:fixed;inset:0;z-index:0;display:block;pointer-events:none;
      background-image: url('{{ bg_url }}');
      background-position:center;background-size:cover;background-repeat:no-repeat;
      opacity:0.40; /* 40% de opacidade conforme pedido */
      filter:brightness(0.9);
    }

    /* container do conteúdo (sobre a imagem) */
    .card {
      position:relative;z-index:2;max-width:900px;width:92%;padding:32px;border-radius:14px;
      background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0.55));
      box-shadow: 0 8px 30px rgba(0,0,0,0.6);backdrop-filter: blur(4px);
      display:flex;gap:24px;align-items:center;flex-wrap:wrap;justify-content:center
    }

    .message {
      text-align:center;color:var(--text-color);
    }

    .message h1{margin:0;font-weight:800;letter-spacing:1px;font-size:clamp(28px,5vw,64px)}
    .message p{margin-top:12px;font-weight:600;opacity:0.95}

    .photo {
      max-width:360px;width:40%;min-width:210px;border-radius:12px;overflow:hidden;border:4px solid rgba(255,255,255,0.06)
    }

    .photo img{display:block;width:100%;height:auto}

    /* responsivo */
    @media (max-width:720px){
      .card{padding:18px}
      .photo{width:100%;max-width:480px}
    }
  </style>
</head>
<body>
  <div class="bg" aria-hidden="true"></div>

  <main class="card">
    <div class="photo" role="img" aria-label="Foto do casal">
      <img src="{{ img_url }}" alt="Foto junto">
    </div>

    <div class="message">
      <h1>Te amo para todo sempre!</h1>
      <p>Deve ter alguma coisa para você no quarto...</p>
    </div>
  </main>
</body>
</html>
"""

@app.route('/')
def index():
    # espera que a imagem esteja em static/amorzão.jpeg
    filename = 'amorzão.jpeg'
    # se preferir outro nome, altere aqui
    bg_url = url_for('static', filename=filename)
    img_url = url_for('static', filename=filename)
    return render_template_string(TEMPLATE, bg_url=bg_url, img_url=img_url)

if __name__ == '__main__':
    # garante que a pasta static exista
    if not os.path.isdir('static'):
        os.makedirs('static', exist_ok=True)
    print('Coloque a imagem que você enviou dentro da pasta ./static com o nome:', 'amorzão.jpeg')
    app.run(debug=True)

