import{k as a,b as o,x as T,aT as ne,j as m,r as n,F as ae}from"./vendor-CPMdfHCh.js";import{I as se,Q as ce}from"./Bugsnag-uqthnw8J.js";const ie={play:"services#play",pause:"services#pause",skipBack:"general#reload",skipForward:"general#reload"};function k({icon:r,label:e,onClick:t,buttonStyle:s}){return o("button",{css:s,onClick:t,"aria-label":e,children:o(se,{symbol:ie[r],css:r==="skipForward"&&le.flipped})})}function N({size:r,iconSize:e,iconColor:t}){return a`
    width: ${r}px;
    height: ${r}px;
    border-radius: ${r/2}px;
    background-color: transparent;
    box-shadow: none;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: ${t};

    svg {
      width: ${e}px;
      height: ${e}px;
    }
  `}const le={flipped:a`
    transform: scaleX(-1);
  `};T.extend(ne);const F=3600,ue=30;function O(r){const e=Math.floor(r/F),t=Math.floor(r%F/60),s=Math.floor(r%60);return{hours:e,minutes:t,seconds:s}}function y(r){const e=O(r),t=e.hours>0?"H:mm:ss":e.minutes>9?"mm:ss":"m:ss";return r?T.duration(e).format(t):""}function P(r){const e=O(r);return r?T.duration(e).format("[PT]H[H]m[M]s[S]"):"PT0H0M0S"}function z({currentTime:r,duration:e,onChange:t,onKeyDown:s,children:d}){const p=ce();return m("div",{css:D.wrapper,children:[o("progress",{"aria-hidden":"true",css:D.progressBar,max:e,value:r.toFixed(4)}),o("input",{type:"range","aria-label":"Playback position","aria-valuetext":`${y(r)} of ${y(e)}`,css:D.progressInput,disabled:p,onChange:t,onKeyDown:s,value:r.toFixed(4),min:0,max:e,step:"any"}),d]})}const B=a`
  -webkit-appearance: none;
  opacity: 0;
  width: 16px;
  height: 16px;
  border-radius: 8px;
  cursor: pointer;
  background-color: var(--color-brand);
  box-shadow: none;
  transition:
    opacity 0.2s ease-in,
    transform 0.2s ease-in;
  border: none;
  transform: scale(0);
  transform-origin: center center;
`,D={wrapper:a`
    flex: 1;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  `,progressInput:a`
    -webkit-appearance: none;
    height: 8px;
    margin: 0;
    background: transparent;
    position: absolute;
    top: 50%;
    left: -8px;
    right: -8px;
    transform: translateY(-50%);
    z-index: 100;
    cursor: pointer;
    border-radius: 4px;

    &::-webkit-slider-thumb {
      ${B}
    }

    &::-moz-range-thumb {
      ${B}
    }

    &::-moz-range-track {
      background: transparent;
    }
    &::-ms-range-track {
      background: transparent;
    }

    &:hover {
      &::-webkit-slider-thumb {
        opacity: 1;
        transform: scale(1);
      }
      &::-moz-range-thumb {
        opacity: 1;
        transform: scale(1);
      }
    }
  `,progressBar:a`
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border: none;
    width: 100%;
    height: 8px;
    border-radius: 4px;
    background-color: var(--scrubber-track-color, var(--color-static-gray100));
    overflow: hidden;
    border: 1px solid var(--color-tint5);

    &::-webkit-progress-bar {
      background-color: var(
        --scrubber-track-color,
        var(--color-static-gray100)
      );
      border-radius: 4px;
    }

    &::-moz-progress-bar {
      background-color: var(--color-brand);
      border-radius: 4px;
    }

    &::-webkit-progress-value {
      background-color: var(--color-brand);
      border-radius: 4px;
    }
  `},de=48,pe=32,I=N({size:de,iconSize:pe,iconColor:"var(--color-static-gray100)"});function be({isPlaying:r,currentTime:e,duration:t,showSkipButtons:s,togglePlayPause:d,handleSkipBack:p,handleSkipForward:f,handleProgressInputChange:g,handleProgressKeyDown:x}){return m("div",{className:"p-a l-0 r-0 b-0 d-f jc-sb ai-c fd-r p-2 g-1",css:b.wrapper,children:[s&&o("div",{css:b.controlsCell,children:o(k,{icon:"skipBack",label:"Skip back 15 seconds",onClick:p,buttonStyle:I})}),o("div",{css:b.controlsCell,children:o(k,{icon:r?"pause":"play",label:r?"Pause":"Play",onClick:d,buttonStyle:I})}),s&&o("div",{css:b.controlsCell,children:o(k,{icon:"skipForward",label:"Skip forward 30 seconds",onClick:f,buttonStyle:I})}),m(z,{currentTime:e,duration:t,onChange:g,onKeyDown:x,children:[o("time",{css:[b.time,b.timeAbsLeft],dateTime:P(e),className:"fs-4",children:e?y(e):"0:00"}),o("time",{css:[b.time,b.timeAbsRight],dateTime:P(t),className:"fs-4",children:y(t)})]})]})}const b={wrapper:a`
    background-image: linear-gradient(
      to top,
      rgba(0, 0, 0, 0.5),
      rgba(0, 0, 0, 0)
    );
  `,controlsCell:a`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
  `,time:a`
    align-self: flex-end;
    color: var(--color-static-gray100);
  `,timeAbsLeft:a`
    position: absolute;
    bottom: -24px;
    left: 0;
  `,timeAbsRight:a`
    position: absolute;
    bottom: -24px;
    right: 0;
  `},me=40,fe=24,R=N({size:me,iconSize:fe,iconColor:"var(--d-icon-color-status-neutral)"});function ge({isPlaying:r,currentTime:e,duration:t,showSkipButtons:s,togglePlayPause:d,handleSkipBack:p,handleSkipForward:f,handleProgressInputChange:g,handleProgressKeyDown:x}){return m("div",{css:w.wrapper,children:[m("div",{css:w.scrubberRow,children:[o("time",{css:w.time,dateTime:P(e),children:e?y(e):"0:00"}),o(z,{currentTime:e,duration:t,onChange:g,onKeyDown:x}),o("time",{css:w.time,dateTime:P(t),children:y(t)})]}),m("div",{css:w.controlsRow,children:[s&&o(k,{icon:"skipBack",label:"Skip back 15 seconds",onClick:p,buttonStyle:R}),o(k,{icon:r?"pause":"play",label:r?"Pause":"Play",onClick:d,buttonStyle:R}),s&&o(k,{icon:"skipForward",label:"Skip forward 30 seconds",onClick:f,buttonStyle:R})]})]})}const w={wrapper:a`
    --scrubber-track-color: var(--d-fill-color-neutral-090);
    display: flex;
    flex-direction: column;
    gap: 8px;
  `,scrubberRow:a`
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
  `,controlsRow:a`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 20px;
  `,time:a`
    font-size: 14px;
    color: var(--d-text-color-secondary);
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  `},ye=n.forwardRef(function({src:e,initialTime:t=0,onPlay:s,onPause:d,onEnded:p,onError:f,onSeeking:g,showSkipButtons:x=!0,variant:$="overlay"},_){const i=n.useRef(null),[L,A]=n.useState(t),[H,M]=n.useState(0),[U,v]=n.useState(!1),l=n.useRef({onPlay:s,onPause:d,onEnded:p,onError:f,onSeeking:g,initialTime:t});l.current={onPlay:s,onPause:d,onEnded:p,onError:f,onSeeking:g,initialTime:t};const K=()=>A(i.current.currentTime),Z=()=>M(i.current.duration),Q=()=>l.current.onError?.(i.current.error),W=()=>{v(!1),l.current.onEnded?.()},X=()=>{v(!0),l.current.onPlay?.()},Y=()=>{v(!1),l.current.onPause?.()},q=()=>{l.current.initialTime>0&&(i.current.currentTime=l.current.initialTime)},G=()=>l.current.onSeeking?.(!0),J=()=>l.current.onSeeking?.(!1);n.useEffect(()=>{const c=i.current;return()=>{c&&(c.pause(),c.currentTime=0)}},[]);const S=n.useCallback(()=>{i.current?.play().catch(c=>{console.error("Audio play failed:",c),v(!1)})},[]),C=n.useCallback(()=>i.current?.pause(),[]),E=n.useCallback(()=>{i.current?.paused?S():C()},[S,C]),V=n.useCallback(c=>{const u=i.current;u&&(u.currentTime=c)},[]),h=n.useCallback(c=>{const u=i.current;u&&(u.currentTime=u.currentTime+c)},[]);n.useImperativeHandle(_,()=>({play:S,pause:C,get currentTime(){return i.current?.currentTime??0}}),[S,C]);const ee=c=>{const u=parseFloat(c.target.value);V(u),A(u)},re=c=>{switch(c.key){case"j":case"ArrowLeft":h(-1);break;case"l":case"ArrowRight":h(1);break;case"k":case" ":c.preventDefault(),E();break}},te=n.useCallback(()=>h(-15),[h]),oe=n.useCallback(()=>h(ue),[h]),j={isPlaying:U,currentTime:L,duration:H,showSkipButtons:x,togglePlayPause:E,handleSkipBack:te,handleSkipForward:oe,handleProgressInputChange:ee,handleProgressKeyDown:re};return m(ae,{children:[e&&o("audio",{ref:i,src:e,preload:"auto",onTimeUpdate:K,onDurationChange:Z,onEnded:W,onPlay:X,onPause:Y,onError:Q,onLoadedData:q,onSeeking:G,onSeeked:J}),$==="overlay"&&o(be,{...j}),$==="stacked"&&o(ge,{...j})]})});export{ye as A,y as f};
//# sourceMappingURL=AudioPlayerControls-BQLknXSK.js.map
