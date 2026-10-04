import{r as a,v as m,b as i,A as I,ab as Be,H as Ve,aL as wr,aN as Ge,bi as xr,bf as Er,ae as Cr,j as f,bj as Tr,F as k,b3 as Sr,k as S,P as h,x as ee,bk as Nr,e as ze,b1 as Rr,D as Z,W as Ae,an as Le,Z as We,$ as kr,q as He,s as Ye,p as Ke,w as Ir,f as Ar,o as Lr,aO as Pr}from"./vendor-CPMdfHCh.js";import{an as Je,u as U,m as Ee,j as ue,V as Xe,i as L,I as P,Q as te,U as pe,p as he,ao as jr,k as Dr,x as se,b as $r,q as Mr,O as Fr,f as Or,g as Pe,h as qr}from"./Bugsnag-uqthnw8J.js";import{e as Qe,c as je}from"./routes-Nyzx--Ux.js";import{j as Ur,a as Ze}from"./queries-BgMR0Pci.js";import{u as Br}from"./useNotifyNativeLoaded-CAbwnrpo.js";import{u as Vr}from"./useLocalStorage-BMP7gFuX.js";import{u as Gr}from"./useMobileDetect-CY4JiwyK.js";import{u as me,a as zr,b as Y}from"./SessionApiResource-BS2aBwQ1.js";import{a as Wr,i as De,c as O,C as Hr}from"./index-A_slZ1CV.js";import{g as Yr}from"./getRelationship-BEK6WIgv.js";import{l as Kr,u as Jr,N as et,b as tt}from"./Notes-CaWIogfU.js";import"./styles-FVDiVcL8.js";import{S as Xr}from"./Subheading-GKFQH-Je.js";import{A as Qr}from"./AudioPlayerControls-BQLknXSK.js";import{L as Zr}from"./Channel-BUgHe8b4.js";import{D as ei}from"./DatetimeFmt-HavA5_TF.js";import{N as ti}from"./NativeHeader-BdWIPdgm.js";import"./RootErrorBoundaryLayout-Cp1Yeyt8.js";import"./Error404-Vj-ClAYf.js";import"./isFirstAttemptForPathname-Brb7p_u3.js";import"./useInfiniteLoadingResource-qBtaqEdA.js";import"./useUpdateEffect-V5RRWpo2.js";import"./Alert-BDgki9Zc.js";import"./trackPendoEvent-dx1IV-g0.js";import"./index-DywPu5by.js";import"./BridgeAlertModalProvider-_ZmlR2cH.js";import"./Modal-DKWffXDr.js";import"./MediaThumbnail-DCkIAfbz.js";const rt=a.createContext(),$e="UNKNOWN",it="INGEST_ELEMENT",nt="INGEST_ELEMENTS",st="REMOVE_ELEMENT",at="SET_CURRENT_TOPIC_ID",ri={data:[],currentTopicId:void 0,included:[],nextLink:void 0};function ot(e){return Ve(e,({type:t,id:r})=>`${t}-${r}`)}function Me(e){return Be(ot(e),t=>-Date.parse(t.attributes.last_replied_at))}function ii(e,t){switch(t.type){case nt:{const r=t.payload;let n=Me([...r.data,...e.data]);return{...e,data:n,included:[...r.included,...e.included],nextLink:r.links.next}}case it:{const r=t.payload;let n=Me([r.data,...e.data]),s=ot([...r.included,...e.included]);return{...e,data:n,included:s}}case st:return{...e,data:e.data.filter(r=>r.id!==t.payload.id)};case at:return{...e,currentTopicId:t.payload.id};default:throw new Error(`Unrecognized action: ${t.type}`)}}function lt({children:e}){const t=a.useContext(Wr),[r,n]=a.useReducer(ii,ri),s=u=>n({type:nt,payload:u}),o=async u=>{const{groupId:l,topicId:p}=ni(u);if(l!==t.id)return;const g=await I.get(`/groups/v2/me/groups/${l}/forum_topics?filter=not_for_sermon&where[id]=${p}&include=author,my_reaction,most_recent_reply,most_recent_reply.author`);if(g.meta.total_count===0)return;const b={...g,data:g.data[0]};return n({type:it,payload:b})},c=u=>n({type:st,payload:{id:u}}),d=u=>n({type:at,payload:{id:u}});return i(rt.Provider,{value:{ingestMany:s,ingest:o,del:c,currentTopic:r.data.find(({id:u})=>u===r.currentTopicId),setCurrentTopicId:d,group:t,groupId:t.id,...r},children:e})}lt.propTypes={children:m.oneOfType([m.arrayOf(m.node),m.node]).isRequired};function ni(e){switch(e.data.type){case"Topic":return{groupId:e.data.relationships.group.data.id,topicId:e.data.id};case"Reply":return{groupId:e.data.relationships.group.data.id,topicId:e.data.relationships.topic.data.id};default:return{topicId:$e,groupId:$e}}}function si(e,t){const r=Object.keys(e),n=Object.keys(t),s=wr([...r,...n]),[o,c]=Ge(s,l=>r.includes(l)&&n.includes(l)),d=c.reduce((l,p)=>({...l,[p]:e[p]||t[p]}),{}),u=o.reduce((l,p)=>({...l,[p]:ai(e[p],t[p])}),{});return{...d,...u}}function ai(e,t){return{...e,...t,attributes:{...e.attributes,...t.attributes,name:e.attributes.name||t.attributes.name,avatar_url:oi(e.attributes.avatar_url,t.attributes.avatar_url)}}}function oi(e,t){return ct(e)?e:t}function ct(e){try{const{pathname:t}=new URL(e);return!li(t)&&!ci(t)}catch{return!1}}function li(e){return/\/uploads\/initials.*/.test(e)}function ci(e){return/\/static\/avatar-generic.*/.test(e)}const G=a.createContext(),fe="INGEST",dt="REMOVE",ut="SET_LEADERS",pt="SET_MEMBER_ATTRS";function di(e,t,r){const n=`/groups/v2/me/groups/${e}/forum_topics/${t}/replies/${r}?include=author,my_reaction`;return I.get(n)}function ui(e,t){return e.pending?t.find(r=>r.attributes.message===e.attributes.message&&e.id!=r.id):!1}function pi(e){return Kr(e).replace(/^<p>/,`<p data-uuid="${Math.random().toString(36)}">`)}const hi={replies:[],authors:{},leaderIds:[],hasMore:!1,totalCount:void 0};function mi(e,t){switch(t.type){case fe:{const{json:r}=t.payload,n=r.included.filter(({type:u})=>u==="Author").reduce((u,l)=>({...u,[l.id]:l}),{}),s=r.included.filter(({type:u})=>u==="Reaction"),o=[r.data].flat(),c=Er(u=>u.map(l=>({...l,myReaction:l.myReaction||Yr({data:l,included:s},"my_reaction")})),u=>Ve(u,l=>l.id),u=>Be(u,l=>[l.pending,l.attributes.created_at]),u=>Cr(u,l=>ui(l,o)))(o.concat(e.replies)),d=r.meta?.human_authored_replies?.count||e.totalCount;return{...e,replies:c,authors:si(e.authors,n),hasMore:Array.isArray(r.data)?!!r.links.next:e.hasMore,totalCount:d}}case dt:{const{id:r}=t.payload;return{...e,replies:e.replies.filter(n=>n.id!==r),totalCount:e.replies.find(n=>n.id===r)?e.totalCount-1:e.totalCount}}case ut:{const{leaderIds:r}=t.payload;return{...e,leaderIds:r}}case pt:{const{personIdsToAttributes:r}=t.payload,n=xr(e.authors,r,(s,o)=>({...s,attributes:{...s.attributes,...o}}));return{...e,authors:n}}default:throw new Error(`Unrecognized action: ${t.type}`)}}const ht="ADD_AUTHOR_IDS",mt="SET_FETCHING_IDS",ft="SET_FETCHED_IDS";function fi(e,t){switch(t.type){case ht:{const{ids:r,value:n}=t.payload;return r.reduce((s,o)=>({...s,[o]:n}),{...e})}case mt:{const{ids:r}=t.payload;return r.reduce((n,s)=>({...n,[s]:"fetching"}),{...e})}case ft:{const{ids:r}=t.payload;return r.reduce((n,s)=>({...n,[s]:"fetched"}),{...e})}default:throw new Error(`Unrecognized action: ${t.type}`)}}function bi(e,t,r){const[n,s]=a.useReducer(fi,{}),o=Object.keys(t),c=Object.keys(n),d=o.filter(l=>!c.includes(l)),u=c.reduce((l,p)=>n[p]==="unfetched"?[...l,p]:l,[]);if(d.length>0){const l=d.some(p=>ct(t[p]?.attributes?.avatar_url));s({type:ht,payload:{ids:d,value:l?"fetched":"unfetched"}})}return a.useEffect(()=>{if(u.length>0){const l=[...u];s({type:mt,payload:{ids:l}}),I.get(`/groups/v2/me/groups/${e.id}/memberships?where[person_id]=${l.join(",")}&filter=phantom`).then(p=>p.data.reduce((g,b)=>({...g,[b.relationships.person.data.id]:{name:`${b.attributes.first_name} ${b.attributes.last_name}`,avatar_url:b.attributes.avatar_url}}),{})).then(p=>{s({type:ft,payload:{ids:l}}),r(p)})}}),n}const bt=({children:e,...t})=>{const{currentTopic:r,group:n}=a.useContext(rt),[s,o]=a.useReducer(mi,{...hi,totalCount:r?.attributes?.human_authored_replies?.count}),c=bi(n,s.authors,b=>o({type:pt,payload:{personIdsToAttributes:b}})),d=a.useCallback(b=>{o({type:fe,payload:{json:b}})},[]),u=b=>o({type:dt,payload:{id:b}}),l=a.useCallback(b=>o({type:ut,payload:{leaderIds:b}}),[]),p=b=>{const y=b.data.relationships.message.data;di(n.id,r.id,y.id).then(E=>{o({type:fe,payload:{json:E}})})},g={...s,authors:Object.keys(s.authors).reduce((b,y)=>({...b,[y]:{...s.authors[y],knownBestAvatarUrl:c[y]==="fetched"}}),{})};return i(G.Provider,{value:{injected:t,ingest:d,del:u,react:p,setLeaders:l,...g},children:e})};bt.propTypes={children:m.node.isRequired};gt.propTypes={repliesFilter:m.shape({queryParamFilter:m.string})};function gt({repliesFilter:e={queryParamFilter:"all_people"}}){let{ingest:t,setLeaders:r,injected:{group:n,topic:s}}=a.useContext(G),[o,c]=(function(){const l=`/groups/v2/me/groups/${n.id}/forum_topics/${s.id}/replies?filter=${e.queryParamFilter}&include=author,my_reaction&per_page=50`;return[me(l),zr(l)]})(),d=(function(){let l=me(`/groups/v2/me/groups/${n.id}/memberships?filter=phantom&where[role]=leader`);return a.useMemo(()=>l.data.map(p=>p.relationships.person.data.id),[l])})();return a.useEffect(()=>{t(o),r(d)},[t,o,r,d]),a.useEffect(()=>()=>c(),[c]),null}function yt({children:e,dataContext:t,events:r,subscribeTo:n,fetchSubscribeTokenURL:s}){const{ingest:o,del:c,react:d}=a.useContext(t),u={ingest:a.useCallback(g=>o(g.data),[o]),remove:a.useCallback(g=>c(g.data.data.id),[c]),react:a.useCallback(g=>d(g.data),[d])},l=a.useCallback(async(g,b)=>(await I.post(s,{data:{attributes:{channel:g,connection_id:b}}})).data.id,[s]),p=Je(l,n);return a.useEffect(()=>{if(p)return p.bind("jolt.subscriptionStats",b=>console.log(`TODO: There are currently ${b.data.subscribers} subscribed chatters on this channel.`))},[p]),r.forEach(({event:g,func:b})=>{a.useEffect(()=>{if(p)return p.bind(g,u[b])},[p])}),e}yt.propTypes={children:m.node.isRequired,events:m.arrayOf(m.exact({event:m.string.isRequired,func:m.string.isRequired})).isRequired,fetchSubscribeTokenURL:m.string.isRequired,subscribeTo:m.string.isRequired};const gi="bot";vt.propTypes={group:m.object.isRequired,topic:m.object.isRequired,children:m.node.isRequired};function vt({group:e,topic:t,children:r}){if(U(!1).data.type!="VerifiedInSessionPerson")return i("div",{children:"Not logged in"});const s=`/groups/v2/me/groups/${e.id}/forum_topics/${t.id}/jolt_subscribe`,o=[{func:"ingest",event:"groups.church_center.v2.events.forum_reply.created"},{func:"ingest",event:"groups.church_center.v2.events.forum_reply.updated"},{func:"remove",event:"groups.church_center.v2.events.forum_reply.destroyed"},{func:"react",event:"groups.church_center.v2.events.forum_reply_reaction.created"},{func:"react",event:"groups.church_center.v2.events.forum_reply_reaction.updated"},{func:"react",event:"groups.church_center.v2.events.forum_reply_reaction.destroyed"}];return i(bt,{group:e,topic:t,children:f(yt,{dataContext:G,subscribeTo:`church_center.groups.messaging.topics.${t.id}`,fetchSubscribeTokenURL:s,events:o,children:[i(gt,{}),r]})})}function _t({groupId:e,topicId:t}){const[r,n]=a.useState(!1),{replies:s,ingest:o,hasMore:c}=a.useContext(G),d=a.useCallback(()=>{n(!0);let u=`/groups/v2/me/groups/${e}/forum_topics/${t}/replies?include=author,my_reaction&per_page=25&offset=${s.length}`;I.get(u).then(l=>o(l)).finally(()=>n(!1))},[s,e,t]);return c?r?i(Ee,{}):i("button",{className:"btn minor-compact-btn",onClick:d,style:{background:"none",padding:"8px",color:`${ue.brand}`},children:"View older replies..."}):null}_t.propTypes={groupId:De.isRequired,topicId:De.isRequired};wt.propTypes={RepliesChunk:m.elementType.isRequired,leaderLabel:m.string,repliesFilter:m.shape({func:m.func})};function wt({RepliesChunk:e,leaderLabel:t="Leader",repliesFilter:r={func:n=>!0}}){const[n]=Xe(),s=n.scroll!=="top",[o,c]=a.useState(s),{replies:d,authors:u,leaderIds:l,totalCount:p,injected:{group:g,topic:b}}=a.useContext(G),y=a.useRef(null),[E,w]=Tr(),{human_authored_replies:v,replies_enabled:_}=b.attributes,x=p||v.count;return a.useEffect(()=>{o&&y.current.scrollIntoView()},[d.length]),a.useEffect(()=>{if(E?.y?.total&&E?.y?.value){const T=E.y.total-E.y.value<100;T!=o&&c(T)}},[o,E?.y?.total,E?.y?.value]),f("div",{className:"messaging__reply-scroller",ref:w,children:[f("div",{className:"messaging__reply-wrapper",children:[f("div",{children:[i(_t,{groupId:g.id,topicId:b.id}),_?i(xt,{children:x}):i(L,{level:3,text:"Replies are turned off"})]}),d.filter(r.func).reduce(yi,[]).map(T=>{const C=be(T[0]),A=u[C],D=l.includes(A.id);return i(e,{chunk:T,author:u[C],leaderIds:l,leaderLabel:D?t:null},T[0].id)})]}),i("div",{ref:y})]})}function xt({children:e}){switch(e){case 0:return i(L,{level:3,text:"No replies"});case 1:return i(L,{level:3,text:"1 reply"});default:return i(L,{level:3,text:`${e} replies`})}}xt.propTypes={children:m.number.isRequired};function yi(e,t,r,n){const s=n[r-1];if(!s)return[...e,[t]];if(!(be(t)===be(s)))return[...e,[t]];const c=e.slice(0,e.length-1),d=e[e.length-1];return[...c,[...d,t]]}function be(e){return e.relationships.author.data.id}const ge="SET_TEXT",Et="ADD_FILE",Ct="REMOVE_FILE",Tt="RESET_FILES",ye="SET_IN_FLIGHT",St={text:"",files:[],inFlight:!1};function vi(e,t){switch(t.type){case ge:return{...e,text:t.payload};case Et:return{...e,files:[...e.files,t.payload]};case Ct:return{...e,files:e.files.filter(r=>r!==t.payload.file)};case Tt:return{...e,files:St.files};case ye:return{...e,inFlight:t.payload};default:throw new Error(`Unrecognized action: ${t.type}`)}}const K=a.createContext();F.propTypes={children:m.node.isRequired};function F({children:e}){const[{text:t,files:r,inFlight:n},s]=a.useReducer(vi,St),{data:o}=U(!1);let{ingest:c,injected:{group:d,topic:u}}=a.useContext(G),l=a.useRef(null);function p(v){return s({type:ge,payload:v})}function g(v){[...v.target.files].map(x=>{const T=new FileReader;T.onload=function(C){s({type:Et,payload:{file:x,img:C.target.result}})},T.readAsDataURL(x)})}function b(v){confirm("Are you sure you want to remove this attachment?")&&s({type:Ct,payload:v})}function y(v){return Promise.all(v.map(_=>new Promise((x,T)=>{I.uploadFile(_.file).then(({data:C})=>{x(C[0].id)}).catch(C=>T(C))})))}const E=!n&&(t.trim()!==""||r.length!==0);let w=function(){if(event.preventDefault(),!E)return;let v=pi(t);const _=`/groups/v2/me/groups/${d.id}/forum_topics/${u.id}/replies?include=author`;c(Fe(v,o,{pending:!0,hasFiles:r.length>0})),l.current.style.height="48px",s({type:ye,payload:!0}),y(r).then(x=>I.post(_,{data:{attributes:{message:v,files:x}}})).then(x=>c(x)).then(()=>s({type:Tt})).catch(()=>{c(Fe(v,o,{error:!0}))}).finally(()=>s({type:ye,payload:!1})),setTimeout(x=>s({type:ge,payload:""}),100),l.current.focus()};return i(K.Provider,{value:{addFiles:g,canSend:E,files:r,handleSubmit:w,inFlight:n,inputRef:l,removeFile:b,setText:p,text:t},children:i("div",{className:"action-drawer messaging__new-reply",children:e})})}F.Editor=Nt;F.AddFilesButton=Ei;F.SingleLineInput=_i;F.MultiLineInput=wi;F.FilePreviews=xi;function Nt({children:e}){const{handleSubmit:t}=a.useContext(K);return i("form",{onSubmit:t,className:"messaging__new-reply-form",children:i("div",{className:"messaging__new-reply-form-wrapper",children:e})})}Nt.propTypes={children:m.node.isRequired};function _i(){const{inputRef:e,text:t,setText:r,canSend:n}=a.useContext(K);return f(k,{children:[i("input",{ref:e,value:t,onChange:s=>r(s.target.value),className:"messaging__new-reply-input",style:{borderRadius:30,backgroundColor:"var(--color-tint10)",borderColor:"var(--color-tint6)",boxShadow:"inset 0 1px 2px var(--color-tint9)"},type:"text",placeholder:"Message this group"}),i("button",{type:"submit",className:"stripped-btn messaging__submit-new-reply messaging__form-btn","aria-label":"Submit message",disabled:!n,children:i(P,{symbol:n?"churchCenter#paper-plane":"churchCenter#paper-plane-o",className:n?"has-text":"no-text",style:{fill:n?"var(--color-brand)":"var(--color-tint3)"}})})]})}function wi(){const{inputRef:e,text:t,setText:r,canSend:n,handleSubmit:s}=a.useContext(K);function o(c){r(c.target.value),c.target.style.height="auto",c.target.style.height=c.target.scrollHeight+"px"}return f(k,{children:[i("textarea",{ref:e,value:t,onChange:o,onKeyPress:c=>{c.which===13&&!c.shiftKey&&s()},className:"messaging__new-reply-textarea",rows:1,style:{backgroundColor:"var(--color-tint10)",borderColor:"var(--color-tint6)",boxShadow:"inset 0 1px 2px var(--color-tint9)",minHeight:"50px",maxHeight:"30vh"},placeholder:"Message this group"}),i("button",{type:"submit",className:"stripped-btn messaging__submit-new-reply messaging__form-btn","aria-label":"Submit message",disabled:!n,children:i(P,{symbol:n?"churchCenter#paper-plane":"churchCenter#paper-plane-o",className:n?"has-text":"no-text",style:{fill:n?"var(--color-brand)":"var(--color-tint4)"}})})]})}function xi(){const{files:e,removeFile:t,inFlight:r}=a.useContext(K);return r||e.length===0?null:i("div",{className:"d-f messaging__file-preview-bar",children:e.map((n,s)=>i(Rt,{file:n,removeFile:t},s))})}function Rt({file:e,removeFile:t}){return f("div",{className:"p-r mr-2",children:[i("span",{className:"messaging__preview-image-container",children:e.img?i("img",{src:e.img,className:"messaging__preview-image",alt:e.file.name}):i(P,{symbol:"churchCenter#photos-o"})}),i("button",{className:"messaging__preview-remove",onClick:()=>t({file:e}),"aria-label":`Remove ${e.file.name}`,children:i(P,{symbol:"general#x"})})]})}Rt.propTypes={file:m.shape({id:m.string,img:m.string}).isRequired,removeFile:m.func.isRequired};function Ei(){const{addFiles:e}=a.useContext(K);return f("button",{className:"messaging__upload-btn messaging__form-btn stripped-btn","aria-label":"Upload a file to this messaging thread.",type:"button",children:[i("label",{htmlFor:"testUpload",css:{color:"var(--color-tint3)",cursor:"pointer",paddingBottom:0,"&:hover":{color:"var(--color-brand)"}},children:i(P,{symbol:"churchCenter#photos-o",style:{verticalAlign:"middle",fontSize:"20px"}})}),i("input",{id:"testUpload",type:"file",accept:"image/gif, image/jpeg, image/png",multiple:"multiple",onChange:e,style:{display:"none"}})]})}function Fe(e,t,r){const n=new Date;return{data:{type:"Reply",id:Math.random().toString(36),attributes:{abilities:{can_update:!1,can_delete:!1},message:e,created_at:n,updated_at:n,expanded_links:{},reactions_summary:{reactions:[],total_count:0}},relationships:{author:{data:{type:"Author",id:t.id}},topic:{data:{type:"Topic",id:"1"}}},links:{},...r},included:[{type:"Author",id:t.id,attributes:{avatar_url:t.attributes.avatar_url,name:t.attributes.name,status:"active"}}]}}function Ci({height:e,width:t},r){return!e||!t?{height:r,width:r}:e>t?{height:r,width:Math.floor(t/e*r)}:{width:r,height:Math.floor(e/t*r)}}function kt({reply:e}){let{files:t}=e.attributes;return t?i(k,{children:t.map(r=>i("div",{children:i(It,{reply:e,file:r})},r.identifier))}):null}kt.propTypes={reply:O.isRequired};const ve=200;function It({reply:e,file:t}){let{width:r,height:n}=a.useMemo(()=>Ci(t,ve),[t]),s={borderRadius:12,margin:"0 -8px 8px",display:"block"};return i(a.Suspense,{fallback:i("div",{style:{width:r,height:n,...s}}),children:i(At,{file:t,reply:e,style:{width:r,height:n,...s}})})}It.propTypes={reply:O.isRequired,file:m.object.isRequired};function At({reply:e,file:t,style:r}){const[n,s]=a.useState(!1);let o=Y(`${e.links.self}/generate_file_link`,{data:{attributes:{identifier:t.identifier,thumb:`${ve}x${ve}`}}}).data?.attributes?.link;return o?f("button",{onClick:()=>s(!n),style:{cursor:"pointer",border:0,padding:0,background:"transparent"},children:[i("img",{src:o,alt:t.identifier,style:r}),n&&i(Lt,{reply:e,file:t})]}):null}At.propTypes={reply:O.isRequired,file:m.object.isRequired,style:m.object.isRequired};function Lt({reply:e,file:t}){let r=Y(`${e.links.self}/generate_file_link`,{data:{attributes:{identifier:t.identifier}}}).data?.attributes?.link;return i("div",{className:"modal--open",children:i("div",{className:"modal-layer",children:i("div",{className:"modal",style:{width:"auto",maxWidth:"800px",paddingTop:0},children:f("div",{className:"modal__body d-f jc-c",children:[i("button",{className:"modal__close-button","aria-label":"Close modal",style:{top:"1.5rem"},children:i(P,{symbol:"general#x"})}),i("img",{src:r,alt:t.identifier,style:{height:"100%",width:"100%"}})]})})})})}Lt.propTypes={reply:m.object.isRequired,file:m.object.isRequired};function Ti(e=""){return Sr.sanitize(e,{ALLOWED_TAGS:["p","a"]})}_e.propTypes={reply:O.isRequired,heading:m.node,leaderIds:m.arrayOf(m.string)};function _e({reply:e,heading:t,leaderIds:r}){const{data:n}=U(!1),{del:s}=a.useContext(G),[o,c]=a.useState(!1),d=n.id===e.relationships.author.data.id,u=r.includes(n.id),l=o&&(d||u)&&!e.pending,p=a.useCallback(function(){confirm("Are you sure you want to remove this message?")&&(s(e.id),I.del(e.links.self))},[e]);return f("div",{style:{opacity:e.pending?"0.5":"1",paddingTop:4,paddingBottom:4,backgroundColor:o?"rgba(0, 0, 0, 0.04)":null,position:"relative",borderRadius:"4px"},css:Ni.reply,onMouseEnter:()=>c(!0),onMouseLeave:()=>c(!1),children:[t,l&&i(Pt,{children:i("button",{className:"reply-action fs-3",onClick:p,children:i(P,{symbol:"publishing#trash"})})}),i(jt,{children:e.attributes.message}),i(kt,{reply:e}),i(Dt,{children:e.errors})]})}function Pt({children:e}){return i("div",{className:"reply-controls d-f ai-c jc-c",children:e})}Pt.propTypes={children:m.node.isRequired};function jt({children:e}){return Jr(e).trim().length===0?null:i("span",{dangerouslySetInnerHTML:{__html:Ti(e)}})}jt.propTypes={children:m.string.isRequired};function Dt({children:e}){return!e||e.length===0?null:i("div",{className:"reply-error d-f ai-c jc-c",children:Si(e)})}Dt.propTypes={children:m.node};function Si(e){return e.length>0?"This message couldn't be posted because you sent too many messages in a row, please try again in 10 seconds.":""}const Ni={reply:S`
    padding: 8px;

    .reply-controls {
      position: absolute;
      top: 0;
      right: 0;
      padding: 4px;
      height: 28px;
      width: 28px;
      border-radius: 3px;
      background: ${ue.tint1};
    }

    .reply-error {
      background-color: #ff9999;
      border: solid 1px red;
      border-radius: 5px;
      font-size: 0.7em;
      padding-left: 3px;
    }

    .reply-action {
      border-radius: 2px;
      border: 0;
      background: rgba(255, 255, 255, 0);
      margin: 0;
      padding: 0.2rem 0.25rem;
      color: ${ue.tint6};

      &:hover {
        background: rgba(255, 255, 255, 0.1);
      }
    }
    p {
      overflow: hidden;
      margin-bottom: 0;
      font-size: 0.865rem;
      line-height: 1.4;
      word-wrap: break-word;
      @media (min-width: 1200px) {
        line-height: 1.5;
        font-size: 0.9rem;
      }

      &[data-uuid] {
        margin-bottom: 0;
      }
    }
  `};function $t({children:e,badge:t}){return i("h4",{children:i("span",{className:"fs-5",children:e?f(k,{children:[i("span",{css:Oe.author,children:e}),t&&i("span",{className:"ml-4p xs-badge badge fw-400",css:Oe.authorBadge,children:t})]}):" "})})}$t.propTypes={children:m.node,badge:m.node};const Oe={author:S`
    color: var(--color-tint2);
  `,authorBadge:S`
    background-color: var(--color-tint2);
    color: var(--color-tint10);
  `};function Ri(e){return e?.relationships?.author?.data?.id!==gi}function Ce({group:e,topic:t,setGroupId:r,leaderLabel:n}){return i(Hr,{group:e,children:i(lt,{children:f(vt,{group:e,topic:t,children:[i(wt,{RepliesChunk:Mt,repliesFilter:{func:Ri,queryParamFilter:"human_authors"},leaderLabel:n}),f(F,{children:[i(Ft,{group:e,setGroupId:r}),i(F.Editor,{children:i(F.SingleLineInput,{})})]})]})})})}Ce.propTypes={group:O.isRequired,topic:O.isRequired,setGroupId:m.func,leaderLabel:m.string};function Mt({chunk:e,author:t,leaderIds:r,leaderLabel:n}){const[s,...o]=e;return f(k,{children:[s&&i(_e,{reply:s,author:t,leaderIds:r,heading:i($t,{badge:n,children:t.attributes.name})}),o.map(c=>i(_e,{reply:c,author:t,leaderIds:r},c.id))]})}Mt.propTypes={chunk:m.arrayOf(O).isRequired,author:O,leaderIds:m.arrayOf(m.string),leaderLabel:m.string};function Ft({group:e,setGroupId:t}){const{data:r}=U(!1);return f("div",{className:"p-4p d-f jc-sb ai-c",children:[i("span",{className:"fs-5 ai-c c-tint3",style:{whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",paddingRight:"1rem",maxWidth:"50%"},children:r&&r.attributes.name}),f("span",{onClick:()=>t(null),className:"fs-5 f-1 ta-r c-tint3",style:{position:"relative",paddingRight:"14px",cursor:"pointer",whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"},children:["Chatting with ",e.attributes.name,i(P,{symbol:"general#down-chevron",style:{fontSize:"10px",position:"absolute",right:"0",top:"3px"}})]})]})}Ft.propTypes={group:O,setGroupId:m.func.isRequired};Ot.propTypes={group:m.object,episode:m.object,episodeTime:m.object,setGroupId:m.func};function Ot({group:e,episode:t,episodeTime:r,setGroupId:n}){const s=Y(`/publishing/v2/episodes/${t.id}/episode_times/${r.id}/generate_topic_token`).data.id,o=Y(`/groups/v2/me/groups/${e.id}/topic_for_episode`,{data:{attributes:{token:s}}}).data;return i(Ce,{group:e,topic:o,setGroupId:n})}function ki({setGroupId:e,group:t}){return i("div",{className:"f-1 d-f jc-c ai-c ta-c",style:{padding:"12px"},children:f("div",{className:"p-2 d-f fd-c g-1",style:{maxWidth:"280px",background:"var(--color-tint8)",borderRadius:"5px"},children:[i(L,{level:4,size:5,text:`Group Messaging is not enabled for the ${t.attributes.name} group.`}),f("button",{className:"btn minor-compact-btn p-2",onClick:()=>e(null),children:[i(P,{symbol:"churchCenter#groups",className:"mr-1"}),"Switch To Another Group"]})]})})}qt.propTypes={episode:m.object,episodeTime:m.object,setGroupId:m.func};function qt({episode:e,episodeTime:t,setGroupId:r}){const n=Y(`/publishing/v2/episodes/${e.id}/episode_times/${t.id}/generate_topic_token`).data.id,s=Y("/groups/v2/topic_for_episode?include=group",{data:{attributes:{token:n}}}),o=s.data,c=s.included[0];return c.attributes.name="General Chat",i(Ce,{group:c,topic:o,setGroupId:r,leaderLabel:"Host"})}Ut.propTypes={episode:m.object,episodeTime:m.object,groupChatEnabled:m.bool,generalChatEnabled:m.bool};function Ut({episode:e,episodeTime:t,groupChatEnabled:r,generalChatEnabled:n}){let s=U(!1);const{isMobile:o}=Gr();return o&&t.attributes.streaming_service==="facebook"?i(Ii,{}):s.data.type!=="VerifiedInSessionPerson"?i(Gt,{generalChatEnabled:n}):i("div",{id:"panel-1",role:"tabpanel",tabIndex:"0","aria-labelledby":"tab-1",className:"set-focus-invisible tab-widget-wrapper",children:i(a.Suspense,{fallback:i(Ee,{}),children:i("div",{className:"tab-widget-content f-1",children:i(Bt,{episode:e,episodeTime:t,groupChatEnabled:r,generalChatEnabled:n})})})})}Bt.propTypes={episode:m.object,episodeTime:m.object,groupChatEnabled:m.bool,generalChatEnabled:m.bool};function Bt({episode:e,episodeTime:t,groupChatEnabled:r,generalChatEnabled:n}){const s=me("/groups/v2/me/groups"),c=`Sermons.Channel.${e.relationships.channel.data.id}.SelectedGroupId`,[d,u]=Vr(c),l=a.useMemo(()=>{if(s)return s.data.find(p=>p.id===d)},[d,s]);return a.useEffect(()=>{n&&!r&&u("general"),!n&&r&&d==="general"&&u(null)},[r,n]),l&&r?l.attributes.abilities.forum_topics.can_read?i(Ot,{group:l,episode:e,episodeTime:t,setGroupId:u}):i(ki,{group:l,setGroupId:u}):d==="general"&&n?i(qt,{episode:e,episodeTime:t,setGroupId:u}):i(Vt,{groups:s.data,setGroupId:u,groupChatEnabled:r,generalChatEnabled:n})}Vt.propTypes={groups:m.object,setGroupId:m.func,groupChatEnabled:m.bool,generalChatEnabled:m.bool};function Vt({groups:e,setGroupId:t,groupChatEnabled:r,generalChatEnabled:n}){return f("div",{className:"p-2 set-focus-invisible",children:[n&&i("div",{className:"mb-1",children:f("button",{onClick:()=>t("general"),className:"d-if ai-c",style:{border:"0",padding:"0",background:"transparent"},children:[i("img",{src:"/images/general-chat-placeholder-graphic.png",alt:"group",className:"d-f ai-c jc-c mr-2 fs-1",css:{width:"99px",height:"56px",borderRadius:"4px",backgroundColor:"var(--color-tint10)",color:"var(--color-tint5)"}}),i("span",{className:"fw-400 c-tint1",children:"General Chat"})]})}),r&&e.map(s=>i("div",{className:"mb-1",children:f("button",{onClick:()=>t(s.id),className:"d-if ai-c ta-l",style:{border:"0",padding:"0",background:"transparent"},children:[i("img",{src:s.attributes.header_image.medium,alt:"group",className:"d-f ai-c jc-c mr-2 fs-1",css:{width:"99px",height:"56px",borderRadius:"4px",backgroundColor:"var(--color-tint10)",color:"var(--color-tint5)"}}),i("span",{className:"fw-400",css:{color:"var(--color-tint1)"},children:s.attributes.name})]})},s.id))]})}Gt.propTypes={generalChatEnabled:m.bool.isRequired};function Gt({generalChatEnabled:e}){return f("section",{className:"action-drawer ta-c d-f ai-c jc-c fd-c g-1",css:{height:"calc(100% - 32px)",width:"100%"},children:[e?i(L,{level:2,size:3,text:"Log in to chat live."}):f(k,{children:[i(L,{level:2,size:3,text:"Log in to chat with any group you are in."}),i(L,{level:3,size:6,color:"tint3",text:"You must already be a member of a group"})]}),i("a",{href:`/login?return=${window.location.href}`,className:"btn compact-btn secondary-btn mt-1",children:"Log in"})]})}function Ii(){return i("section",{className:"action-drawer ta-c d-f ai-c jc-c fd-c mb-1",css:{height:"calc(100% - 32px)",width:"100%"},children:i(L,{level:2,size:4,text:"Chat is unavailable on mobile."})})}zt.propTypes={subscribersCount:h.number};function zt({subscribersCount:e}){return e?f("div",{className:"badge",style:{position:"absolute",top:"8px",right:"8px",zIndex:"1",padding:"4px 8px",background:"rgba(33,33,33, 0.4)",color:"white"},children:[i(P,{symbol:"general#show-eye",className:"c-tint10 mr-1 p-r t-2p"}),e]}):i("div",{})}we.propTypes={episodeTime:h.object,videoEmbedCode:h.string.isRequired,joltChannel:h.object};function we({episodeTime:e,videoEmbedCode:t,joltChannel:r}){const[n,s]=a.useState(!1);return a.useEffect(()=>{r&&t&&!n&&(s(!0),r.send({event:e?"client.liveWatchStats":"client.libraryWatchStats",data:{playerState:"PLAYING",playerCurrentTime:0}}))},[e,r,t,n]),a.useMemo(()=>t?i("div",{className:"video-embed",dangerouslySetInnerHTML:{__html:t}}):i("div",{children:"unsupported video URL"}),[t])}Te.propTypes={html:h.string,url:h.string.isRequired,streamingService:h.string.isRequired,showControls:h.bool,enforceSync:h.bool,episodeTime:h.shape({links:h.shape({self:h.string.isRequired})}),joltChannel:h.object};const Ai=10,Li=3600,Pi=2,ji=15;function Te({html:e,url:t,streamingService:r,showControls:n,enforceSync:s,episodeTime:o,joltChannel:c}){if(t){let d=null;return r==="youtube"?t.match(/embed\/live_stream\?.*channel=([a-z0-9-_]+)/i)?d=we:d=Ht:r==="vimeo"?d=Wt:r==="livestream_com"?d=Kt:r==="boxcast"?d=Jt:d=we,i("div",{css:qe.videoContainer,children:i(d,{showControls:n,enforceSync:s,isPlayingFromLivestream:!!o,timestamp:o&&o.attributes.current_timestamp,url:t,videoEmbedCode:e,episodeTime:o,joltChannel:c})})}else return i("div",{css:qe.videoContainer,style:{backgroundColor:"var(--color-gray25)"},children:i("div",{className:"no-video-url",children:"no video url"})})}Wt.propTypes={showControls:h.bool,enforceSync:h.bool,timestamp:h.number,url:h.string.isRequired,joltChannel:h.object,isPlayingFromLivestream:h.bool.isRequired};function Wt({enforceSync:e,timestamp:t,url:r,joltChannel:n,isPlayingFromLivestream:s}){const o=a.useRef(null),c=w=>new Promise(v=>{o.current.getDuration().then(_=>{_===0||w<0||w>_||o.current.setCurrentTime(w).then(v).catch(x=>console.log(`Error seeking: ${x}`))}).catch(_=>console.log(_))}),d=a.useMemo(()=>new Yt(()=>o.current.getCurrentTime(),c),[r,e]),u=({playerState:w,playerCurrentTime:v})=>{n.send({event:s?"client.liveWatchStats":"client.libraryWatchStats",data:{playerState:w,playerCurrentTime:v}})},[l,p]=a.useState(!1);a.useEffect(()=>{l&&e&&d.checkDrift(t)},[l,e,t]);const[g,b]=a.useState(!!window.Vimeo),y=r.match(/^https:\/\/(player\.)?vimeo\.com\/(event\/|video\/)?\d+/i),E=()=>{window.Vimeo?b(!0):setTimeout(E,100)};return a.useEffect(()=>{if(y){if(!g){setTimeout(E,100);return}return document.querySelector("#player").innerHTML="",o.current=new Vimeo.Player("player",{url:r,height:"390",width:"640",autoplay:!1,byline:!1,controls:!0,title:!1}),o.current.on("loaded",()=>{o.current.setVolume(1),e?c(t).then(()=>o.current.play().catch(console.log)).catch(console.log):o.current.play()}),o.current.on("pause",()=>p(!1)),o.current.on("play",()=>p(!0)),o.current.on("play",({seconds:w})=>u({playerState:"PLAYING",playerCurrentTime:w})),o.current.on("pause",({seconds:w})=>u({playerState:"PAUSED",playerCurrentTime:w})),o.current.on("ended",({seconds:w})=>u({playerState:"ENDED",playerCurrentTime:w})),()=>{o.current?.destroy()}}},[r,g]),r?f(k,{children:[i("script",{async:!0,src:"https://player.vimeo.com/api/player.js"}),i("div",{id:"player"})]}):i("div",{children:"problem loading player"})}Ht.propTypes={showControls:h.bool,enforceSync:h.bool,timestamp:h.number,url:h.string.isRequired,joltChannel:h.object,isPlayingFromLivestream:h.bool.isRequired};function Ht({showControls:e,enforceSync:t,timestamp:r,url:n,joltChannel:s,isPlayingFromLivestream:o}){const c=n.match(/(watch\?v=|youtu\.be\/|live\/|embed\/)([a-z0-9-_]+)/i),d=c&&c[2],u=new URL(n).searchParams.get("t"),l=r||u,p=a.useRef(null),g=a.useMemo(()=>new Yt(()=>new Promise(_=>_(p.current.getCurrentTime())),_=>p.current.seekTo(_)),[]),b=({playerState:_,playerCurrentTime:x})=>{s.send({event:o?"client.liveWatchStats":"client.libraryWatchStats",data:{playerState:_,playerCurrentTime:x}})},[y,E]=a.useState(!1);a.useEffect(()=>{y&&t&&g.checkDrift(l)},[y,t,l,g]);const[w,v]=a.useState(!!(window.YT&&window.YT.Player));return window.onYouTubeIframeAPIReady=()=>v(!0),a.useEffect(()=>{if(d&&w)return p.current=new YT.Player("player",{videoId:d,height:"390",width:"640",playerVars:{autoplay:0,controls:e?1:0,playsinline:1,rel:0},events:{onReady:()=>{p.current.seekTo(l,!0),p.current.playVideo()},onStateChange:()=>{const _=p.current.getPlayerState(),x=_===YT.PlayerState.PLAYING,T=_===YT.PlayerState.ENDED,C=_===YT.PlayerState.PAUSED;if(E(x),!x&&!T&&!C)return;let A="PLAYING";T?A="ENDED":C&&(A="PAUSED"),b({playerState:A,playerCurrentTime:p.current.getCurrentTime()})}}}),()=>{p.current&&p.current.hasOwnProperty("stopVideo")&&p.current.hasOwnProperty("destroy")&&(p.current.stopVideo(),p.current.destroy())}},[d,w]),d?f(k,{children:[i("script",{async:!0,src:"https://www.youtube.com/iframe_api"}),i("div",{id:"player"})]}):i("div",{children:"problem loading player"})}class Yt{constructor(t,r){this.getPlayerTimestamp=t,this.setPlayerTimestamp=r,this.enabled=!0,this.corrections=0,this.rapidCorrections=0}checkDrift(t){this.enabled&&this.getDrift(t).then(r=>{if(r>Li){console.log("drift is excessively high; disabling drift correction"),this.enabled=!1;return}if(r>Ai){if(this.corrections++,this.rapidCorrections++,this.corrections>ji){console.log(`we have made ${this.corrections} drift corrections overall; disabling drift correction`),this.enabled=!1;return}if(this.rapidCorrections>Pi){console.log(`we have made ${this.rapidCorrections} rapid drift corrections in a row; disabling drift correction`),this.enabled=!1;return}console.log(`seeking to ${t}`),this.setPlayerTimestamp(t),setTimeout(()=>{this.rapidCorrections--},1e3)}})}getDrift(t){return new Promise(r=>{this.getPlayerTimestamp().then(n=>{r(Math.abs(n-t))})})}}Kt.propTypes={episodeTime:h.object,joltChannel:h.object,url:h.string.isRequired};function Kt({url:e,episodeTime:t,joltChannel:r}){const[n,s]=a.useState(!1);return a.useEffect(()=>{r&&!n&&(s(!0),r.send({event:t?"client.liveWatchStats":"client.libraryWatchStats",data:{playerState:"PLAYING",playerCurrentTime:0}}))},[t,r,n]),i("iframe",{title:"Livestream VOD",src:`${e}/player`,frameBorder:"0",scrolling:"no",allowFullScreen:!0})}Jt.propTypes={episodeTime:h.object,joltChannel:h.object,url:h.string.isRequired};function Jt({url:e,episodeTime:t,joltChannel:r}){const[n,s]=a.useState(!1),o=e.replace("/view/","/view-embed/");return a.useEffect(()=>{r&&!n&&(s(!0),r.send({event:t?"client.liveWatchStats":"client.libraryWatchStats",data:{playerState:"PLAYING",playerCurrentTime:0}}))},[t,r,n]),i("iframe",{title:"Boxcast Video Player",src:o,frameBorder:"0",scrolling:"no",allowFullScreen:!0})}const qe={videoContainer:S`
    position: relative;
    padding-bottom: 56.25%; /*16:9*/
    height: 0;
    overflow: hidden;

    iframe,
    object,
    embed {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }

    img {
      width: 50px;
      height: 35px;
      @media (min-width: 960px) {
        width: 58px;
        height: 40px;
      }
      display: inline-flex;
    }

    .no-video-url {
      background: #ef5350;
      color: var(--color-tint10);
      padding: 8px 16px;
      border-radius: 3px;
    }

    header h1 {
      opacity: 0.8;
      font-weight: bold;
      font-size: 44px;
      @media (min-width: 960px) {
        font-size: 52px;
      }
      text-transform: uppercase;
    }

    header h2 {
      font-size: 16px;
      @media (min-width: 960px) {
        font-size: 20px;
      }
      opacity: 0.6;
    }

    header h3.timer {
      font-size: 40px;
      @media (min-width: 960px) {
        font-size: 44px;
      }
      display: inline;
      background-image: linear-gradient(to right, #41a5f5, #66bb6a);
      color: transparent;
      -webkit-background-clip: text;
      background-clip: text;
    }
  `};function Se(e,t){const r=a.useRef(null);a.useEffect(()=>{r.current=e},[e]),a.useEffect(()=>{function n(){r.current()}if(t!==null){let s=setInterval(n,t);return()=>clearInterval(s)}},[t])}Xt.propTypes={startTime:h.object.isRequired,onFinished:h.func};function Xt({startTime:e,onFinished:t}){const[,r]=a.useState(),n=e.diff(ee(),"seconds"),[s,o]=a.useState(n<=0),[c,d]=a.useState(null);Se(()=>{r({})},1e3),a.useEffect(()=>{!s&&n<=0&&(o(!0),t&&t())},[s,n,t]);let u;if(s)u="0:00";else{const l=Math.floor(n/60/60),p=Math.floor(n/60%60),g=p<10?`0${p}`:p,b=n%60,y=b<10?`0${b}`:b;u=l>0?`${l}:${g}:${y}`:`${p}:${y}`}return a.useEffect(()=>{Nr.video({inline:!0}).then(({result:l})=>{d(l)})},[]),i("div",{css:Di.videoContainer,className:"video-countdown d-f fd-c ai-c jc-c ta-c",children:i("div",{className:"action-drawer countdown",children:i("header",{children:c?f(k,{children:[i("img",{src:"/assets/gfx-video-start.svg",alt:""}),i(L,{level:1,text:"Welcome"}),i(L,{level:2,text:"Our live stream will begin in"}),i("h3",{className:"timer",children:u})]}):i("figure",{className:"play-btn-container d-f",children:i("button",{className:"primary-btn btn",name:"play",onClick:()=>d(!0)})})})})})}const Di={videoContainer:S`
    position: relative;
    padding-bottom: 56.25%; /*16:9*/
    height: 0;
    overflow: hidden;

    .countdown {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }

    img {
      width: 50px;
      height: 35px;
      @media (min-width: 960px) {
        width: 58px;
        height: 40px;
      }
      display: inline-flex;
    }

    .no-video-url {
      background: #ef5350;
      color: var(--color-gray0);
      padding: 8px 16px;
      border-radius: 3px;
    }

    header h1 {
      opacity: 0.8;
      font-weight: bold;
      font-size: 44px;
      @media (min-width: 960px) {
        font-size: 52px;
      }
      text-transform: uppercase;
    }

    header h2 {
      font-size: 16px;
      @media (min-width: 960px) {
        font-size: 20px;
      }
      opacity: 0.6;
    }

    header h3.timer {
      font-size: 40px;
      @media (min-width: 960px) {
        font-size: 44px;
      }
      display: inline;
      background-image: linear-gradient(to right, #41a5f5, #66bb6a);
      color: transparent;
      -webkit-background-clip: text;
      background-clip: text;
    }

    .play-btn-container button[name="play"] {
      width: 50px;
      height: 50px;
      margin: auto;
    }
    .play-btn-container button[name="play"]:focus {
      outline: 0;
      border: 1px solid hsl(0deg 0% 60%);
      box-shadow: 0 0 0 3px hsl(0deg 0% 73% / 50%);
    }

    .play-btn-container button[name="play"]::after {
      /* This is the caret inside the button */
      content: "";
      display: inline-block;
      position: relative;
      top: 1px;
      left: 3px;
      border-style: solid;
      border-width: 10px 0 10px 20px;
      border-color: transparent transparent transparent white;
    }
  `};function Qt(e,t){let r;try{return r=new URL(e),!t&&$i(r.hostname)&&Mi(r.pathname)}catch(n){return console.warn(n),!1}}function $i(e){if(e.match(/\.churchcenteronline\.com$/)||e.match(/\.churchcenter\.com$/)||e.match(/\.church\.center$/)||e.match(/\.churchcenter\.test$/))return!0;throw"ChurchCenterModal: hostname '"+e+"' is not supported. Use 'https://[yoursubdomain].churchcenteronline.com'"}function Mi(e){const t=e.slice(1).split("/"),r=t[0];if(r==="giving"||r==="people"&&t[1]==="forms")return!0;throw"ChurchCenterModal: the app '"+r+"' is not supported yet."}function le(e){return["giving_fund","people_form"].indexOf(e.attributes.kind)>-1?`${e.attributes.url}?source=cca`:e.attributes.url}function Zt(e){return/^(https?:)?\/\//.test(e)}Ne.propTypes={episodeDescription:h.string,episodeResources:h.array,notesToggleButton:h.node,showFullDescription:h.bool};function Ne({episodeDescription:e,episodeResources:t,notesToggleButton:r,showFullDescription:n=!1,...s}){const o={generic_url:"fa-link",giving_fund:"fa-money-bill",people_form:"fa-user-plus",services_public_page:"fa-list-ul"},[c,d]=a.useState(t.length===0),[u,l]=a.useState("");a.useEffect(()=>{if(!e)return;let g=e;const b=e.split(" ");b.length>35&&(g=b.slice(0,25).join(" ")+"...");const y=g.split(`
`);y.length>4&&(g=y.slice(0,3).join(`
`)+"..."),l(g)},[e]);const p=!n&&e!==u&&t.length>0;return f("div",{...s,children:[e&&i("div",{"data-name":"episode summary",className:"action-drawer mb-2",children:f("p",{className:"mb-0",css:{whiteSpace:"pre-line"},children:[i("span",{children:c||n?e:u}),p&&i("button",{style:{display:"block",height:"auto"},className:"btn link-btn mt-1",onClick:()=>d(!c),children:c?"Show Less":"Show More"})]})}),f("div",{className:"d-f fd-c g-1",children:[r,t.map(g=>i(ce,{icon:g?.attributes?.icon&&`fa-${g.attributes.icon}`||o[g?.attributes?.kind],title:g.attributes.title,url:le(g)},g.id))]})]})}ce.propTypes={icon:h.string,onClick:h.func,title:h.string.isRequired,url:h.string.isRequired};function ce({icon:e="fa-link",onClick:t,title:r,url:n}){const s=te();return f(ze,{className:"d-f ai-c jc-sb ta-l c-tint2 fs-3 mb-1 w-100%","data-open-in-church-center-modal":Qt(n,s),css:Ue.resourceLink,to:n,onClick:t,...Zt(n)?{rel:"noopener noreferrer",target:"_blank"}:{},children:[i("span",{className:"mr-2",children:i(P,{symbol:e,"aria-hidden":!0})}),i("span",{className:"f-1",children:r}),i(P,{css:Ue.resourceChevron,symbol:"general#right-chevron","aria-hidden":!0})]})}const Ue={resourceLink:S`
    border: 1px solid var(--color-tint6);
    border-radius: 4px;
    padding: 0.5rem 1rem;
    height: 42px;
    font-weight: 400;

    &:hover {
      background-color: var(--color-tint6);
    }
  `,resourceChevron:S`
    width: 12px;
    height: 12px;
    color: var(--color-tint3);
  `};ee.extend(Rr);const ae="discussion",W="resources",oe="notes";er.propTypes={joltChannel:h.object,episode:h.object,episodeTime:h.object,channel:h.object,featuredResource:h.object,episodeResources:h.array,subscribersCount:h.number};function er({episode:e,episodeTime:t,channel:r,joltChannel:n,featuredResource:s,episodeResources:o}){const[c,d]=a.useState(W),[u,l]=a.useState(),p=te(),g=!!t,{notesEnabled:b}=qi(e,r),y=g&&(r.attributes.group_chat_enabled||r.attributes.general_chat_enabled),{width:E}=pe(),w=b&&!p&&E>=he.LG;return a.useEffect(()=>{E<he.LG&&c===oe&&d(W)},[c,E]),a.useEffect(()=>{!y&&c===ae&&d(W)},[c,y]),a.useEffect(()=>{p&&window.ReactNativeWebView.postMessage(JSON.stringify({type:"stopAudio"}))},[p]),a.useEffect(()=>{if(n)return n.bind("jolt.subscriptionStats",_=>l(_.data.subscribers))},[n]),f("div",{css:rr.videoChatGridContainer,children:[f("div",{className:"video-block",style:{position:"relative"},children:[i(zt,{subscribersCount:u,className:"sub-counter"}),i(tr,{episode:e,episodeTime:t,joltChannel:n})]}),f("div",{className:"sermons__messaging chat-block f-1 fw-w",children:[f("div",{className:"action-item-row d-f jc-sb",children:[f("div",{className:"tab-items",role:"tablist","aria-label":"Episode Chat and Info",children:[i("button",{role:"tab","aria-selected":"true","aria-controls":"panel-2",id:"tab-2",className:Z("h4 tab fs-4 mr-3 set-focus-invisible",{"tab--active":c===W}),onClick:()=>d(W),children:"Info"}),y&&i("button",{role:"tab","aria-selected":"true","aria-controls":"panel-1",id:"tab-1",tabIndex:"0",className:Z("h4 tab fs-4 mr-3 set-focus-invisible",{"tab--active":c===ae}),onClick:()=>d(ae),children:"Chat"}),w&&i("button",{role:"tab","aria-selected":"true","aria-controls":"panel-3",id:"tab-3",tabIndex:"0",className:Z("h4 tab fs-4 mr-3 set-focus-invisible",{"tab--active":c===oe}),onClick:()=>d(oe),children:"Notes"})]}),s&&i("a",{href:le(s),className:"compact-btn secondary-btn btn","data-open-in-church-center-modal":Qt(le(s),p),...Zt(le(s))?{rel:"noopener noreferrer",target:"_blank"}:{},children:s.attributes.title})]}),c===ae&&y&&i(Ut,{episode:e,episodeTime:t,groupChatEnabled:r.attributes.group_chat_enabled,generalChatEnabled:r.attributes.general_chat_enabled}),c===W&&i("div",{id:"panel-2",role:"tabpanel",tabIndex:"0","aria-labelledby":"tab-2",className:"p-2 set-focus-invisible tab-widget-wrapper",children:i("div",{className:"tab-widget-content f-1",style:{padding:"8px"},children:i(Ne,{episodeDescription:e.attributes.description,episodeResources:o,notesToggleButton:b&&!w&&i(ce,{icon:"accounts#editor",title:"Take notes",url:`${Qe(e)}/notes?return_to_episode=true`})})})}),b&&c===oe&&i("div",{id:"panel-3",role:"tabpanel",tabIndex:"0","aria-labelledby":"tab-3",className:"set-focus-invisible tab-widget-wrapper live-episode-notes-panel",children:i("div",{className:"tab-widget-content f-1",children:i(et.Suspense,{children:i(tt,{episodeId:e.id})})})})]})]})}tr.propTypes={episode:h.object.isRequired,episodeTime:h.object,joltChannel:h.object};const Fi=1e4;function tr({episode:e,episodeTime:t,joltChannel:r}){const n=We(),[s,o]=a.useState(t),c=a.useCallback(()=>{s&&I.get(s.links.self).then(({data:y})=>{o(y)})},[s,o]);Se(c,Fi);const d=e.attributes.published_to_library;let u,l,p;if(s?Oi(s)&&d?n(`/episodes/${e.id}`,{replace:!0}):(u=s.attributes.video_url,l=s.attributes.streaming_service,p=s.attributes.video_embed_code):d?(u=e.attributes.library_video_url,l=e.attributes.library_streaming_service,p=e.attributes.library_video_embed_code):e.attributes.video_url?(u=e.attributes.video_url,l=e.attributes.streaming_service,p=e.attributes.video_embed_code):e.attributes.library_video_url&&(u=e.attributes.library_video_url,l=e.attributes.library_streaming_service,p=e.attributes.library_video_embed_code),s?.attributes.current_timestamp<0){const y=ee().add(Math.abs(s.attributes.current_timestamp),"seconds");return i(Xt,{startTime:y,onFinished:()=>setTimeout(c,500)})}const g="scheduled_event",b="prerecorded";return u?i(Te,{html:p,url:u,streamingService:l,showControls:!s,enforceSync:s&&[g,b].includes(e.attributes.stream_type),episodeTime:s,joltChannel:r}):i("div",{css:rr.videoContainer,children:i("div",{className:"d-f jc-c ai-c",style:{position:"absolute",top:"0",left:"0",right:"0",bottom:"0"},children:i("span",{className:"no-video-url",children:"The video URL could not be found."})})})}function Oi(e){return e?.attributes.ends_at&&ee(e.attributes.ends_at).add(1,"hour").isSameOrBefore(ee())}const rr={videoChatGridContainer:S`
    display: flex;
    flex-direction: column;
    flex: 1;
    @media (min-width: 960px) {
      display: grid;
      grid-template-columns: 1.3fr 0.7fr;
      grid-template-rows: 1fr;
      gap: 24px 24px;
      grid-template-areas: ". .";
    }

    .sub-counter {
      position: absolute;
      top: 12px;
      right: 12px;
    }

    .action-item-row {
      padding: 0 0.75rem;
      width: 100%;
      align-items: center;
      @media (max-width: 959px) {
        box-shadow: 0 1px 0 var(--color-tint9);
      }
      @media (min-width: 960px) {
        padding-right: 0;
        padding-left: 0;
        height: 32px;
        align-items: flex-end;
        border-bottom: 0;
      }

      > .btn {
        @media (min-width: 960px) {
          margin-bottom: 12px;
        }
      }

      .tab {
        cursor: pointer;
        color: var(--color-tint3);
        background: transparent;
        text-transform: capitalize;
        border: 0;
        border-bottom: 4px solid transparent;
        border-radius: 0;
        display: inline-block;
        padding: 12px 0 12px 0;

        @media (min-width: 960px) {
          padding-top: 0;
          font-size: 16px;
        }
      }
      /* TODO: Remove once a fix is provided.
      This temporarily gives minions specificity over the ongoing work in dark mode.
      An issue was raised with R&F about minions not needing greater specificity than a compatible theming system */

      .tab--active {
        /* TODO: */
        color: var(--color-tint1);
        border-color: var(--color-tint4);
      }
    }

    .chat-block {
      position: relative;
      @media (max-width: 959px) {
        display: flex;
      }
    }

    .video-embed {
      /* need these styles to maintain aspect ratio for responsive views */
      position: relative;
      padding-bottom: 56.25%;
      height: 0px;
      overflow: hidden;
    }

    .video-embed iframe {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 100%;
      height: 100%;
    }
  `,videoContainer:S`
    position: relative;
    padding-bottom: 56.25%; /*16:9*/
    height: 0;
    overflow: hidden;
    border-radius: 5px;

    .no-video-url {
      background: #ef5350;
      color: var(--color-tint10);
      padding: 8px 16px;
      border-radius: 3px;
    }
  `};function qi(e,t){const r=t.attributes.enabled_formats.sermon_notes,{isLoading:n,data:s}=Ae({enabled:r,queryFn:()=>I.get(`/publishing/v2/episodes/${e.id}/note`,{"fields[Note]":"id"}),queryKey:["episode",e.id,"note","id"],retry:!1,select:({data:l})=>l.id,staleTime:1/0}),{isLoading:o,data:c}=Ae({enabled:r,queryFn:()=>I.get(`/publishing/v2/episodes/${e.id}/note_template`,{"fields[NoteTemplate]":"id"}),queryKey:["episode",e.id,"noteTemplate","id"],retry:!1,select:({data:l})=>l.id,staleTime:1/0}),d=!Le(c),u=!Le(s);return{loading:r&&(n||o),notesEnabled:r&&(d||u)}}const Ui=2,Bi=15e3;ir.propTypes={audioDownloadLink:h.string,autoplay:h.bool,episode:h.object,personEpisodeProgress:h.object,setAudioDownloadLink:h.func};function Vi(e,t){I.post(`${e}/record_progress`,{data:{type:"RecordProgressAction",attributes:{progress_seconds:Math.floor(t)}}})}function ir({audioDownloadLink:e,autoplay:t,episode:r,personEpisodeProgress:n,setAudioDownloadLink:s}){const{meta:{authenticated:o}}=U(!1),c=n?.attributes.progress_seconds||0,d=r.attributes.sermon_audio.attributes.source==="remote"||r.attributes.sermon_audio.attributes.source==="hosted",[u,l]=a.useState(!1),[p,g]=a.useState(!1),[b,y]=a.useState(null),[E,w]=a.useState(!1),v=a.useRef(null),{library_art_url:_}=r.attributes,x=r.links.self,T=a.useCallback(N=>{o&&N!==c&&Vi(x,N)},[o,x,c]),C=jr(T,200),{mutate:A,isPending:D}=kr({mutationFn:()=>{const N={data:{attributes:{}}};return I.post(`/publishing/v2/episodes/${r.id}/audio_download`,N).then(({data:ie})=>ie.attributes.url)},onSuccess:N=>s(N),onError:({errors:[N]})=>{switch(N?.code){case"hard_limit_error":l(!0);break;case"disabled_episode_error":g(!0);break;default:alert("Something went wrong. Please, try again.");break}}}),R=D||E,z=N=>{if(N?.code===Ui)console.log("Audio link expired, requesting new link..."),A();else if(N)throw N},B=()=>{C(0),y(null)},re=()=>{b||y(Bi)},J=()=>{C(v.current.currentTime),y(null)},$=N=>{w(N),N||C(v.current.currentTime)};Se(()=>{v.current&&C(v.current.currentTime)},b);const V=te();return a.useEffect(()=>{d&&!e&&!V&&A()},[d,e,A,V]),a.useEffect(()=>{e&&t&&v.current?.play()},[e,t]),f("div",{className:"p-r",children:[f("div",{className:"p-r",children:[i("img",{className:"d-b",alt:"Episode art",css:Q.image,src:_}),i("div",{className:"p-a l-0 r-0 b-0 t-0 d-f jc-c ai-c",children:R&&i("div",{css:Q.loadingSpinner})})]}),V&&i("div",{className:"p-a l-0 r-0 b-0 d-f jc-sb ai-c fd-r p-2",css:Q.controlsWrapper,children:i("button",{css:[Q.playPause,Q.play],onClick:()=>lr(r),children:"Play"})}),!V&&i(Qr,{ref:v,src:e,initialTime:c,onPlay:re,onPause:J,onEnded:B,onError:z,onSeeking:$,showSkipButtons:!0,variant:"overlay"}),i(nr,{hardLimitError:u,setHardLimitError:l}),i(sr,{episodeDisabledError:p,setEpisodeDisabledError:g})]})}nr.propTypes={hardLimitError:h.bool.isRequired,setHardLimitError:h.func.isRequired};function nr({hardLimitError:e,setHardLimitError:t}){const{layout:{organization_contact_email:r}}=a.useContext(Dr),n=a.useRef(null),s=()=>t(!1);return e?f(Ke,{leastDestructiveRef:n,onDismiss:s,children:[i(He,{children:"Error: Download limit reached"}),f(Ye,{children:["Your church has reached it’s limit of audio downloads, please contact your ",r?i("a",{href:`mailto:${r}`,children:"church"}):"church"," for help.",i("div",{className:"d-f jc-fe mt-3",children:i("button",{onClick:s,children:"Close"})})]})]}):null}sr.propTypes={episodeDisabledError:h.bool.isRequired,setEpisodeDisabledError:h.func.isRequired};function sr({episodeDisabledError:e,setEpisodeDisabledError:t}){const r=a.useRef(null),n=()=>t(!1);return e?f(Ke,{leastDestructiveRef:r,onDismiss:n,children:[i(He,{children:"Error: Episode audio download disabled"}),f(Ye,{children:["Audio download for this episode has been temporarily disabled. Please check back later.",i("div",{className:"d-f jc-fe mt-3",children:i("button",{onClick:n,children:"Close"})})]})]}):null}const Q={controlsWrapper:S`
    background-image: linear-gradient(
      to top,
      rgba(0, 0, 0, 0.5),
      rgba(0, 0, 0, 0)
    );
  `,image:S`
    width: 100%;
    aspect-ratio: 16 / 9;
    object-fit: cover;
  `,loadingSpinner:S`
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    content: "";
    display: block;
    width: 48px;
    height: 48px;
    background-color: var(--color-static-gray100);
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center center;
    mask-image: url("data:image/svg+xml, %3Csvg version='1.1' id='loader-1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'  viewBox='0 0 50 50' style='enable-background:new 0 0 50 50;' xml:space='preserve'%3E%3Cpath fill='%23000' d='M25.251,6.461c-10.318,0-18.683,8.365-18.683,18.683h4.068c0-8.071,6.543-14.615,14.615-14.615V6.461z'%3E%3CanimateTransform attributeType='xml' attributeName='transform' type='rotate' from='0 25 25' to='360 25 25' dur='0.6s' repeatCount='indefinite'/%3E%3C/path%3E%3C/svg%3E");
  `,playPause:S`
    width: 48px;
    height: 48px;
    border-radius: 24px;
    background-color: transparent;
    box-shadow: none;
    border: none;
    text-indent: 200%;
    white-space: nowrap;
    position: relative;
    overflow: hidden;

    &:after {
      content: "";
      display: block;
      width: 32px;
      height: 32px;
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center center;
      background-color: var(--color-static-gray100);
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  `,play:S`
    &:after {
      width: 48px;
      height: 48px;
      mask-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='m0 0h24v24h-24z' fill='none'/%3E%3Cpath d='m8 5v14l11-7z'/%3E%3C/svg%3E");
    }
  `},q="video",M="audio";ar.propTypes={audioDownloadLink:h.string,channel:h.object,episode:h.object,episodeResources:h.array,featuredResource:h.object,joltChannel:h.object,personEpisodeProgress:h.object,series:h.object,speaker:h.object,setAudioDownloadLink:h.func};function ar({audioDownloadLink:e,channel:t,episode:r,episodeResources:n,featuredResource:s,joltChannel:o,personEpisodeProgress:c,series:d,speaker:u,setAudioDownloadLink:l}){const{library_streaming_service:p,library_video_url:g,library_video_embed_code:b,sermon_audio:y,streaming_service:E,video_url:w}=r.attributes,[v,_]=Xe({media_intent:null}),{media_intent:x,autoplay:T}=v,C=te(),{width:A}=pe(),{meta:{authenticated:D}}=U(),R=!!r.relationships.note_template.data,{data:z}=Ur(r.id,{enabled:D}),B=!!z?.content,re=R&&t.attributes.enabled_formats.sermon_notes,J=C||A<he.LG,[$,V]=a.useState(!1),[N,ie]=a.useState(!0),[Re,ke]=a.useState(null),[cr,dr]=a.useReducer(()=>!1,!0),{id:ur}=t,pr=d?{"where[series_id]":d.id}:{"where[channel_id]":ur},hr=g?{url:g,html:b,streamingService:p}:{videoUrl:w,streamingService:E},Ie=y.attributes.source==="hosted"||y.attributes.source==="remote",de=!!w||!!g,[ne,mr]=a.useState(de?q:M),{width:fr}=pe(),br=fr<960,gr=U().meta.authenticated;function yr(j){_({...v,media_intent:j})}function X(j){mr(j),ke(j),C||yr(j),dr(),j===q&&C&&Gi(),j===M&&C&&lr(r)}function vr(){return $?"Hide notes":gr&&B?"View notes":"Take notes"}return a.useEffect(()=>{C&&!cr&&!N&&ke(null)},[N]),a.useEffect(()=>{![M,q].includes(x)||C&&!T||X(x)},[x]),a.useEffect(()=>{C&&(window.setIsFocused=ie)},[!!C,ie]),a.useEffect(()=>{J&&$&&V(!1)},[J,$]),f("div",{className:"d-f jc-c g-3",css:$?{display:"grid",gridTemplateColumns:"1fr 1fr"}:{},children:[f("div",{className:"w-100%",children:[i(or,{episodeId:r.id}),f("div",{className:"mb-3",css:[H.bleedContainer],children:[ne===q&&i(k,{children:Re===q?i(Te,{...hr,showControls:!0,enforceSync:!1,joltChannel:o}):i(xe,{artUrl:r.attributes.library_art_url,buttonLabel:"Play video",showButton:de,onClick:()=>X(q)})}),ne===M&&i(k,{children:Re===M?i(ir,{audioDownloadLink:e,autoplay:x===M,episode:r,personEpisodeProgress:c,setAudioDownloadLink:l}):i(xe,{artUrl:r.attributes.library_art_url,buttonLabel:"Play audio",showButton:Ie,onClick:()=>X(M)})})]}),f("div",{css:[H.container,$?{"@media (min-width: 960px)":{gridTemplateColumns:"1fr"}}:{}],children:[f("div",{children:[f("div",{className:"d-f jc-sb ai-fs mb-2",css:H.tabs,children:[f("header",{className:"d-f fd-c g-4p",children:[i(L,{level:2,text:r.attributes.title}),f("p",{className:"mb-0",children:[r.attributes.published_to_library_at?i(ei,{start:r.attributes.published_to_library_at,style:"standard",year:!0}):i(k,{children:"Not Published"}),u&&f("span",{children:[" • ",u.attributes.formatted_name]}),d&&f("span",{children:[" • Series: ",i("a",{href:d.attributes.church_center_path,children:d.attributes.title})]})]})]}),Ie&&de&&f("div",{className:"tab-items",role:"tablist","aria-label":"Watch or Listen to Episode",children:[i("button",{role:"tab","aria-selected":"true","aria-controls":"panel-2",id:"tab-2",className:Z("tab fs-4 mr-1 set-focus-invisible",{"tab--active":ne===q}),onClick:()=>X(q),children:"Watch"}),i("button",{role:"tab","aria-selected":"true","aria-controls":"panel-1",id:"tab-1",tabIndex:"0",className:Z("tab fs-4 set-focus-invisible",{"tab--active":ne===M}),onClick:()=>X(M),children:"Listen"})]})]}),i(Ne,{css:H.resources,episodeDescription:r.attributes.description,episodeResources:[s,...n].filter(Boolean),showFullDescription:!br,notesToggleButton:re&&i(ce,{icon:$?"general#hide-eye":"accounts#editor",onClick:j=>{J||(j.preventDefault(),j.stopPropagation(),V(_r=>!_r))},title:vr(),url:`${Qe(r)}/notes?return_to_episode=true`})})]}),i("div",{className:"d-f fd-c g-2",children:i(Zr,{excludeId:r.id,queryParams:{...pr,per_page:3,filter:"published_to_library",order:"-published_to_library_at"},children:i(Xr,{level:4,text:`More from ${d?d.attributes.title:t.attributes.name}`})})})]})]}),re&&$&&i("div",{css:H.notesWrapper,children:i(et.Suspense,{children:i(tt,{episodeId:r.id})})})]})}xe.propTypes={artUrl:h.string,buttonLabel:h.string,showButton:h.bool,onClick:h.func};function xe({artUrl:e,buttonLabel:t,showButton:r,onClick:n}){return f("div",{className:"p-r",css:{paddingBottom:9/16*100+"%",backgroundColor:"var(--color-tint8)"},children:[i("img",{className:"d-b p-a t-0 l-0 w-100% h-100%",alt:"Episode art",css:{objectFit:"cover"},src:e}),r&&i("button",{className:"p-a btn",css:{top:"50%",left:"50%",transform:"translate(-50%,-50%)",textIndent:"150%",overflow:"hidden",background:"white",width:64,height:64,borderRadius:32,padding:0,"&:after":{display:"block",content:"''",width:"50%",height:"50%",position:"absolute",left:"50%",top:"50%",transform:"translate(-50%,-50%)",background:"var(--color-static-gray45)",maskImage:`url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='currentColor'%3E%3Cpath d='M5 15L15 8L5 1V15Z'%3E%3C/path%3E%3C/svg%3E")`}},onClick:n,children:t})]})}function or({episodeId:e}){const{data:t}=Ze(e),r=t.included.filter(n=>n.type==="EpisodeTime"&&n.attributes.current_state==="active").sort((n,s)=>n.attributes.starts_at-s.attributes.starts_at).reverse();return r.length===0?null:f(se.Pane,{css:H.bleedContainer,className:"mb-2",children:[i(se.Column,{children:i(se.Description,{children:"Livestream in progress"})}),i(se.Action,{children:i(ze,{className:"btn",to:`/episodes/${e}?episode_time_id=${r[0].id}`,children:"Join the livestream"})})]})}or.propTypes={episodeId:h.string.isRequired};function lr(e){const{name:t,source:r}=e.attributes.sermon_audio.attributes;window.ReactNativeWebView.postMessage(JSON.stringify({type:"playAudio",episode:e,url:r==="remote"?t:null}))}function Gi(){window.ReactNativeWebView.postMessage(JSON.stringify({type:"stopAudio"}))}const H={bleedContainer:S`
    max-width: min(100vw, 900px);
    margin-inline: auto;

    @media (max-width: 600px) {
      margin-bottom: 16px;
    }
  `,container:S`
    max-width: min(100cqw - 2rem, 900px);
    margin-inline: auto;
    display: grid;
    grid-template-columns: 1fr;
    column-gap: 32px;
    row-gap: 32px;

    [data-cca-platform="ios"] & {
      width: min(100vw - 40px, 900px);
    }
    [data-cca-platform="android"] & {
      width: min(100vw - 32px, 900px);
    }

    header p {
      font-size: 16px;
    }

    [data-name="episode summary"] {
      padding: 0;
      background: transparent;
    }

    @media (min-width: 960px) {
      grid-template-columns: 2fr 1fr;
    }
  `,tabs:S`
    gap: 24px;

    .tab {
      cursor: pointer;
      color: var(--color-tint2);
      background: transparent;
      text-transform: capitalize;
      border: 0;
      display: inline-flex;
      justify-content: center;
      align-items: center;
      height: 32px;
      padding: 0 12px;
      border-radius: 16px;
    }
    /* TODO: Remove once a fix is provided.
      This temporarily gives minions specificity over the ongoing work in dark mode.
      An issue was raised with R&F about minions not needing greater specificity than a compatible theming system */

    .tab-items {
      display: flex;
      flex-wrap: nowrap;
    }
    .tab--active {
      color: var(--color-static-gray100);
      background-color: var(--color-brand);
    }
  `,resources:S`
    p {
      margin-bottom: 24px;
    }
  `,notesWrapper:S`
    border: 1px solid var(--color-tint6);
    border-radius: 4px;

    @media screen and (min-width: 960px) {
      position: sticky;
      max-height: calc(100vh - 68px - 32px);
      overflow-y: scroll;
      top: calc(68px + 16px);
      flex: 1;

      .notes-header {
        top: 0;
      }
    }
  `},_n=Ir(function(){const{episodeId:t}=Ar(),{data:r}=Ze(t),n=We(),s=Lr(),o=te(),c=r.data,d=r.included.find(R=>R.type==="Channel"),u=r.included.find(R=>R.type==="PersonEpisodeProgress"),l=r.included.find(R=>R.type==="Series"),p=r.included.find(R=>R.type==="Speaker"),g=s.search.match(/episode_time_id=(\d+)/),b=g&&r.included.find(R=>R.type==="EpisodeTime"&&R.id===g[1]),y=!!b,[[E],w]=Ge(Pr(r.included,["type","EpisodeResource"]),["attributes.featured",!0]);let v=`church_center.publishing.sermons.episodes.${t}`,_=`/publishing/v2/episodes/${t}/jolt_subscribe`;b&&(v=`${v}.episode_times.${b.id}`,_=`/publishing/v2/episodes/${t}/episode_times/${b.id}/jolt_subscribe`),Br(),$r();const[x,T]=a.useState(""),C=Mr(),A=a.useCallback(async(R,z)=>{try{return z||C.notify(new Error("Jolt connection_id is missing")),(await I.post(_,{data:{attributes:{channel:R,connection_id:z}}})).data.id}catch(B){B.errors[0]?.status==="404"?(alert("This episode cannot be found. It may have been removed."),n(je(d))):console.error("failed to subscribe to Jolt channel",B)}},[d,_,n]);a.useEffect(()=>{T("")},[t]);const D=Je(A,v);return D?f(k,{children:[i(Fr,{title:c.attributes.title,imageUrl:c.attributes.library_art_url,description:c.attributes.description}),i("script",{async:!0,src:"https://js.churchcenter.com/modal/v1"}),i(k,{children:d.attributes.podcast_feed_url&&i("link",{rel:"alternate",type:"application/rss+xml",href:d.attributes.podcast_feed_url,title:d.attributes.podcast_settings.attributes.title})}),i(ti,{title:c.attributes.title,rightType:"share",shareUrl:c.attributes.church_center_url,hideBottomDrawer:!0}),f("div",{className:y?"full-height-col-to-xl":void 0,children:[!o&&f(Or,{children:[i(Pe,{linkUrl:je(d),pageText:d.attributes.name}),i(qr,{}),i(Pe,{pageText:c.attributes.title,isActive:!0})]}),y?i(er,{channel:d,episode:c,episodeResources:w,episodeTime:b,featuredResource:E,joltChannel:D},t):i(ar,{audioDownloadLink:x,channel:d,episode:c,episodeResources:w,featuredResource:E,joltChannel:D,personEpisodeProgress:u,series:l,speaker:p,setAudioDownloadLink:T},t)]})]}):i(Ee,{})});export{_n as default};
//# sourceMappingURL=Episode-DZaN9JJU.js.map
