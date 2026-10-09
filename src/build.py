# Gera ../index.html a partir de index.tpl.html, embutindo os logos oficiais (simple-icons + favicon do ML) e o logo da LB.
import os, re
D = os.path.dirname(os.path.abspath(__file__))
A = lambda f: open(os.path.join(D, 'assets', f)).read().strip()
SHOPEE, TT, LOGO = A('shopee.path'), A('tiktok.path'), A('logo.b64')
ML = re.sub(r'<svg[^>]*>', '', A('ml.svg'), count=1).rsplit('</svg>', 1)[0]
ML_VB = re.search(r'viewBox="([^"]+)"', A('ml.svg')).group(1)
R = lambda px: max(6, round(px * .26))
def logo(mp, px):
    r = R(px)
    if mp == 'shopee':
        return f'<span class="mp-logo shopee" style="width:{px}px;height:{px}px;border-radius:{r}px"><svg width="{px*.62:.0f}" height="{px*.62:.0f}" viewBox="0 0 24 24"><path fill="#fff" d="{SHOPEE}"/></svg></span>'
    if mp == 'tiktok':
        s = f'{px*.6:.0f}'
        return (f'<span class="mp-logo tiktok" style="width:{px}px;height:{px}px;border-radius:{r}px"><svg width="{s}" height="{s}" viewBox="0 0 24 24">'
                f'<path fill="#25F4EE" transform="translate(-.8,-.6)" d="{TT}"/><path fill="#FE2C55" transform="translate(.8,.6)" d="{TT}"/><path fill="#fff" d="{TT}"/></svg></span>')
    if mp == 'ml':
        return f'<span class="mp-logo ml" style="width:{px}px;height:{px}px;border-radius:{r}px"><svg width="{px*.86:.0f}" height="{px*.86:.0f}" viewBox="{ML_VB}">{ML}</svg></span>'
    if mp == 'shein':
        return f'<span class="mp-logo shein" style="width:{px}px;height:{px}px;border-radius:{r}px;font-size:{px*.24:.1f}px">SHEIN</span>'
GOOGLE = '<svg width="20" height="20" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>'
CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M20 6 9 17l-5-5"/></svg>'
t = open(os.path.join(D, 'index.tpl.html')).read()
t = re.sub(r'\{\{L_(SHOPEE|ML|TIKTOK|SHEIN)_(\d+)\}\}', lambda m: logo(m.group(1).lower(), int(m.group(2))), t)
for mp in ['shopee', 'ml', 'tiktok', 'shein']:  # versão JS com tamanho variável
    js = logo(mp, 999).replace('`', '\\`')
    js = js.replace('width:999px;height:999px', 'width:${px}px;height:${px}px').replace(f'border-radius:{R(999)}px', 'border-radius:${Math.max(6,Math.round(px*.26))}px')
    js = re.sub(r'width="(\d+)" height="\1"', lambda m: f'width="${{Math.round(px*{int(m.group(1))/999:.2f})}}" height="${{Math.round(px*{int(m.group(1))/999:.2f})}}"', js)
    js = js.replace('font-size:239.8px', 'font-size:${(px*.24).toFixed(1)}px')
    t = t.replace('{{JS_%s}}' % mp.upper(), js)
t = t.replace('{{LOGO}}', LOGO).replace('{{GOOGLE}}', GOOGLE).replace('{{CHECK}}', CHECK)
assert '{{' not in t, re.findall(r'\{\{[^}]+\}\}', t)
open(os.path.join(D, '..', 'index.html'), 'w').write(t)
print('ok', len(t))
