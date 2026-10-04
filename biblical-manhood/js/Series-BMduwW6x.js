import{k as p,w as u,f as b,b as r,j as t,F as h}from"./vendor-CPMdfHCh.js";import{u as g}from"./SessionApiResource-BS2aBwQ1.js";import{b as f,O as x,f as v,g as o,h as _,i as w}from"./Bugsnag-uqthnw8J.js";import{E as N}from"./Error404-Vj-ClAYf.js";import{L as y}from"./Channel-BUgHe8b4.js";import{N as B}from"./NativeHeader-BdWIPdgm.js";import{u as I}from"./queries-BgMR0Pci.js";import"./styles-FVDiVcL8.js";import"./useLocalStorage-BMP7gFuX.js";import"./MediaThumbnail-DCkIAfbz.js";import"./DatetimeFmt-HavA5_TF.js";import"./routes-Nyzx--Ux.js";import"./useNotifyNativeLoaded-CAbwnrpo.js";import"./getRelationship-BEK6WIgv.js";import"./RootErrorBoundaryLayout-Cp1Yeyt8.js";import"./isFirstAttemptForPathname-Brb7p_u3.js";const L=p`
  @media (max-width: 719px) {
    max-width: 100vw;
    margin-top: -1.5rem;
    margin-inline: -24px;

    [data-cca-platform="ios"] & {
      margin-inline: -20px;
    }

    [data-cca-platform="android"] & {
      margin-inline: -16px;
    }
  }
`,M=u(function(){const{channelId:a,seriesId:i}=b(),s=g(`/publishing/v2/channels/${a}/series/${i}`),{data:{data:n}}=I(a);if(f(),s.errors?.[0]?.status==="404")return r(N,{});const e=s.data,{art:d,description:c,title:m}=e.attributes,l=e.attributes.art.attributes.variants.medium;return t(h,{children:[r(x,{title:m,imageUrl:d.attributes.variants.small,description:c}),r(B,{title:m,rightType:"share",shareUrl:`${e.attributes.church_center_url}`}),t(v,{children:[r(o,{linkUrl:`/channels/${a}`,pageText:n.attributes.name}),r(_,{}),r(o,{pageText:e.attributes.title,isActive:!0})]}),t("div",{className:"d-f@md fd-r mb-3 pb-3",style:{borderBottom:"1px solid var(--color-tint7)"},children:[r("div",{className:"w-48%@md item-show__image",css:L,children:r("img",{className:"d-b aspect-16-9",alt:"Series art",src:l})}),t("div",{className:"f-1 d-f fd-c g-4p g-1@md pl-6@md",children:[r(w,{level:1,text:e.attributes.title}),e.attributes.description&&r("p",{className:"mb-0",children:e.attributes.description})]})]}),r(y,{queryParams:{"where[series_id]":i,filter:"published_to_library",order:"-published_to_library_at"}})]})});export{M as default};
//# sourceMappingURL=Series-BMduwW6x.js.map
