import{t as i}from"./vendor-CPMdfHCh.js";function s(e){return e.hasOwnProperty("id")?e.id:e}function h(e){return`/channels/${s(e)}`}function u(e,t={}){const a=new URLSearchParams;for(const[o,n]of Object.entries(t))n&&a.append(i(o),n);const r=a.size>0;return`/episodes/${s(e)}${r?`?${a.toString()}`:""}`}export{h as c,u as e};
//# sourceMappingURL=routes-Nyzx--Ux.js.map
