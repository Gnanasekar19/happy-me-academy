from pathlib import Path
import shutil,json
p=Path('/workspace/sites/happy-me-academy'); a=p/'dist/assets'; src=Path('/workspace/scratch/0154cbb03413/references')
for source,target in [('55 PM','home'),('56 PM (1)','gallery'),('57 PM','footer')]:
 shutil.copyfile(src/f'WhatsApp Image 2026-10-11 at 11.06.{source}.jpeg',a/f'{target}.jpg')
m=json.loads((p/'.openai/hosting.json').read_text());m['static']={'directory':'dist'};(p/'.openai/hosting.json').write_text(json.dumps(m,indent=2))
