/* ui-kit/_frames.js - the parent half of the specimen frame handshake.

   A specimen is a page of its own, so the vitrine cannot measure it by reading
   its document: under file:// every document has its own opaque origin. The
   specimen posts its height instead, which crosses origins by design. The frame
   is matched by identity (contentWindow), not by the origin string, because
   from file:// that string is "null" for everyone. No em dash. */
(function () {
  /* A specimen is rendered at the width it declares, because that width is what
     its media queries answer to. When the column is narrower, the frame is
     scaled down rather than squeezed: the layout stays the layout, and the
     label says what it is being shown at. */
  function fit(f) {
    var box = f.parentElement, w = +f.getAttribute('width');
    /* The available width is the figure's, not the box's: the box is about to be
       resized to whatever we decide, so measuring it would measure our own
       previous answer. */
    var avail = box.parentElement.clientWidth;
    var s = Math.min(1, avail / w);
    var h = parseFloat(f.style.height || f.getAttribute('height'));
    f.style.transformOrigin = '0 0';
    f.style.transform = s < 1 ? 'scale(' + s + ')' : 'none';
    /* The border hugs the specimen instead of leaving a strip of empty canvas. */
    box.style.width = Math.ceil(w * s) + 'px';
    box.style.height = Math.ceil(h * s) + 'px';
    var tag = box.parentElement.querySelector('.ck-zoom');
    if (tag) { tag.textContent = s < 1 ? Math.round(s * 100) + '%' : ''; tag.hidden = s >= 1; }
  }

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.specimen || !(d.height > 0)) return;
    var frames = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < frames.length; i++) {
      if (frames[i].contentWindow === e.source) {
        frames[i].style.height = d.height + 'px';
        fit(frames[i]);
        return;
      }
    }
  });
  window.addEventListener('resize', function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) fit(f[i]);
  });
  /* A frame that finished before this script ran has already spoken and will
     not speak again, so ask it once it is there. */
  var ask = function (f) {
    try { f.contentWindow.postMessage({ping: true}, '*'); } catch (err) {}
  };
  var all = function () {
    var f = document.querySelectorAll('iframe[data-specimen]');
    for (var i = 0; i < f.length; i++) { ask(f[i]); f[i].addEventListener('load', ask.bind(null, f[i])); }
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all);
  else all();
  window.addEventListener('load', all);
})();
