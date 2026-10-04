import{w as r,a as l,u as n,j as e,b as a,M as d,L as s,S as o,c,O as h,F as m}from"./vendor-CPMdfHCh.js";import{B as f}from"./Bugsnag-uqthnw8J.js";import{G as y}from"./GoogleTagManager-DDCwrwCE.js";import"./styles-FVDiVcL8.js";import"./useLocalStorage-BMP7gFuX.js";function w(){return!1}function x({children:t}){const i=n("root")?.configuration.csrfToken;return e("html",{lang:"en",children:[e("head",{children:[a("meta",{name:"viewport",content:"width=device-width,initial-scale=1.0"}),a("meta",{name:"theme-color",content:"#FAFAFA"}),a("meta",{name:"apple-mobile-web-app-title",content:"Church Center"}),a("link",{rel:"manifest",href:"/manifest.json"}),i&&a("meta",{name:"csrf-token",content:i}),a(d,{}),a(s,{}),a(y,{})]}),e("body",{className:"sans-serif",children:[a("a",{href:"/platform-admin",rel:"nofollow",style:{display:"none"},"aria-hidden":"true",children:"Platform Admin"}),a("a",{href:"#main_page_content",className:"screen-reader-text",children:"Skip to content"}),t,a("noscript",{children:e("div",{style:{margin:"4rem auto",maxWidth:600,padding:"1rem"},children:["Church Center requires JavaScript to be enabled.",a("br",{}),a("br",{}),"Here are some"," ",a("a",{href:"https://www.enable-javascript.com/",children:"instructions to enable JavaScript in your web browser"}),"."]})}),a(o,{}),a(c,{})]})]})}const N=r(function(){return a(f,{children:a(h,{})})}),S=l(function(){return e(m,{children:[a("script",{dangerouslySetInnerHTML:{__html:`
    if (typeof window !== "undefined" && new URLSearchParams(window.location.search).get("theme") === "dark") {
      document.documentElement.classList.add("hydrate-dark");
    }
  `}}),a("style",{dangerouslySetInnerHTML:{__html:`
    @keyframes shimmer {
      0% { background-position: -400px 0; }
      100% { background-position: 400px 0; }
    }
    .hydrate-fallback-shimmer {
      background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
      background-size: 800px 100%;
      animation: shimmer 1.5s infinite linear;
      border-radius: 4px;
    }
    .hydrate-fallback-header {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 136px;
      background-color: #fafafa;
      border-bottom: 1px solid #f2f2f2;
    }
    .hydrate-fallback-header-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 900px;
      padding: 24px 32px 24px 24px;
    }
    .hydrate-fallback-body {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      background-color: #ffffff;
    }
    .hydrate-fallback-nav {
      display: none;
    }
    .hydrate-fallback-nav-burger {
      display: block;
    }
    .hydrate-dark .hydrate-fallback-shimmer {
      background: linear-gradient(90deg, #2a2a2a 25%, #3a3a3a 50%, #2a2a2a 75%);
      background-size: 800px 100%;
    }
    .hydrate-dark .hydrate-fallback-header {
      background-color: #1a1a1a;
      border-bottom-color: #2a2a2a;
    }
    .hydrate-dark .hydrate-fallback-body {
      background-color: #111111;
    }
    .hydrate-fallback-loading {
      font-size: 16px;
      color: hsl(0, 0%, 81%);
      display: flex;
      justify-content: center;
      padding: 1.5rem;
    }
    .hydrate-dark .hydrate-fallback-loading {
      color: hsl(0, 0%, 32%);
    }
    .hydrate-fallback-dot-1 {
      animation: dot1 1.4s infinite step-end;
    }
    .hydrate-fallback-dot-2 {
      animation: dot2 1.4s infinite step-end;
    }
    .hydrate-fallback-dot-3 {
      animation: dot3 1.4s infinite step-end;
    }
    @keyframes dot1 {
      0%, 25% { visibility: hidden; }
      25.1%, 100% { visibility: visible; }
    }
    @keyframes dot2 {
      0%, 50% { visibility: hidden; }
      50.1%, 100% { visibility: visible; }
    }
    @keyframes dot3 {
      0%, 75% { visibility: hidden; }
      75.1%, 100% { visibility: visible; }
    }
    @media screen and (min-width: 720px) {
      .hydrate-fallback-nav {
        display: flex;
      }
      .hydrate-fallback-nav-burger {
        display: none;
      }
      .hydrate-fallback-loading {
        padding: 2rem;
      }
    }
  `}}),e("div",{className:"hydrate-fallback-body",children:[a("header",{className:"hydrate-fallback-header",children:e("div",{className:"hydrate-fallback-header-content",children:[a("div",{className:"hydrate-fallback-shimmer",style:{width:200,height:20}}),e("div",{className:"hydrate-fallback-nav",style:{gap:24,alignItems:"center"},children:[a("div",{className:"hydrate-fallback-shimmer",style:{width:48,height:14}}),a("div",{className:"hydrate-fallback-shimmer",style:{width:56,height:14}}),a("div",{className:"hydrate-fallback-shimmer",style:{width:40,height:14}}),a("div",{className:"hydrate-fallback-shimmer",style:{width:52,height:14}}),a("div",{className:"hydrate-fallback-shimmer",style:{width:44,height:14}})]}),a("div",{className:"hydrate-fallback-shimmer hydrate-fallback-nav-burger",style:{width:40,height:36}})]})}),a("div",{className:"hydrate-fallback-loading",children:e("span",{children:["Loading",a("span",{className:"hydrate-fallback-dot-1",children:"."}),a("span",{className:"hydrate-fallback-dot-2",children:"."}),a("span",{className:"hydrate-fallback-dot-3",children:"."})]})})]})]})});export{S as HydrateFallback,x as Layout,N as default,w as shouldRevalidate};
//# sourceMappingURL=root-DmccKtbu.js.map
