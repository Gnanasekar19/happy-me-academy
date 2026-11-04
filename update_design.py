from pathlib import Path
import shutil
p=Path('/workspace/sites/happy-me-academy/dist')
shutil.copyfile('/workspace/scratch/0154cbb03413/generated_images/exec-dfd28818-7a53-445b-b299-fbb905dff237.png',p/'assets/hero-art.png')
s=(p/'app.js').read_text()
a=s.index('`<section class="hero"><h1');b=s.index(":page==='classes'?",a)
s=s[:a]+'''`<section class="hero-desktop"><div class="hero-copy"><div class="hero-brand" role="img" aria-label="Happy Me Academy — Happy, Healthy & Successful Kids"></div><div class="gold-divider" aria-hidden="true">✦</div><p class="welcome">Welcome to</p><h1>Happy Me Academy</h1><p class="hero-subtitle">Nurturing young minds for a<br>brighter tomorrow</p><div class="hero-buttons"><a class="button" href="#contact">Book a Trial Class <span aria-hidden="true">→</span></a><a class="button outline" href="#classes">View Classes <span aria-hidden="true">→</span></a></div></div></section>`:page==='about'?about'''+s[b:]
s=s.replace("document.querySelector('#main').innerHTML=", "document.body.dataset.page=page;document.querySelector('#main').innerHTML=")
s=s.replace("<h3>${p[0]}</h3>","<h3><span class=\"program-icon\" aria-hidden=\"true\">${['◇','▣','▦','♧','अ','✎','✒','♞','◇','♧','♫','☼','▣','▤','✂','♡','◇'][programs.indexOf(p)]}</span>${p[0]}</h3>")
(p/'app.js').write_text(s)
