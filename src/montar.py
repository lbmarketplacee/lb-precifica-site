# Junta parts/ (landing nova) + CSS/HTML/JS do app (parts/old.tpl.html) em index.tpl.html, com o tema escuro.
import re
L=open('parts/old.tpl.html').read().split('\n')
app_css='\n'.join(L[122:317])
rest='\n'.join(L[410:])
rep=[
 ('<span class="pill" style="color:#7a5a17;background:var(--goldbg);border-color:#ecdcb4">Acesso vitalício</span>','<span class="badge-top" style="padding:5px 12px;font-size:12.5px">Acesso vitalício</span>'),
 ("font:600 26px/1.1 Oswald,sans-serif","font:800 26px/1.1 var(--disp)"),
 ("Oswald,sans-serif","var(--disp)"),
 (".app-top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.88)",".app-top{position:sticky;top:0;z-index:20;background:rgba(10,9,8,.78)"),
 (".menu-box{position:absolute;right:0;top:44px;background:#fff",".menu-box{position:absolute;right:0;top:44px;background:var(--surface2)"),
 (".seg button.on{background:#fff;color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,.1)}",".seg button.on{background:var(--goldbg);color:var(--gold2);box-shadow:0 0 0 1px var(--goldln) inset}"),
 ("cursor:pointer;background:#fff;text-align:left}","cursor:pointer;background:var(--surface);text-align:left;color:var(--ink)}"),
 ("border:2px solid #fff;box-shadow:0 0 0 1px var(--line2)}","border:2px solid var(--bg);box-shadow:0 0 0 1px var(--goldln)}"),
 ("background:var(--ink);color:#fff;font-size:13px;flex:none}","background:linear-gradient(180deg,#f0cf7a,#d9ae52);color:#1d1606;font-size:13px;flex:none}"),
 (".pack .tag{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--ink);color:#fff",".pack .tag{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:linear-gradient(180deg,#f0cf7a,#d9ae52);color:#1d1606"),
 (".best{display:flex;align-items:center;gap:16px;background:var(--dark);color:#fff;",".best{display:flex;align-items:center;gap:16px;background:radial-gradient(400px 160px at 0 0,rgba(217,174,82,.25),transparent 70%),#15120d;border:1px solid var(--goldln);color:var(--ink);"),
 ("color:#7a5a17","color:var(--gold2)"),
 ("border:1px solid #ecdcb4","border:1px solid var(--goldln)"),
 (".toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:#fff;",".toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--surface2);color:var(--ink);border:1px solid var(--goldln);"),
 (".tog span{position:absolute;inset:0;background:#d8d3c6;",".tog span{position:absolute;inset:0;background:#3a3631;"),
 ("background:var(--surface);border:1px solid var(--line2);border-radius:10px;transition:.15s;min-width:0}","background:var(--surface2);border:1px solid var(--line2);border-radius:12px;transition:.15s;min-width:0}"),
 ("rgba(217,174,82,.16),transparent),var(--bg)}","rgba(217,174,82,.22),transparent),var(--bg)}"),
 ("main.app{padding-top:28px;padding-bottom:64px}","main.app{padding-top:32px;padding-bottom:64px;position:relative}"),
 (".page-h h1{font-size:26px;font-weight:800}",".page-h h1{font-size:clamp(28px,3.4vw,40px);font-weight:800;letter-spacing:-.04em}"),
 (".lock .blur{filter:blur(5px);pointer-events:none;user-select:none;opacity:.6}",".lock .blur{filter:blur(6px);pointer-events:none;user-select:none;opacity:.45}"),
 (".chip.on{border-color:var(--gold);background:var(--goldbg);box-shadow:0 0 0 1px var(--gold) inset}",".chip.on{border-color:var(--gold);background:var(--goldbg);color:var(--gold2);box-shadow:0 0 0 1px var(--gold) inset}"),
 ('CORES = { taxa: "#9a9384", frete: "#5b7fbf", promo: "#e0a24a", imp: "#a074c4", custo: "#5d5a52", lucro: "#2f9e63" }','CORES = { taxa: "#8d8576", frete: "#5b8fd6", promo: "#e8a948", imp: "#b48ae0", custo: "#4d4840", lucro: "#3fbf7a" }'),
 ('style="color:${t.lucro < 0 ? "#ff8a75" : "#7fe0a8"}"','style="color:${t.lucro < 0 ? "var(--bad)" : "var(--ok)"}"'),
]
for a,b in rep:
  if a not in app_css and a not in rest: raise SystemExit('nao achei: '+a[:60])
  app_css=app_css.replace(a,b); rest=rest.replace(a,b)
js=open('parts/landing.js').read()
rest=rest.replace('// ---------- Início ----------','// ---------- Início ----------\nmontarLanding();')
rest=rest.replace('// ---------- Calculadora (todas',js+'\n// ---------- Calculadora (todas',1)
out=open('parts/head.html').read()+open('parts/landing.css').read()+'\n'+app_css+'\n</style>\n</head>\n<body>\n\n'+open('parts/landing.html').read()+rest
open('index.tpl.html','w').write(out); print('ok')
