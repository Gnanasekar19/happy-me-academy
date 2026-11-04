from pathlib import Path
import shutil
p=Path('/workspace/sites/happy-me-academy/dist')
shutil.copyfile('/workspace/scratch/0154cbb03413/generated_images/exec-557ce581-1282-4c60-a24b-95bed5d4c321.png',p/'assets/hero-logo-transparent.png')
s=(p/'app.js').read_text()
s=s.replace('<section class="about">','<section id="about" class="about" aria-labelledby="about-title">').replace('<h1>About the Academy</h1>','<h2 id="about-title">About the Academy</h2>')
s=s.replace('<section class="wrap offerings">','<section id="classes" class="wrap offerings" aria-labelledby="classes-title">').replace('<h${all?\'1\':\'2\'} class="rule">Classes & Programs</h${all?\'1\':\'2\'}>','<h2 id="classes-title" class="rule">Classes & Programs</h2>')
s=s.replace('<section class="wrap"><h1 class="center rule">Gallery</h1>','<section id="gallery" class="wrap" aria-labelledby="gallery-title"><h2 id="gallery-title" class="center rule">Gallery</h2>')
s=s.replace('<section class="contact">','<section id="contact" class="contact" aria-labelledby="contact-title">').replace('<h1 class="center rule">Contact Us</h1>','<h2 id="contact-title" class="center rule">Contact Us</h2>')
a=s.index('function render()');b=s.index("document.querySelector('.menu').onclick",a)
hero=s[s.index('`<section class="hero-desktop">',a)+1:s.index("`:page==='about'",a)]
hero=hero.replace('<section class="hero-desktop">','<section id="home" class="hero-desktop" aria-labelledby="home-title"><div class="hero-backdrop" aria-hidden="true"></div>')
hero=hero.replace('<div class="hero-brand" role="img" aria-label="Happy Me Academy — Happy, Healthy & Successful Kids"></div>','<img class="hero-logo" src="assets/hero-logo-transparent.png" alt="Happy Me Academy — Happy, Healthy & Successful Kids" width="1776" height="888" fetchpriority="high">')
hero=hero.replace('<h1>Happy Me Academy</h1>','<h1 id="home-title">Happy Me Academy</h1>')
hero=hero.replace('<div class="gold-divider" aria-hidden="true">✦</div>','<div class="lotus-divider" aria-hidden="true"><span></span><svg viewBox="0 0 80 50" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M40 43C22 32 28 14 40 4c12 10 18 28 0 39Z"/><path d="M40 43C17 42 9 28 9 16c16 0 27 10 31 27Zm0 0c23-1 31-15 31-27-16 0-27 10-31 27Z"/><path d="M40 43C20 50 6 39 2 30c10-2 25 1 38 13Zm0 0c20 7 34-4 38-13-10-2-25 1-38 13Z"/></svg><span></span></div>')
s=s[:a]+'''function render(){
 document.body.dataset.page='single';
 document.querySelector('#main').innerHTML=`'''+hero+'''${about}${offering(true)}${gallery()}${contact()}`;
 document.title='Happy Me Academy | Happy, Healthy & Successful Kids';
}
function markActive(id){document.querySelectorAll('nav a').forEach(a=>{const active=a.hash==='#'+id&&!a.classList.contains('button');a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}
function syncNavigation(){const id=location.hash.slice(1)||'home';if(['home','about','classes','gallery','contact'].includes(id))markActive(id);document.querySelector('nav').classList.remove('open');document.querySelector('.menu').setAttribute('aria-expanded','false')}
'''+s[b:]
s=s.replace("if(p){const item=", "if(p){e.preventDefault();const item=")
s=s.replace("window.addEventListener('hashchange',render);render();",'''render();syncNavigation();window.addEventListener('hashchange',syncNavigation);
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{for(const entry of entries){if(entry.isIntersecting)markActive(entry.target.id)}},{rootMargin:'-15% 0px -65% 0px',threshold:0});document.querySelectorAll('#main > section[id]').forEach(section=>observer.observe(section))}
if(location.hash){requestAnimationFrame(()=>{document.getElementById(location.hash.slice(1))?.scrollIntoView({behavior:'instant'})})}
document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('nav').classList.remove('open');document.querySelector('.menu').setAttribute('aria-expanded','false')}));''')
(p/'app.js').write_text(s)
