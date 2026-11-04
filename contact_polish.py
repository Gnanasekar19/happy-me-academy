from pathlib import Path
p=Path('/workspace/sites/happy-me-academy/dist');s=(p/'app.js').read_text()
icons={
'Address':'<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
'Phone':'<path d="m8 3 3 5-3 3c1 3 3 5 6 6l3-3 5 3c-1 4-3 5-6 4C8 19 3 14 2 7c0-3 2-5 6-4Z"/>',
'Email':'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m3 6 9 7 9-7"/>',
'Working Hours':'<circle cx="12" cy="12" r="9"/><path d="M12 6v6l4 2"/>'}
a=s.index('const contact=');b=s.index('function render()',a);c=s[a:b]
for title,paths in icons.items():
 c=c.replace(f'<h3>{title}</h3>',f'<h3><span class="contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{paths}</svg></span>{title}</h3>')
c=c.replace('Prepare Email Enquiry →','Submit Enquiry <span class="submit-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m9 5 7 7-7 7"/></svg></span>')
c=c.replace('<a class="button outline" href="tel:+919884400201">Call the Academy</a>','')
c=c.replace('name="phone" type="tel"','name="phone" type="tel" inputmode="tel"')
s=s[:a]+c+s[b:];(p/'app.js').write_text(s)
