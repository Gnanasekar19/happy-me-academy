(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('.parent-video-grid,.gallery-video-grid').forEach(track => {
    const originals = [...track.children], count = originals.length;
    if (count < 2) return;
    const shell = document.createElement('div');
    shell.className = 'video-carousel';
    shell.setAttribute('role', 'region');
    shell.setAttribute('aria-roledescription', 'carousel');
    shell.setAttribute('aria-label', track.classList.contains('parent-video-grid') ? 'Parents review videos' : 'Academy videos');
    track.before(shell); shell.append(track);
    track.classList.add('video-carousel-track');
    track.tabIndex = 0;
    track.setAttribute('aria-label', 'Swipe or use left and right arrow keys to browse videos');
    const before = originals.map(card => card.cloneNode(true));
    const after = originals.map(card => card.cloneNode(true));
    track.prepend(...before); track.append(...after);
    const cards = [...track.children];
    cards.forEach((card, i) => {card.classList.add('video-slide'); card.dataset.videoIndex = i % count;});
    const controls = document.createElement('div'); controls.className = 'video-carousel-controls';
    const dots = document.createElement('div'); dots.className = 'video-carousel-dots'; dots.setAttribute('aria-label','Choose a video');
    const toggle = document.createElement('button'); toggle.type = 'button'; toggle.className = 'video-auto-toggle';
    controls.append(dots, toggle); shell.append(controls);
    let position = count, settling, hovering = false, touching = false, auto = !reduced.matches;
    const logical = () => ((position % count) + count) % count;
    const target = i => cards[i].offsetLeft - (track.clientWidth - cards[i].offsetWidth) / 2;
    const draw = () => {
      cards.forEach((card,i) => {
        card.classList.toggle('is-active', i === position);
        card.classList.toggle('is-before', i < position);
        card.classList.toggle('is-after', i > position);
        if (i !== position) card.querySelector('video').pause();
        card.inert = i !== position;
        card.setAttribute('aria-hidden', String(i !== position));
      });
      [...dots.children].forEach((dot,i) => dot.setAttribute('aria-current',String(i === logical())));
    };
    const go = (i, smooth = true) => {
      position = Math.max(0, Math.min(cards.length - 1, i));
      i = position;
      track.scrollTo({left: target(i), behavior: smooth && !reduced.matches ? 'smooth' : 'instant'});
      draw();
    };
    originals.forEach((_,i) => {
      const dot=document.createElement('button'); dot.type='button'; dot.setAttribute('aria-label',`Show video ${i+1}`);
      dot.addEventListener('click',()=>go(count+i)); dots.append(dot);
    });
    const label = () => {toggle.textContent=auto?'Ⅱ':'▶';toggle.setAttribute('aria-label',auto?'Pause automatic slides':'Start automatic slides');toggle.setAttribute('aria-pressed',String(!auto));};
    label(); toggle.addEventListener('click',()=>{auto=!auto;label()});
    reduced.addEventListener('change',()=>{auto=!reduced.matches;label()});
    track.addEventListener('scroll',()=>{
      clearTimeout(settling);
      settling=setTimeout(()=>{
        position=cards.reduce((best,card,i)=>Math.abs(target(i)-track.scrollLeft)<Math.abs(target(best)-track.scrollLeft)?i:best,0);
        const playing=cards[position].querySelector('video');
        if ((position<count||position>=2*count) && playing.paused) go(count+logical(),false);
        else draw();
      },160);
    },{passive:true});
    track.addEventListener('keydown',event=>{
      if(event.target!==track || !['ArrowLeft','ArrowRight'].includes(event.key))return;
      event.preventDefault();go(position+(event.key==='ArrowRight'?1:-1));
    });
    shell.addEventListener('mouseenter',()=>hovering=true);shell.addEventListener('mouseleave',()=>hovering=false);
    shell.addEventListener('pointerdown',()=>touching=true);
    window.addEventListener('pointerup',()=>touching=false);window.addEventListener('pointercancel',()=>touching=false);
    const visible = () => {const r=shell.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight;};
    setInterval(()=>{
      if(!auto||document.hidden||hovering||touching||!visible()||shell.contains(document.activeElement)||[...document.querySelectorAll('video')].some(v=>!v.paused&&!v.ended))return;
      if(position<count||position>=2*count)go(count+logical(),false);
      go(position+1);
    },5500);
    new ResizeObserver(()=>go(position,false)).observe(track);
    requestAnimationFrame(()=>go(count,false));
  });
})();
