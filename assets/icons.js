/* assets/icons.js - the ONE icon sprite, and it is a script for one measured reason.

   Every screen and every kit page loads this file once and reaches a glyph as
   <use href="#i-name">. No document carries a copy.

   WHY A SCRIPT AND NOT THE .svg IT WAS FOR ONE DAY. On 2026-08-09 this became
   assets/icons.svg, referenced as <use href="../assets/icons.svg#i-name">, and that
   is a CROSS-DOCUMENT reference. file:// gives every file its own opaque origin, so
   a page opened by double-clicking it resolved none of them: measured, 0 of 34 glyphs
   drawn on event-feed.html and 39 console errors, while the stroked inline marks beside
   them drew fine. The price was written into every page and it was still the wrong
   trade, because THESE PAGES ARE READ FROM DISK. A script has no such rule: it loads
   from file:// and from a server alike, so the sprite is injected into the document and
   every <use> is same-document again. Measured both ways before this file was written.

   Solar, by 480 Design, licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
   No path data is altered. Two symbols are composed differently and ../NOTICE.md says
   which and why. The ink is NOT here: it comes from the referencing element through
   currentColor.

   TWO FAMILIES SINCE 2026-08-13, AND THE PREFIX IS THE DIFFERENCE. `#i-` is Solar filled,
   29 symbols. `#l-` is the line family, 6 symbols, and they are NOT Solar: they are the
   product's own two-stroke drawings, which is why a cross has no interior and why the
   consolidation of 2026-08-09 could not fill them. `components/base.css` keys its filled
   floor to `#i-`, so a symbol declares its family by its name and no document has to.

   A copy in 121 places is a copy that drifts, which is why there is one file at all:
   i-bookmark-b was TWO different drawings, the product's on 111 documents and an older
   one on 3 kit pages, and nothing could see it because every copy is internally
   consistent. A symbol deleted here disappears from every document silently, because
   <use> fails without a word. That is the price of one file and it is paid by reading.

   No em dash. */
(function () {
  var SYMBOLS = [
    '<symbol id="i-bell-b" viewBox="0 0 24 24"><path fill="currentColor" d="M18.75 9.71v-.705C18.75 5.136 15.726 2 12 2S5.25 5.136 5.25 9.005v.705a4.4 4.4 0 0 1-.692 2.375L3.45 13.81c-1.011 1.575.062 3.68 1.966 3.843a51 51 0 0 0 13.167 0c1.904-.163 2.977-2.268 1.966-3.843l-1.108-1.725a4.4 4.4 0 0 1-.692-2.375"/><path fill="currentColor" d="M7.243 18.545a5.002 5.002 0 0 0 9.513 0c-3.145.28-6.367.281-9.513 0"/></symbol>',
    '<symbol id="i-bookmark-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M21 11.098v4.993c0 3.096 0 4.645-.734 5.321c-.35.323-.792.526-1.263.58c-.987.113-2.14-.907-4.445-2.946c-1.02-.901-1.529-1.352-2.118-1.47a2.2 2.2 0 0 0-.88 0c-.59.118-1.099.569-2.118 1.47c-2.305 2.039-3.458 3.059-4.445 2.945a2.24 2.24 0 0 1-1.263-.579C3 20.736 3 19.188 3 16.091v-4.994C3 6.81 3 4.666 4.318 3.333S7.758 2 12 2s6.364 0 7.682 1.332S21 6.81 21 11.098M8.25 6A.75.75 0 0 1 9 5.25h6a.75.75 0 0 1 0 1.5H9A.75.75 0 0 1 8.25 6" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-cat-crypto" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2S2 6.477 2 12s4.477 10 10 10m.75-16a.75.75 0 0 0-1.5 0v.317c-1.63.292-3 1.517-3 3.183c0 1.917 1.813 3.25 3.75 3.25c1.377 0 2.25.906 2.25 1.75s-.873 1.75-2.25 1.75c-1.376 0-2.25-.906-2.25-1.75a.75.75 0 0 0-1.5 0c0 1.666 1.37 2.891 3 3.183V18a.75.75 0 0 0 1.5 0v-.317c1.63-.292 3-1.517 3-3.183c0-1.917-1.813-3.25-3.75-3.25c-1.376 0-2.25-.906-2.25-1.75s.874-1.75 2.25-1.75c1.377 0 2.25.906 2.25 1.75a.75.75 0 0 0 1.5 0c0-1.666-1.37-2.891-3-3.183z" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-cat-culture" viewBox="0 0 24 24"><path fill="currentColor" d="m21.537 9.136l-.846 3.297c-.43 1.676-1.306 2.855-2.336 3.685c.219-1.144.214-2.418-.144-3.814l-.864-3.37l-.15-.584a.9.9 0 0 1 .599-.044c.378.101.608.406.637.702a.75.75 0 1 0 1.493-.145c-.091-.942-.783-1.749-1.742-2.006a2.4 2.4 0 0 0-1.418.05l-.017-.044c-.224-.596-.552-1.229-1.171-1.693a3.5 3.5 0 0 0-1.13-.562c-.759-.215-1.463-.076-2.064.124c-.558.185-1.21.49-1.924.825l-.072.034c-1.185.555-1.659.773-2.144.928q-.22.07-.446.127l.327-1.267c.44-1.719.661-2.578 1.236-3.01c.193-.145.41-.252.638-.317c.684-.194 1.461.17 3.015.897c1.15.54 1.726.809 2.326 1q.314.099.632.176c.612.149 1.239.216 2.493.351c1.694.182 2.54.273 3.04.798c.167.177.303.383.4.609c.292.675.072 1.534-.368 3.253"/><path fill="currentColor" fill-rule="evenodd" d="m16.758 12.677l-.845-3.298c-.44-1.719-.66-2.578-1.236-3.01a2 2 0 0 0-.638-.317c-.684-.194-1.46.17-3.015.897c-1.15.54-1.726.809-2.326 1a10 10 0 0 1-.632.176c-.611.149-1.238.216-2.493.351c-1.694.182-2.54.273-3.04.798a2.1 2.1 0 0 0-.4.609c-.292.675-.072 1.534.369 3.253l.845 3.297c.993 3.876 4.296 5.096 6.516 5.473c.677.115 1.016.172 2.044-.116s1.294-.514 1.825-.968c1.742-1.487 4.02-4.27 3.026-8.145m-10.753.691c.029-.296.26-.6.638-.702c.379-.102.73.047.903.29a.75.75 0 0 0 1.22-.873c-.55-.77-1.552-1.123-2.511-.866s-1.651 1.064-1.743 2.006a.75.75 0 0 0 1.493.145m5.796-1.553c.029-.296.26-.6.638-.702c.379-.102.73.047.903.289a.75.75 0 1 0 1.22-.872c-.55-.77-1.552-1.123-2.511-.866s-1.651 1.063-1.743 2.006a.75.75 0 0 0 1.493.145m1.846 3.814a.75.75 0 0 1-.885 1.211l-.01-.006a2 2 0 0 0-.485-.2c-.36-.098-.929-.163-1.685.04c-.756.202-1.216.543-1.48.808a2 2 0 0 0-.32.416l-.005.01a.75.75 0 0 1-1.372-.607l.688.298c-.688-.298-.687-.3-.687-.3v-.001l.002-.004l.004-.009l.01-.022l.033-.064q.04-.078.115-.196c.1-.156.252-.36.468-.578c.437-.44 1.125-.924 2.156-1.2c1.031-.277 1.87-.2 2.467-.038c.296.08.53.18.694.266a3 3 0 0 1 .258.151l.02.015l.008.005l.003.003h.002z" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-cat-fire" viewBox="0 0 24 24"><path fill="currentColor" d="M12.832 21.801c3.126-.626 7.168-2.875 7.168-8.69c0-5.291-3.873-8.815-6.658-10.434c-.619-.36-1.342.113-1.342.828v1.828c0 1.442-.606 4.074-2.29 5.169c-.86.559-1.79-.278-1.894-1.298l-.086-.838c-.1-.974-1.092-1.565-1.87-.971C4.461 8.46 3 10.33 3 13.11C3 20.221 8.289 22 10.933 22q.232 0 .484-.015C10.111 21.874 8 21.064 8 18.444c0-2.05 1.495-3.435 2.631-4.11c.306-.18.663.055.663.41v.59c0 .45.175 1.155.59 1.637c.47.546 1.159-.026 1.214-.744c.018-.226.246-.37.442-.256c.641.375 1.46 1.175 1.46 2.473c0 2.048-1.129 2.99-2.168 3.357"/></symbol>',
    '<symbol id="i-cat-general" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M2 6.634a4.634 4.634 0 1 1 9.268 0a4.634 4.634 0 0 1-9.268 0m10.732 10.732a4.634 4.634 0 1 1 9.268 0a4.634 4.634 0 0 1-9.268 0" clip-rule="evenodd"/><path fill="currentColor" d="M2 17.5c0-2.121 0-3.182.659-3.841S4.379 13 6.5 13s3.182 0 3.841.659S11 15.379 11 17.5s0 3.182-.659 3.841S8.621 22 6.5 22s-3.182 0-3.841-.659S2 19.621 2 17.5m11-11c0-2.121 0-3.182.659-3.841S15.379 2 17.5 2s3.182 0 3.841.659S22 4.379 22 6.5s0 3.182-.659 3.841S19.621 11 17.5 11s-3.182 0-3.841-.659S13 8.621 13 6.5"/></symbol>',
    '<symbol id="i-cat-politics" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M21.25 8.5c0-1.404 0-2.107-.337-2.611a2 2 0 0 0-.552-.552c-.441-.295-1.034-.332-2.115-.336q.005.438.004.91V7.25h1a.75.75 0 0 1 0 1.5h-1v1.5h1a.75.75 0 0 1 0 1.5h-1v1.5h1a.75.75 0 0 1 0 1.5h-1v6.5h-1.5V6c0-1.886 0-2.828-.586-3.414S14.636 2 12.75 2h-2c-1.886 0-2.828 0-3.414.586S6.75 4.114 6.75 6v15.25h-1.5v-6.5h-1a.75.75 0 0 1 0-1.5h1v-1.5h-1a.75.75 0 0 1 0-1.5h1v-1.5h-1a.75.75 0 0 1 0-1.5h1V5.91q-.001-.47.004-.91c-1.081.005-1.674.042-2.115.337a2 2 0 0 0-.552.552C2.25 6.393 2.25 7.096 2.25 8.5v12.75h-.5a.75.75 0 0 0 0 1.5h20a.75.75 0 0 0 0-1.5h-.5zM9 11.75a.75.75 0 0 1 .75-.75h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1-.75-.75m0 3a.75.75 0 0 1 .75-.75h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1-.75-.75m2.75 3.5a.75.75 0 0 1 .75.75v2.25H11V19a.75.75 0 0 1 .75-.75M9 6.25a.75.75 0 0 1 .75-.75h4a.75.75 0 0 1 0 1.5h-4A.75.75 0 0 1 9 6.25m0 3a.75.75 0 0 1 .75-.75h4a.75.75 0 0 1 0 1.5h-4A.75.75 0 0 1 9 9.25" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-chat-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2S2 6.477 2 12c0 1.6.376 3.112 1.043 4.453c.178.356.237.763.134 1.148l-.595 2.226a1.3 1.3 0 0 0 1.591 1.592l2.226-.596a1.63 1.63 0 0 1 1.149.133A9.96 9.96 0 0 0 12 22"/></symbol>',
    '<symbol id="i-check-circle-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M22 12c0 5.523-4.477 10-10 10S2 17.523 2 12S6.477 2 12 2s10 4.477 10 10m-5.97-3.03a.75.75 0 0 1 0 1.06l-5 5a.75.75 0 0 1-1.06 0l-2-2a.75.75 0 1 1 1.06-1.06l1.47 1.47l2.235-2.235L14.97 8.97a.75.75 0 0 1 1.06 0" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-clock-circle-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M22 12c0 5.523-4.477 10-10 10S2 17.523 2 12S6.477 2 12 2s10 4.477 10 10M12 7.25a.75.75 0 0 1 .75.75v3.69l2.28 2.28a.75.75 0 1 1-1.06 1.06l-2.5-2.5a.75.75 0 0 1-.22-.53V8a.75.75 0 0 1 .75-.75"/></symbol>',
    '<symbol id="i-danger-triangle-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M5.312 10.762C8.23 5.587 9.689 3 12 3s3.77 2.587 6.688 7.762l.364.644c2.425 4.3 3.638 6.45 2.542 8.022S17.786 21 12.364 21h-.728c-5.422 0-8.134 0-9.23-1.572s.117-3.722 2.542-8.022zM12 7.25a.75.75 0 0 1 .75.75v5a.75.75 0 0 1-1.5 0V8a.75.75 0 0 1 .75-.75M12 17a1 1 0 1 0 0-2a1 1 0 0 0 0 2" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-global-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M2.028 11.25A10 10 0 0 1 12 2c-.83 0-1.57.364-2.18.921c-.605.554-1.116 1.328-1.53 2.242c-.416.92-.74 1.996-.959 3.163a20 20 0 0 0-.318 2.924zm0 1.5h4.985c.036 1.002.143 1.988.318 2.924c.22 1.167.543 2.243.959 3.163c.414.914.925 1.688 1.53 2.242c.61.557 1.35.921 2.18.921c-5.27 0-9.589-4.077-9.972-9.25" clip-rule="evenodd"/><path fill="currentColor" d="M12 3.395c-.275 0-.63.117-1.043.495c-.416.381-.833.978-1.201 1.791c-.366.808-.663 1.783-.867 2.873c-.16.858-.26 1.768-.296 2.696h6.814a18.5 18.5 0 0 0-.296-2.696c-.204-1.09-.5-2.065-.867-2.873c-.368-.813-.784-1.41-1.2-1.79c-.414-.379-.769-.496-1.044-.496M8.889 15.446c.204 1.09.501 2.065.867 2.873c.368.813.785 1.41 1.2 1.79c.414.379.77.496 1.044.496c.275 0 .63-.117 1.043-.495c.417-.381.833-.978 1.201-1.791c.366-.808.663-1.783.867-2.873c.161-.858.261-1.768.296-2.696H8.593c.035.928.135 1.838.296 2.696"/><path fill="currentColor" d="M12 2c.831 0 1.57.364 2.18.921c.605.554 1.117 1.328 1.53 2.242c.417.92.74 1.996.959 3.163c.175.936.282 1.922.318 2.924h4.985A10 10 0 0 0 12 2m4.669 13.674c-.219 1.167-.542 2.243-.959 3.163c-.413.914-.925 1.688-1.53 2.242c-.61.557-1.349.921-2.18.921c5.27 0 9.589-4.077 9.972-9.25h-4.985a20 20 0 0 1-.318 2.924"/></symbol>',
    '<symbol id="i-graph-up-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.464 3.464C2 4.93 2 7.286 2 12s0 7.071 1.464 8.535C4.93 22 7.286 22 12 22s7.071 0 8.535-1.465C22 19.072 22 16.714 22 12s0-7.071-1.465-8.536C19.072 2 16.714 2 12 2S4.929 2 3.464 3.464M13.75 10c0 .414.336.75.75.75h.69l-2.013 2.013a.25.25 0 0 1-.354 0l-1.586-1.586a1.75 1.75 0 0 0-2.474 0L6.47 13.47a.75.75 0 1 0 1.06 1.06l2.293-2.293a.25.25 0 0 1 .354 0l1.586 1.586a1.75 1.75 0 0 0 2.474 0l2.013-2.012v.689a.75.75 0 0 0 1.5 0V10a.75.75 0 0 0-.75-.75h-2.5a.75.75 0 0 0-.75.75" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-heart-b" viewBox="0 0 24 24"><path fill="currentColor" d="M2 9.137C2 14 6.02 16.591 8.962 18.911C10 19.729 11 20.5 12 20.5s2-.77 3.038-1.59C17.981 16.592 22 14 22 9.138s-5.5-8.406-10-3.985C7.5.735 2 4.275 2 9.137"/></symbol>',
    '<symbol id="i-inbox-b" viewBox="0 0 24 24"><path fill="currentColor" d="M3.464 20.536C4.93 22 7.286 22 12 22s7.071 0 8.535-1.465c1.271-1.27 1.44-3.213 1.462-6.785H18.84c-.974 0-1.229.016-1.442.114c-.214.099-.392.282-1.026 1.02l-.605.707l-.088.102c-.502.587-.9 1.052-1.45 1.305s-1.162.253-1.934.252h-.589c-.773 0-1.385.002-1.935-.252c-.55-.253-.948-.718-1.45-1.305l-.088-.102l-.605-.706c-.634-.74-.812-.922-1.026-1.02c-.213-.099-.468-.115-1.442-.115H2.003c.023 3.572.19 5.515 1.461 6.785"/><path fill="currentColor" d="M20.536 3.464C19.07 2 16.714 2 12 2S4.929 2 3.464 3.464C2 4.93 2 7.286 2 12v.25h3.295c.772 0 1.384-.002 1.934.252c.55.253.948.718 1.45 1.305l.088.102l.605.706c.634.74.812.922 1.026 1.02c.213.099.468.115 1.442.115h.32c.974 0 1.229-.016 1.442-.114c.214-.099.392-.282 1.026-1.02l.605-.707l.088-.102c.502-.587.9-1.052 1.45-1.305c.55-.254 1.162-.253 1.935-.252H22V12c0-4.714 0-7.071-1.465-8.536"/></symbol>',
    '<symbol id="i-info-circle-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M22 12c0 5.523-4.477 10-10 10S2 17.523 2 12S6.477 2 12 2s10 4.477 10 10m-10 5.75a.75.75 0 0 0 .75-.75v-6a.75.75 0 0 0-1.5 0v6c0 .414.336.75.75.75M12 7a1 1 0 1 1 0 2a1 1 0 0 1 0-2" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-list-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.25 7A.75.75 0 0 1 4 6.25h16a.75.75 0 0 1 0 1.5H4A.75.75 0 0 1 3.25 7m0 5a.75.75 0 0 1 .75-.75h11a.75.75 0 0 1 0 1.5H4a.75.75 0 0 1-.75-.75m0 5a.75.75 0 0 1 .75-.75h5a.75.75 0 0 1 0 1.5H4a.75.75 0 0 1-.75-.75" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-login-3-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.5 9.568v4.864c0 2.294 0 3.44.722 4.153c.655.647 1.674.706 3.596.712l-.015-.105c-.115-.844-.115-1.916-.115-3.247v-.053c0-.403.331-.73.74-.73c.408 0 .739.327.739.73c0 1.396.001 2.37.101 3.105c.098.714.275 1.093.548 1.362s.656.445 1.379.54c.744.1 1.731.101 3.146.101h.985c1.415 0 2.401-.002 3.146-.1c.723-.096 1.106-.272 1.378-.541c.273-.27.451-.648.548-1.362c.1-.734.102-1.709.102-3.105V8.108c0-1.397-.002-2.37-.102-3.105c-.097-.714-.275-1.093-.547-1.362c-.273-.27-.656-.445-1.38-.54C17.728 3 16.742 3 15.327 3h-.985c-1.415 0-2.402.002-3.146.1c-.723.096-1.106.272-1.379.541c-.273.27-.45.648-.548 1.362c-.1.734-.101 1.708-.101 3.105c0 .403-.331.73-.74.73a.734.734 0 0 1-.739-.73v-.053c0-1.33 0-2.403.115-3.247l.015-.105c-1.922.006-2.94.065-3.596.712c-.722.713-.722 1.86-.722 4.153m9.885 5.38l2.464-2.432a.723.723 0 0 0 0-1.032l-2.464-2.432a.746.746 0 0 0-1.045 0a.723.723 0 0 0 0 1.032l1.202 1.186H6.457a.734.734 0 0 0-.74.73c0 .403.331.73.74.73h7.085l-1.202 1.186a.723.723 0 0 0 0 1.032a.746.746 0 0 0 1.045 0" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-magnifer-o" viewBox="0 0 24 24"><g transform="translate(0.8472 0.8472) scale(0.9294)"><path fill="currentColor" fill-rule="evenodd" d="M11.5 2.75a8.75 8.75 0 1 0 0 17.5a8.75 8.75 0 0 0 0-17.5M1.25 11.5c0-5.66 4.59-10.25 10.25-10.25S21.75 5.84 21.75 11.5c0 2.56-.939 4.902-2.491 6.698l3.271 3.272a.75.75 0 1 1-1.06 1.06l-3.272-3.271A10.2 10.2 0 0 1 11.5 21.75c-5.66 0-10.25-4.59-10.25-10.25" clip-rule="evenodd"/></g></symbol>',
    '<symbol id="i-seo-chart" viewBox="0 0 24 24"><path fill="currentColor" d="M5 21a1.5 1.5 0 0 1-1.5-1.5v-3a1.5 1.5 0 0 1 3 0v3A1.5 1.5 0 0 1 5 21m7 0a1.5 1.5 0 0 1-1.5-1.5v-8a1.5 1.5 0 0 1 3 0v8A1.5 1.5 0 0 1 12 21m7 0a1.5 1.5 0 0 1-1.5-1.5V6a1.5 1.5 0 0 1 3 0v13.5A1.5 1.5 0 0 1 19 21"/></symbol>',
    '<symbol id="i-seo-guide" viewBox="0 0 24 24"><path fill="currentColor" d="M11 4.2C9.6 3.3 7.9 2.8 6 2.8c-1.1 0-2.1.2-3 .5C2.4 3.5 2 4 2 4.6v12.2c0 .9.9 1.5 1.7 1.2c.7-.2 1.5-.3 2.3-.3c1.8 0 3.4.6 4.6 1.5c.2.2.5.3.8.3V5c-.1-.3-.2-.6-.4-.8m2 0c-.2.2-.3.5-.4.8v14.5c.3 0 .6-.1.8-.3c1.2-.9 2.8-1.5 4.6-1.5c.8 0 1.6.1 2.3.3c.8.3 1.7-.3 1.7-1.2V4.6c0-.6-.4-1.1-1-1.3c-.9-.3-1.9-.5-3-.5c-1.9 0-3.6.5-5 1.4"/></symbol>',
    '<symbol id="i-seo-qa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a6 6 0 0 0-6 6a1.5 1.5 0 0 0 3 0a3 3 0 1 1 4.3 2.7c-1.1.6-2.8 1.7-2.8 3.8v.5a1.5 1.5 0 0 0 3 0v-.5c0-.3.4-.7 1.1-1.1A6 6 0 0 0 12 2m0 16.5A1.75 1.75 0 1 0 12 22a1.75 1.75 0 0 0 0-3.5"/></symbol>',
    '<symbol id="i-share-b" viewBox="0 0 24 24"><path fill="currentColor" d="M13.803 5.333c0-1.84 1.507-3.333 3.365-3.333c1.86 0 3.366 1.492 3.366 3.333c0 1.841-1.507 3.334-3.366 3.334a3.38 3.38 0 0 1-2.037-.678l-4.67 3.204a3.3 3.3 0 0 1 0 1.62l4.67 3.204a3.38 3.38 0 0 1 2.037-.677c1.86 0 3.366 1.492 3.366 3.333S19.028 22 17.168 22c-1.858 0-3.365-1.492-3.365-3.333q0-.413.098-.804l-4.67-3.204a3.38 3.38 0 0 1-2.037.677C5.507 15.336 4 13.843 4 12.002s1.507-3.333 3.365-3.333c.762 0 1.474.252 2.037.677l4.67-3.204a3.3 3.3 0 0 1-.099-.809"/></symbol>',
    '<symbol id="i-shield-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.378 5.082C3 5.62 3 7.22 3 10.417v1.574c0 5.638 4.239 8.375 6.899 9.536c.721.315 1.082.473 2.101.473c1.02 0 1.38-.158 2.101-.473C16.761 20.365 21 17.63 21 11.991v-1.574c0-3.198 0-4.797-.378-5.335c-.377-.537-1.88-1.052-4.887-2.081l-.573-.196C13.595 2.268 12.812 2 12 2s-1.595.268-3.162.805L8.265 3c-3.007 1.03-4.51 1.545-4.887 2.082M15.06 10.5a.75.75 0 0 0-1.12-.999l-3.011 3.374l-.87-.974a.75.75 0 0 0-1.118 1l1.428 1.6a.75.75 0 0 0 1.119 0z" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-sort-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3.464 20.536C4.93 22 7.286 22 12 22s7.071 0 8.535-1.465C22 19.072 22 16.714 22 12s0-7.071-1.465-8.536C19.072 2 16.714 2 12 2S4.929 2 3.464 3.464C2 4.93 2 7.286 2 12s0 7.071 1.464 8.535M14.75 16a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75M16 12.75a.75.75 0 0 0 0-1.5H8a.75.75 0 0 0 0 1.5zM18.75 8a.75.75 0 0 1-.75.75H6a.75.75 0 0 1 0-1.5h12a.75.75 0 0 1 .75.75" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-transfer-horizontal-b" viewBox="0 0 24 24"><path fill="currentColor" d="M10.25 4a.75.75 0 0 0-1.303-.507l-5.5 6A.75.75 0 0 0 4 10.75h16a.75.75 0 0 0 0-1.5h-9.75zm3.5 16v-5.25H4a.75.75 0 0 1 0-1.5h16a.75.75 0 0 1 .553 1.257l-5.5 6A.75.75 0 0 1 13.75 20"/></symbol>',
    '<symbol id="i-user-b" viewBox="0 0 24 24"><circle cx="12" cy="6" r="4" fill="currentColor"/><path fill="currentColor" d="M20 17.5c0 2.485 0 4.5-8 4.5s-8-2.015-8-4.5S7.582 13 12 13s8 2.015 8 4.5"/></symbol>',
    '<symbol id="i-verified-b" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M9.592 3.2a6 6 0 0 1-.495.399c-.298.2-.633.338-.985.408c-.153.03-.313.043-.632.068c-.801.064-1.202.096-1.536.214a2.71 2.71 0 0 0-1.655 1.655c-.118.334-.15.735-.214 1.536a6 6 0 0 1-.068.632c-.07.352-.208.687-.408.985c-.087.13-.191.252-.399.495c-.521.612-.782.918-.935 1.238c-.353.74-.353 1.6 0 2.34c.153.32.414.626.935 1.238c.208.243.312.365.399.495c.2.298.338.633.408.985c.03.153.043.313.068.632c.064.801.096 1.202.214 1.536a2.71 2.71 0 0 0 1.655 1.655c.334.118.735.15 1.536.214c.319.025.479.038.632.068c.352.07.687.209.985.408c.13.087.252.191.495.399c.612.521.918.782 1.238.935c.74.353 1.6.353 2.34 0c.32-.153.626-.414 1.238-.935c.243-.208.365-.312.495-.399c.298-.2.633-.338.985-.408c.153-.03.313-.043.632-.068c.801-.064 1.202-.096 1.536-.214a2.71 2.71 0 0 0 1.655-1.655c.118-.334.15-.735.214-1.536c.025-.319.038-.479.068-.632c.07-.352.209-.687.408-.985c.087-.13.191-.252.399-.495c.521-.612.782-.918.935-1.238c.353-.74.353-1.6 0-2.34c-.153-.32-.414-.626-.935-1.238a6 6 0 0 1-.399-.495a2.7 2.7 0 0 1-.408-.985a6 6 0 0 1-.068-.632c-.064-.801-.096-1.202-.214-1.536a2.71 2.71 0 0 0-1.655-1.655c-.334-.118-.735-.15-1.536-.214a6 6 0 0 1-.632-.068a2.7 2.7 0 0 1-.985-.408a6 6 0 0 1-.495-.399c-.612-.521-.918-.782-1.238-.935a2.71 2.71 0 0 0-2.34 0c-.32.153-.626.414-1.238.935m6.781 6.663a.814.814 0 0 0-1.15-1.15l-4.85 4.85l-1.596-1.595a.814.814 0 0 0-1.15 1.15l2.17 2.17a.814.814 0 0 0 1.15 0z" clip-rule="evenodd"/></symbol>',
    '<symbol id="i-widget-b" viewBox="0 0 24 24"><path fill="currentColor" d="M2 6.5c0-2.121 0-3.182.659-3.841S4.379 2 6.5 2s3.182 0 3.841.659S11 4.379 11 6.5s0 3.182-.659 3.841S8.621 11 6.5 11s-3.182 0-3.841-.659S2 8.621 2 6.5m11 11c0-2.121 0-3.182.659-3.841S15.379 13 17.5 13s3.182 0 3.841.659S22 15.379 22 17.5s0 3.182-.659 3.841S19.621 22 17.5 22s-3.182 0-3.841-.659S13 19.621 13 17.5m-11 0c0-2.121 0-3.182.659-3.841S4.379 13 6.5 13s3.182 0 3.841.659S11 15.379 11 17.5s0 3.182-.659 3.841S8.621 22 6.5 22s-3.182 0-3.841-.659S2 19.621 2 17.5m11-11c0-2.121 0-3.182.659-3.841S15.379 2 17.5 2s3.182 0 3.841.659S22 4.379 22 6.5s0 3.182-.659 3.841S19.621 11 17.5 11s-3.182 0-3.841-.659S13 8.621 13 6.5"/></symbol>',
    /* THE ONE PLUS THAT IS NOT A LINE, added 2026-08-13. `.bal-add` is the only control in the
       product standing on a SOLID brass ground: its mark is not beside a word, the mark IS the
       button, and a 1.65px stroke on a filled disc reads as unfinished next to the Solar mass of
       the swap and the bookmark either side of it. The rule "a movement is a line" was written for
       a mark on a transparent ground beside a label and this placement is not that, so the
       exception is a NAME here rather than a stroke override in a component.
       AND THE LINE PLUS IS GONE WITH IT, WHICH IS NOT WHAT THE DECISION EXPECTED. The choice was
       taken as "filled on this control, line on the other 84", and there are no other 84: **all
       85 plus marks in the product stand on `.bal-add`**, so the product's plus IS filled and
       `#l-plus` became a symbol nothing references. A `<use>` that finds nothing fails without a
       word, which is the hazard the head of this file names, so the drawing leaves rather than
       waits. It is recorded in ../docs/decisions.md and on `ui-kit/icons.html`, and the family
       rule it belonged to is unchanged: a plus is a movement, and this product's only plus does
       not stand where that rule was written for.
       IT IS ON THE SAME OPTICAL GRID AS THE LINE IT REPLACES, which is what stops this being a
       second drawing of one thing: paint 16.2 x 16.2 and field 3.9, the numbers `ui-kit/icons.html`
       audits for `plus`, so only the WEIGHT differs, 2.6 units against 1.8. Two rounded rects and
       not a path, because a union of two rects is exactly a plus and a hand-written path of the
       same shape is a chance to get a corner wrong. ../docs/decisions.md, 2026-08-13. */
    '<symbol id="i-plus-b" viewBox="0 0 24 24"><rect x="10.7" y="3.9" width="2.6" height="16.2" rx="1.3" fill="currentColor"/><rect x="3.9" y="10.7" width="16.2" height="2.6" rx="1.3" fill="currentColor"/></symbol>',
    /* ---- the LINE family, added 2026-08-13. Five drawings, 898 placements, and until today
       every one of them was a hand-written <path> in the markup of 163 documents rather
       than a reference to anything, over 119 documents. `ui-kit/icons.html` calls them what they are: a cross, a
       chevron, a plus, a tick, an arrow and a hamburger are MOVEMENTS, NOT THINGS, so they
       are stroked where the Solar glyphs above are filled, and that is why they were never
       in this file: `base.css` turned every <use> into the filled family with an
       !important. The floor asks for `#i-` now, so a family is a property of the GLYPH and
       is carried by its name, which is the same argument backlog 133 used against a class
       per icon size. **THIS BUYS ONE SOURCE AND NOT BYTES, and the honest number says so**:
       the markup lost 4,947 bytes and this file gained 2,334, a net 2,613 over 163 documents,
       because `<use href="#l-chevron-down"/>` is longer than the chevron it replaces. What it
       buys is that a drawing has one place to be wrong in. Proof it changed nothing: 238
       full-page screenshots over 119 documents at two widths, **0 differing of 238**, against
       a control of 0 of 238 taken the same way.

       ONE OF THE SIX HAS A NEAR-TWIN THAT IS NOT A COPY OF IT, and the sweep swallowed it
       before the stand said so. `M5 5l14 14M19 5L5 19` is a cross 17% larger than the close
       across the same box, and `ui-kit/icons.html` had already ruled on it: it is the X
       BRAND mark of the footer social row, not a close, and it stays a brand mark. It has 0
       product placements since backlog 144 cut that row and 4 on the stand, which are the
       only copies of it left and are written out by hand on purpose. The lesson is the
       cheap one: two drawings that look alike are not evidence of drift, and the page that
       already decided is the place to look before unifying anything.

       `vector-effect` is an ATTRIBUTE here and not a rule, because it is not an inherited
       property and `.ic *` cannot reach into a <use> shadow tree. Without it the stroke
       would scale with the box and a 22px mark in a 24 viewBox would render 1.51 rather
       than the 1.65 the system declares. Everything else, the fill, the stroke, the width
       and the caps, IS inherited and comes from `.ic` exactly as it did when these were
       written out by hand. */
    '<symbol id="l-close" viewBox="0 0 24 24"><path vector-effect="non-scaling-stroke" d="M6 6l12 12M18 6L6 18"/></symbol>',
    '<symbol id="l-chevron-down" viewBox="0 0 24 24"><path vector-effect="non-scaling-stroke" d="M6 9l6 6 6-6"/></symbol>',
    '<symbol id="l-menu" viewBox="0 0 24 24"><path vector-effect="non-scaling-stroke" d="M3 6h18M3 12h18M3 18h18"/></symbol>',
    '<symbol id="l-arrow-right" viewBox="0 0 24 24"><path vector-effect="non-scaling-stroke" d="M5 12h14M13 6l6 6-6 6"/></symbol>',
    '<symbol id="l-check" viewBox="0 0 24 24"><path vector-effect="non-scaling-stroke" d="M4 13l4 4L20 5"/></symbol>'

  ].join('');
  var box = document.createElement('div');
  box.id = 'pm-icon-sprite';
  box.setAttribute('aria-hidden', 'true');
  box.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden';
  box.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg">' + SYMBOLS + '</svg>';
  /* First child of <body>, so a <use> earlier in the document resolves as soon as the
     target exists. <use> is live: a reference that found nothing at parse time updates
     the moment the symbol is inserted. */
  function put() {
    var host = document.body || document.documentElement;
    host.insertBefore(box, host.firstChild);
  }
  if (document.body) put();
  else document.addEventListener('DOMContentLoaded', put);
})();
