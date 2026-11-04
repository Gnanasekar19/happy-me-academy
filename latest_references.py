from pathlib import Path
import re
p=Path('/workspace/sites/happy-me-academy/dist');s=(p/'app.js').read_text()
s=re.sub(r'<span class="program-icon".*?</span>','',s)
s=s.replace("page==='about'?about:","page==='about'?about+offering():")
a=s.index('const offering=');b=s.index('const gallery=',a)
s=s[:a]+'''const policy=`<article class="card policy-card"><h3>Common for all Events</h3><ul><li>Level Completion Certificate</li><li>Quarterly Feedback Meetings</li><li>Class Cancellation & Compensation Policy</li><li>Daily Learning Updates for Parents</li><li>Holidays</li></ul><a class="details" href="#contact">View Details →</a></article>`;
const offering=(all=false)=>`<section class="wrap offerings"><div class="center"><p class="eyebrow">Our Offerings</p><h${all?'1':'2'} class="rule">Classes & Programs</h${all?'1':'2'}></div>${all?[programs.slice(0,3),programs.slice(3,8),programs.slice(8,13),programs.slice(13)].map((group,i)=>`<div class="program-group grid group-${i}">${cards(group)}${i===3?policy:''}</div>`).join(''):`<div class="program-group grid group-0">${cards(programs.slice(0,3))}</div><div class="callout"><a class="button outline" href="#classes">View All Programs →</a></div>`}</section>`;
'''+s[b:]
(p/'app.js').write_text(s)
s=(p/'index.html').read_text().replace('<h2>Happy Me Academy</h2><p>Happy, Healthy & Successful Kids</p>','<a href="#home" class="footer-brand" aria-label="Happy Me Academy — Happy, Healthy & Successful Kids"></a>')
(p/'index.html').write_text(s)
