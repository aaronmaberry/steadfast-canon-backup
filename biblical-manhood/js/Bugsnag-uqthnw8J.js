import{v as c,k as x,r,b as a,j as p,D as A,bo as xn,bp as wn,bq as Cn,br as _n,bs as kn,bt as Nn,bu as Rn,bv as Sn,bw as Tn,bx as En,by as Dn,bz as In,bA as Ln,bB as $n,bC as An,bD as Pe,bE as Pn,bF as Mn,bG as Bn,bH as Me,bI as Fn,bJ as Hn,bK as qn,bL as On,bM as jn,bN as Wn,bO as zn,bP as Yn,bQ as Un,bR as Gn,bS as Vn,bT as Qn,bU as Jn,bV as Be,bW as Kn,bX as Xn,bY as Zn,P as y,bZ as ea,b_ as ta,b$ as na,c0 as aa,c1 as oa,c2 as ra,c3 as ia,c4 as sa,c5 as ca,c6 as Ze,c7 as la,c8 as da,c9 as ua,e as _e,ca as ha,F as O,X as k,N as pa,o as z,C as ma,A as j,cb as ga,W as et,m as L,cc as Fe,Z as tt,cd as fa,ce as ba,x as H,at as va,as as ya,aM as xa,a$ as wa,cf as Ca,cg as _a,J as ka,aJ as Na,I as nt,bb as He,z as Ra,a4 as at,a5 as ot,a6 as we,a7 as rt,ch as Sa,ci as it,cj as Ta,ac as Ea,ad as Da,ck as st,E as Ia,cl as La,cm as $a,cn as Aa}from"./vendor-CPMdfHCh.js";import{u as te,r as B}from"./useLocalStorage-BMP7gFuX.js";Pa.propTypes={panels:c.arrayOf(c.shape({name:c.string.isRequired,heading:c.node.isRequired,content:c.node.isRequired})).isRequired,listIcon:c.oneOf(["none","arrow","radio"]),exclusiveOpen:c.bool,className:c.string,defaultOpenPanel:c.string,onPanelChange:c.func};function Pa({panels:e,listIcon:t="radio",exclusiveOpen:n=!0,className:o="",defaultOpenPanel:i,onPanelChange:s=()=>{}}){const[l,d]=r.useState(i||e[0].name),h=u=>{if(e.length!==1){if(l===u){d(null),s(null);return}d(u),s(u)}};return a("div",{css:Ma,children:a("div",{className:A("accordion",o),children:e.map((u,m)=>p("div",{className:A("accordion--panel",{open:n&&l===u.name,hasIcon:t!=="none"}),children:[p("div",{role:"button",className:A("accordion--titleContainer",{inert:e.length===1}),tabIndex:0,onKeyDown:f=>f.key==="Enter"&&h(u.name),onClick:()=>h(u.name),children:[e.length>1&&a("div",{className:A("accordion--listIcon",t),children:a("div",{})}),a("div",{className:"accordion--title",children:u.heading})]}),a("div",{role:"definition",className:"accordion--contentDrawer",children:a("div",{className:"accordion--content",children:u.content})})]},m))})})}const Ma=x`
  .accordion {
    box-shadow: inset 0 1px 2px var(--color-tint9);
    border: 1px solid var(--color-tint5);
    border-radius: 4px;
  }

  .accordion--panel {
    border-bottom: 1px solid var(--color-tint5);
    overflow: hidden;
  }

  .accordion--panel:last-child {
    border-bottom: none;
  }

  .accordion--titleContainer {
    display: flex;
    align-items: center;
    gap: 1rem;
    cursor: pointer;
    padding: 1rem;
    color: var(--color-tint2);
    transition: color 200ms ease-in;
  }

  .accordion--titleContainer.inert {
    cursor: default;
  }

  .accordion--titleContainer:hover {
    color: var(--color-tint1);
    transition: color 200ms ease-in;
  }

  .accordion--panel.open .accordion--titleContainer {
    color: var(--color-topaz);
    transition: color 200ms ease-in;
  }

  .accordion--listIcon.none {
    display: none;
  }

  .accordion--listIcon.radio {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 1rem;
    height: 1rem;
    border-radius: 50%;
    border: 1px solid var(--color-tint2);
    transition:
      border-color 200ms ease-in,
      background-color 200ms ease-in;
  }

  .accordion--listIcon.radio div {
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 50%;
    background-color: transparent;
    transition: background-color 200ms ease-in;
  }

  .accordion--titleContainer:hover .accordion--listIcon.radio {
    border-color: var(--color-tint1);
    transition: border-color 200ms ease-in;
  }

  .accordion--panel.open .accordion--listIcon.radio {
    border-color: var(--color-topaz);
    background-color: var(--color-topaz);
    transition:
      border-color 200ms ease-in,
      background-color 200ms ease-in;
  }

  .accordion--panel.open .accordion--listIcon.radio div {
    background-color: var(--color-tint10);
    transition: background-color 200ms ease-in;
  }

  .accordion--title {
    font-weight: 600;
    line-height: 2rem;
  }

  .accordion--contentDrawer {
    box-sizing: border-box;
    max-height: 0;
    overflow: hidden;
    transition: max-height 400ms ease-in;
  }

  .accordion--panel.open .accordion--contentDrawer {
    max-height: 700px;
    transition: max-height 400ms ease-in;
  }

  .accordion--content {
    padding: 0 1rem 1rem 1rem;
  }
`,Ba={1:"fs-0",2:"fs-21",3:"fs-2",4:"fs-3",5:"fs-4",6:"fs-5"},Fa=e=>`c-${e}`,Ha=(e,t)=>Ba[t||e],Q=({color:e="tint0",isUppercase:t=!1,level:n,size:o=void 0,text:i})=>{const s=`h${n}`;return a(s,{className:A("lh-1.333",Fa(e),Ha(n,o),t&&"tt-u","fw-600"),children:i})};xn.add(wn,Cn,_n,kn,Nn,Rn,Sn,Tn,En,Dn,In,Ln,$n,An,Pe,Pe,Pn,Mn,Bn,Me,Me,Fn,Hn,qn,On,jn,Wn,zn,Yn,Un,Gn,Vn,Qn,Jn,Be,Be,Kn,Xn,Zn);const qa={accounts:da,brand:la,general:Ze,"check-ins":ca,logomark:sa,people:ia,publishing:ra,churchCenter:oa,services:aa,giving:na,registrations:ta};function $({symbol:e,pathPrefix:t="",...n}){const o=/^fa-/.test(e),[i,s]=e.replace(".svg","").split("#");return o?a(ea,{icon:["fa-facebook-f","fa-instagram","fa-twitter","fa-youtube"].includes(e)?`fab ${e}`:`fa-solid ${e}`,...n}):a(ua.Symbol,{symbol:`${t}${qa[i]}#${s}`,...n})}$.propTypes={symbol:y.string.isRequired,pathPrefix:y.string};q.propTypes={as:c.elementType,children:c.node.isRequired,className:c.string,style:c.object};function q({as:e="div",className:t="",children:n,style:o,...i}){return a(e,{className:`d-f ai-c jc-sb px-2 action-drawer action-bar ${t}`,style:{gap:"1rem",...o},...i,children:n})}ct.propTypes={children:c.node.isRequired,className:c.string};function ct({className:e="",children:t,...n}){return a(q,{className:`p-s fd-c fd-r@xs ta-c ta-l@xs ${e}`,...n,children:t})}q.Pane=ct;lt.propTypes={children:c.node.isRequired,className:c.string,to:c.string.isRequired};function lt({className:e="",children:t,to:n="",...o}){return p(q,{as:_e,to:n,className:`fd-r ta-l mb-0 ${e}`,...o,children:[a(q.Column,{children:t}),a(q.Action,{children:a("span",{className:"c-tint3 fs-4",children:a($,{symbol:"general#right-chevron","aria-hidden":!0})})})]})}q.Link=lt;dt.propTypes={children:c.node.isRequired,className:c.string};function dt({children:e,className:t=""}){return a("div",{className:`d-f fd-c ai-fs fg-1 ${t}`,children:e})}q.Column=dt;ut.propTypes={children:c.node.isRequired,className:c.string};function ut({children:e,className:t=""}){return a("div",{className:`d-f fd-c fd-r@xs fg-1 ${t}`,children:e})}q.Row=ut;ht.propTypes={children:c.node.isRequired};function ht({children:e,...t}){return a(Q,{level:2,size:4,color:"tint1",text:e,...t})}q.Title=ht;pt.propTypes={children:c.node.isRequired};function pt({children:e}){return a("p",{className:"fs-4 m-0 c-tint1",children:e})}q.Description=pt;mt.propTypes={children:c.node.isRequired,className:c.string};function mt({children:e,className:t=""}){return a("div",{className:t,children:e})}q.Action=mt;ke.propTypes={children:c.node,className:c.string,type:c.string,icon:c.string};function ke({children:e,className:t="",type:n="error",icon:o="",...i}){const s=A(t,`${n}-alert alert`);return p("div",{...i,className:s,style:o?{display:"flex",gap:"0.5rem"}:void 0,children:[o&&a($,{symbol:o,style:{color:(()=>{let d="";return n==="error"&&(d="var(--color-ruby)"),n==="warning"&&(d="var(--color-citrine)"),n==="info"&&(d="var(--color-topaz)"),n==="success"&&(d="var(--color-emerald)"),d})(),marginTop:"2px"}}),a("div",{className:"f-1",children:e})]})}const Oa=r.createContext(null),re=r.createContext(null);function gt(){const e=r.useContext(re),t=r.useContext(Oa);if(e){const[,,n]=e;return n}return t||"light"}function R(e,t=document.body){return window.getComputedStyle(t).getPropertyValue(e).trim()}const ja=[56,96,128,200,256,400,600,900];za.propTypes={url:c.string.isRequired,alt:c.string,className:c.string};const qe=e=>R(e)?ha(R(e)).hex().replace("#",""):"";function ft({isHeader:e=!1}={}){gt();const t=qe(e?"--d-fill-color-neutral-070":"--d-fill-color-neutral-030"),n=qe(e?"--d-fill-color-neutral-020":"--d-fill-color-neutral-070");return{foregroundColor:t,backgroundColor:n}}function Wa(e){return e.split("?")[0]}function za({url:e,alt:t="avatar",className:n=""}){const{foregroundColor:o,backgroundColor:i}=ft(),s=Wa(e).replace("http:","https:"),l=`background_color=${i}&color=${o}`,d=ja.map(u=>`${s}?g=${u}x${u}%23&${l} ${u}w`).join(", "),h=`${s}?g=200x200%23&${l}`;return a("img",{src:h,srcSet:d,sizes:"auto",alt:t,loading:"lazy",className:n,style:{borderRadius:"50%",aspectRatio:"1 / 1",objectFit:"cover"}})}const bt=({size:e,theme:t,children:n})=>a("span",{className:A("badge",`${t}-badge`,`${e}-badge`),children:n}),Ya=({iconSize:e=16})=>a("span",{className:"d-if ai-c jc-c mr-4p",children:a("svg",{role:"img","aria-hidden":"true",xmlns:"http://www.w3.org/2000/svg",width:e,height:e,viewBox:"0 0 16 16",className:"featured-badge__icon",style:{fill:"currentcolor"},children:a("path",{d:"m8 .5 2.472 4.937L16 6.23l-4 3.843.944 5.427L8 12.937 3.056 15.5 4 10.073 0 6.229l5.528-.793L8 .5Z"})})}),vt=({size:e="md"})=>p(bt,{size:e,theme:"featured",children:[a(Ya,{iconSize:e==="sm"?10:14}),"Featured"]});vt.displayName="Badge.Featured";const yt=({size:e="md",text:t,theme:n="default"})=>a(bt,{size:e,theme:n,children:t});yt.Featured=vt;const xt=({disabled:e=!1,isLoading:t=!1,onClick:n=void 0,size:o="lg",text:i,theme:s="primary",type:l="button",variant:d="filled"})=>p("button",{type:l,className:A("btn",`${o}-btn`,`${d}-btn`,`${s}-btn`,t&&"loading-btn"),disabled:e||t,onClick:n,children:[t&&a("span",{className:"spinner"}),i]});function Ua({className:e,children:t,...n}){return a("section",{css:ie.root,className:e,...n,children:t})}function Ga({symbol:e}){return a("div",{css:ie.icon,children:a($,{symbol:e,"aria-hidden":!0})})}function Va({children:e}){return a("div",{css:ie.content,children:e})}function Qa({text:e,level:t=2}){return a("div",{css:ie.heading,children:a(Q,{level:t,size:3,text:e})})}function Ja({text:e}){return a("p",{css:ie.description,children:e})}function Ka({onClick:e,text:t}){return a(xt,{variant:"outline",size:"sm",text:t,onClick:e})}const Ci={Root:Ua,Icon:Ga,Content:Va,Heading:Qa,Description:Ja,Button:Ka},ie={root:x`
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
    text-align: center;
    margin: 0 auto;
    padding: 16px 0;
    max-width: 460px;
  `,icon:x`
    font-size: 32px;
    line-height: 0;
    color: var(
      --d-fill-color-neutral-020
    ); // TODO: Replace with icon token when available
  `,content:x`
    display: flex;
    flex-direction: column;
    gap: 4px;
  `,heading:x`
    & > :is(h1, h2, h3, h4, h5, h6) {
      color: var(--d-text-color);
    }
  `,description:x`
    color: var(--d-text-color-secondary);
    line-height: 1.3;
    margin: 0;
  `};function Xa(){return r.useState(null)}const Ne=r.createContext([null,()=>{}]),Za=({children:e})=>{const t=Xa();return a(Ne.Provider,{value:t,children:e})},eo=()=>{const[e,t]=r.useContext(Ne);return e&&a("nav",{"aria-label":"Breadcrumb",className:"breadcrumbs",children:a("div",{className:"breadcrumbs__layout",children:e})})},to=({children:e})=>{const[t,n]=r.useContext(Ne);return r.useEffect(()=>(n(e),()=>n(null)),[e]),a(O,{})};function no({linkUrl:e,linkState:t,pageText:n,isActive:o}){let i,s;return o?(i="breadcrumbs__page breadcrumbs__current-page",s="location"):(i="breadcrumbs__page",s="false"),a(O,{children:e?p(_e,{to:e,state:t,className:i,"aria-current":s,"aria-label":n,children:[a("span",{className:"text",children:n}),a("span",{className:"icon",children:a($,{symbol:"churchCenter#three-dots"})})]}):a("div",{className:i,"aria-current":s,children:n})})}function _i({children:e}){return p(to,{children:[a(no,{linkUrl:"/me",pageText:"Me"}),a(ao,{}),e]})}function ki({isActive:e,children:t}){let n,o;return e?(n="breadcrumbs__page breadcrumbs__current-page",o="location"):(n="breadcrumbs__page",o="false"),a("div",{className:n,"aria-current":o,children:t})}function ao(){return a("span",{className:"breadcrumbs__divider-icon",children:a($,{symbol:"general#right-chevron","aria-hidden":!0})})}const oo={1:"lg",2:"md",3:"sm",4:"xs",5:"2xs"},ro=({children:e,className:t,level:n,size:o})=>{const i=`h${n}`,s=o||oo[n];return a(i,{className:A("dds-heading",`dds-heading--${s}`,t),children:e})};function ee({as:e="article",badges:t=[],children:n,description:o,footnote:i,heading:s,layout:l="column",link:d,poster:h,posterAltText:u="",posterAspectRatio:m="16 / 9"}){const f=e,v=typeof d=="object"&&d?.as||"a",b=typeof d=="string"?{as:void 0,href:d||void 0,css:{}}:d,w=l==="row";return a(f,{css:[F.card,w&&F.cardHorizontal],children:p(v,{...b,children:[a("div",{css:[F.poster,w&&F.posterHorizontal],children:typeof h=="string"?a("img",{loading:"lazy",src:h,alt:u,style:{aspectRatio:m}}):h}),p("div",{css:[F.cardContentWrapper,w&&F.cardContentWrapperHorizontal],children:[p("div",{css:[F.cardContent],children:[s&&a(ee.Heading,{children:s}),o&&a(ee.Description,{children:o}),i&&a(ee.HeadingUppercase,{text:i}),n]}),a(io,{badges:t})]})]})})}function io({badges:e=[]}){const t=e.filter(n=>!!n);return t.length===0?null:a("div",{css:[F.cardFooter],children:t.map(({theme:n="default",label:o},i)=>n==="featured"?p("div",{className:"badge",children:[a($,{symbol:"general#closed-star",css:F.featured}),o]},i):n==="confidential"?p("div",{className:"badge",children:[a($,{symbol:"general#hide-eye",css:F.confidential}),o]},i):a(yt,{theme:n,text:o},i))})}const so=({children:e})=>a(ro,{level:3,size:"xs",children:e}),co=({text:e})=>a("h4",{css:F.cardHeadingUppercase,children:e}),lo=({children:e})=>a("p",{css:F.cardDescription,children:e});ee.Heading=so;ee.HeadingUppercase=co;ee.Description=lo;const F={card:x`
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;

    &:before {
      border-radius: 8px;
      bottom: 0;
      box-shadow: inset 0 0 0 1px var(--d-fill-color-neutral-000);
      content: "";
      display: block;
      left: 0;
      position: absolute;
      right: 0;
      top: 0;
      pointer-events: none;
      z-index: 5;
      opacity: 0.055;
    }

    [data-color-scheme="dark"] &:before {
      opacity: 0.11;
    }

    > * {
      position: relative;
      display: flex;
      flex-direction: column;
      flex: 1;
      border-radius: 8px;
      overflow: hidden;
    }

    img {
      width: 100%;
      display: block;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      object-position: center center;
    }
  `,cardHorizontal:x`
    &:before {
      display: none;
    }

    > * {
      display: grid;
      grid-template-columns: minmax(150px, 1fr) 2fr;
      grid-template-rows: auto;
      gap: 12px;
      border-radius: 0;
    }
  `,poster:x`
    overflow: hidden;
    > * {
      border-radius: 0;
    }
  `,posterHorizontal:x`
    > * {
      border-radius: 8px;
    }
  `,cardContentWrapper:x`
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 12px;
    padding: 12px;
    flex: 1;
    background-color: var(--d-fill-color-neutral-100);
  `,cardContentWrapperHorizontal:x`
    padding: 0;
    justify-content: flex-start;
  `,cardContent:x`
    display: flex;
    flex-direction: column;
    gap: 4px;
  `,cardFooter:x`
    display: flex;
    align-items: center;
    gap: 4px;
  `,cardDescription:x`
    color: var(--color-tint1);
    font-size: 13px;
    margin-bottom: 0;
  `,cardHeadingUppercase:x`
    color: var(--color-tint3);
    font-size: 12px;
    text-transform: uppercase;
  `,featured:x`
    color: var(--color-citrine);
    font-size: 14px;
    margin-right: 4px;
  `,confidential:x`
    color: var(--color-tint2);
    font-size: 14px;
    margin-right: 4px;
  `},Oe=x({width:32,height:32,padding:0,borderRadius:"50%",display:"inline-flex",alignItems:"center",justifyContent:"center"}),uo=()=>window.matchMedia?.("(prefers-reduced-motion: reduce)").matches??!1,K="1rem";function Ni({children:e}){const t=r.useRef(null),[n,o]=r.useState(!1),[i,s]=r.useState(!1),l=r.useCallback(()=>{const u=t.current;u&&(o(u.scrollLeft>0),s(u.scrollLeft+u.clientWidth<u.scrollWidth-1))},[]),d=r.Children.count(e);if(r.useEffect(()=>{const u=t.current;if(!u)return;l();const m=new ResizeObserver(l);return m.observe(u),()=>m.disconnect()},[l,d]),d===1)return a("div",{css:{maxWidth:350},children:r.Children.toArray(e)[0]});const h=u=>{const m=t.current;if(!m)return;const f=parseFloat(getComputedStyle(m).columnGap)||0,v=m.firstElementChild?m.firstElementChild.clientWidth+f:m.clientWidth,b=Math.round(m.scrollLeft/v);m.scrollTo({left:(b+u)*v,behavior:uo()?"auto":"smooth"})};return p("div",{css:{borderRadius:8,paddingBlock:K,paddingInline:K,display:"flex",flexDirection:"column",gap:"0.75rem",backgroundColor:"var(--d-fill-color-neutral-090)",border:"1px solid var(--d-fill-color-neutral-090)"},children:[a("div",{ref:t,onScroll:l,css:{display:"flex",gap:K,overflowX:"auto",scrollSnapType:"x mandatory",scrollbarWidth:"none",msOverflowStyle:"none","&::-webkit-scrollbar":{display:"none"},marginInline:`-${K}`,paddingInline:K,scrollPaddingInline:K,"& > *":{flex:"0 0 45%",scrollSnapAlign:"start","@media (max-width: 600px)":{flex:"0 0 90%"}},"& > *:last-child":{scrollSnapAlign:"end"},"& > .action-drawer":{borderRadius:8}},children:e}),(n||i)&&p("div",{className:"d-f ai-c g-1",children:[a("button",{type:"button",className:"btn secondary-btn minor-btn",css:Oe,"aria-label":"Scroll left",disabled:!n,onClick:()=>h(-1),children:a($,{symbol:"general#left-chevron"})}),a("button",{type:"button",className:"btn secondary-btn minor-btn",css:Oe,"aria-label":"Scroll right",disabled:!i,onClick:()=>h(1),children:a($,{symbol:"general#right-chevron"})})]})]})}ho.propTypes={as:c.string,children:c.node.isRequired};function ho({as:e="section",children:t}){return a(e,{css:po.wrapper,children:t})}const po={wrapper:x`
    display: grid;
    grid-template-rows: auto;
    grid-template-columns: repeat(auto-fill, minmax(272px, 1fr));
    gap: 24px;
  `};mo.propTypes={label:c.string,className:c.string,children:c.node};function mo({label:e,className:t,children:n}){const o={container:{boxShadow:"inset 0 1px 2px var(--color-tint9)",borderStyle:"solid",borderColor:"var(--color-tint5)",borderWidth:n?"1px":"1px 0 0 0",padding:n?"1rem":"0",borderRadius:n?"4px":"0",position:"relative"},labelContainer:{position:"absolute",height:"24px",top:"-14px",left:"0",right:"0",fontSize:"12px",display:"flex",justifyContent:"center"},label:{backgroundColor:"white",padding:"0.25rem 0.5rem",color:"var(--color-tint3)"}};return p("div",{className:t,css:o.container,children:[a("div",{css:o.labelContainer,children:a("div",{css:o.label,children:e})}),n]})}const de=e=>e.attributes.items.map(({label:t,uri:n})=>({href:n,children:t}));function go(e){throw new wt(e)}function fo(e){return e instanceof wt}function wt(e){this.uri=e}ue.propTypes={children:c.node};function ue({children:e}){const t=z();return a(ue.Component,{location:t,children:e})}ue.Component=class extends k.Component{static getDerivedStateFromProps(e,t){const n=ue.Component;return e.location!==t.previous_location?n.resetState(e):null}static initialState(e){return{isRedirect:!1,uri:void 0,previous_location:e.location}}static resetState(e){return this.initialState(e)}constructor(e){super(e),this.state=this.constructor.initialState(e)}componentDidCatch(e,t){if(!fo(e))throw e;this.setState(n=>({...n,isRedirect:!0,uri:e.uri}))}render(){return this.state.isRedirect?a(pa,{to:this.state.uri,replace:!0}):this.props.children}};const bo="VerifiedInSessionPerson",vo="VerifiedInMemoryPerson",pe=r.createContext(),Ct=r.createContext(null);function Ri({children:e}){const{current_person:t}=r.useContext(pe),[n,o]=r.useState({current_person:t}),[i,s]=r.useState("session"),l=ma(),d=r.useCallback((f,v)=>{s(v),o(b=>({...b,current_person:f})),l.invalidateQueries({refetchType:"all"})},[l]),h=r.useCallback(async()=>{console.debug("[DynamicSession] refreshing session now");const f=await j.check();d(f,"session")},[d]),u=r.useCallback(async f=>{console.debug("[DynamicSession] refreshing session (embedded mode)");const b=await(await fetch("/token_person",{headers:{Authorization:`Bearer ${f}`}})).json();d(b,"embedded")},[d]),m={session:n,authMode:i,refreshSession:h,refreshSessionFromToken:u};return a(Ct.Provider,{value:m,children:e})}function _t(){const e=r.useContext(Ct);if(!e)throw new Error("useDynamicSession must be used within a DynamicSessionProvider");return e}function J(e=!1){const{session:t}=_t(),{current_person:n}=t,o={authenticated:[bo,vo].includes(n.data.type)};return e&&!o.authenticated&&go(`/login?return=${window.location.href}`),{...n,meta:o}}kt.propTypes={children:c.node.isRequired};function kt({children:e}){const n="ProtectAgainstChangingSessions-id",[o,i]=te(n,null),{data:s}=J(!1),{authMode:l}=_t(),d=`${s.id}`,[h,u]=r.useState(!1);r.useEffect(m,[d]),r.useEffect(()=>(window.addEventListener("storage",f),()=>{window.removeEventListener("storage",f)})),r.useEffect(()=>{if(l==="embedded")return;const b=window.setInterval(v,6e4);return()=>window.clearInterval(b)});function m(){i(d)}function f(b){if(b.key!==n)return;const w=b.newValue;u(d!==w)}async function v(){try{const w=`${(await j.check()).data.id}`;u(d!==w)}catch(b){if(b.message!=="Failed to fetch")throw b}}return h?p(r.Fragment,{children:[p("div",{className:"d-f fs-0 g-1",children:[a("span",{"aria-label":"waving hand emoji",role:"img",children:"👋"}),a(Q,{level:1,text:"Hey!"})]}),a("p",{className:"my-2",children:"Logging in and out of Church Center changed in another browser window. Sometimes this will happen on a shared computer. To make sure you're logged in as who you expect to be, we'll need to refresh the page."}),a("div",{className:"d-f py-2",children:a("button",{className:"btn",onClick:()=>window.location.reload(),children:"Refresh"})})]}):e}const yo={joltConnectionId:void 0,requestJoltInstance:()=>{},subscribe:()=>{},unsubscribe:()=>{}},Re=r.createContext(yo),xo=async()=>(await j.post("/global/v2/jolt_connect")).data.id,wo=async(e,t)=>(await j.post("/notifications/v2/me/jolt_subscribe",{data:{attributes:{channel:e,connection_id:t}}})).data.id,Co=async(e,t)=>(await j.post("/chat/v2/me/jolt_subscribe",{data:{attributes:{channel:e,cid:t}}})).data.id;class _o{constructor(t){this.jolt=t,this.subscriptions={}}get connection(){return this.jolt.connection}get connectionId(){return this.jolt.connection.connectionId}disconnect(){this.jolt.disconnect()}subscribe(t,n){return this.subscriptions[t]||(this.subscriptions[t]={subscription:this.jolt.subscribe(t,n),subscribers:0}),this.subscriptions[t].subscribers+=1,this.subscriptions[t].subscription}unsubscribe(t){this.subscriptions[t]&&(this.subscriptions[t].subscribers-=1,this.subscriptions[t].subscribers===0&&(this.jolt.unsubscribe(t),delete this.subscriptions[t]))}}function ko(e,t){return e?new _o(new ga(e,{fetchAuthTokenFn:t},{logToConsole:!0})):null}function No(){const{data:e}=J(!1),t=e?.id?`church_center.notifications.people.${e.id}`:null;return me(wo,t)}function Ro(){const{data:e}=J(!1),t=e?.id?`chat.people.${e.id}`:null;return me(Co,t)}const Nt=({children:e})=>{const t=r.useRef(null),[n,o]=r.useState(),{joltWebsocketUrl:i}=r.useContext(P),s=r.useCallback(()=>{if(t.current)return;const h=ko(i,xo);h&&(t.current=h,t.current.connectionId.then(u=>o(u)))},[i]),l=r.useCallback((h,u)=>{if(h)return s(),t.current?.subscribe(h,u)},[s]),d=r.useCallback(h=>{h&&t.current?.unsubscribe(h)},[]);return a(Re.Provider,{value:{joltConnectionId:n,requestJoltInstance:s,subscribe:l,unsubscribe:d},children:e})};Nt.propTypes={children:c.oneOfType([c.arrayOf(c.node),c.node])};function Rt({subscriptionTokenPath:e,prefetchedToken:t}){const n=mi();return r.useCallback(async(o,i)=>{if(t)return t;i||n.notify(new Error("Jolt connection_id is missing"));const s={data:{attributes:{channel:o,connection_id:i}}};return await j.post(e,s).then(d=>d.data.id).catch(d=>console.error("failed to subscribe to Jolt channel",d))},[e,t])}function me(e,t){const{subscribe:n,unsubscribe:o}=r.useContext(Re),[i,s]=r.useState();return r.useEffect(()=>{const l=n(t,{fetchSubscribeTokenFn:e});return s(l),()=>o(t)},[t,e,n,o]),i}function St(e,t,n){r.useEffect(()=>(t.forEach(o=>e?.bind(o,n)),()=>{t.forEach(o=>e?.unbind(o,n))}),[e,t,n])}function Si(e,t,n,o){const i=Rt({subscriptionTokenPath:e}),s=me(i,t),l=r.useMemo(()=>Array.isArray(n)?n:[n],[n]);St(s,l,o)}function se(e,t,n,o){const i=Rt({prefetchedToken:e}),s=me(i,t),l=r.useMemo(()=>Array.isArray(n)?n:[n],[n]);St(s,l,o)}function Tt(){return!!J().data.id}function So(){return Tt()?a(Eo,{}):null}function To(e,t){if(!e)throw new Error("fetchPublishingJoltToken: connectionId is required");return j.post("/publishing/v2/jolt_subscribe",{data:{attributes:{channel:[`organization-${t}.publishing.church_center.v2.events.theme_settings`,`organization-${t}.publishing.church_center.v2.events.page`,`organization-${t}.publishing.church_center.v2.events.church_center_app_menu`,`organization-${t}.publishing.church_center.v2.events.draft_mode`].join(","),connection_id:e}}})}function Eo(){const{joltConnectionId:e,requestJoltInstance:t}=r.useContext(Re),{currentOrganization:{id:n}}=r.useContext(P),{data:o}=et({queryKey:["publishingJoltToken",n,e],queryFn:()=>To(e,n).catch(i=>console.error("failed to fetch publishingJoltToken",i)),select:i=>i?.data.id,enabled:!!e,staleTime:1/0});return r.useEffect(()=>{o||t()},[o,t]),o?a(W,{publishingJoltToken:o}):null}W.propTypes={publishingJoltToken:y.string.isRequired};function W({publishingJoltToken:e}){const{currentOrganization:{id:t},reactToCandidateEvents:n,setDraftMode:o}=r.useContext(P),{data:i}=J(!1),s=r.useCallback(d=>{const{data:h}=d.data;n(h)},[n]);se(e,`organization-${t}.publishing.church_center.v2.events.theme_settings`,"publishing.church_center.v2.events.theme_settings.created",s),se(e,`organization-${t}.publishing.church_center.v2.events.page`,"publishing.church_center.v2.events.page.created",s),se(e,`organization-${t}.publishing.church_center.v2.events.church_center_app_menu`,"publishing.church_center.v2.events.church_center_menu.created",s);const l=r.useCallback(d=>{const h=d.data;L(h,"data.relationships.person.data.id")===i.id&&o(d.event===W.draftModeStarted)},[i.id,o]);return se(e,`organization-${t}.publishing.church_center.v2.events.draft_mode`,W.draftModeEvents,l),null}W.draftModeStarted="publishing.church_center.v2.events.draft_mode.started";W.draftModeFinished="publishing.church_center.v2.events.draft_mode.finished";W.draftModeEvents=[W.draftModeStarted,W.draftModeFinished];const Et="doxy-token-theme-overrides";function Do(e){const t=e.flatMap(({themeableTokens:i,newLightValue:s})=>i.map(l=>`${l}: ${je(l,s,"light")};`)).join(`
      `),n=e.flatMap(({themeableTokens:i,newDarkValue:s})=>i.map(l=>`${l}: ${je(l,s,"dark")};`)).join(`
      `),o=document.createElement("style");o.id=Et,o.textContent=`
    :root {
      ${t}
    }

    body[data-color-scheme="dark"] {
      ${n}
    }

    @media (prefers-color-scheme: dark) {
      body[data-color-scheme="system"] {
        ${n}
      }
    }
  `,document.head.appendChild(o)}function je(e,t,n){if(e in Fe){const s=Fe[e][n];return Io(s,t)}return t}function Io(e,t){return e.replace(/hsla?\s*\([^)]+\)/gi,t).replace(/rgba?\s*\([^)]+\)/gi,t).replace(/#[0-9a-fA-F]{3,8}\b/gi,t)}function Lo(){const e=document.getElementById(Et);e&&e.remove()}const Dt=()=>null,It="BOOTING",$o=300*1e3,We="WebBoot.v9",ze="WebBoot.draftMode",P=r.createContext(),he=r.createRef();he.current=Dt;function Ti(){he.current()}Ao.propTypes={defaultState:y.object,children:y.node.isRequired};function Ao({defaultState:e="BOOTING",children:t}){const n=tt(),{search:o}=z(),[i,s]=te(We,e),[l,d]=te(ze,!1),h=l?"draft":"published",u=L(i,`${h}ThemeSettings.attributes.primary_color`),m=L(i,`${h}ThemeSettings.attributes.dark_primary_color`),f=L(i,`${h}ThemeSettings.attributes.theme_enabled`),v=r.useRef(o.includes("start_draft_mode=1")),b=L(i,"abilities.publishing.draft_mode")||!1;r.useEffect(()=>{v.current&&b&&(d(!0),v.current=!1)},[b]);const w=!!window.ReactNativeWebView;r.useEffect(()=>{w&&(window.setDraftMode=d)},[w,d]),r.useEffect(()=>{f&&u&&(document.body.style.setProperty("--color-brand-light",u),document.body.style.setProperty("--color-brand-dark",m||u),document.body.style.setProperty("--color-brand-gradient-start","var(--color-brand)"),document.body.style.setProperty("--color-brand-gradient-end","var(--color-brand)"),Lo(),Do([{themeableTokens:ba.brand,newLightValue:u,newDarkValue:m||u}]))},[f,u,m]),r.useEffect(()=>{if(o.includes("start_draft_mode=1")){let g=new URL(window.location.toString());g.searchParams.delete("start_draft_mode"),g=g.toString().substring(g.origin.length),n(g.toString(),{state:{...history.state},replace:!0})}},[l]);const N=Tt(),{data:D,refetch:C}=et({queryKey:["webBoot"],queryFn:Bo,refetchInterval:!N&&$o,refetchOnWindowFocus:!N,refetchOnReconnect:!N});r.useEffect(()=>{D&&Fo(i,D)&&s(D)},[D]),r.useEffect(()=>{B("WebBoot.v1"),B("WebBoot.v2"),B("WebBoot.v3"),B("WebBoot.v4"),B("WebBoot.v5"),B("WebBoot.v6"),B("WebBoot.v7"),B("WebBoot.v8")},[]);const Y=r.useCallback(()=>{B(We),B(ze)},[]);r.useEffect(()=>(he.current=Y,()=>he.current=Dt),[Y]);const U=r.useCallback(g=>{Po(g)||C()},[C]),E={...i,draftMode:l,reactToCandidateEvents:U,setDraftMode:d};return i===It?a(zr,{}):a(P.Provider,{value:E,children:t})}const Po=e=>L(e,"type")==="Page"&&L(e,"relationships.slug.data.id")!=="home";function Mo(e){const t=n=>{const o=L(e,`data.relationships.${n}.data.0.type`),i=L(e,`data.relationships.${n}.data.0.id`);return e.included.find(s=>s.type===o&&s.id===i)};return{abilities:L(e,"data.attributes.abilities"),analyticsUrl:L(e,"data.attributes.analytics_url"),builtInPages:L(e,"data.attributes.built_in_pages"),currentOrganization:t("current_organization"),draftHomePage:t("draft_home_page"),draftMenu:t("draft_menu"),draftThemeSettings:t("draft_theme_settings"),features:L(e,"data.attributes.features"),joltWebsocketUrl:L(e,"data.attributes.jolt_websocket_url"),myChurchCenterEnabled:L(e,"data.attributes.my_church_center_enabled"),publishedHomePage:t("published_home_page"),publishedMenu:t("published_menu"),publishedThemeSettings:t("published_theme_settings")}}function Bo(){const t=`/publishing/v2/web_boot?include=${["draft_menu","draft_home_page","draft_theme_settings","published_menu","published_home_page","published_theme_settings","current_organization"]}`;return j.get(t).then(Mo)}const Fo=(e,t)=>{if(e===It)return!0;const n=["draftHomePage","publishedHomePage"];return e.draftHomePage?.id!==t.draftHomePage?.id||e.publishedHomePage?.id!==t.publishedHomePage?.id?!0:Object.keys(e).some(o=>n.includes(o)?!1:!fa(e[o],t[o]))};function Ei(e){const t=r.useContext(P),{pathname:n}=z(),o=t.draftMode?de(t.draftMenu):de(t.publishedMenu);return n.startsWith("/giving/profile")?e:o.find(s=>n.startsWith(s.href))?.children||e}function Ho(){const{currentOrganization:e}=r.useContext(P);return L(e,"attributes.datetime_fmt_configuration.timeZone","America/Los_Angeles")}H.extend(va);H.extend(ya);H.extend(xa);const qo="YYYY-MM-DD",Oo=new Date().getFullYear()-1885;function Ye(e,t){if(!e)return null;if(e instanceof Date)return isFinite(e.getTime())?e:null;try{const n=H(e,[t,qo],!0);if(n.isValid()){const o=new Date(n.year(),n.month(),n.date());if(isFinite(o.getTime()))return o}}catch(n){console.warn("Failed to parse date value:",e,n)}return null}const Di=({value:e,onChange:t,showOnLoad:n=!1,errorClass:o,maxCap:i=20,minCap:s=Oo,placeholder:l,popperClassName:d,...h})=>{const{currentOrganization:{attributes:{datetime_fmt_configuration:u}}}=r.useContext(P),m=r.useRef(null),f=Ho(),v=u.dateFirst?"DD/MM/YYYY":"MM/DD/YYYY",[b,w]=r.useState(()=>Ye(e,v)),N=new Date().getFullYear(),D=new Date(N-s,0,1),C=new Date(N+i,11,31);r.useEffect(()=>{if(!e){w(null);return}const E=Ye(e,v);E&&w(E)},[e,v,f]),r.useEffect(()=>{n&&m.current&&m.current.setFocus()},[n]);const Y=E=>{if(w(E),t){const g=E?new Date(E.getFullYear(),E.getMonth(),E.getDate()):null,_={target:{value:g?H(g).format("YYYY-MM-DD"):""}};t(_)}},U=E=>{const g=E.target.value;/^\d{4}-\d{2}-\d{2}$/.test(g)&&setTimeout(()=>{const[S,_,I]=g.split("-").map(Number),T=new Date(S,_-1,I);if(w(T),t){const be={target:{value:H(T).format("YYYY-MM-DD")}};t(be)}},0),/^\d{2}-\d{2}-\d{4}$/.test(g)&&setTimeout(()=>{let S;if(u.dateFirst){const[_,I,T]=g.split("-").map(Number);S=new Date(T,I-1,_)}else{const[_,I,T]=g.split("-").map(Number);S=new Date(T,_-1,I)}if(w(S),t){const I={target:{value:H(S).format("YYYY-MM-DD")}};t(I)}},0),/^\d{4,8}$/.test(g)&&setTimeout(()=>{let S;const _=parseInt(g.substring(4,8),10),I=Number.isNaN(_)?N:_;if(u.dateFirst){const T=parseInt(g.substring(0,2),10),M=parseInt(g.substring(2,4),10);S=new Date(I,M-1,T)}else{const T=parseInt(g.substring(0,2),10),M=parseInt(g.substring(2,4),10);S=new Date(I,T-1,M)}if(w(S),t){const M={target:{value:H(S).format("YYYY-MM-DD")}};t(M)}},0)};return p("div",{className:`date-field ${o||""}`,children:[a("span",{className:"date-field__icon",children:a($,{symbol:"general#calendar",title:"Date"})}),a(wa,{ref:m,selected:b,onChange:Y,onChangeRaw:U,dateFormat:u.dateFirst?"dd/MM/yyyy":"MM/dd/yyyy",minDate:D,maxDate:C,showYearDropdown:!0,showMonthDropdown:!0,showPopperArrow:!1,dropdownMode:"select",wrapperClassName:"w-100%",placeholderText:l||(u.dateFirst?"DD/MM/YYYY":"MM/DD/YYYY"),popperClassName:d??"",...h})]})},Lt=({disabled:e=!1,hidden:t=!1,label:n,value:o})=>a("option",{disabled:e,hidden:t,value:o,children:n});Lt.displayName="Select.Option";const $t=({children:e,disabled:t=!1,label:n})=>a("optgroup",{label:n,disabled:t,children:e});$t.displayName="Select.OptGroup";const At=({options:e})=>a(O,{children:e.map(t=>a("option",{value:t.value,disabled:t.disabled,children:t.label},t.value))}),G=({id:e,name:t,value:n,onChange:o,disabled:i=!1,ariaLabel:s,className:l="select",style:d,children:h,options:u,readOnly:m,label:f,size:v="md",required:b=!1,onBlur:w})=>{const N=e||t,D=A(l,{[`${v}-select`]:v!=="md"||f!==void 0,readOnly:m});return p(O,{children:[f&&p("label",{htmlFor:N,children:[f,b?a("span",{className:"c-ruby ml-4p",children:"*"}):null]}),a("select",{"aria-label":s,className:D,disabled:i,id:N,name:t,onBlur:w,onChange:o,required:b,style:d,value:n,children:h||u&&a(At,{options:u})})]})};G.Option=Lt;G.OptGroup=$t;G.Options=At;const jo=[{label:"Month",value:""},{label:"January",value:"1"},{label:"February",value:"2"},{label:"March",value:"3"},{label:"April",value:"4"},{label:"May",value:"5"},{label:"June",value:"6"},{label:"July",value:"7"},{label:"August",value:"8"},{label:"September",value:"9"},{label:"October",value:"10"},{label:"November",value:"11"},{label:"December",value:"12"}],Pt=new Date().getFullYear(),Wo=Pt-99,zo=Pt+1,Yo={day:"",month:"",year:""},Uo=({name:e,onChange:t,disabled:n=!1,initialValue:o=null,isDayFirst:i=!1,label:s=null,labelStyle:l,selectStyle:d,readOnly:h})=>{const[u,m]=r.useState(Yo),[f,v]=r.useState(31),[b,w]=r.useState(n);r.useEffect(()=>{n&&w(!0)},[]),r.useEffect(()=>{if(!o)return;const g=H(o);m({day:g.date().toString(),month:(g.month()+1).toString(),year:g.year().toString()}),v(g.daysInMonth())},[o]);const N=g=>{m(S=>{const _={...S,...g},I=C(_),T=Y(I);return T.isValid()?t(T.format("YYYY-MM-DD"),_):t(null,_),_})},D=[{label:"Year",value:""},...u.year?[{label:"---",value:"1885"}]:[],...Ca(Wo,zo).map(g=>({label:g.toString(),value:g.toString()}))],C=g=>Object.fromEntries(Object.entries(g).map(([S,_])=>[S,_?Number(_):null])),Y=({year:g,month:S,day:_})=>{const I=S-1,T=H().year(g||new Date().getFullYear()).month(I),M=T.daysInMonth();return v(M),!g||!_?H(null):_>0&&_<=M?T.date(_):H(null)},U=f+1,E=[{label:"Day",value:""},..._a(1,U).map(g=>({label:g.toString(),value:g.toString()}))];return p("div",{children:[s&&a("label",{className:"label",style:l,htmlFor:`${e}_${i?"day":"month"}`,children:s}),p("div",{className:"d-f",style:{gap:"0.5rem"},children:[i&&a(G,{disabled:b,style:d,name:`${e}_day`,ariaLabel:"select day",value:u.day,onChange:({target:{value:g}})=>N({day:g}),options:E,readOnly:h}),a(G,{disabled:b,style:d,name:`${e}_month`,ariaLabel:"select month",value:u.month,onChange:({target:{value:g}})=>N({month:g}),options:jo,readOnly:h}),!i&&a(G,{disabled:b,style:d,name:`${e}_day`,ariaLabel:"select day",value:u.day,onChange:({target:{value:g}})=>N({day:g}),options:E,readOnly:h}),a(G,{disabled:b,style:d,name:`${e}_year`,ariaLabel:"select year",value:u.year,onChange:({target:{value:g}})=>N({year:g}),options:D,readOnly:h})]})]})};Uo.propTypes={disabled:c.bool,initialValue:c.string,isDayFirst:c.bool,label:c.node,labelStyle:c.object,selectStyle:c.object,name:c.string.isRequired,onChange:c.func.isRequired,readOnly:c.bool};const ve={emerald:"var(--color-emerald)",tint0:"var(--color-tint0)",tint1:"var(--color-tint1)",tint2:"var(--color-tint2)",tint3:"var(--color-tint3)",tint4:"var(--color-tint4)",tint5:"var(--color-tint5)",tint6:"var(--color-tint6)",tint7:"var(--color-tint7)",tint8:"var(--color-tint8)",tint9:"var(--color-tint9)",tint10:"var(--color-tint10)",brand:"var(--color-brand)",brandGradientStart:"var(--color-brand-gradient-start)",brandGradientEnd:"var(--color-brand-gradient-end)"};function Ii(){return{topaz:R("--color-topaz"),turquoise:R("--color-turquoise"),emerald:R("--color-emerald"),ruby:R("--color-ruby"),marigold:R("--color-marigold"),tint0:R("--color-tint0"),tint1:R("--color-tint1"),tint2:R("--color-tint2"),tint3:R("--color-tint3"),tint4:R("--color-tint4"),tint5:R("--color-tint5"),tint6:R("--color-tint6"),tint7:R("--color-tint7"),tint8:R("--color-tint8"),tint9:R("--color-tint9"),tint10:R("--color-tint10"),brand:R("--color-brand"),brandGradientStart:R("--color-brand-gradient-start"),brandGradientEnd:R("--color-brand-gradient-end")}}function Mt(e,t=0,n){return r.useCallback(ka(e,t,n),[e,t,n])}function Li(e,t=0,n){const o=r.useRef(e),[i,s]=r.useState(e),l=Mt(d=>s(d),t,n);return r.useEffect(()=>{if(e!==o.current)return l(e),o.current=e,l.cancel},[e]),i}const Bt=r.createContext({}),Go=({children:e})=>{const[t,n]=r.useState({width:window.innerWidth,height:window.innerHeight,breakpoint:null}),o=Mt(()=>{n({width:window.innerWidth,height:window.innerHeight}),document.documentElement.style.setProperty("--window-inner-height",window.innerHeight+"px")},200);return r.useEffect(()=>(o(),window.addEventListener("resize",o,{passive:!0}),()=>{window.removeEventListener("resize",o)}),[]),a(Bt.Provider,{value:t,children:e})},ge=r.createContext(),Vo=ge.Provider,Ce={qrCode:null,showQRCode:!1,pageUsesQRCode:!1};function Qo(e=Ce,t){switch(t.type){case"setPageUsesQRCode":return{...e,pageUsesQRCode:t.payload};case"setQRCode":return{...e,qrCode:t.payload};case"setShowQRCode":return{...e,showQRCode:!!t.payload};case"resetQRCodeState":return{...Ce};default:return e}}const Ft=({children:e})=>a(Vo,{value:r.useReducer(Qo,Ce),children:e});Ft.propTypes={children:c.node.isRequired};const Jo=()=>{const[{showQRCode:e,qrCode:t,pageUsesQRCode:n},o]=r.useContext(ge),i=()=>{o({type:"setShowQRCode",payload:!e})};return r.useEffect(()=>{if(n&&e&&!t){const l={errorCorrectionLevel:"H",margin:0,width:1024,color:{dark:"#313437",light:"#FFF"}};Na.toDataURL(window.location.toString(),l,(d,h)=>{d||o({type:"setQRCode",payload:h})})}},[t,e,n,window.location.toString()]),n&&a("ul",{className:"site-footer__links o-3 d-n d-f@md",children:a("li",{className:"site-footer__link",children:a("button",{style:{background:"none",border:"none",padding:0,fontWeight:400},className:"fs-5 c-tint3",onClick:()=>{i(),setTimeout(()=>{window.scrollTo(0,1e7)},0)},children:"Get QR code"})})})},Ko=()=>{const[{showQRCode:e,qrCode:t,pageUsesQRCode:n},o]=r.useContext(ge),i=r.useRef(null);return n&&e?a("div",{className:"container container--narrow",children:p("div",{id:"qrcode-wrapper",className:"action-drawer d-f p-2 mt-4",children:[a("div",{className:"mr-2",children:a("img",{id:"qrcode",alt:"qrcode",src:t,width:150})}),p("div",{className:"f-1",children:[a("p",{children:`Use this graphic in printed materials or on displayed screens. People can scan the code using their phone's built-in code reader ("Camera" on iOS, "Google Assistant" on Android) to be brought straight to this URL – without having to type it.`}),a("p",{children:a("a",{ref:i,className:"qrcode-download c-brand",href:t,download:"qrcode.png",children:a("span",{id:"qrcode",children:"Download QR Code"})})})]})]})}):a("div",{})},Xo=(...e)=>{const[,t]=r.useContext(ge);r.useEffect(()=>(t({type:"setPageUsesQRCode",payload:!0}),()=>{t({type:"resetQRCodeState"})}),e)};function $i(){return Xo(),null}function Ai(){const{abilities:e,draftMode:t,setDraftMode:n}=r.useContext(P);return e.publishing.draft_mode?p("div",{children:[a("div",{className:"d-f ai-c mt-2 jc-sb mb-2",children:a(Q,{level:2,size:3,text:"Administrator tools"})}),p("div",{className:"action-drawer mb-1",children:[p("div",{className:"d-f ai-c",children:[a("span",{className:"c-tint3 p-r t-1p mr-1",children:a($,{symbol:"general#outlined-envelope"})}),a(Q,{level:3,size:4,text:`Draft preview mode: ${t?"Enabled":"Disabled"}`})]}),a("div",{className:"mt-2",children:"This setting is available because you are a Publishing Administrator in Planning Center Publishing. When enabled, you'll see the draft version of content."}),a("div",{className:"mt-2",children:t?a("button",{className:"minor-btn secondary-btn btn",onClick:()=>n(!1),children:"Finish"}):a("button",{className:"minor-btn secondary-btn btn",onClick:()=>n(!0),children:"Start"})})]})]}):null}function Zo(){const{draftMode:e,setDraftMode:t}=r.useContext(P);return Ie()||!e?null:a("div",{style:{alignItems:"center",background:"var(--draft-mode-banner-bg-color)",color:"white",padding:"1rem",position:"relative",transition:"opacity 0.4s ease, margin-top 0.4s ease"},children:p("div",{className:"d-f ai-c jc-c",children:[a($,{symbol:"logomark#publishing",style:{width:24,height:24,marginRight:"0.5rem"}}),a("p",{className:"fs-2 mb-0 mr-1",style:{letterSpacing:"0.02em"},children:a("strong",{children:"Draft preview mode"})}),a("div",{children:a("button",{className:"minor-btn secondary-btn btn",style:{color:"#464C59",border:"none"},onClick:()=>t(!1),children:"Finish"})})]})})}function ce(e){window.parent?.postMessage({type:e},"*")}function Ue(e){e.keyCode===27&&(e.target===document.body?ce("close"):e.target?.blur&&e.target.blur())}function er(e){try{return new URLSearchParams(e).has("embed")?!1:window.self!==window.top}catch{return!0}}function Ht(){const[e,t]=r.useState("unknown"),{search:n}=z(),[o]=r.useState(er(n)),i=r.useCallback(()=>{t("yes")},[]),s=r.useCallback(()=>{e==="unknown"&&(t("no"),console.log("Trying to put Giving on your website? Use the fully supported ChurchCenterModal! Instructions are available at https://help.planningcenter.com/en/144372-link-to-your-donation-form-on-your-website.html"))},[e]),l=r.useCallback(()=>{ce("close")},[]),d=r.useCallback(u=>{const m=new URL(u.origin),f=m.protocol==="https:"||m.host.slice(0,9)==="localhost"||m.host.match(/\.test$/);if(u.data.type==="verified")if(f)i(),ce("show");else throw"ChurchCenterButton: must be called from an HTTPS page."},[i]),h=r.useCallback(()=>{window.scrollTo(0,0),ce("ready"),setTimeout(s,1e3)},[s]);return r.useEffect(()=>{if(o)return window.addEventListener("message",d,!1),document.addEventListener("keyup",Ue),h(),()=>{window.removeEventListener("message",d),document.removeEventListener("keyup",Ue)}},[o,d,h]),{inIframe:o,blessed:e,close:l}}const qt=r.createContext({close:()=>{},inIframe:!1,blessed:"unknown"});function tr({children:e}){const t=Ht();return r.useEffect(()=>{const n=document.body.classList;n.remove("iframed"),n.remove("iframed--blessed-yes"),n.remove("iframed--blessed-no"),n.remove("iframed--blessed-unknown"),t.inIframe&&(n.add("iframed"),n.add(`iframed--blessed-${t.blessed}`))},[t.inIframe,t.blessed]),a(qt.Provider,{value:t,children:e})}function nr(){const e=r.useContext(qt);if(e===void 0)throw new Error("useChurchCenterIframeContext must be used within a ChurchCenterIframeProvider");return e}function ar(){const{close:e,blessed:t}=nr();return t!=="yes"?null:a("button",{className:"close-iframe",onClick:e,style:{border:"none",background:"none"},children:a("span",{className:"icon d-if ai-c",children:p("svg",{className:"symbol",id:"Layer_1","data-name":"Layer 1",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 16 16",children:[a("title",{children:"x"}),a("polygon",{points:"16 1.611 14.389 0 8 6.389 1.611 0 0 1.611 6.389 8 0 14.389 1.611 16 8 9.611 14.389 16 16 14.389 9.611 8 16 1.611"})]})})})}function or(){const{layout:{organization_name:e}}=r.useContext(pe);return a(nt,{titleTemplate:`%s - ${e}`,defaultTitle:e})}function rr(e={}){const{search:t,pathname:n}=z(),[o,i]=r.useState(()=>({...e,...He.parse(t,{parseBooleans:!0,parseNumbers:!0})})),s=r.useCallback(l=>{const d=He.stringify(l),h=[n,d].filter(u=>u).join("?");i(l),window.history.replaceState(l,new Date().getTime(),h)},[i,n]);return[o,s]}const ir=()=>{const{search:e,pathname:t}=z();return{embedded:!!new URLSearchParams(e).get("embed")&&t==="/calendar"}};function Ot(){const{embedded:e}=ir(),{inIframe:t}=Ht();return e||t}function sr({title:e,imageUrl:t,description:n}){const{currentOrganization:{attributes:{name:o,avatar_url:i}}}=r.useContext(P),s=e?`${e} - ${o}`:o,l=n||(e?`${o}'s ${e} on Church Center.`:`${o} on Church Center.`),d=t||i;return p(nt,{title:e,children:[a("meta",{name:"description",content:l}),a("meta",{property:"og:type",content:"website"}),a("meta",{property:"og:url",content:window.location.href}),a("meta",{property:"og:title",content:s}),a("meta",{property:"og:description",content:l}),a("meta",{property:"og:image",content:d}),a("meta",{property:"twitter:card",content:"summary_large_image"}),a("meta",{property:"twitter:url",content:window.location.href}),a("meta",{property:"twitter:title",content:s}),a("meta",{property:"twitter:description",content:l}),a("meta",{property:"twitter:image",content:d})]})}const Ge="narrow";function cr(e={layoutWidth:Ge,footerVisible:!0,headerVisible:"initialRender",embedded:!1}){function t(n,o){switch(o.type){case"setLayoutWidth":return{...n,layoutWidth:o.payload??Ge};case"showFooter":return{...n,footerVisible:!0};case"hideFooter":return{...n,footerVisible:!1};case"showHeader":return{...n,headerVisible:!0};case"hideHeader":return{...n,headerVisible:!1}}}return r.useReducer(t,e)}const jt=()=>{const[e,t]=r.useContext(re),n=r.useCallback(o=>{t({type:o?"showHeader":"hideHeader"})},[t]);return[e.headerVisible,n]},lr=()=>{const[e,t]=r.useContext(re),n=r.useCallback(o=>{t({type:o?"showFooter":"hideFooter"})},[t]);return[e.footerVisible,n]},Pi=()=>{const[e,t]=jt();r.useEffect(()=>(t(!1),()=>t(!0)),[t])},dr={domain:window.location.host,"max-age":3600*24*30,path:"/"},ur=Object.entries(dr).map(([e,t])=>`${e}=${t}`).join("; ");function hr(e){const n=document.cookie.split(";").map(o=>o.trim()).find(o=>o.startsWith(`${e}=`));return n&&decodeURIComponent(n.split("=")[1])}function pr(e){const[t,n]=r.useState(()=>hr(e)),o=r.useCallback(i=>{document.cookie=`${e}=${encodeURIComponent(i)}; ${ur}`,n(i)},[e]);return[t,o]}const Wt="chat",mr=new RegExp(`#${Wt}=([^]+)`),gr="chatFragmentRoute";function fr(){const[e,t]=pr(gr),[n,o]=r.useState(Ve(location.hash));r.useEffect(()=>{function s(){o(Ve(location.hash))}return window.addEventListener("hashchange",s),()=>window.removeEventListener("hashchange",s)},[]);const i=r.useCallback((s,l={})=>{const d=new URLSearchParams(l).toString(),h=s&&d?`${s}?${d}`:s,u=h?`#${Wt}=${h}`:"#";o(h),history.replaceState(void 0,void 0,u),h!==null&&t(h)},[t,o]);return{lastOpenRoute:e,route:n,setRoute:i}}function Ve(e){const t=e.match(mr);return t?t[1]||"":null}const zt=r.createContext();Yt.propTypes={children:y.node.isRequired,pcoChatEnabled:y.bool};function Yt({children:e,pcoChatEnabled:t=!1}){const[n,o]=r.useState(!1),{route:i,setRoute:s,lastOpenRoute:l}=fr(),d=()=>{l&&!i&&s(l),o(!0)},h=()=>{o(!1),s(null)},u=()=>{n?h():d()};return a(zt.Provider,{value:{closeDrawer:h,isOpen:n,openDrawer:d,pcoChatEnabled:t,route:i,setRoute:s,toggleDrawer:u},children:e})}const Se=()=>r.useContext(zt),Qe=360,Ut=100;Gt.propTypes={children:y.node.isRequired};function Gt({children:e}){const{isOpen:t,route:n,openDrawer:o}=Se(),i=vr(t,Ut);return r.useEffect(()=>{n&&!t&&o()},[n,t,o]),p(k.Fragment,{children:[a("style",{children:br}),a("div",{className:`ChatDrawer ${t?"is-open":""}`,id:"chat-drawer",role:"dialog","aria-modal":t,"aria-label":"Chat",tabIndex:t?0:-1,inert:t?void 0:"",children:i&&e})]})}const br=`
  .ChatDrawer {
    background: var(--color-tint9);
    border-left: 1px solid var(--color-tint5);
    box-shadow: -2px 0 6px rgba(0,0,0,0.1);
    height: 100%;
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 1001; /* Thanks to .Header for setting its z-index to 1000 🙃 */
    visibility: hidden;
    opacity: 0;
  }

  .ChatDrawer.is-open {
    visibility: visible;
    opacity: 1;
  }

  @media (min-width: 600px) {
    .ChatDrawer {
      left: auto;
      width: ${Qe}px;
      transform: translateX(${Qe}px);
      transition: transform ${Ut}ms ease-in-out;
      visibility: visible;
      opacity: 1;
    }

    .ChatDrawer.is-open {
      transform: translateX(0);
    }
  }
`;function vr(e,t){const[n,o]=r.useState(e);return r.useEffect(()=>{if(e)o(!0);else{const i=setTimeout(()=>o(!1),t);return()=>clearTimeout(i)}},[e]),n}Vt.propTypes={isLoading:y.bool.isRequired,message:y.string};function Vt({isLoading:e=!0,message:t="Loading"}){return e?p(k.Fragment,{children:[a("style",{children:yr}),a("div",{className:"loading-indicator",role:"status","aria-live":"polite","aria-label":`${t} Chat`,children:p("div",{className:"loading-indicator__text",children:[t,a("span",{className:"loading-indicator__dot","aria-hidden":"true",children:"."}),a("span",{className:"loading-indicator__dot","aria-hidden":"true",children:"."}),a("span",{className:"loading-indicator__dot","aria-hidden":"true",children:"."})]})})]}):null}const yr=`
  .loading-indicator {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
  }

  .loading-indicator__text {
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--color-tint4);
    transform: translateY(68px);
  }

  .loading-indicator__dot {
    opacity: 0;
    animation: loading-dots-1 1s infinite;
  }

  .loading-indicator__dot:nth-of-type(1) {
    animation: loading-dots-1 1s infinite;
  }

  .loading-indicator__dot:nth-of-type(2) {
    animation: loading-dots-2 1s infinite;
  }

  .loading-indicator__dot:nth-of-type(3) {
    animation: loading-dots-3 1s infinite;
  }

  @keyframes loading-dots-1 {
    0%, 20% {
      opacity: 1;
    }
    21%, 39% {
      opacity: 0;
    }
    40%, 100% {
      opacity: 1;
    }
  }

  @keyframes loading-dots-2 {
    0%, 20% {
      opacity: 1;
    }
    21%, 59% {
      opacity: 0;
    }
    60%, 100% {
      opacity: 1;
    }
  }

  @keyframes loading-dots-3 {
    0%, 20% {
      opacity: 1;
    }
    21%, 79% {
      opacity: 0;
    }
    80%, 100% {
      opacity: 1;
    }
  }
`;Te.propTypes={callback:y.func.isRequired,params:y.shape({messageType:y.string.isRequired})};function Te(e,{messageType:t}){k.useEffect(()=>{const n=o=>{o.origin===window.location.origin&&o.data.type===t&&e(o)};return window.addEventListener("message",n),()=>{window.removeEventListener("message",n)}},[])}function xr({route:e,onInternalPathChange:t}){const[n,o]=r.useState(e),i=r.useRef(e),l=[Ra("/chat"),n].filter(Boolean).join("/"),d=r.useCallback(h=>{const[u,m]=h.data.payload.split("?"),f=u.replace(/^\/?chat/,"").replace(/^\/+/,"")||"/",v=new URLSearchParams(m),b=[f,v.toString()].filter(Boolean).join("?");i.current=b,t(f,v)},[t]);return Te(d,{messageType:"NEW_ROUTE_RENDERED"}),r.useEffect(()=>{e!==i.current&&o(e)},[e]),l}function wr(){const[e,t]=k.useState(!0),{closeDrawer:n,route:o,setRoute:i}=Se(),s=r.useCallback(()=>{n()},[n]),l=xr({onInternalPathChange:i,route:o});return Te(s,{messageType:"CLOSE_DRAWER"}),p(k.Fragment,{children:[a(Vt,{isLoading:e}),a("iframe",{onLoad:()=>t(!1),src:l,title:"Chat",style:{backgroundColor:"white",border:"none",height:"100%",width:"100%",zIndex:"1"}})]})}const oe=136,le=32,Je=le;Qt.propTypes={chatUnread:c.bool,links:c.arrayOf(c.object).isRequired,loginLink:c.object.isRequired,myChurchCenterLink:c.object.isRequired,notificationCount:c.number,notificationLink:c.object.isRequired,organizationDisplayName:c.string.isRequired,organizationImageUrl:c.string,organizationLink:c.object.isRequired,pcoChatEnabled:c.bool,personDisplayName:c.string.isRequired,personIdentified:c.bool.isRequired,personImageUrl:c.string.isRequired};function Qt({links:e,loginLink:t,myChurchCenterLink:n,notificationCount:o,notificationLink:i,organizationDisplayName:s,organizationImageUrl:l,organizationLink:d,pcoChatEnabled:h=!1,personDisplayName:u,personIdentified:m,personImageUrl:f,chatUnread:v=!1}){const b=_r(),N=Cr()>oe,D=b?Jt:Kt;return p(Yt,{pcoChatEnabled:h,children:[a(kr,{}),h&&a(Gt,{children:a(wr,{})}),N&&a("div",{className:"condensed-header-placeholder"}),a("header",{className:`Header ${N&&"condensed-header"}`,children:p("div",{className:"Header__layout",children:[a("div",{className:"Header__org-wrapper",children:a(V,{...d,className:"Header__org-link",children:l?a("img",{src:l,alt:s,className:"Header__org-avatar"}):a("h1",{className:"Header__org-name",children:s})})}),a(D,{links:e,loginLink:t,myChurchCenterLink:n,notificationCount:o,notificationLink:i,personDisplayName:u,personIdentified:m,personImageUrl:f,chatUnread:v})]})})]})}function Cr(){const[e,t]=r.useState(0),n=k.useCallback(()=>t(window.pageYOffset),[t]);return r.useEffect(()=>(window.addEventListener("scroll",n,{passive:!0}),()=>window.removeEventListener("scroll",n)),[n]),e}Jt.propTypes={chatUnread:c.bool,links:c.arrayOf(c.object).isRequired,loginLink:c.object.isRequired,myChurchCenterLink:c.object.isRequired,notificationCount:c.number,notificationLink:c.object.isRequired,personDisplayName:c.string.isRequired,personIdentified:c.bool.isRequired,personImageUrl:c.string.isRequired};function Jt({links:e,loginLink:t,myChurchCenterLink:n,notificationCount:o,notificationLink:i,personDisplayName:s,personIdentified:l,personImageUrl:d,chatUnread:h}){let u,m;return e.length>5?(u=e.slice(0,4),m=e.slice(4)):u=e,p("nav",{className:"Navigation d-n@iframe",children:[u.map(({key:f,...v})=>a(V,{className:"Navigation__link",...v},f)),m&&a(rt,{children:({isOpen:f})=>p(k.Fragment,{children:[p(at,{className:"Navigation__more-button Navigation__link",children:["More",a("span",{className:"Navigation__more-button-toggle",children:a(Nr,{style:{transform:f?"scaleY(-1)":"scaleY(1)",transition:"transform 0.2s"}})})]}),a(ot,{className:"Navigation-menu",children:m.map(({key:v,...b})=>a(we,{className:"Navigation-link",...b},v))})]})}),l?p(k.Fragment,{children:[a(Ee,{notificationCount:o,notificationLink:i}),a(De,{unread:h}),a(V,{className:"Navigation__link",...n,children:a(en,{displayName:s,imageUrl:d})})]}):a(V,{className:"Navigation__link",...t})]})}Kt.propTypes={chatUnread:c.bool,links:c.arrayOf(c.object).isRequired,loginLink:c.object.isRequired,myChurchCenterLink:c.object.isRequired,notificationCount:c.number,notificationLink:c.object.isRequired,personDisplayName:c.string.isRequired,personIdentified:c.bool.isRequired,personImageUrl:c.string.isRequired};function Kt({links:e,loginLink:t,myChurchCenterLink:n,notificationCount:o,notificationLink:i,personDisplayName:s,personIdentified:l,personImageUrl:d,chatUnread:h}){return p("nav",{className:"AltNavigation d-n@iframe",children:[l&&p(k.Fragment,{children:[a(Ee,{notificationCount:o,notificationLink:i}),a(De,{unread:h}),a(V,{className:"Navigation__link",...n,children:a("img",{src:d,alt:`${s}'s avatar`,className:"AltNavigation__person-avatar"})})]}),a(rt,{children:()=>p(k.Fragment,{children:[a(Ke,{}),p(ot,{className:"AltNavigation__layout",children:[a("div",{className:`AltNavigation__person-box ${l&&"logged-in"}`,children:p("div",{className:"display-flex align-items-center justify-content-space-between",children:[a("div",{className:"AltNavigation__person"}),a(Ke,{})]})}),e.map(({key:u,...m})=>a(we,{className:"AltNavigation__link",...m},u)),!l&&a(we,{className:"AltNavigation__link",...t})]})]})})]})}function Ke(){return a(at,{className:"AltNavigation__trigger",children:p("div",{className:"icon",children:[a("span",{className:"line"}),a("span",{className:"line"}),a("span",{className:"line"})]})})}const Xt=720;function _r(){const[e,t]=k.useState(window.innerWidth),n=k.useCallback(()=>t(window.innerWidth),[t]);return k.useEffect(()=>(window.addEventListener("resize",n),window.addEventListener("orientationchange",n),()=>{window.removeEventListener("resize",n),window.removeEventListener("orientationchange",n)}),[n]),e>=Xt}function kr(){const e=`
  /* Header */
  .Header {
    background-color: var(--color-tint9);
    border-bottom: 1px solid var(--color-tint7);
    height: ${oe}px;
    padding: 1.5rem 2rem 1.5rem 1.5rem;
    z-index: 1000; /* Thanks to Vimeo for setting their z-index to 999 😠*/
  }

  .iframed .Header { position: relative }

  @media (min-width: ${Xt}px) {
    .Header { padding: 1.5rem 2rem }
  }

  .Header__layout {
    align-items: center;
    display: flex;
    height: 100%;
    justify-content: space-between;
    margin: 0 auto;
    max-width: 900px;
    width: 100%;
  }
  .Header__org-wrapper {
    padding-right: 2rem;
  }
  .Header__org-link {
    display: block;
  }
  .Header__org-name {
    font-size: 18px;
    line-height: 1.2;
    margin: 0;
    max-width: 220px;
  }
  .Header__org-avatar {
    max-height: 80px;
    width: 100%;
    max-width: 200px;
    object-fit: contain;
    object-position: center left;
  }
  [data-color-scheme="dark"][data-contrast="low"] .Header__org-avatar {
    background-color: var(--color-tint0);
    border-radius: 4px;
    padding: 2px;
  }

  /* Condensed Header */
  .condensed-header {
    border-bottom-color: var(--color-tint6);
    height: ${oe/2}px;
    position: fixed;
    top: 0;
    width: 100%;
    animation: fade-in 0.25s;
  }

  .condensed-header-placeholder {
    height: ${oe}px; /* this keeps the browser from jumping when scrolling to the bottom of a short page  */
  }
  .condensed-header .Navigation-wrapper,
  .condensed-header .Navigation-button {
    height: 34px;
  }
  .condensed-header .Navigation-avatar {
    height: 24px;
    width: 24px;
    min-width: 24px;
  }

  .condensed-header .Navigation-displayName {
    font-size: 12px;
  }

  .condensed-header .Header__org-avatar {
    max-height: 48px;
  }

  .condensed-header .Navigation__link {
    font-size: 0.875rem;
  }

  .condensed-header .AltNavigation__trigger .icon .line {
    height: 3px;
    margin: 4px auto;
    width: 28px;
    transition: all 0.2s;
  }

  @keyframes fade-in {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  /* Navigation */
  .Navigation {
    align-items: center;
    display: flex;
    justify-content: flex-end;
    white-space: nowrap;
  }
  .Navigation__link,
  .ChatButton {
    color: var(--color-tint2);
    margin-right: 1.5rem;
  }
  .Navigation__link[aria-current=true],
  .Navigation__link[aria-current=page] {
    color: var(--color-tint1);
    font-weight: 600;
  }
  .Navigation__more-button {
    background-color: transparent;
    border: 0;
    font-weight: 400;
    padding: 0;
  }
  .Navigation__more-button-toggle {
    font-size: 10px;
    padding-left: 6px;
  }

  /* AltNavigation */
  .AltNavigation {
    justify-content: center;
    align-items: center;
    display: flex;
    gap: 1.5rem;
  }
  .AltNavigation .NotificationBell {
    padding: 4px;
  }
  .AltNavigation .NotificationBell:after {
    right: 4px;
    top: 8px;
  }
  .AltNavigation__layout[data-reach-menu-list]{
    animation: slide-in 0.3s ease;
    background: var(--color-tint9);
    border: 0;
    border-left: 1px solid var(--color-tint5);
    bottom: 0;
    box-shadow: -2px 0 6px rgba(0,0,0,0.1);
    overflow: auto;
    padding: 0;
    position: fixed;
    right: 0;
    top: 0;
    width: 280px;
    z-index: 998;
  }
  .AltNavigation__layout [data-reach-menu-item] { outline: none }
  .AltNavigation__link {
    color: var(--color-tint1);
    display: block;
    border-bottom: 1px solid var(--color-tint6);
    padding: 1rem;
  }
  .AltNavigation__link[data-selected] {
    background: var(--color-tint7);
    color: var(--color-tint1);
  }
  .AltNavigation .Navigation__link,
  .AltNavigation .ChatButton {
    margin-right: 0;
  }
  .AltNavigation__trigger {
    background: transparent;
    border: 0;
    padding: 0;
  }
  .AltNavigation__person-box {
    border-bottom: 1px solid var(--color-tint5);
    display: flex;
    flex-direction: column;
    height: ${oe}px;
    justify-content: center;
    padding: 0 1.5rem;
  }
  .AltNavigation__person-box.logged-in {
    justify-content: space-between;
    padding: 2rem 1.5rem 0 1.5rem;
  }
  .AltNavigation__person {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
  }
  .AltNavigation__person-avatar {
    border-radius: 100%;
    width: 32px;
    display: block;
    max-width: unset;
  }
  .AltNavigation__person-name,
  .AltNavigation__person-name[data-selected] {
    background: transparent;
    color: var(--color-tint1);
    font-size: 1rem;
    font-weight: 500;
    padding-left: 1rem;
  }
  .AltNavigation__person-actions {
    font-size: 0.875rem;
    padding-top: 0.5rem;
  }
  .AltNavigation__trigger .icon .line {
    background-color: var(--color-tint3);
    border-radius: 4px;
    display: block;
    height: 4px;
    margin: 6px auto;
    -webkit-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
    width: 32px;
  }

  .AltNavigation__trigger .icon .line:first-child {
    margin-top: 0;
  }

  .AltNavigation__trigger .icon .line:nth-child(3){ margin-bottom: 0 }
  .AltNavigation__trigger .icon:hover { cursor: pointer }
  .AltNavigation__trigger[aria-expanded=true] .icon .line:nth-child(2) {
    opacity: 0;
  }
  .AltNavigation__trigger[aria-expanded=true] .icon .line:nth-child(1) {
    -webkit-transform: translateY(10px) rotate(45deg);
    -ms-transform: translateY(10px) rotate(45deg);
    -o-transform: translateY(10px) rotate(45deg);
    transform: translateY(10px) rotate(45deg);
  }
  .AltNavigation__trigger[aria-expanded=true] .icon .line:nth-child(3) {
    -webkit-transform: translateY(-10px) rotate(-45deg);
    -ms-transform: translateY(-10px) rotate(-45deg);
    -o-transform: translateY(-10px) rotate(-45deg);
    transform: translateY(-10px) rotate(-45deg);
  }
  @keyframes slide-in {
    0% { transform: translateX(100%) }
    100% { transform: translateX(0) }
  }

  /* LoggedInLinks */
  .LoggedInLinks {
    align-items: flex-start;
    display: flex;
    margin: 0 -1.5rem
  }
  .LoggedInLinks > * { flex: 1 }
  .LoggedInLinks > div:last-child { border-left: 1px solid var(--color-tint5) }
  .LoggedInLinks [data-reach-menu-item],
  .LoggedInLinks [data-selected] {
    background: var(--color-tint7);
    color: var(--color-tint1);
    display: block;
    flex: 1;
    font-size: 0.875rem;
    line-height: 1;
    padding: 0.75rem;
    text-align: center;
  }

  /* NotificationBell */
  .NotificationBell--has-notifications {
    position: relative;
  }

  .Navigation .nav-icon {
    width: 24px;
    height: 24px;
  }

  @media screen and (pointer: fine) {
    .Navigation .nav-icon {
      width: 20px;
      height: 20px;
    }
  }

  .condensed-header .Navigation .nav-icon {
    width: 20px;
    height: 20px;
  }

  .AltNavigation .nav-icon {
    width: 24px;
    height: 24px;
  }

  .NotificationBell--has-notifications:after {
    background-color: var(--color-ruby);
    border-radius: 100%;
    border: 1px solid var(--color-tint10);
    content: "";
    position: absolute;
    height: 7px;
    right: 0;
    top: 4px;
    width: 7px;
  }

  /* utility */
  .display-flex { display: flex }
  .align-items-center { align-items: center }
  .justify-content-space-between { justify-content: space-between }
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  /* Chat Components */
  .ChatButton {
    appearance: none;
    background: none;
    border: none;
    color: var(--color-tint2);
    cursor: pointer;
    padding: 0;
    position: relative;
  }

  .ChatButton.is-open {
    color: var(--color-tint1);
  }

  .ChatButton--unread:after {
    background-color: var(--color-ruby);
    border-radius: 100%;
    border: 1px solid var(--color-tint10);
    content: "";
    position: absolute;
    height: 7px;
    right: -3px;
    top: 2px;
    width: 7px;
  }
`;return a("style",{children:e})}V.propTypes={as:c.any};function V({as:e="a",...t}){return a(e,{...t})}Ee.propTypes={notificationCount:c.number.isRequired,notificationLink:c.object.isRequired};function Ee({notificationCount:e,notificationLink:t}){return a(V,{...t,className:`Navigation__link NotificationBell ${e>0&&"NotificationBell--has-notifications"}`,children:a("span",{children:a(Zt,{notificationCount:e})})})}Zt.propTypes={notificationCount:c.number.isRequired};function Zt({notificationCount:e}){return a(it.Symbol,{symbol:`${Sa}#notification`,className:"p-r nav-icon","aria-label":`${e} notifications`})}function Nr({style:e={}}){return p("svg",{className:"symbol",role:"img",title:"down-chevron icon",style:e,children:[p("symbol",{xmlns:"http://www.w3.org/2000/svg",id:"Navigation-svg-symbol-down-chevron",viewBox:"0 0 16 16",children:[a("title",{children:"down-chevron"}),a("polygon",{points:"8.003 14.068 0.005 6.07 1.782 4.293 8.003 10.514 14.223 4.293 16 6.07 8.003 14.068"})]}),a("use",{href:"#Navigation-svg-symbol-down-chevron"})]})}en.propTypes={displayName:c.string,imageUrl:c.string.isRequired};function en({displayName:e,imageUrl:t}){const n=`
    .Navigation-avatar {
      border-radius: 100%;
      height: ${Je}px;
      width: ${le}px;
      min-width: ${le}px;
    }

    @media screen and (pointer:fine) {
      .Navigation-avatar {
        height: 24px;
        width: 24px;
        min-width: 24px;
      }
    }
  `;return p("div",{children:[a("style",{children:n}),a("img",{className:"Navigation-avatar d-b",width:le,height:Je,alt:`${e}'s avatar`,src:t})]})}De.propTypes={unread:c.bool.isRequired};function De({unread:e}){const{toggleDrawer:t,isOpen:n,pcoChatEnabled:o}=Se();return o?p("button",{className:`ChatButton ${n?"is-open":""} ${e?"ChatButton--unread":""}`,onClick:t,"aria-expanded":n,"aria-label":`${e?"New messages in chat":"Chat"}`,"aria-controls":"chat-drawer",title:`${e?"New messages in chat":"Chat"}`,children:[a(Rr,{}),e&&a("span",{className:"sr-only",children:"New messages available"})]}):null}function Rr(){return a(it.Symbol,{symbol:`${Ze}#text-message`,className:"p-r nav-icon","aria-hidden":"true"})}const tn="header:notificationCount",nn="header:chatPerson";function Mi(){B(tn),B(nn)}function Sr({personIdentified:e,notificationsChannel:t,notificationDelay:n=1e3}){const[o,i]=k.useState(0),[s,l]=te(tn,0);k.useEffect(()=>{if(!e)return;let h=!0,u=window.setTimeout(()=>{j.get("/notifications/v2/me/notifications?where[read_at]=&per_page=0").then(m=>h&&l(m.meta.total_count)).catch(()=>l(null))},n);return()=>{h=!1,window.clearTimeout(u)}},[e,o,n]);const d=k.useCallback(()=>i(h=>h+1),[i]);return k.useEffect(()=>{if(!t||!e)return;const u=["notifications.church_center.v2.events.notification.updated","notifications.church_center.v2.events.notification.created","notifications.church_center.v2.events.notification.destroyed"].map(m=>t.bind(m,d));return()=>u.forEach(m=>m())},[t,e]),s}function Tr({channel:e,personId:t,personIdentified:n,delay:o=1e3}){const[i,s]=k.useState(0),[l,d]=te(nn,{can_chat_pending_age_check:!1,unread_messages:!1});k.useEffect(()=>{if(!n)return;let u=!0,m=window.setTimeout(()=>{j.get("/chat/v2/me?fields[Person]=can_chat_pending_age_check,unread_messages").then(f=>u&&d({can_chat_pending_age_check:f.data.attributes.can_chat_pending_age_check,unread_messages:f.data.attributes.unread_messages})).catch(()=>d({can_chat_pending_age_check:!1,unread_messages:!1}))},o);return()=>{u=!1,window.clearTimeout(m)}},[n,i,o]);const h=k.useCallback(()=>s(u=>u+1),[s]);return k.useEffect(()=>{if(!e||!n||!t)return;const m=e.bind("STREAM_USER_UPDATED",h);return()=>m()},[e,n,t]),{chatUnread:l.unread_messages,pcoChatEnabled:l.can_chat_pending_age_check}}function ae({href:e,...t}){e.startsWith(window.origin)&&(e=e.replace(window.origin,""));const n=e.startsWith("/"),o=e;return n?{as:Ta,key:o,to:e,...t}:{as:"a",key:o,href:e,target:"_blank",rel:"noopener noreferrer",...t}}const Er={LG:960,MD:720,SM:600,XS:480},Bi=()=>r.useContext(Bt);function Dr(){const[e,t]=jt(),{currentOrganization:n}=r.useContext(P),o=!!n.attributes.dark_mode_avatar_url,s=z().pathname==="/login";r.useEffect(()=>{if(e==="initialRender"){const h=window.setTimeout(()=>t(!0),100);return()=>window.clearTimeout(h)}},[e,t]);const l=e===!0?"1.0":"0.0",d=r.useMemo(()=>({opacity:l,transition:"opacity 0.4s ease",[`@media screen and (max-width: ${Er.LG-1}px)`]:{".sermon-episode-layout &":{display:"none"}},...o&&{'[data-color-scheme="dark"][data-contrast="low"] & .Header__org-avatar':{backgroundColor:"transparent"}},...s&&{".Header__org-wrapper":{display:"none"},".Header__layout":{justifyContent:"center"}}}),[l,o,s]);return a("div",{css:d,children:a(Qt,{...Ir()})})}function Ir(){const{search:e,pathname:t}=z(),{currentOrganization:n,draftMenu:o,draftMode:i,publishedMenu:s}=r.useContext(P),{data:l,meta:{authenticated:d}}=J(!1),h=No(),u=Ro(),m=gt(),f=de(i?o:s),{foregroundColor:v,backgroundColor:b}=ft({isHeader:!0}),w=n.attributes.name,N=n.attributes.avatar_url,D=n.attributes.dark_mode_avatar_url,C=m==="dark"&&D?D:N,Y=l.attributes.first_name,U=l.attributes.avatar_url+`?g=120x120%23&background_color=${b}&color=${v}&theme=${m}`,E=t.startsWith("/notifications")?0:1e3,g=Sr({personIdentified:d,notificationsChannel:h,notificationDelay:E}),{chatUnread:S,pcoChatEnabled:_}=Tr({personIdentified:d,personId:l.id,channel:u,delay:1e3}),I=["/profile","/logout","/login"],T=f.filter(({href:yn})=>!I.includes(yn)).map(ae),M=new URLSearchParams(e).get("return"),be=ae({href:t==="/login"&&!M?window.location.href:`/login?return=${M||window.location.href}`,children:"Log in"}),fn=ae({href:"/"}),bn=ae({href:"/notifications"}),vn=ae({href:"/me"});return{links:T,loginLink:be,myChurchCenterLink:vn,notificationCount:g,notificationLink:bn,organizationDisplayName:w,organizationImageUrl:C,organizationLink:fn,pcoChatEnabled:_,personDisplayName:Y,personIdentified:d,personImageUrl:U,chatUnread:S}}function Lr(){return()=>{}}function $r(){return r.useSyncExternalStore(Lr,()=>!0,()=>!1)}Pr.propTypes={children:c.node.isRequired};function an(){return $r()&&!!window.ReactNativeWebView}function Ie(){const{search:e}=z(),t=an();return e.includes("source=cca")||t}window.setForceTheme=e=>{window.forceTheme=e};function Ar(){const e="(prefers-color-scheme: dark)",t=r.useContext(P).features,[n]=rr({theme:null}),[o,i]=te("ChurchCenterTheme",null);let s,l;const d=an();d?(s=!1,l=window.forceTheme||"light"):t.ROLLOUT_dark_mode&&o?(s=!1,l=o||"light"):(s=!1,l="light");const[h,u]=r.useState(l),m=o||h;r.useEffect(()=>{n.theme!==null&&i(n.theme)},[n.theme]),r.useEffect(()=>{d&&(window.setForceTheme=u)},[d,u]),r.useEffect(()=>{if(!s)return;const v=window.matchMedia(e),b=w=>u(w.matches?"dark":"light");return v.addEventListener("change",b),()=>v.removeEventListener("change",b)},[s,u]);const f=r.useMemo(()=>{switch(m){case"dark-low":case"dark":return"dark";default:return"light"}},[m]);return r.useEffect(()=>{document.body.setAttribute("data-color-scheme",f),document.body.setAttribute("data-contrast","low"),document.body.setAttribute("data-background-color","")},[f]),f}function Pr({children:e}){const{flash:t}=r.useContext(pe),{error:n}=t,[o,i]=cr(),s=Ot(),l=Ar(),d=Ie();return a(re.Provider,{value:[o,i,l],children:a(tr,{children:p(Nt,{children:[a(So,{}),a(Ft,{children:a(Go,{children:a(Za,{children:p(ui,{children:[a(sr,{}),a(or,{}),p(on,{layoutWidth:o.layoutWidth,children:[a(ar,{}),a(hi,{}),a(Zo,{}),!s&&!d&&a(Dr,{}),!d&&a(eo,{}),a(rn,{id:"main_page_content",role:"main",className:A("f-1",{"page-content":!s,"pb-0":!o.footerVisible}),children:p("div",{className:`f-1 container container--${o.layoutWidth}`,children:[n&&a(ke,{className:"mb-3",children:n}),s?a(r.Suspense,{fallback:a(ne,{}),children:e}):a(kt,{children:a(r.Suspense,{fallback:a(ne,{}),children:e})})]})}),!d&&a(Ko,{}),!s&&!d&&a(Mr,{})]})]})})})})]})})})}function on({layoutWidth:e="",children:t}){return a("div",{className:`page-container d-f fd-c ${e}`,children:t})}on.propTypes={layoutWidth:c.string,children:c.node};function Mr(){const[e]=lr(),{layout:t}=r.useContext(pe),{organization_contact_email:n,organization_contact_phone:o,organization_name:i}=t;return e?p("footer",{className:"site-footer",role:"contentinfo",children:[p("ul",{className:"site-footer__links o-2 o-1@sm",children:[a("li",{className:"site-footer__link",children:a("a",{className:"c-tint2",href:"https://planning.center/terms/",rel:"noopener noreferrer",target:"_blank",children:"Terms of Service"})}),a("li",{className:"site-footer__link",children:a("a",{className:"c-tint2",href:"https://planning.center/privacy/",rel:"noopener noreferrer",target:"_blank",children:"Privacy Policy"})})]}),p("ul",{className:"site-footer__links o-1 o-2@sm",children:[a("li",{className:"site-footer__link",children:i}),n&&a("li",{className:"site-footer__link",children:a("a",{className:"fw-400 c-tint2",href:`mailto:${n}`,children:n})}),o&&a("li",{className:"site-footer__link",children:a("a",{className:"fw-400 c-tint2",href:`tel:${o}`,children:o})})]}),a(Jo,{})]}):null}function rn({children:e,...t}){const n=r.useRef(null),o=Ot();return r.useEffect(()=>{if(!o||!n.current||!window.ResizeObserver)return;const i=new ResizeObserver(()=>{const s=n.current.querySelector(".container"),l=s?s.scrollHeight:Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);window.parent.postMessage({pageHeight:l},"*")});return i.observe(n.current),()=>i.disconnect()},[o]),a("div",{ref:n,...t,children:e})}rn.propTypes={children:c.node};function fe(e){const[t,n]=r.useContext(re),o=r.useCallback(i=>{n({type:"setLayoutWidth",payload:i})},[n]);r.useLayoutEffect(()=>(o(e),()=>{o(null)}),[e,o])}fe.propTypes={width:c.oneOf(["fullscreen","wide","sermon-episode-layout","narrow"]).isRequired};const Br=({children:e})=>(fe("fullscreen"),a(O,{children:e}));Br.propTypes={children:c.node.isRequired};const Fr=({children:e})=>(fe("wide"),a(O,{children:e}));Fr.propTypes={children:c.node.isRequired};const Hr=({children:e})=>(fe("sermon-episode-layout"),a(O,{children:e}));Hr.propTypes={children:c.node.isRequired};const sn=({children:e})=>a(O,{children:e});sn.propTypes={children:c.node.isRequired};function Fi(){const{meta:{authenticated:e}}=J(!1),t=`/login?return=${window.location.href}`;return a(sn,{children:p("div",{className:"ta-c",children:[a("div",{css:Xe.iconCircleBackground,children:a("div",{css:Xe.icon,children:a($,{symbol:"general#lock","aria-label":"forbidden"})})}),a(Q,{level:1,text:"You don't have access"}),!e&&p("p",{className:"mt-1",children:["Do you need to ",a(_e,{to:t,children:"log in"}),"?"]})]})})}const Xe={iconCircleBackground:x`
    background-image: linear-gradient(
      135deg,
      ${ve.brandGradientStart} 0%,
      ${ve.brandGradientEnd} 100%
    );
    border-radius: 100%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 64px;
    margin-bottom: 1.5rem;
    position: relative;
    text-align: center;
    width: 64px;

    &:before {
      background-color: white;
      border-radius: 100%;
      content: "";
      height: 58px;
      left: 3px;
      position: absolute;
      top: 3px;
      width: 58px;
    }
  `,icon:x`
    color: ${ve.brand};
    font-size: 32px;
    position: relative;
  `},X={base:["","rounded"],xs:["xs:rounded-none","xs:rounded"],sm:["sm:rounded-none","sm:rounded"],md:["md:rounded-none","md:rounded"],lg:["lg:rounded-none","lg:rounded"],xl:["xl:rounded-none","xl:rounded"]};function qr(e){const t=Array.isArray(e),n=t?e[0]:e,o=t?e[1]:void 0;return[n&&X.base[n?1:0],o?.xs!==void 0&&X.xs[o.xs?1:0],o?.sm!==void 0&&X.sm[o.sm?1:0],o?.md!==void 0&&X.md[o.md?1:0],o?.lg!==void 0&&X.lg[o.lg?1:0],o?.xl!==void 0&&X.xl[o.xl?1:0]]}const Or=({aspectRatio:e="auto",alt:t,rounded:n=!1,src:o})=>a("img",{alt:t,className:A("block","w-full",n&&qr(n)),src:o,style:{aspectRatio:e}});function jr({alt:e,src:t}){return a("div",{css:Wr.heroImageWrapper,children:a(Or,{rounded:[!1,{md:!0}],alt:e,src:t})})}jr.propTypes={alt:c.string,src:c.string};const Wr={heroImageWrapper:x`
    margin: -1rem -1.5rem 1rem;

    @media (min-width: 720px) {
      margin: 0;
      order: 2;
    }
  `};cn.propTypes={hasMore:c.bool,loadMore:c.func,loadMoreButtonText:c.string,loadingMore:c.bool,keepLoadingOnScroll:c.bool,children:c.node};function cn({hasMore:e,loadMore:t,loadMoreButtonText:n,loadingMore:o,keepLoadingOnScroll:i,children:s}){return p(O,{children:[a(Ea,{hasMore:i&&e,loadMore:t,loader:a(ne,{},"loading"),children:s}),!i&&a("div",{className:"d-f jc-c mt-3",children:a(Le,{loadingMore:o,hasMore:e,loadMoreButtonText:n,loadMore:t})})]})}Le.propTypes={loadingMore:c.bool,hasMore:c.bool,loadMoreButtonText:c.string,loadMore:c.func};function Le({loadingMore:e,hasMore:t,loadMoreButtonText:n,loadMore:o}){return e?a(ne,{},"loading"):t?a("button",{className:"btn",onClick:o,children:n}):null}cn.LoadingIndicator=Le;ne.propTypes={message:c.string};function ne({message:e="Loading"}){const[t,n]=r.useState(0);r.useEffect(()=>{const i=setTimeout(()=>n((t+1)%4),350);return()=>{clearTimeout(i)}},[t]),o.propTypes={visible:c.bool.isRequired};function o({visible:i}){return a("span",{style:{visibility:i?"visible":"hidden"},children:"."})}return a("div",{className:"d-f ai-c c-tint4 loading-wrapper",children:p("span",{className:"d-f f-1 jc-c",children:[e,a(o,{visible:t>0}),a(o,{visible:t>1}),a(o,{visible:t>2})]})})}function zr(){return a("div",{style:{display:"flex",flexDirection:"column",height:"calc(100vh)",justifyContent:"center"},children:a(ne,{})})}const Yr=["Backspace","Delete","Tab","Escape","Enter","ArrowLeft","ArrowRight","ArrowUp","ArrowDown","Home","End",".",","],Ur=({id:e,name:t,value:n="",min:o=0,max:i=1/0,step:s,onChange:l,onBlur:d,onKeyDown:h,className:u="text-input",placeholder:m,disabled:f=!1,required:v=!1,...b})=>a("input",{type:"number",inputMode:"decimal",id:e,name:t,min:o,max:i,step:s,value:n,onChange:C=>{l(C)},onBlur:C=>{d&&d(C)},onKeyDown:C=>{if(Yr.includes(C.key)){h&&h(C);return}if(C.ctrlKey||C.metaKey||C.altKey||C.shiftKey){h&&h(C);return}if(C.key==="-"&&C.target.value===""){h&&h(C);return}/^[0-9]$/.test(C.key)||C.preventDefault(),h&&h(C)},className:u,placeholder:m,disabled:f,required:v,...b});Ur.propTypes={id:y.string,name:y.string,value:y.oneOfType([y.string,y.number]),min:y.number,max:y.number,step:y.number,onChange:y.func.isRequired,onBlur:y.func,onKeyDown:y.func,className:y.string,placeholder:y.string,disabled:y.bool,required:y.bool};const Gr=({heading:e="Uh oh!",message:t,actions:n})=>p("div",{className:"container container--narrow ta-c",children:[a("img",{className:"error-img pt-2 pt-0@md",style:{maxWidth:"240px"},src:"/static/errors/cco-error.png",alt:"Error graphic"}),a("div",{className:"mt-3 mb-3",children:a(Q,{level:1,text:e})}),a("div",{className:"mt-3 mb-3",children:t}),n]});Gr.propTypes={heading:c.string,message:c.node.isRequired,actions:c.node.isRequired};function Vr(e,t){const{href:n,target:o}=e.target;n&&n.startsWith(window.origin)&&o!=="_blank"&&(e.preventDefault(),t(n.replace(window.origin,"")))}function Qr(e){const t=e.target.closest("a");t&&(e.preventDefault(),window.open(t.href,"_blank","noopener,noreferrer"))}Jr.propTypes={className:y.string,html:y.string.isRequired,styles:y.object,openLinksInNewTab:y.bool};function Jr({html:e,styles:t,className:n,openLinksInNewTab:o=!1}){const i=tt();function s(l){o?Qr(l):Vr(l,i)}return a("div",{css:t||Kr.htmlContent,className:n,"data-preformatted-content":"heading-scale:legacy-church-center",onClick:s,dangerouslySetInnerHTML:{__html:e}})}const ye=e=>`${Da.size(e)}px`,Kr={htmlContent:x`
    > *:not([data-section-header]) {
      max-width: 640px;
      margin-left: auto;
      margin-right: auto;
    }

    [data-block] {
      margin-bottom: ${ye(3)};
    }

    [data-text] {
      > div,
      > p {
        margin-bottom: 20px;
      }

      div:not(:has(div, p, iframe, h1, h2, h3, h4, h5, h6)) {
        margin-bottom: 20px;
      }
    }

    hr {
      height: 1px;
      border: none;
      background-color: var(--color-tint5);
      margin-bottom: 24px;
      display: block;
    }

    iframe {
      border: none;
      margin: 4px 0 24px;
    }

    iframe[src*="boxcast.tv"],
    iframe[src*="facebook.com"],
    iframe[src*="livestream.com"],
    iframe[src*="resi.io"],
    iframe[src*="vimeo.com"],
    iframe[src*="youtube.com"] {
      margin: 0 auto 24px;
      max-width: 640px;
      display: block;
      width: 100%;
      height: auto;
      aspect-ratio: 16/9;
    }

    pre {
      white-space: pre-wrap;
    }

    a {
      overflow-wrap: break-word;
      word-wrap: break-word;
      -ms-word-break: break-all;
      word-break: break-word;

      &:hover {
        text-decoration: underline;
      }
    }

    .attachment {
      margin: 0;

      .attachment__caption {
        text-align: center;
        padding-top: 8px;
        font-weight: 400;
        color: var(--color-tint2);
        font-size: 14px;
        font-style: italic;
      }

      a:hover .attachment__caption {
        text-decoration: none;
      }
    }

    .attachment-gallery {
      figure + figure,
      action-text-attachment ~ action-text-attachment .attachment {
        margin-top: 20px;
      }
    }

    img {
      display: block;
      margin: 0 auto;
      --image--border-radius: 0;
    }

    [data-image] {
      margin-bottom: 24px;
    }

    [data-text~="text-align:center"] {
      text-align: center;

      ol,
      ul {
        list-style-position: inside;
      }
    }

    [data-text~="text-align:right"] {
      text-align: right;

      ol,
      ul {
        list-style-position: inside;
      }
    }

    [data-section-header] {
      display: flex;
      margin-bottom: 24px;
      margin-left: -1.5em;
      margin-right: -1.5em;

      + [data-section-header] {
        margin-top: -24px;
      }

      + [data-section-header~="height:auto"] {
        margin-top: 0;
      }

      &:first-child {
        margin-top: -1.5em;
      }

      @media screen and (min-width: 720px) {
        margin-left: -2em;
        margin-right: -2em;

        &:first-child {
          margin-top: -2em;
        }
      }
    }

    [data-section-header~="height:regular"] {
      height: 300px;
    }

    [data-section-header~="height:tall"] {
      height: 500px;
    }

    [data-section-header--img] {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: ${ye(3)};
      margin-bottom: 0;
      background-image: var(--background-image-url);
      background-position: center center;
      background-repeat: no-repeat;
      background-size: cover;
    }

    [data-section-header--img~="false"] {
      padding: 0 ${ye(3)};
    }

    [data-section-header--callout] {
      max-width: 900px;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

      > * {
        max-width: 450px;
        width: 100%;
      }
    }

    [data-section-header--callout-button-wrap] {
      align-items: flex-start;
      display: flex;
      flex-direction: column;
      margin-bottom: 0;
    }

    [data-section-header--callout~="position:left"] {
      align-items: flex-start;
    }

    [data-section-header--callout~="position:right"] {
      align-items: flex-start;

      @media screen and (min-width: 720px) {
        align-items: flex-end;
      }
    }

    [data-section-header--callout~="position:center"] {
      [data-section-header--callout-text] {
        text-align: center;
      }
      [data-section-header--callout-button-wrap] {
        align-items: center;
      }
    }

    [data-section-header--callout~="position:right"] {
      [data-section-header--callout-text] {
        text-align: right;
      }
      [data-section-header--callout-button-wrap] {
        align-items: flex-end;
      }
    }

    [data-section-header--callout-text],
    [data-section-header--callout-button-wrap] {
      max-width: 450px;
    }

    [data-section-header--callout-text] {
      background: transparent;
      border: 0;
      margin: 0;
      font-size: 24px;
      line-height: 32px;
      font-weight: 600;
      overflow: hidden;
      resize: none;

      @media screen and (min-width: 600px) {
        font-weight: 500;
        font-size: 32px;
        line-height: 40px;
      }

      @media screen and (min-width: 960px) {
        font-size: 42px;
        line-height: 56px;
      }
    }

    [data-section-header--callout-text]
      + [data-section-header--callout-button-wrap] {
      margin-top: 16px;
    }

    [data-section-header--img="true"]
      [data-section-header--callout-text~="color:light"] {
      color: #fff;
    }

    [data-section-header--img="true"]
      [data-section-header--callout-text~="color:dark"] {
      color: #000;
      font-weight: 700;

      @media screen and (min-width: 600px) {
        font-weight: 600;
      }
    }

    [data-section-header--img="false"] [data-section-header--callout-text] {
      [data-color-scheme="light"] & {
        font-weight: 700;

        @media screen and (min-width: 600px) {
          font-weight: 600;
        }
      }
    }

    a[data-section-header--callout-button] {
      text-decoration: none;
    }

    [data-button-wrap],
    [data-giving] {
      display: flex;
      justify-content: center;
    }

    [data-giving] {
      gap: 16px;
      flex-wrap: wrap;
      > * {
        flex: 0 1 7ch;
        display: flex;
        flex-direction: column;
        align-items: stretch;
      }

      h2 {
        flex-basis: 100%;
        font-size: 30px;
        margin-bottom: -4px;
      }

      &[data-alignment="center"] {
        justify-content: center;

        h2 {
          text-align: center;
        }
      }

      &[data-alignment="left"] {
        justify-content: flex-start;

        h2 {
          text-align: left;
        }
      }

      &[data-alignment="right"] {
        justify-content: flex-end;

        h2 {
          text-align: right;
        }
      }
    }

    [data-button-wrap="position:center"] {
      justify-content: center;
    }

    [data-button-wrap="position:left"] {
      justify-content: flex-start;
    }

    [data-button-wrap="position:right"] {
      justify-content: flex-end;
    }

    [data-button] {
      border: none;
      padding: 0;
      background-color: transparent;

      a:hover {
        text-decoration: none;
      }
    }

    [data-contact],
    [data-social] {
      max-width: 640px;
      height: 48px;
      margin: 0 auto 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 32px;
    }

    [data-contact--item],
    [data-social--item] {
      display: flex;
      align-items: center;
      color: var(--color-tint3);
      text-decoration: none;
      font-weight: 400;
      gap: 8px;
    }

    [data-contact--item] .symbol {
      color: var(--color-tint3);
    }

    [data-social--item] .symbol {
      height: 2em;
      width: 2em;
    }

    [data-location--map] {
      height: auto;
      width: 100%;
      margin-bottom: 16px;
    }

    [data-location--meta] {
      display: flex;
      width: 100%;
      flex-direction: row;
      justify-content: space-between;
      align-items: flex-start;
    }

    [data-location--address] {
      line-height: 20px;
    }

    [data-location--address~="location-type:lat_long"] {
      white-space: pre-line;
    }

    [data-event-schedule] {
      max-width: 640px;
      margin: 0 auto 24px;
    }

    [data-event-schedule--dayname] {
      margin: 16px 0 6px;
      padding: 0;
      color: var(--heading-color);
      font-weight: 600;
    }

    [data-event-schedule--list] {
      list-style: none;
      margin: 0;
      padding: 0;
    }

    [data-event-schedule--list] li {
      display: flex;
      padding: 4px 0;
      color: var(--color-tint-1);
    }

    [data-event-schedule--start-time] {
      flex: 1;
      max-width: 100px;
      padding-right: 10px;
    }

    [data-event-schedule--name] {
      flex: 2;
      flex-grow: 1;
      padding-left: 10px;
    }

    [data-grid],
    [data-collection] {
      display: grid;
      grid-template-rows: auto;
      gap: 16px;
    }

    [data-grid][data-grid-layout-style="full"],
    [data-collection][data-collection-layout-style="full"] {
      gap: 0;

      @media screen and (max-width: 599px) {
        margin-inline: -24px;
      }
    }

    [data-grid-columns-mobile="3"],
    [data-collection-columns-mobile="3"] {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    [data-grid-columns-mobile="2"],
    [data-collection-columns-mobile="2"] {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    [data-grid-columns-mobile="1"],
    [data-collection-columns-mobile="1"] {
      grid-template-columns: 1fr;
    }

    @media screen and (min-width: 600px) {
      [data-grid-columns-desktop="3"],
      [data-collection-columns-desktop="3"] {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }

      [data-grid-columns-desktop="2"],
      [data-collection-columns-desktop="2"] {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }

    [data-grid-image-constrain="true"] img,
    [data-collection-image-constrain="true"] img {
      object-fit: cover;
      aspect-ratio: 16 / 9;
    }

    [data-grid-image-scale-up="true"],
    [data-grid-image-scale-up="true"] img,
    [data-collection-image-scale-up="true"],
    [data-collection-image-scale-up="true"] img {
      width: 100%;
    }

    [data-grid-item],
    [data-collection-item] {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 12px;
    }

    [data-grid-item] :is(h2, p),
    [data-collection-item] :is(h2, p) {
      margin: 0;
    }

    [data-grid-item] h2,
    [data-collection-item] h2 {
      font-size: 21px;
      line-height: 1.2;
      margin: -4px 0;
      width: 100%;
      overflow-wrap: break-word;
    }

    [data-grid-item] p,
    [data-collection-item] p {
      margin: -2px 0;
      width: 100%;
      overflow-wrap: break-word;
    }

    [data-grid-alignment="left"] [data-grid-item],
    [data-collection-alignment="left"] [data-collection-item] {
      align-items: flex-start;
    }

    [data-grid-alignment="center"] [data-grid-item],
    [data-collection-alignment="center"] [data-collection-item] {
      align-items: center;
      > :is(h2, p) {
        text-align: center;
      }
    }

    [data-grid-alignment="right"] [data-grid-item],
    [data-collection-alignment="right"] [data-collection-item] {
      align-items: flex-end;
      > :is(h2, p) {
        text-align: right;
      }
    }

    [data-grid-item] .btn,
    [data-collection-item] .btn {
      white-space: pre;
    }
  `},$e=({width:e="100%",height:t="auto",aspectRatio:n=void 0,borderRadius:o=void 0})=>a("div",{css:[ni.skeleton,{width:e,height:t,aspectRatio:n,borderRadius:o}]}),Z=({width:e=void 0,height:t=void 0,aspectRatio:n=void 0})=>a($e,{width:e,height:t,aspectRatio:n}),Xr=({width:e,height:t="40px"})=>a($e,{width:e,height:t,borderRadius:"30px"}),Zr=({size:e})=>a($e,{aspectRatio:"1 / 1",borderRadius:"100%",width:e,height:e}),ei=()=>p("div",{className:"d-f fd-c g-1",children:[a(Z,{width:"100%"}),a(Z,{width:"80%"}),a(Z,{width:"100%"}),a(Z,{width:"90%"}),a(Z,{width:"50%"})]}),ti=st`
  100% {
    transform: translateX(100%);
  }
`,ni={skeleton:x`
    border-radius: 8px;
    position: relative;
    overflow: hidden;
    background-color: var(--color-tint6);
    width: 100%;
    min-height: 16px;
    display: block;
    &:after {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      transform: translateX(-100%);
      background-image: linear-gradient(
        90deg,
        hsla(0, 0%, 100%, 0),
        hsla(0, 0%, 100%, 0.2),
        hsla(0, 0%, 100%, 0.5),
        hsla(0, 0%, 100%, 0.2),
        hsla(0, 0%, 100%, 0)
      );
      animation: ${ti} 2s infinite;
      content: "";
    }
    [data-color-scheme="dark"] &:after {
      background-image: linear-gradient(
        90deg,
        hsla(0, 0%, 30%, 0),
        hsla(0, 0%, 30%, 0.2),
        hsla(0, 0%, 30%, 0.5),
        hsla(0, 0%, 30%, 0.2),
        hsla(0, 0%, 30%, 0)
      );
    }
  `},Hi=Object.assign(Z,{Button:Object.assign(Xr,{displayName:"Skeleton.Button"}),Circle:Object.assign(Zr,{displayName:"Skeleton.Circle"}),Paragraph:Object.assign(ei,{displayName:"Skeleton.Paragraph"})}),ai="data:image/svg+xml,%3csvg%20width='200px'%20height='200px'%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20100%20100'%20preserveAspectRatio='xMidYMid'%20style='background:%20none;'%3e%3ccircle%20cx='50'%20cy='50'%20fill='none'%20stroke='%23333'%20stroke-width='8'%20r='35'%20stroke-dasharray='164.93361431346415%2056.97787143782138'%20transform='rotate(6%2050%2050)'%3e%3canimateTransform%20attributeName='transform'%20type='rotate'%20calcMode='linear'%20values='0%2050%2050;360%2050%2050'%20keyTimes='0;1'%20dur='1s'%20begin='0s'%20repeatCount='indefinite'%3e%3c/animateTransform%3e%3c/circle%3e%3c/svg%3e";function oi({alt:e,opacity:t=1}){return a("img",{src:ai,alt:e,style:{height:"1em",width:"1em",position:"absolute",opacity:t}})}oi.propTypes={alt:c.string.isRequired,opacity:c.number};const ri=r.forwardRef(({autoComplete:e="on",disabled:t=!1,id:n,label:o="",name:i="",onChange:s,placeholder:l="",readOnly:d=void 0,required:h=!1,size:u="md",value:m},f)=>p(O,{children:[o&&p("label",{htmlFor:n,children:[o,h&&a("span",{className:"c-ruby",children:" *"})]}),a("input",{className:A("text-input",u==="sm"&&"sm-input",d&&"pe-n"),autoComplete:e,disabled:t,id:n,name:i||n,onChange:v=>typeof s=="function"&&s(v),placeholder:l,ref:f,readOnly:d,required:h,type:"text",value:m})]}));ri.displayName="TextInput";const ln=r.createContext(),ii=({children:e})=>{const[t,n]=r.useState([]),o=r.useCallback(s=>{n(l=>[{id:Ia(),...s},...l])},[n]),i=r.useCallback(s=>{n(l=>l.filter(d=>d.id!==s))},[n]);return p(ln.Provider,{value:{addToast:o,removeToast:i},children:[a(un,{toasts:t}),e]})};ii.propTypes={children:c.node};function si(){const e=r.useContext(ln);if(e===void 0)throw new Error("useToast must be used within a ToastProvider");return e}const ci={success:"general#check",info:"general#outlined-info-circle",warning:"general#exclamation-triangle",error:"general#exclamation-triangle"},dn=({id:e,message:t,type:n="info"})=>{const{removeToast:o}=si(),i=`var(--${n}-alert--text)`;return r.useEffect(()=>{const s=setTimeout(()=>{o(e)},6e3);return()=>{clearTimeout(s)}},[e,o]),p("div",{css:{padding:"1rem 4px 1rem 1rem",backgroundColor:i,color:"var(--color-tint9)",borderRadius:"4px",boxShadow:"0 8px 16px #0000001f",display:"grid",columnGap:"1rem",gridTemplateColumns:"14px 1fr 42px",animation:`${li} 6s forwards`},children:[a($,{css:{color:"var(--color-tint9)",marginTop:"4px"},symbol:ci[n]}),a("div",{children:t}),a(xt,{text:a($,{symbol:"general#x",css:{color:"var(--color-tint9)",opacity:"0.7"}}),variant:"naked",size:"sm",onClick:()=>o(e)})]})};dn.propTypes={id:c.string,message:c.string.isRequired,type:c.oneOf(["success","info","warning","error"]).isRequired};const un=({toasts:e})=>{const t=Ie(),n=t?"3%":"0";return a("div",{css:{position:"fixed",top:t?"0.75rem":"2rem",left:n,right:n,pointerEvents:"auto",maxWidth:"500px",margin:"auto",zIndex:1001,display:"flex",flexDirection:"column",gap:"1rem"},children:e.map(i=>a(dn,{...i},i.id))})};un.propTypes={toasts:c.node.isRequired};const li=st`
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  4%,
  96% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(0);
  }
`,qi=r.forwardRef(function({active:t,children:n,name:o,onClick:i,className:s,...l},d){return p("label",{...l,className:`p-r d-ib p-0${s?` ${s}`:""}`,css:x`
        cursor: pointer;
      `,ref:d,children:[a("input",{type:"radio",name:o,checked:t,onChange:()=>i?.(),className:"visually-hidden"}),a("span",{className:"btn text-btn w-100%@md",css:[xe.button,xe.buttonFocus,t&&xe.buttonActive],children:n})]})}),xe={button:x`
    background: var(--d-fill-color-chip);
    border: 1px solid var(--d-border-color-chip);
    border-radius: 1.5rem;
    color: var(--d-text-color-chip);
    padding-inline: 1rem;
  `,buttonActive:x`
    background: transparent;

    @supports (background: hsl(from white h s l)) {
      background: hsl(
        from var(--d-fill-color-chip-selected) h s
          var(--d-hsl-lightness-chip-selected)
      );
    }

    border-width: 2px;
    border-color: var(--d-border-color-chip-selected);
    color: var(--d-text-color-chip-selected);
    font-weight: 500;
  `,buttonFocus:x`
    input[type="radio"]:focus-visible + & {
      box-shadow:
        inset 0 0 0 1px var(--d-fill-color-neutral-100),
        inset 0 0 0 3px var(--d-focus-ring-color);
    }
  `};function di(){return r.useState(null)}const Ae=r.createContext([null,()=>{}]),ui=({children:e})=>{const t=di();return a(Ae.Provider,{value:t,children:e})},hi=()=>{const[e,t]=r.useContext(Ae);return e},Oi=({children:e})=>{const[t,n]=r.useContext(Ae);return r.useEffect(()=>(n(e),()=>n(null)),[e,n]),a(O,{})};function pi({onRestart:e}){return p("div",{className:"mx-8 my-4 ta-c",children:[a(ke,{children:"Something unexpected happened. Please try again."}),a("button",{className:"secondary-btn btn mb-3 mt-3",onClick:e,children:"Start over"})]})}const hn=r.createContext(null);function mi(){const e=r.useContext(hn);if(e===null)throw new Error("useBugsnagClient must be used within a Bugsnag Provider.");return e}const gi=['Could not load "util".',"null is not an object (evaluating 's.id')"],fi=e=>e.errors[0].stacktrace.some(function(t){return t.file&&t.file.indexOf("webkit-masked-url")!==-1});function bi(e){if(gi.includes(e.errors[0].errorMessage)||fi(e))return!1}const pn=La.createClient({apiKey:"9c8418b49ed77b0fd3e33d9334a32847",appVersion:"44832cadeb70b9f9cce00d120eb016ab3bda4c5a",enabledReleaseStages:["prototype","staging","production"],releaseStage:"production",user:{id:"anonymous"},onError:bi,plugins:[new $a(Aa)]}),vi=pn.getPlugin("react");mn.propTypes={children:c.node.isRequired};function mn({children:e}){const{Provider:t}=hn;return a(t,{value:pn,children:e})}function gn({fallback:e,...t}){function n({error:o,info:i}){return r.cloneElement(e,{error:o,info:i})}return a(vi,{FallbackComponent:n,...t})}gn.propTypes={fallback:c.node.isRequired};function yi({children:e}){const[t,n]=r.useState(0);function o(){t===0?n(1):window.location.reload()}function i(s){s.addMetadata("app",{errorBoundary:"BugsnagWrapper"})}return a(mn,{children:a(gn,{fallback:a(pi,{onRestart:o,onError:i}),children:e},t)})}yi.propTypes={children:c.node};export{Ii as $,za as A,yi as B,ho as C,gt as D,de as E,ae as F,Mi as G,Ti as H,$ as I,_i as J,Ai as K,cn as L,Br as M,sn as N,sr as O,Hi as P,Ie as Q,Jr as R,Hr as S,Li as T,Bi as U,rr as V,P as W,ro as X,go as Y,Oi as Z,Ct as _,Fr as a,No as a0,Or as a1,pn as a2,ri as a3,Uo as a4,G as a5,ue as a6,Ri as a7,Ao as a8,Pr as a9,zr as aa,vo as ab,Ni as ac,si as ad,ii as ae,qi as af,xe as ag,jr as ah,mo as ai,Pa as aj,Di as ak,Ur as al,Ho as am,me as an,Mt as ao,Fi as ap,fo as aq,$i as ar,ze as as,qa as at,ir as au,Xo as b,Ei as c,Ci as d,ee as e,to as f,no as g,ao as h,Q as i,ve as j,pe as k,yt as l,ne as m,ke as n,Ht as o,Er as p,mi as q,ki as r,ai as s,Gr as t,J as u,oi as v,Si as w,q as x,xt as y,Pi as z};
//# sourceMappingURL=Bugsnag-uqthnw8J.js.map
