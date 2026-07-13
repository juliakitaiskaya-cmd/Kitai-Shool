/* @ds-bundle: {"format":3,"namespace":"KitaiSchoolDesignSystem_9bf691","components":[],"sourceHashes":{"banners/image-slot.js":"9309434cb09c","ui_kits/platform/Icons.jsx":"37ba8a9a38d1","ui_kits/platform/Screens.jsx":"c3810599945c","ui_kits/platform/Sidebar.jsx":"6559e74dc1f1","ui_kits/website/Chrome.jsx":"9cad1f140186","ui_kits/website/Sections.jsx":"860d21cc33e4"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.KitaiSchoolDesignSystem_9bf691 = window.KitaiSchoolDesignSystem_9bf691 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// banners/image-slot.js
try { (() => {
// @ds-adherence-ignore -- omelette starter scaffold (raw elements/hex/px by design)
/* BEGIN USAGE */
/**
 * <image-slot> — user-fillable image placeholder.
 *
 * Drop this into a deck, mockup, or page wherever you want the user to
 * supply an image. You control the slot's shape and size; the user fills it
 * by dragging an image file onto it (or clicking to browse). The dropped
 * image persists across reloads via a .image-slots.state.json sidecar —
 * same read-via-fetch / write-via-window.omelette pattern as
 * design_canvas.jsx, so the filled slot shows on share links, downloaded
 * zips, and PPTX export. Outside the omelette runtime the slot is read-only.
 *
 * The host bridge only allows sidecar writes at the project root, so the
 * HTML that uses this component is assumed to live at the project root too
 * (same constraint as design_canvas.jsx).
 *
 * Attributes:
 *   id           Persistence key. REQUIRED for the drop to survive reload —
 *                every slot on the page needs a distinct id.
 *   shape        'rect' | 'rounded' | 'circle' | 'pill'   (default 'rounded')
 *                'circle' applies 50% border-radius; on a non-square slot
 *                that's an ellipse — set equal width and height for a true
 *                circle.
 *   radius       Corner radius in px for 'rounded'.       (default 12)
 *   mask         Any CSS clip-path value. Overrides `shape` — use this for
 *                hexagons, blobs, arbitrary polygons.
 *   fit          object-fit: cover | contain | fill.       (default 'cover')
 *                With cover (the default) double-clicking the filled slot
 *                enters a reframe mode: the whole image spills past the mask
 *                (translucent outside, opaque inside), drag to reposition,
 *                corner-drag to scale. The crop persists alongside the image
 *                in the sidecar. contain/fill stay static.
 *   position     object-position for fit=contain|fill.     (default '50% 50%')
 *   placeholder  Empty-state caption.                      (default 'Drop an image')
 *   src          Optional initial/fallback image URL. A user drop overrides
 *                it; clearing the drop reveals src again.
 *
 * Size and layout come from ordinary CSS on the element — width/height
 * inline or from a parent grid — so it composes with any layout.
 *
 * Usage:
 *   <image-slot id="hero"   style="width:800px;height:450px" shape="rounded" radius="20"
 *               placeholder="Drop a hero image"></image-slot>
 *   <image-slot id="avatar" style="width:120px;height:120px" shape="circle"></image-slot>
 *   <image-slot id="kite"   style="width:300px;height:300px"
 *               mask="polygon(50% 0, 100% 50%, 50% 100%, 0 50%)"></image-slot>
 */
/* END USAGE */

(() => {
  const STATE_FILE = '.image-slots.state.json';
  // 2× a ~600px slot in a 1920-wide deck — retina-sharp without making the
  // sidecar enormous. A 1200px WebP at q=0.85 is ~150-300KB.
  const MAX_DIM = 1200;
  // Raster formats only. SVG is excluded (can carry script; createImageBitmap
  // on SVG blobs is inconsistent). GIF is excluded because the canvas
  // re-encode keeps only the first frame, so an animated GIF would silently
  // go still — better to reject than surprise.
  const ACCEPT = ['image/png', 'image/jpeg', 'image/webp', 'image/avif'];

  // ── Shared sidecar store ────────────────────────────────────────────────
  // One fetch + immediate write-on-change for every <image-slot> on the
  // page. Reads via fetch() so viewing works anywhere the HTML and sidecar
  // are served together; writes go through window.omelette.writeFile, which
  // the host allowlists to *.state.json basenames only.
  const subs = new Set();
  let slots = {};
  // ids explicitly cleared before the sidecar fetch resolved — otherwise
  // the merge below can't tell "never set" from "just deleted" and would
  // resurrect the sidecar's stale value.
  const tombstones = new Set();
  let loaded = false;
  let loadP = null;
  function load() {
    if (loadP) return loadP;
    loadP = fetch(STATE_FILE).then(r => r.ok ? r.json() : null).then(j => {
      // Merge: sidecar loses to any in-memory change that raced ahead of
      // the fetch (drop or clear) so neither is clobbered by hydration.
      if (j && typeof j === 'object') {
        const merged = Object.assign({}, j, slots);
        // A framing-only write that raced ahead of hydration must not
        // drop a user image that's only on disk — inherit u from the
        // sidecar for any in-memory entry that lacks one.
        for (const k in slots) {
          if (merged[k] && !merged[k].u && j[k]) {
            merged[k].u = typeof j[k] === 'string' ? j[k] : j[k].u;
          }
        }
        for (const id of tombstones) delete merged[id];
        slots = merged;
      }
      tombstones.clear();
    }).catch(() => {}).then(() => {
      loaded = true;
      subs.forEach(fn => fn());
    });
    return loadP;
  }

  // Serialize writes so two near-simultaneous drops on different slots
  // can't reorder at the backend and leave the sidecar with only the
  // first. A save requested mid-flight just marks dirty and re-fires on
  // completion with the then-current slots.
  let saving = false;
  let saveDirty = false;
  function save() {
    if (saving) {
      saveDirty = true;
      return;
    }
    const w = window.omelette && window.omelette.writeFile;
    if (!w) return;
    saving = true;
    Promise.resolve(w(STATE_FILE, JSON.stringify(slots))).catch(() => {}).then(() => {
      saving = false;
      if (saveDirty) {
        saveDirty = false;
        save();
      }
    });
  }
  const S_MAX = 5;
  const clampS = s => Math.max(1, Math.min(S_MAX, s));

  // Normalize a stored slot value. Pre-reframe sidecars stored a bare
  // data-URL string; newer ones store {u, s, x, y}. Either shape is valid.
  function getSlot(id) {
    const v = slots[id];
    if (!v) return null;
    return typeof v === 'string' ? {
      u: v,
      s: 1,
      x: 0,
      y: 0
    } : v;
  }
  function setSlot(id, val) {
    if (!id) return;
    if (val) {
      slots[id] = val;
      tombstones.delete(id);
    } else {
      delete slots[id];
      if (!loaded) tombstones.add(id);
    }
    subs.forEach(fn => fn());
    // A drop is rare + high-value — write immediately so nav-away can't lose
    // it. Gate on the initial read so we don't overwrite a sidecar we haven't
    // merged yet; the merge in load() keeps this change once the read lands.
    if (loaded) save();else load().then(save);
  }

  // ── Image downscale ─────────────────────────────────────────────────────
  // Encode through a canvas so the sidecar carries resized bytes, not the
  // raw upload. Longest side is capped at 2× the slot's rendered width
  // (retina) and at MAX_DIM. WebP keeps alpha and is ~10× smaller than PNG
  // for photos, so there's no need for per-image format picking.
  async function toDataUrl(file, targetW) {
    const bitmap = await createImageBitmap(file);
    try {
      const cap = Math.min(MAX_DIM, Math.max(1, Math.round(targetW * 2)) || MAX_DIM);
      const scale = Math.min(1, cap / Math.max(bitmap.width, bitmap.height));
      const w = Math.max(1, Math.round(bitmap.width * scale));
      const h = Math.max(1, Math.round(bitmap.height * scale));
      const canvas = document.createElement('canvas');
      canvas.width = w;
      canvas.height = h;
      canvas.getContext('2d').drawImage(bitmap, 0, 0, w, h);
      return canvas.toDataURL('image/webp', 0.85);
    } finally {
      bitmap.close && bitmap.close();
    }
  }

  // ── Custom element ──────────────────────────────────────────────────────
  const stylesheet = ':host{display:inline-block;position:relative;vertical-align:top;' + '  font:13px/1.3 system-ui,-apple-system,sans-serif;color:rgba(0,0,0,.55);width:240px;height:160px}' + '.frame{position:absolute;inset:0;overflow:hidden;background:rgba(0,0,0,.04)}' +
  // .frame img (clipped) and .spill (unclipped ghost + handles) share the
  // same left/top/width/height in frame-%, computed by _applyView(), so the
  // inside-mask crop and the outside-mask spill stay pixel-aligned.
  '.frame img{position:absolute;max-width:none;transform:translate(-50%,-50%);' + '  -webkit-user-drag:none;user-select:none;touch-action:none}' +
  // Reframe mode (double-click): the full image spills past the mask. The
  // spill layer is sized to the IMAGE bounds so its corners are where the
  // resize handles belong. The ghost <img> inside is translucent; the real
  // clipped <img> underneath shows the opaque in-mask crop.
  '.spill{position:absolute;transform:translate(-50%,-50%);display:none;z-index:1;' + '  cursor:grab;touch-action:none}' + ':host([data-panning]) .spill{cursor:grabbing}' + '.spill .ghost{position:absolute;inset:0;width:100%;height:100%;opacity:.35;' + '  pointer-events:none;-webkit-user-drag:none;user-select:none;' + '  box-shadow:0 0 0 1px rgba(0,0,0,.2),0 12px 32px rgba(0,0,0,.2)}' + '.spill .handle{position:absolute;width:12px;height:12px;border-radius:50%;' + '  background:#fff;box-shadow:0 0 0 1.5px #c96442,0 1px 3px rgba(0,0,0,.3);' + '  transform:translate(-50%,-50%)}' + '.spill .handle[data-c=nw]{left:0;top:0;cursor:nwse-resize}' + '.spill .handle[data-c=ne]{left:100%;top:0;cursor:nesw-resize}' + '.spill .handle[data-c=sw]{left:0;top:100%;cursor:nesw-resize}' + '.spill .handle[data-c=se]{left:100%;top:100%;cursor:nwse-resize}' + ':host([data-reframe]){z-index:10}' + ':host([data-reframe]) .spill{display:block}' + ':host([data-reframe]) .frame{box-shadow:0 0 0 2px #c96442}' + '.empty{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;' + '  justify-content:center;gap:6px;text-align:center;padding:12px;box-sizing:border-box;' + '  cursor:pointer;user-select:none}' + '.empty svg{opacity:.45}' + '.empty .cap{max-width:90%;font-weight:500;letter-spacing:.01em}' + '.empty .sub{font-size:11px}' + '.empty .sub u{text-underline-offset:2px;text-decoration-color:rgba(0,0,0,.25)}' + '.empty:hover .sub u{color:rgba(0,0,0,.75);text-decoration-color:currentColor}' + ':host([data-over]) .frame{outline:2px solid #c96442;outline-offset:-2px;' + '  background:rgba(201,100,66,.10)}' + '.ring{position:absolute;inset:0;pointer-events:none;border:1.5px dashed rgba(0,0,0,.25);' + '  transition:border-color .12s}' + ':host([data-over]) .ring{border-color:#c96442}' + ':host([data-filled]) .ring{display:none}' +
  // Controls sit BELOW the mask (top:100%), absolutely positioned so the
  // author-declared slot height is unaffected. The gap is padding, not a
  // top offset, so the hover target stays contiguous with the frame.
  '.ctl{position:absolute;top:100%;left:50%;transform:translateX(-50%);padding-top:8px;' + '  display:flex;gap:6px;opacity:0;pointer-events:none;transition:opacity .12s;z-index:2;' + '  white-space:nowrap}' + ':host([data-filled][data-editable]:hover) .ctl,:host([data-reframe]) .ctl' + '  {opacity:1;pointer-events:auto}' + '.ctl button{appearance:none;border:0;border-radius:6px;padding:5px 10px;cursor:pointer;' + '  background:rgba(0,0,0,.65);color:#fff;font:11px/1 system-ui,-apple-system,sans-serif;' + '  backdrop-filter:blur(6px)}' + '.ctl button:hover{background:rgba(0,0,0,.8)}' + '.err{position:absolute;left:8px;bottom:8px;right:8px;color:#b3261e;font-size:11px;' + '  background:rgba(255,255,255,.85);padding:4px 6px;border-radius:5px;pointer-events:none}';
  const icon = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' + 'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' + '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/>' + '<path d="m21 15-5-5L5 21"/></svg>';
  class ImageSlot extends HTMLElement {
    static get observedAttributes() {
      return ['shape', 'radius', 'mask', 'fit', 'position', 'placeholder', 'src', 'id'];
    }
    constructor() {
      super();
      const root = this.attachShadow({
        mode: 'open'
      });
      // .spill and .ctl sit OUTSIDE .frame so overflow:hidden + border-radius
      // on the frame (circle, pill, rounded) can't clip them.
      root.innerHTML = '<style>' + stylesheet + '</style>' + '<div class="frame" part="frame">' + '  <img part="image" alt="" draggable="false" style="display:none">' + '  <div class="empty" part="empty">' + icon + '    <div class="cap"></div>' + '    <div class="sub">or <u>browse files</u></div></div>' + '  <div class="ring" part="ring"></div>' + '</div>' + '<div class="spill">' + '  <img class="ghost" alt="" draggable="false">' + '  <div class="handle" data-c="nw"></div><div class="handle" data-c="ne"></div>' + '  <div class="handle" data-c="sw"></div><div class="handle" data-c="se"></div>' + '</div>' + '<div class="ctl"><button data-act="replace" title="Replace image">Replace</button>' + '  <button data-act="clear" title="Remove image">Remove</button></div>' + '<input type="file" accept="' + ACCEPT.join(',') + '" hidden>';
      this._frame = root.querySelector('.frame');
      this._ring = root.querySelector('.ring');
      this._img = root.querySelector('.frame img');
      this._empty = root.querySelector('.empty');
      this._cap = root.querySelector('.cap');
      this._sub = root.querySelector('.sub');
      this._spill = root.querySelector('.spill');
      this._ghost = root.querySelector('.ghost');
      this._err = null;
      this._input = root.querySelector('input');
      this._depth = 0;
      this._gen = 0;
      this._view = {
        s: 1,
        x: 0,
        y: 0
      };
      this._subFn = () => this._render();
      // Shadow-DOM listeners live with the shadow DOM — bound once here so
      // disconnect/reconnect (e.g. React remount) doesn't stack handlers.
      this._empty.addEventListener('click', () => this._input.click());
      root.addEventListener('click', e => {
        const act = e.target && e.target.getAttribute && e.target.getAttribute('data-act');
        if (act === 'replace') {
          this._exitReframe(true);
          this._input.click();
        }
        if (act === 'clear') {
          this._exitReframe(false);
          this._gen++;
          this._local = null;
          if (this.id) setSlot(this.id, null);else this._render();
        }
      });
      this._input.addEventListener('change', () => {
        const f = this._input.files && this._input.files[0];
        if (f) this._ingest(f);
        this._input.value = '';
      });
      // naturalWidth/Height aren't known until load — re-apply so the cover
      // baseline is computed from real dimensions, not the 100%×100% fallback.
      this._img.addEventListener('load', () => this._applyView());
      // Gated on editable + fit=cover so share links and contain/fill slots
      // stay static.
      this.addEventListener('dblclick', e => {
        if (!this.hasAttribute('data-editable') || !this._reframes()) return;
        e.preventDefault();
        if (this.hasAttribute('data-reframe')) this._exitReframe(true);else this._enterReframe();
      });
      // Pan + resize both originate on the spill layer. A handle pointerdown
      // drives an aspect-locked resize anchored at the opposite corner; any
      // other pointerdown on the spill pans. Offsets are frame-% so a
      // reframed slot survives responsive resize / PPTX export.
      this._spill.addEventListener('pointerdown', e => {
        if (e.button !== 0 || !this.hasAttribute('data-reframe')) return;
        e.preventDefault();
        e.stopPropagation();
        this._spill.setPointerCapture(e.pointerId);
        const rect = this.getBoundingClientRect();
        const fw = rect.width || 1,
          fh = rect.height || 1;
        const corner = e.target.getAttribute && e.target.getAttribute('data-c');
        let move;
        if (corner) {
          // Resize about the OPPOSITE corner. Viewport-px throughout (rect
          // fw/fh, not clientWidth) so the math survives a transform:scale()
          // ancestor — deck_stage renders slides scaled-to-fit.
          const iw = this._img.naturalWidth || 1,
            ih = this._img.naturalHeight || 1;
          const base = Math.max(fw / iw, fh / ih);
          const sx = corner.includes('e') ? 1 : -1;
          const sy = corner.includes('s') ? 1 : -1;
          const s0 = this._view.s;
          const w0 = iw * base * s0,
            h0 = ih * base * s0;
          const cx0 = (50 + this._view.x) / 100 * fw;
          const cy0 = (50 + this._view.y) / 100 * fh;
          const ox = cx0 - sx * w0 / 2,
            oy = cy0 - sy * h0 / 2;
          const diag0 = Math.hypot(w0, h0);
          const ux = sx * w0 / diag0,
            uy = sy * h0 / diag0;
          move = ev => {
            const proj = (ev.clientX - rect.left - ox) * ux + (ev.clientY - rect.top - oy) * uy;
            const s = clampS(s0 * proj / diag0);
            const d = diag0 * s / s0;
            this._view.s = s;
            this._view.x = (ox + ux * d / 2) / fw * 100 - 50;
            this._view.y = (oy + uy * d / 2) / fh * 100 - 50;
            this._clampView();
            this._applyView();
          };
        } else {
          this.setAttribute('data-panning', '');
          const start = {
            px: e.clientX,
            py: e.clientY,
            x: this._view.x,
            y: this._view.y
          };
          move = ev => {
            this._view.x = start.x + (ev.clientX - start.px) / fw * 100;
            this._view.y = start.y + (ev.clientY - start.py) / fh * 100;
            this._clampView();
            this._applyView();
          };
        }
        const up = () => {
          try {
            this._spill.releasePointerCapture(e.pointerId);
          } catch {}
          this._spill.removeEventListener('pointermove', move);
          this._spill.removeEventListener('pointerup', up);
          this._spill.removeEventListener('pointercancel', up);
          this.removeAttribute('data-panning');
          this._dragUp = null;
        };
        // Stashed so _exitReframe (Escape / outside-click mid-drag) can
        // tear the capture + listeners down synchronously.
        this._dragUp = up;
        this._spill.addEventListener('pointermove', move);
        this._spill.addEventListener('pointerup', up);
        this._spill.addEventListener('pointercancel', up);
      });
      // Wheel zoom stays available inside reframe mode as a trackpad nicety —
      // zooms toward the cursor (offset' = cursor·(1-k) + offset·k).
      this.addEventListener('wheel', e => {
        if (!this.hasAttribute('data-reframe')) return;
        e.preventDefault();
        const r = this.getBoundingClientRect();
        const cx = (e.clientX - r.left) / r.width * 100 - 50;
        const cy = (e.clientY - r.top) / r.height * 100 - 50;
        const prev = this._view.s;
        const next = clampS(prev * Math.pow(1.0015, -e.deltaY));
        if (next === prev) return;
        const k = next / prev;
        this._view.s = next;
        this._view.x = cx * (1 - k) + this._view.x * k;
        this._view.y = cy * (1 - k) + this._view.y * k;
        this._clampView();
        this._applyView();
      }, {
        passive: false
      });
    }
    connectedCallback() {
      // Warn once per page — an id-less slot works for the session but
      // cannot persist, and two id-less slots would share nothing.
      if (!this.id && !ImageSlot._warned) {
        ImageSlot._warned = true;
        console.warn('<image-slot> without an id will not persist its dropped image.');
      }
      this.addEventListener('dragenter', this);
      this.addEventListener('dragover', this);
      this.addEventListener('dragleave', this);
      this.addEventListener('drop', this);
      subs.add(this._subFn);
      // width%/height% in _applyView encode the frame aspect at call time —
      // a host resize (responsive grid, pane divider) would stretch the
      // image until the next _render. Re-render on size change: _render()
      // re-seeds _view from stored before clamp/apply, so a shrink→grow
      // cycle round-trips instead of ratcheting x/y toward the narrower
      // frame's clamp range.
      this._ro = new ResizeObserver(() => this._render());
      this._ro.observe(this);
      load();
      this._render();
    }
    disconnectedCallback() {
      subs.delete(this._subFn);
      this.removeEventListener('dragenter', this);
      this.removeEventListener('dragover', this);
      this.removeEventListener('dragleave', this);
      this.removeEventListener('drop', this);
      if (this._ro) {
        this._ro.disconnect();
        this._ro = null;
      }
      this._exitReframe(false);
    }
    _enterReframe() {
      if (this.hasAttribute('data-reframe')) return;
      this.setAttribute('data-reframe', '');
      this._applyView();
      // Close on click outside (the spill handler stopPropagation()s so
      // in-image drags don't reach this) and on Escape. Listeners are held
      // on the instance so _exitReframe / disconnectedCallback can detach
      // exactly what was attached.
      this._outside = e => {
        if (e.composedPath && e.composedPath().includes(this)) return;
        this._exitReframe(true);
      };
      this._esc = e => {
        if (e.key === 'Escape') this._exitReframe(true);
      };
      document.addEventListener('pointerdown', this._outside, true);
      document.addEventListener('keydown', this._esc, true);
    }
    _exitReframe(commit) {
      if (!this.hasAttribute('data-reframe')) return;
      if (this._dragUp) this._dragUp();
      this.removeAttribute('data-reframe');
      this.removeAttribute('data-panning');
      if (this._outside) document.removeEventListener('pointerdown', this._outside, true);
      if (this._esc) document.removeEventListener('keydown', this._esc, true);
      this._outside = this._esc = null;
      if (commit) this._commitView();
    }
    attributeChangedCallback() {
      if (this.shadowRoot) this._render();
    }

    // handleEvent — one listener object for all four drag events keeps the
    // add/remove symmetric and the depth counter correct.
    handleEvent(e) {
      if (e.type === 'dragenter' || e.type === 'dragover') {
        // Without preventDefault the browser never fires 'drop'.
        e.preventDefault();
        e.stopPropagation();
        if (e.dataTransfer) e.dataTransfer.dropEffect = 'copy';
        if (e.type === 'dragenter') this._depth++;
        this.setAttribute('data-over', '');
      } else if (e.type === 'dragleave') {
        // dragenter/leave fire for every descendant crossing — count depth
        // so hovering the icon inside the empty state doesn't flicker.
        if (--this._depth <= 0) {
          this._depth = 0;
          this.removeAttribute('data-over');
        }
      } else if (e.type === 'drop') {
        e.preventDefault();
        e.stopPropagation();
        this._depth = 0;
        this.removeAttribute('data-over');
        const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
        if (f) this._ingest(f);
      }
    }
    async _ingest(file) {
      this._setError(null);
      if (!file || ACCEPT.indexOf(file.type) < 0) {
        this._setError('Drop a PNG, JPEG, WebP, or AVIF image.');
        return;
      }
      // toDataUrl can take hundreds of ms on a large photo. A Clear or a
      // newer drop during that window would be clobbered when this await
      // resumes — bump + capture a generation so stale encodes bail.
      const gen = ++this._gen;
      try {
        const w = this.clientWidth || this.offsetWidth || MAX_DIM;
        const url = await toDataUrl(file, w);
        if (gen !== this._gen) return;
        // Only exit reframe once the new image is in hand — a rejected type
        // or decode failure leaves the in-progress crop untouched.
        this._exitReframe(false);
        const val = {
          u: url,
          s: 1,
          x: 0,
          y: 0
        };
        setSlot(this.id || '', val);
        // Keep a session-local copy for id-less slots so the drop still
        // shows, even though it cannot persist.
        if (!this.id) {
          this._local = val;
          this._render();
        }
      } catch (err) {
        if (gen !== this._gen) return;
        this._setError('Could not read that image.');
        console.warn('<image-slot> ingest failed:', err);
      }
    }
    _setError(msg) {
      if (this._err) {
        this._err.remove();
        this._err = null;
      }
      if (!msg) return;
      const d = document.createElement('div');
      d.className = 'err';
      d.textContent = msg;
      this.shadowRoot.appendChild(d);
      this._err = d;
      setTimeout(() => {
        if (this._err === d) {
          d.remove();
          this._err = null;
        }
      }, 3000);
    }

    // Reframing (pan/resize) is only meaningful for fit=cover — contain/fill
    // keep the old object-fit path and double-click is a no-op.
    _reframes() {
      return this.hasAttribute('data-filled') && (this.getAttribute('fit') || 'cover') === 'cover';
    }

    // Cover-baseline geometry, shared by clamp/apply/resize. Null until the
    // img has loaded (naturalWidth is 0 before that) or when the slot has no
    // layout box — ResizeObserver fires with a 0×0 rect under display:none,
    // and clamping against a degenerate 1×1 frame would silently pull the
    // stored pan toward zero.
    _geom() {
      const iw = this._img.naturalWidth,
        ih = this._img.naturalHeight;
      const fw = this.clientWidth,
        fh = this.clientHeight;
      if (!iw || !ih || !fw || !fh) return null;
      return {
        iw,
        ih,
        fw,
        fh,
        base: Math.max(fw / iw, fh / ih)
      };
    }
    _clampView() {
      // Pan range on each axis is half the overflow past the frame edge.
      const g = this._geom();
      if (!g) return;
      const mx = Math.max(0, (g.iw * g.base * this._view.s / g.fw - 1) * 50);
      const my = Math.max(0, (g.ih * g.base * this._view.s / g.fh - 1) * 50);
      this._view.x = Math.max(-mx, Math.min(mx, this._view.x));
      this._view.y = Math.max(-my, Math.min(my, this._view.y));
    }
    _applyView() {
      const g = this._geom();
      const fit = this.getAttribute('fit') || 'cover';
      if (fit !== 'cover' || !g) {
        // Non-cover, or dimensions not known yet (before img load).
        this._img.style.width = '100%';
        this._img.style.height = '100%';
        this._img.style.left = '50%';
        this._img.style.top = '50%';
        this._img.style.objectFit = fit;
        this._img.style.objectPosition = this.getAttribute('position') || '50% 50%';
        return;
      }
      // Cover baseline: img fills the frame on its tighter axis at s=1, so
      // pan works immediately on the overflowing axis without zooming first.
      // Width/height and left/top are all frame-% — depends only on the
      // frame aspect ratio, so a responsive resize keeps the same crop. The
      // spill layer mirrors the same box so its corners = image corners.
      const k = g.base * this._view.s;
      const w = g.iw * k / g.fw * 100 + '%';
      const h = g.ih * k / g.fh * 100 + '%';
      const l = 50 + this._view.x + '%';
      const t = 50 + this._view.y + '%';
      this._img.style.width = w;
      this._img.style.height = h;
      this._img.style.left = l;
      this._img.style.top = t;
      this._img.style.objectFit = '';
      this._spill.style.width = w;
      this._spill.style.height = h;
      this._spill.style.left = l;
      this._spill.style.top = t;
    }
    _commitView() {
      const v = {
        s: this._view.s,
        x: this._view.x,
        y: this._view.y
      };
      if (this._userUrl) v.u = this._userUrl;
      // Framing-only (no u) persists too so an author-src slot remembers its
      // crop; clearing the sidecar still falls through to src=.
      if (this.id) setSlot(this.id, v);else {
        this._local = v;
      }
    }
    _render() {
      // Shape / mask. Presets use border-radius so the dashed ring can
      // follow the rounded outline; clip-path is only applied for an
      // explicit `mask` (the ring is hidden there since a rectangle
      // dashed border chopped by an arbitrary polygon looks broken).
      const mask = this.getAttribute('mask');
      const shape = (this.getAttribute('shape') || 'rounded').toLowerCase();
      let radius = '';
      if (shape === 'circle') radius = '50%';else if (shape === 'pill') radius = '9999px';else if (shape === 'rounded') {
        const n = parseFloat(this.getAttribute('radius'));
        radius = (Number.isFinite(n) ? n : 12) + 'px';
      }
      this._frame.style.borderRadius = mask ? '' : radius;
      this._frame.style.clipPath = mask || '';
      this._ring.style.borderRadius = mask ? '' : radius;
      this._ring.style.display = mask ? 'none' : '';

      // Controls and reframe entry gate on this so share links stay read-only.
      const editable = !!(window.omelette && window.omelette.writeFile);
      this.toggleAttribute('data-editable', editable);
      this._sub.style.display = editable ? '' : 'none';

      // Content. The sidecar is also writable by the agent's write_file
      // tool, so its value isn't guaranteed canvas-originated — only accept
      // data:image/ URLs from it. The `src` attribute is author-controlled
      // (Claude wrote it into the HTML) so it passes through unchanged.
      let stored = this.id ? getSlot(this.id) : this._local;
      if (stored && stored.u && !/^data:image\//i.test(stored.u)) stored = null;
      const srcAttr = this.getAttribute('src') || '';
      this._userUrl = stored && stored.u || null;
      const url = this._userUrl || srcAttr;
      // Don't clobber an in-flight reframe with a store-triggered re-render.
      if (!this.hasAttribute('data-reframe')) {
        this._view = {
          s: stored && Number.isFinite(stored.s) ? clampS(stored.s) : 1,
          x: stored && Number.isFinite(stored.x) ? stored.x : 0,
          y: stored && Number.isFinite(stored.y) ? stored.y : 0
        };
      }
      this._cap.textContent = this.getAttribute('placeholder') || 'Drop an image';
      // Toggle via style.display — the [hidden] attribute alone loses to
      // the display:flex / display:block rules in the stylesheet above.
      if (url) {
        if (this._img.getAttribute('src') !== url) {
          this._img.src = url;
          this._ghost.src = url;
        }
        this._img.style.display = 'block';
        this._empty.style.display = 'none';
        this.setAttribute('data-filled', '');
        this._clampView();
        this._applyView();
      } else {
        this._img.style.display = 'none';
        this._img.removeAttribute('src');
        this._ghost.removeAttribute('src');
        this._empty.style.display = 'flex';
        this.removeAttribute('data-filled');
      }
    }
  }
  if (!customElements.get('image-slot')) {
    customElements.define('image-slot', ImageSlot);
  }
})();
})(); } catch (e) { __ds_ns.__errors.push({ path: "banners/image-slot.js", error: String((e && e.message) || e) }); }

// ui_kits/platform/Icons.jsx
try { (() => {
/* Icons.jsx — Kitai School platform outline icon set.
   Linear SVGs (Lucide-style, stroke=currentColor 1.75) replacing the old emoji.
   Usage: <Icon name="home" /> — size via CSS on the wrapping element's font-size? no:
   each svg is 1em-agnostic; we size with width/height props (default 20). */

function Icon({
  name,
  size = 20,
  stroke = 1.75,
  style
}) {
  const p = {
    width: size,
    height: size,
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: stroke,
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    style: {
      display: 'block',
      ...style
    }
  };
  switch (name) {
    case 'home':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M3 10.5 12 3l9 7.5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M5 9.5V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M9.5 21v-6h5v6"
      }));
    case 'layers':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "m12 3 9 4.5-9 4.5-9-4.5L12 3Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "m3 12 9 4.5L21 12"
      }), /*#__PURE__*/React.createElement("path", {
        d: "m3 16.5 9 4.5 9-4.5"
      }));
    case 'book-open':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M12 6.5C10.5 5 8 4.5 4 4.8V18c4-.3 6.5.2 8 1.7 1.5-1.5 4-2 8-1.7V4.8c-4-.3-6.5.2-8 1.7Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M12 6.5v13.2"
      }));
    case 'book':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M6 3h11a1 1 0 0 1 1 1v15.5a.5.5 0 0 1-.5.5H7a2 2 0 0 1-2-2V4a1 1 0 0 1 1-1Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M5 17.5A2 2 0 0 1 7 16h11"
      }));
    case 'route':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "6",
        cy: "19",
        r: "2.5"
      }), /*#__PURE__*/React.createElement("circle", {
        cx: "18",
        cy: "5",
        r: "2.5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M8.5 19H14a3.5 3.5 0 0 0 0-7h-4a3.5 3.5 0 0 1 0-7h5.5"
      }));
    case 'trend':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M3 17l6-6 4 4 8-8"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M17 7h4v4"
      }));
    case 'chat':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M20 12a7.5 7.5 0 0 1-10.8 6.7L4 20l1.3-5.2A7.5 7.5 0 1 1 20 12Z"
      }));
    case 'target':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "12",
        cy: "12",
        r: "8.5"
      }), /*#__PURE__*/React.createElement("circle", {
        cx: "12",
        cy: "12",
        r: "4.5"
      }), /*#__PURE__*/React.createElement("circle", {
        cx: "12",
        cy: "12",
        r: "1"
      }));
    case 'cards':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("rect", {
        x: "3",
        y: "7",
        width: "13",
        height: "13",
        rx: "2"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M8 4h9a2 2 0 0 1 2 2v9"
      }));
    case 'edit':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M4 20h4l10-10a2 2 0 0 0-3-3L5 17v3Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M13.5 6.5l3 3"
      }));
    case 'shuffle':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M16 4h4v4"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M20 4 4 20"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M16 20h4v-4"
      }), /*#__PURE__*/React.createElement("path", {
        d: "m15 15 5 5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M4 4l5 5"
      }));
    case 'message':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M5 5h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-4 4V6a1 1 0 0 1 1-1Z"
      }));
    case 'brush':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M15 4 8.5 10.5a3 3 0 0 0 0 4.2L13 19l5-5a3 3 0 0 0 0-4.2L15 4Z",
        transform: "rotate(45 13 12)"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M6 16c-2 .5-3 2-3 4 2 0 3.5-1 4-3"
      }));
    case 'family':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "8",
        cy: "8",
        r: "3"
      }), /*#__PURE__*/React.createElement("circle", {
        cx: "16.5",
        cy: "9",
        r: "2.5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M2.5 20c0-3 2.5-5 5.5-5s5.5 2 5.5 5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M15 15c2.8 0 5 1.8 5 5"
      }));
    case 'bell':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M10 19a2 2 0 0 0 4 0"
      }));
    case 'flame':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M12 3c1 3-1.5 4-1.5 6.5a1.5 1.5 0 0 0 3 0c0-.5 0-1-.3-1.5 2 1.3 3.3 3.4 3.3 5.8a6.5 6.5 0 0 1-13 0C3.5 10 7 7 8 4.5c.7 1.5 2 2 2.5 3 .8-1.6.8-3 1.5-4.5Z"
      }));
    case 'help':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "12",
        cy: "12",
        r: "9"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M9.3 9.3a2.7 2.7 0 0 1 5.2 1c0 1.8-2.7 2.3-2.7 4"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M12 17.5v.01"
      }));
    case 'search':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "11",
        cy: "11",
        r: "7"
      }), /*#__PURE__*/React.createElement("path", {
        d: "m20 20-3.5-3.5"
      }));
    case 'volume':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M4 9.5h3L12 5v14l-5-4.5H4Z"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M16 9a4 4 0 0 1 0 6"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M18.5 6.5a7 7 0 0 1 0 11"
      }));
    case 'mic':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("rect", {
        x: "9",
        y: "3",
        width: "6",
        height: "11",
        rx: "3"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M5 11a7 7 0 0 0 14 0"
      }), /*#__PURE__*/React.createElement("path", {
        d: "M12 18v3"
      }));
    case 'arrow-left':
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("path", {
        d: "M19 12H5"
      }), /*#__PURE__*/React.createElement("path", {
        d: "m11 6-6 6 6 6"
      }));
    default:
      return /*#__PURE__*/React.createElement("svg", p, /*#__PURE__*/React.createElement("circle", {
        cx: "12",
        cy: "12",
        r: "9"
      }));
  }
}
Object.assign(window, {
  Icon
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/platform/Icons.jsx", error: String((e && e.message) || e) }); }

// ui_kits/platform/Screens.jsx
try { (() => {
/* Screens.jsx — Kitai School platform screens: Header, Dashboard, Learn hub, Flashcard. */
const {
  useState: useStateS
} = React;

/* ---------- shared greeting header ---------- */
function Header() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-header"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", {
    className: "ks-greet"
  }, "\u041F\u0440\u0438\u0432\u0435\u0442, \u0410\u043D\u043D\u0430!"), /*#__PURE__*/React.createElement("div", {
    className: "ks-greet-sub"
  }, "\u041F\u0443\u0442\u044C \u043A HSK3")), /*#__PURE__*/React.createElement("div", {
    className: "ks-header-right"
  }, /*#__PURE__*/React.createElement("button", {
    className: "ks-support"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "help",
    size: 16
  }), " \u041F\u043E\u0434\u0434\u0435\u0440\u0436\u043A\u0430"), /*#__PURE__*/React.createElement("span", {
    className: "ks-streak"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "flame",
    size: 16
  }), " 1")));
}

/* ---------- DASHBOARD (Главная) ---------- */
function Dashboard() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-screen"
  }, /*#__PURE__*/React.createElement(Header, null), /*#__PURE__*/React.createElement("div", {
    className: "ks-card ks-pad"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-card-title"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "family",
    size: 19,
    style: {
      color: 'var(--brick)'
    }
  }), " \u0414\u043E\u0441\u0442\u0443\u043F \u0434\u043B\u044F \u0440\u043E\u0434\u0438\u0442\u0435\u043B\u0435\u0439"), /*#__PURE__*/React.createElement("p", {
    className: "ks-card-text"
  }, "\u0421\u0433\u0435\u043D\u0435\u0440\u0438\u0440\u0443\u0439\u0442\u0435 \u0441\u0441\u044B\u043B\u043A\u0443 \u0434\u043B\u044F \u0440\u043E\u0434\u0438\u0442\u0435\u043B\u0435\u0439. \u041E\u043D\u0438 \u0443\u0432\u0438\u0434\u044F\u0442 \u0440\u0430\u0441\u043F\u0438\u0441\u0430\u043D\u0438\u0435, \u043F\u0440\u043E\u0433\u0440\u0435\u0441\u0441 \u0438 \u0414\u0417 \u2014 \u043D\u043E \u043D\u0435 \u0447\u0430\u0442 \u0438 \u043D\u0435 \u0442\u0440\u0435\u043D\u0430\u0436\u0451\u0440."), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-soft"
  }, "\u0421\u043E\u0437\u0434\u0430\u0442\u044C \u0441\u0441\u044B\u043B\u043A\u0443")), /*#__PURE__*/React.createElement("div", {
    className: "ks-card ks-pad"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-card-title"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "bell",
    size: 19,
    style: {
      color: 'var(--brick)'
    }
  }), " Telegram-\u0443\u0432\u0435\u0434\u043E\u043C\u043B\u0435\u043D\u0438\u044F"), /*#__PURE__*/React.createElement("p", {
    className: "ks-card-text"
  }, "\u041F\u043E\u043B\u0443\u0447\u0430\u0439\u0442\u0435 \u043D\u0430\u043F\u043E\u043C\u0438\u043D\u0430\u043D\u0438\u044F \u043E\u0431 \u0443\u0440\u043E\u043A\u0430\u0445, \u0414\u0417 \u0438 \u0441\u043E\u043E\u0431\u0449\u0435\u043D\u0438\u044F\u0445 \u0432 \u0447\u0430\u0442\u0435 \u043F\u0440\u044F\u043C\u043E \u0432 Telegram."), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-soft"
  }, "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0438\u0442\u044C Telegram")), /*#__PURE__*/React.createElement("div", {
    className: "ks-goal"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-goal-ring"
  }, "4/5"), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    className: "ks-goal-title"
  }, "\u0415\u0436\u0435\u0434\u043D\u0435\u0432\u043D\u0430\u044F \u0446\u0435\u043B\u044C"), /*#__PURE__*/React.createElement("div", {
    className: "ks-goal-sub"
  }, "\u0412\u044B\u0443\u0447\u0438 \u0435\u0449\u0451 1 \u0441\u043B\u043E\u0432\u043E"))), /*#__PURE__*/React.createElement("div", {
    className: "ks-tiles"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-tile"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "book",
    size: 22
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-num"
  }, "612 / 1289"), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-cap"
  }, "\u0441\u043B\u043E\u0432\u0430")), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "layers",
    size: 22
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-num"
  }, "38 / 102"), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-cap"
  }, "\u0443\u0440\u043E\u043A\u0438")), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "target",
    size: 22
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-num"
  }, "78%"), /*#__PURE__*/React.createElement("div", {
    className: "ks-tile-cap"
  }, "\u0442\u043E\u0447\u043D\u043E\u0441\u0442\u044C"))), /*#__PURE__*/React.createElement("div", {
    className: "ks-eyebrow ks-section-label"
  }, "\u0411\u043B\u0438\u0436\u0430\u0439\u0448\u0438\u0439 \u0443\u0440\u043E\u043A"), /*#__PURE__*/React.createElement("div", {
    className: "ks-card ks-pad ks-lesson-row"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    className: "ks-card-title",
    style: {
      marginBottom: 4
    }
  }, "HSK3 \xB7 \u0423\u0440\u043E\u043A 39"), /*#__PURE__*/React.createElement("div", {
    className: "ks-card-text",
    style: {
      margin: 0
    }
  }, "\u0417\u0430\u0432\u0442ra, 18:00 \xB7 \u041A\u043E\u043D\u0441\u0442\u0440\u0443\u043A\u0446\u0438\u044F \u628A")), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-primary"
  }, "\u041A \u0443\u0440\u043E\u043A\u0443")));
}

/* ---------- LEARN hub (Учить) ---------- */
const KS_MODES = [{
  icon: 'cards',
  title: 'Карточки',
  hint: 'ПОМНЮ / НЕ ПОМНЮ',
  opens: true
}, {
  icon: 'edit',
  title: 'Заполни\nпропуск',
  hint: 'ВЫБЕРИ СЛОВО'
}, {
  icon: 'shuffle',
  title: 'Порядок\nслов',
  hint: 'СОБЕРИ ПРЕДЛОЖЕНИЕ'
}, {
  icon: 'message',
  title: 'Диалог',
  hint: 'КОНТЕКСТ'
}, {
  icon: 'brush',
  title: 'Написание',
  hint: 'ПОРЯДОК ЧЕРТ'
}];
function Learn({
  onOpenCard
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-screen"
  }, /*#__PURE__*/React.createElement(Header, null), /*#__PURE__*/React.createElement("div", {
    className: "ks-card ks-pad ks-progress"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-progress-bar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: '47%'
    }
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-progress-row"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("b", {
    className: "ks-progress-num"
  }, "612"), " ", /*#__PURE__*/React.createElement("span", {
    className: "ks-muted"
  }, "/ 1289 \u0441\u043B\u043E\u0432")), /*#__PURE__*/React.createElement("b", {
    className: "ks-progress-pct"
  }, "47%")), /*#__PURE__*/React.createElement("div", {
    className: "ks-legend"
  }, /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    className: "d g"
  }), "\u0432\u044B\u0443\u0447\u0435\u043D\u043E 612"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    className: "d y"
  }), "\u043F\u043E\u0432\u0442\u043E\u0440\u044F\u044E 187"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    className: "d r"
  }), "\u0443\u0447\u0443 64"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("i", {
    className: "d n"
  }), "\u043D\u043E\u0432\u044B\u0435 426"))), /*#__PURE__*/React.createElement("div", {
    className: "ks-chip-row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "ks-chip"
  }, /*#__PURE__*/React.createElement("i", {
    className: "ks-chip-dot"
  }), "\u041F\u0438\u043D\u044C\u0438\u043D\u044C"), /*#__PURE__*/React.createElement("span", {
    className: "ks-chip"
  }, /*#__PURE__*/React.createElement("i", {
    className: "ks-chip-dot"
  }), "\u041F\u0435\u0440\u0435\u0432\u043E\u0434")), /*#__PURE__*/React.createElement("div", {
    className: "ks-search"
  }, /*#__PURE__*/React.createElement("span", {
    className: "ks-search-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "search",
    size: 18
  })), " \u041F\u043E\u0438\u0441\u043A \u0441\u043B\u043E\u0432\u0430: ", /*#__PURE__*/React.createElement("span", {
    className: "ks-han"
  }, "\u6C49\u5B57"), ", pinyin \u0438\u043B\u0438 \u043F\u0435\u0440\u0435\u0432\u043E\u0434\u2026"), /*#__PURE__*/React.createElement("div", {
    className: "ks-modes"
  }, KS_MODES.map((m, i) => /*#__PURE__*/React.createElement("button", {
    key: i,
    className: "ks-mode",
    onClick: () => m.opens && onOpenCard()
  }, /*#__PURE__*/React.createElement("span", {
    className: "ks-mode-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: m.icon,
    size: 24
  })), /*#__PURE__*/React.createElement("span", {
    className: "ks-mode-title"
  }, m.title), /*#__PURE__*/React.createElement("span", {
    className: "ks-mode-hint"
  }, m.hint)))), /*#__PURE__*/React.createElement("button", {
    className: "ks-accordion"
  }, "\u25B8 \u041A\u0430\u0440\u0442\u0430 \u043F\u0440\u043E\u0433\u0440\u0435\u0441\u0441\u0430 (\u0432\u0441\u0435 \u0441\u043B\u043E\u0432\u0430)"));
}

/* ---------- FLASHCARD / pronunciation ---------- */
function Flashcard({
  onBack
}) {
  const [graded, setGraded] = useStateS(false);
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-screen ks-flash-screen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-top"
  }, /*#__PURE__*/React.createElement("button", {
    className: "ks-round",
    onClick: onBack
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "arrow-left",
    size: 17
  })), /*#__PURE__*/React.createElement("button", {
    className: "ks-round"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "home",
    size: 17
  })), /*#__PURE__*/React.createElement("span", {
    className: "ks-counter"
  }, "4", /*#__PURE__*/React.createElement("br", null), "/", /*#__PURE__*/React.createElement("br", null), "10"), /*#__PURE__*/React.createElement("span", {
    className: "ks-flash-mode"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "cards",
    size: 15,
    style: {
      display: 'inline-block',
      verticalAlign: '-2px',
      marginRight: 5
    }
  }), " \u041A\u0430\u0440\u0442\u043E\u0447\u043A\u0438")), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-card"
  }, /*#__PURE__*/React.createElement("button", {
    className: "ks-round ks-audio"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "volume",
    size: 16
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-han"
  }, "\u6216\u8005"), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-pin"
  }, "hu\xF2 zh\u011B"), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-mean"
  }, "\u0438\u043B\u0438, \u0432\u043E\u0437\u043C\u043E\u0436\u043D\u043E, \u0438\u043B\u0438 (\u0432 \u0443\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435\u043B\u044C\u043D\u044B\u0445 \u043F\u0440\u0435\u0434\u043B\u043E\u0436\u0435\u043D\u0438\u044F\u0445)"), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-tag"
  }, "HSK3 \xB7 \u0423\u0440\u043E\u043A 3"), graded && /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-grade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-tone-row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "ks-tone"
  }, "\u6216\u8005", /*#__PURE__*/React.createElement("sub", null, "\u6216 78%")), /*#__PURE__*/React.createElement("span", {
    className: "ks-tone"
  }, "\u6216\u8005", /*#__PURE__*/React.createElement("sub", null, "\u8005 72%"))), /*#__PURE__*/React.createElement("div", {
    className: "ks-tone-score"
  }, "\u041E\u0431\u0449\u0430\u044F \u043E\u0446\u0435\u043D\u043A\u0430: 75/100"), /*#__PURE__*/React.createElement("div", {
    className: "ks-highlight"
  }, "\u0425\u043E\u0440\u043E\u0448\u043E! \u0422\u043E\u043D \u0432 \u043F\u0435\u0440\u0432\u043E\u043C \u0441\u043B\u043E\u0433\u0435 \u6216 \u0443\u0436\u0435 \u0431\u043B\u0438\u0437\u043E\u043A \u2014 \u043F\u043E\u043F\u0440\u043E\u0431\u0443\u0439\u0442\u0435 \u0435\u0449\u0451 \u0440\u0435\u0437\u0447\u0435, \u043A\u0430\u043A \u043A\u043E\u043C\u0430\u043D\u0434\u0430 \xAB\u0421\u0442\u043E\u043F!\xBB. \u0412\u043E \u0432\u0442\u043E\u0440\u043E\u043C \u0441\u043B\u043E\u0433\u0435 \u8005 \u2014 \u0433\u043E\u043B\u043E\u0441 \u043D\u044B\u0440\u044F\u0435\u0442 \u0432\u043D\u0438\u0437 \u0438 \u0441\u043D\u043E\u0432\u0430 \u0432\u0432\u0435\u0440\u0445."), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-soft ks-again"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "mic",
    size: 15
  }), " \u0415\u0449\u0451 \u0440\u0430\u0437")), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-example"
  }, "\u82F9\u679C\u6216\u8005\u6A58\u5B50 ", /*#__PURE__*/React.createElement("button", {
    className: "ks-round ks-sm"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: "volume",
    size: 13
  })), /*#__PURE__*/React.createElement("div", {
    className: "ks-muted"
  }, "\u042F\u0431\u043B\u043E\u043A\u0438 \u0438\u043B\u0438 \u0430\u043F\u0435\u043B\u044C\u0441\u0438\u043D\u044B"))), /*#__PURE__*/React.createElement("div", {
    className: "ks-flash-actions"
  }, /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-soft",
    onClick: onBack
  }, "\u0421\u043B\u043E\u0436\u043D\u043E"), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-ghost",
    onClick: () => setGraded(true)
  }, "\u041F\u043E\u0432\u0442\u043E\u0440"), /*#__PURE__*/React.createElement("button", {
    className: "ks-btn ks-btn-success",
    onClick: onBack
  }, "\u0417\u043D\u0430\u044E")));
}
Object.assign(window, {
  Header,
  Dashboard,
  Learn,
  Flashcard
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/platform/Screens.jsx", error: String((e && e.message) || e) }); }

// ui_kits/platform/Sidebar.jsx
try { (() => {
/* Sidebar.jsx — fixed left icon navigation for the Kitai School learning platform.
   Outline icons (see Icons.jsx) per design-system update. */
const {
  useState
} = React;
const KS_NAV = [{
  id: 'home',
  icon: 'home',
  label: 'Главная'
}, {
  id: 'lessons',
  icon: 'layers',
  label: 'Уроки'
}, {
  id: 'learn',
  icon: 'book-open',
  label: 'Учить'
}, {
  id: 'words',
  icon: 'book',
  label: 'Слова'
}, {
  id: 'path',
  icon: 'route',
  label: 'Путь'
}, {
  id: 'growth',
  icon: 'trend',
  label: 'Рост'
}, {
  id: 'chat',
  icon: 'chat',
  label: 'Чат'
}];
function Sidebar({
  active,
  onNavigate
}) {
  return /*#__PURE__*/React.createElement("nav", {
    className: "ks-sidebar"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-side-logo"
  }, "\u542F"), /*#__PURE__*/React.createElement("div", {
    className: "ks-side-items"
  }, KS_NAV.map(item => /*#__PURE__*/React.createElement("button", {
    key: item.id,
    className: 'ks-side-item' + (active === item.id ? ' on' : ''),
    onClick: () => onNavigate(item.id)
  }, /*#__PURE__*/React.createElement("span", {
    className: "ks-side-ico"
  }, /*#__PURE__*/React.createElement(Icon, {
    name: item.icon,
    size: 20
  })), /*#__PURE__*/React.createElement("span", {
    className: "ks-side-label"
  }, item.label)))));
}
Object.assign(window, {
  Sidebar,
  KS_NAV
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/platform/Sidebar.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/Chrome.jsx
try { (() => {
/* Chrome.jsx — Kitai School marketing site header + footer */
function SiteHeader() {
  return /*#__PURE__*/React.createElement("header", {
    className: "site-header"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/kitai-logo.svg",
    alt: "Kitai School"
  })), /*#__PURE__*/React.createElement("nav", {
    className: "site-nav"
  }, /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u0418\u043D\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043B\u044C\u043D\u043E"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u0413\u0440\u0443\u043F\u043F\u044B"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u0411\u0438\u0437\u043D\u0435\u0441-\u043A\u0438\u0442\u0430\u0439\u0441\u043A\u0438\u0439"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u041F\u043E\u0434\u0433\u043E\u0442\u043E\u0432\u043A\u0430 \u043A HSK"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u041F\u043E\u0441\u0442\u0443\u043F\u043B\u0435\u043D\u0438\u0435 \u0432 \u041A\u0438\u0442\u0430\u0439")), /*#__PURE__*/React.createElement("a", {
    className: "tg-btn",
    href: "#"
  }, "\u041D\u0430\u043F\u0438\u0441\u0430\u0442\u044C \u0432 Telegram")));
}
function SiteFooter() {
  return /*#__PURE__*/React.createElement("footer", {
    className: "site-footer"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "foot-brand"
  }, /*#__PURE__*/React.createElement("div", {
    className: "name"
  }, "Kitai School"), /*#__PURE__*/React.createElement("div", {
    className: "sub"
  }, "\u0428\u043A\u043E\u043B\u0430 \u043A\u0438\u0442\u0430\u0439\u0441\u043A\u043E\u0433\u043E \u044F\u0437\u044B\u043A\u0430", /*#__PURE__*/React.createElement("br", null), "\u0441 2005 \u0433\u043E\u0434\u0430 \xB7 EST \xB7 2005 \xB7 MOSCOW")), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h4", null, "\u041A\u043E\u043D\u0442\u0430\u043A\u0442\u044B"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "+7 (958) 538-70-80"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "info@kitai-school.ru"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "Telegram \xB7 @kitai_school"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "VK \xB7 vk.com/kitai_school")), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h4", null, "\u041B\u0438\u0446\u0435\u043D\u0437\u0438\u044F"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u2116 \u041B035-01298-77/02285772"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u0414\u0435\u043F\u0430\u0440\u0442\u0430\u043C\u0435\u043D\u0442 \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u044F \u041C\u043E\u0441\u043A\u0432\u044B"), /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u0421\u043A\u0430\u0447\u0430\u0442\u044C PDF \u2192")), /*#__PURE__*/React.createElement("div", {
    className: "foot-copy"
  }, "\xA9 2005\u20132026 Kitai School. \u0412\u0441\u0435 \u043F\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043D\u044B. \xB7 \u041D\u0430\u043B\u043E\u0433\u043E\u0432\u044B\u0439 \u0432\u044B\u0447\u0435\u0442 13% \xB7 \u0414\u043E\u0433\u043E\u0432\u043E\u0440-\u043E\u0444\u0435\u0440\u0442\u0430")));
}
Object.assign(window, {
  SiteHeader,
  SiteFooter
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/Chrome.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/Sections.jsx
try { (() => {
/* Sections.jsx — Kitai School marketing-site sections */

function Hero() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "hero"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("span", {
    className: "badge"
  }, "\u041B\u0438\u0446\u0435\u043D\u0437\u0438\u044F \u0414\u0435\u043F\u0430\u0440\u0442\u0430\u043C\u0435\u043D\u0442\u0430 \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u044F \xB7 20 \u043B\u0435\u0442 \u043E\u043F\u044B\u0442\u0430"), /*#__PURE__*/React.createElement("h1", null, "\u041D\u0430\u0443\u0447\u0438\u043C \u0433\u043E\u0432\u043E\u0440\u0438\u0442\u044C \u043F\u043E\u2011\u043A\u0438\u0442\u0430\u0439\u0441\u043A\u0438 ", /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "\u0443\u0432\u0435\u0440\u0435\u043D\u043D\u043E"), " \u0438 \u0441\u0432\u043E\u0431\u043E\u0434\u043D\u043E"), /*#__PURE__*/React.createElement("p", null, "\u041F\u0440\u043E\u0432\u0435\u0440\u0435\u043D\u043D\u0430\u044F \u043C\u0435\u0442\u043E\u0434\u0438\u043A\u0430, \u0441\u043E\u0431\u0441\u0442\u0432\u0435\u043D\u043D\u0430\u044F \u043F\u043B\u0430\u0442\u0444\u043E\u0440\u043C\u0430 \u0438 \u043A\u043E\u043D\u0442\u0440\u043E\u043B\u044C \u043A\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u043A\u0430\u0436\u0434\u043E\u0433\u043E \u0443\u0440\u043E\u043A\u0430. \u0414\u043B\u044F \u0432\u0437\u0440\u043E\u0441\u043B\u044B\u0445 \u0438 \u0434\u0435\u0442\u0435\u0439 \u043E\u0442 6 \u043B\u0435\u0442."), /*#__PURE__*/React.createElement("div", {
    className: "hero-cta"
  }, /*#__PURE__*/React.createElement("a", {
    className: "btn btn-primary",
    href: "#"
  }, "\u0417\u0430\u043F\u0438\u0441\u0430\u0442\u044C\u0441\u044F \u043D\u0430 \u0434\u0438\u0430\u0433\u043D\u043E\u0441\u0442\u0438\u0447\u0435\u0441\u043A\u0438\u0439 \u0443\u0440\u043E\u043A"), /*#__PURE__*/React.createElement("a", {
    className: "btn btn-ghost",
    href: "#"
  }, "\u0423\u0437\u043D\u0430\u0442\u044C \u0441\u0442\u043E\u0438\u043C\u043E\u0441\u0442\u044C")), /*#__PURE__*/React.createElement("div", {
    className: "hero-also"
  }, "\u0422\u0430\u043A\u0436\u0435: ", /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u041F\u043E\u0441\u0442\u0443\u043F\u043B\u0435\u043D\u0438\u0435 \u0432 \u041A\u0438\u0442\u0430\u0439"), " \xB7 ", /*#__PURE__*/React.createElement("a", {
    href: "#"
  }, "\u041B\u0430\u0433\u0435\u0440\u044C \u043B\u0435\u0442\u043E\u043C 2026"))), /*#__PURE__*/React.createElement("div", {
    className: "hero-photo"
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/founder-yulia.jpg",
    alt: "\u042E\u043B\u0438\u044F \u0413\u043E\u0440\u044F\u0438\u043D\u0430 \u2014 \u043E\u0441\u043D\u043E\u0432\u0430\u0442\u0435\u043B\u044C Kitai School"
  }), /*#__PURE__*/React.createElement("div", {
    className: "hero-cap"
  }, /*#__PURE__*/React.createElement("b", null, "\u042E\u043B\u0438\u044F \u0413\u043E\u0440\u044F\u0438\u043D\u0430"), /*#__PURE__*/React.createElement("span", null, "\u041E\u0441\u043D\u043E\u0432\u0430\u0442\u0435\u043B\u044C Kitai School \xB7 \u0441 2005 \u0433\u043E\u0434\u0430")))));
}
const METHOD = [{
  n: 'I',
  t: 'Структура каждого урока',
  d: 'Разминка, повторение, новый материал, отработка, рефлексия. Никакой импровизации — только система.',
  m: '5 этапов · 55 минут'
}, {
  n: 'II',
  t: 'Тренажёр HSK на платформе',
  d: '2292 слова уровней HSK 1–4, шесть режимов, проверка произношения через AI и интервальные повторения.',
  m: '2292 слова · 6 режимов · SRS'
}, {
  n: 'III',
  t: 'Контроль качества каждого урока',
  d: 'Каждое занятие оценивается методистом по 11 критериям. Слабые места исправляются сразу.',
  m: '11 критериев · после каждого урока'
}, {
  n: 'IV',
  t: 'Обратная связь после урока',
  d: 'Развёрнутый комментарий: что получилось, над чем работаем, какое домашнее задание.',
  m: 'персонально каждому ученику'
}];
function Methodology() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "eyebrow"
  }, "\u041F\u043E\u0447\u0435\u043C\u0443 \u0443 \u043D\u0430\u0441 \u043F\u043E\u043B\u0443\u0447\u0430\u0435\u0442\u0441\u044F"), /*#__PURE__*/React.createElement("h2", {
    className: "sec-title"
  }, "\u041C\u0435\u0442\u043E\u0434\u0438\u043A\u0430 \u2014 \u043D\u0435 \u0441\u043B\u043E\u0432\u043E \u043D\u0430 \u0441\u0430\u0439\u0442\u0435, \u0430 ", /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "\u0441\u0438\u0441\u0442\u0435\u043C\u0430"), " \u043D\u0430 \u043A\u0430\u0436\u0434\u044B\u0439 \u0434\u0435\u043D\u044C"), /*#__PURE__*/React.createElement("p", {
    className: "sec-lead"
  }, "\u041A\u0443\u0440\u0441 \u041E\u0414\u0438\u041D \u041C \u2014 \u0435\u0434\u0438\u043D\u0441\u0442\u0432\u0435\u043D\u043D\u0430\u044F \u043A\u043E\u043C\u043F\u043B\u0435\u043A\u0441\u043D\u0430\u044F \u043C\u0435\u0442\u043E\u0434\u0438\u043A\u0430 \u043F\u0440\u0435\u043F\u043E\u0434\u0430\u0432\u0430\u043D\u0438\u044F \u043A\u0438\u0442\u0430\u0439\u0441\u043A\u043E\u0433\u043E \u0432 \u0420\u043E\u0441\u0441\u0438\u0438. \u041A\u0430\u0436\u0434\u044B\u0439 \u044D\u043B\u0435\u043C\u0435\u043D\u0442 \u0440\u0430\u0431\u043E\u0442\u0430\u0435\u0442 \u043D\u0430 \u0443\u0447\u0435\u043D\u0438\u043A\u0430 \u0438 \u043A\u0430\u0436\u0434\u044B\u0439 \u044D\u043B\u0435\u043C\u0435\u043D\u0442 \u043F\u0440\u043E\u0432\u0435\u0440\u044F\u0435\u043C."), /*#__PURE__*/React.createElement("div", {
    className: "method-grid"
  }, METHOD.map(x => /*#__PURE__*/React.createElement("div", {
    className: "method",
    key: x.n
  }, /*#__PURE__*/React.createElement("div", {
    className: "num"
  }, x.n), /*#__PURE__*/React.createElement("h3", null, x.t), /*#__PURE__*/React.createElement("p", null, x.d), /*#__PURE__*/React.createElement("div", {
    className: "meta"
  }, x.m)))));
}
function Stats() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "stats"
  }, /*#__PURE__*/React.createElement("div", {
    className: "stat"
  }, /*#__PURE__*/React.createElement("div", {
    className: "big"
  }, "100%"), /*#__PURE__*/React.createElement("div", {
    className: "lab"
  }, "\u0443\u0447\u0435\u043D\u0438\u043A\u043E\u0432 \u0441\u0434\u0430\u044E\u0442", /*#__PURE__*/React.createElement("br", null), "HSK \u0441 \u043F\u0435\u0440\u0432\u043E\u0433\u043E \u0440\u0430\u0437\u0430")), /*#__PURE__*/React.createElement("div", {
    className: "stat"
  }, /*#__PURE__*/React.createElement("div", {
    className: "big"
  }, "80%"), /*#__PURE__*/React.createElement("div", {
    className: "lab"
  }, "\u043F\u0440\u0438\u0445\u043E\u0434\u044F\u0442 \u043A \u043D\u0430\u043C", /*#__PURE__*/React.createElement("br", null), "\u043F\u043E \u0440\u0435\u043A\u043E\u043C\u0435\u043D\u0434\u0430\u0446\u0438\u044F\u043C")), /*#__PURE__*/React.createElement("div", {
    className: "stat"
  }, /*#__PURE__*/React.createElement("div", {
    className: "big"
  }, "20"), /*#__PURE__*/React.createElement("div", {
    className: "lab"
  }, "\u043B\u0435\u0442 \u0440\u0430\u0437\u0432\u0438\u0432\u0430\u0435\u043C", /*#__PURE__*/React.createElement("br", null), "\u043C\u0435\u0442\u043E\u0434\u0438\u043A\u0443 \u043F\u0440\u0435\u043F\u043E\u0434\u0430\u0432\u0430\u043D\u0438\u044F"))));
}
const FORMATS = [{
  t: 'Индивидуально',
  tag: 'Под ваш график и темп',
  why: 'Когда нужен фокус на личных целях — экзамене, поступлении, бизнес-задаче.',
  li: ['Подбор преподавателя под цель', 'Любой темп: 1–3+ занятий в неделю', 'Программа под ваши задачи'],
  price: 'от 2 100 ₽',
  per: 'за урок',
  cta: 'Узнать стоимость →'
}, {
  t: 'В паре',
  tag: 'Учиться вдвоём дешевле',
  why: 'С другом, супругом или коллегой — общий ритм, взаимная мотивация.',
  li: ['Дешевле индивидуальных', 'Общий план и расписание', 'Подбор пары к вашему уровню'],
  price: '2 200 ₽',
  per: 'за урок · с человека',
  cta: 'Записаться →'
}, {
  t: 'В мини-группе',
  tag: '3–4 человека, баланс цены и качества',
  why: 'Когда важна разговорная практика с учениками одного уровня.',
  li: ['Группы по уровням и целям', 'Фиксированное расписание', 'Не более 4 человек'],
  price: '1 800 ₽',
  per: 'за урок · с человека',
  cta: 'Записаться →'
}, {
  t: 'Гибридный формат',
  tag: 'Платформа + живые занятия',
  why: 'Для самостоятельных — экономия времени и денег без потери качества.',
  li: ['Полный курс на платформе', 'Куратор проверяет ДЗ', '2 живых урока за 3 месяца'],
  price: 'от 12 000 ₽',
  per: 'за 3 месяца',
  cta: 'Записаться →'
}];
function Formats() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "eyebrow"
  }, "\u0424\u043E\u0440\u043C\u0430\u0442\u044B"), /*#__PURE__*/React.createElement("h2", {
    className: "sec-title"
  }, "\u041F\u043E\u0434\u0431\u0435\u0440\u0451\u043C \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0443 \u043F\u043E\u0434 \u0432\u0430\u0448 ", /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "\u0440\u0438\u0442\u043C")), /*#__PURE__*/React.createElement("p", {
    className: "sec-lead"
  }, "\u0427\u0435\u0442\u044B\u0440\u0435 \u0444\u043E\u0440\u043C\u0430\u0442\u0430 \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u044F. \u0412\u044B\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u043E\u0442, \u043A\u043E\u0442\u043E\u0440\u044B\u0439 \u0441\u043E\u043E\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u0432\u0430\u0448\u0438\u043C \u0446\u0435\u043B\u044F\u043C \u0438 \u0433\u0440\u0430\u0444\u0438\u043A\u0443."), /*#__PURE__*/React.createElement("div", {
    className: "formats"
  }, FORMATS.map(f => /*#__PURE__*/React.createElement("div", {
    className: "fmt",
    key: f.t
  }, /*#__PURE__*/React.createElement("h3", null, f.t), /*#__PURE__*/React.createElement("div", {
    className: "tagline"
  }, f.tag), /*#__PURE__*/React.createElement("div", {
    className: "why"
  }, f.why), /*#__PURE__*/React.createElement("ul", null, f.li.map((l, i) => /*#__PURE__*/React.createElement("li", {
    key: i
  }, l))), /*#__PURE__*/React.createElement("div", {
    className: "price"
  }, f.price), /*#__PURE__*/React.createElement("div", {
    className: "per"
  }, f.per), /*#__PURE__*/React.createElement("a", {
    className: "btn btn-primary",
    href: "#"
  }, f.cta)))));
}
const CMP = [['Методика', 'Курс Т.В. Иоффе с 30-летней практикой — единый стандарт для всех преподавателей', 'Стандартный учебник + личные эксперименты преподавателя'], ['Контроль', 'Система видит отставание и сразу подключает методиста', 'Контроль раз в семестр на родительском собрании'], ['Разбор урока', 'Анализ по 11 критериям, преподавателю дают точки роста', 'Завуч заходит на 1 урок в год'], ['Темп прогресса', 'HSK3 за 8–12 месяцев', 'Часто 2–3 года — а нет даже уверенного HSK2'], ['Гарантия', 'Лицензия, договор, гарантия результата, вычет 13%', 'Услуги без юридических гарантий']];
function Comparison() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "eyebrow"
  }, "\u0427\u0442\u043E \u043E\u0442\u043B\u0438\u0447\u0430\u0435\u0442 \u043D\u0430\u0441"), /*#__PURE__*/React.createElement("h2", {
    className: "sec-title"
  }, "\u0427\u0442\u043E \u043E\u0442\u043B\u0438\u0447\u0430\u0435\u0442 ", /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "Kitai School")), /*#__PURE__*/React.createElement("p", {
    className: "sec-lead"
  }, "\u041D\u0435 \u043F\u0440\u043E\u0441\u0442\u043E \u0443\u0440\u043E\u043A\u0438 \u043A\u0438\u0442\u0430\u0439\u0441\u043A\u043E\u0433\u043E. \u0410 \u0441\u0438\u0441\u0442\u0435\u043C\u0430 \u043A\u043E\u043D\u0442\u0440\u043E\u043B\u044F, \u043C\u0435\u0442\u043E\u0434\u0438\u043A\u0430 \u0441 30-\u043B\u0435\u0442\u043D\u0435\u0439 \u043F\u0440\u0430\u043A\u0442\u0438\u043A\u043E\u0439 \u0438 \u043F\u043B\u0430\u0442\u0444\u043E\u0440\u043C\u0430, \u043A\u043E\u0442\u043E\u0440\u043E\u0439 \u043D\u0435\u0442 \u043D\u0438 \u0443 \u0440\u0435\u043F\u0435\u0442\u0438\u0442\u043E\u0440\u043E\u0432, \u043D\u0438 \u0443 \u043E\u0431\u044B\u0447\u043D\u044B\u0445 \u0448\u043A\u043E\u043B."), /*#__PURE__*/React.createElement("div", {
    className: "cmp"
  }, /*#__PURE__*/React.createElement("div", {
    className: "cmp-col us"
  }, /*#__PURE__*/React.createElement("div", {
    className: "cmp-head us"
  }, "Kitai School", /*#__PURE__*/React.createElement("small", null, "EST \xB7 2005")), CMP.map((r, i) => /*#__PURE__*/React.createElement("div", {
    className: "cmp-row",
    key: i
  }, /*#__PURE__*/React.createElement("span", {
    className: "k"
  }, r[0]), r[1]))), /*#__PURE__*/React.createElement("div", {
    className: "cmp-col them"
  }, /*#__PURE__*/React.createElement("div", {
    className: "cmp-head them"
  }, "\u041E\u0431\u044B\u0447\u043D\u043E\u0435 \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435", /*#__PURE__*/React.createElement("small", null, "\u0440\u0435\u043F\u0435\u0442\u0438\u0442\u043E\u0440 \u0438\u043B\u0438 \u0441\u0440\u0435\u0434\u043D\u044F\u044F \u0448\u043A\u043E\u043B\u0430")), CMP.map((r, i) => /*#__PURE__*/React.createElement("div", {
    className: "cmp-row",
    key: i
  }, /*#__PURE__*/React.createElement("span", {
    className: "k"
  }, r[0]), r[2])))));
}
const TEAM = [{
  img: 'team-yulia.webp',
  role: 'Основатель школы',
  name: 'Юлия Горяина',
  who: 'Преподаватель МГУ, китаист с 20-летним стажем',
  p: 'Создала Kitai School в 2005 году. Отбирает лучшие методики и лично контролирует стандарты качества.'
}, {
  img: 'team-tatyana.webp',
  role: 'Главный методист',
  name: 'Татьяна Иоффе',
  who: 'Преподаватель ОмГУ, китаист с 30-летним стажем',
  p: 'Автор курса ОДиН М — единственной комплексной методики преподавания китайского в России.'
}, {
  img: 'team-jenny.webp',
  role: 'Операционный директор',
  name: 'Женни Рэй',
  who: 'Технологии и качество процессов',
  p: 'Отвечает за то, чтобы платформа, расписания, оплаты и связь работали безупречно.'
}];
function Team() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "eyebrow"
  }, "\u041D\u0430\u0448\u0430 \u043A\u043E\u043C\u0430\u043D\u0434\u0430"), /*#__PURE__*/React.createElement("h2", {
    className: "sec-title"
  }, /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "\u041A\u0442\u043E"), " \u0441\u0442\u043E\u0438\u0442 \u0437\u0430 Kitai School"), /*#__PURE__*/React.createElement("p", {
    className: "sec-lead"
  }, "\u041F\u0440\u0435\u043F\u043E\u0434\u0430\u0432\u0430\u0442\u0435\u043B\u0438 \u0441 \u043F\u0435\u0434\u0430\u0433\u043E\u0433\u0438\u0447\u0435\u0441\u043A\u0438\u043C \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435\u043C, \u043C\u0435\u0442\u043E\u0434\u0438\u0441\u0442\u044B \u0441 \u043C\u043D\u043E\u0433\u043E\u043B\u0435\u0442\u043D\u0438\u043C \u043E\u043F\u044B\u0442\u043E\u043C, \u043E\u043F\u0435\u0440\u0430\u0446\u0438\u043E\u043D\u043D\u0430\u044F \u043A\u043E\u043C\u0430\u043D\u0434\u0430."), /*#__PURE__*/React.createElement("div", {
    className: "team"
  }, TEAM.map(m => /*#__PURE__*/React.createElement("div", {
    className: "member",
    key: m.name
  }, /*#__PURE__*/React.createElement("img", {
    src: '../../assets/' + m.img,
    alt: m.name
  }), /*#__PURE__*/React.createElement("div", {
    className: "role"
  }, m.role), /*#__PURE__*/React.createElement("h3", null, m.name), /*#__PURE__*/React.createElement("div", {
    className: "who"
  }, m.who), /*#__PURE__*/React.createElement("p", null, m.p)))));
}
function Quote() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "quote"
  }, /*#__PURE__*/React.createElement("blockquote", null, "\u041C\u044B \u0443\u0447\u0438\u043C \u0431\u044B\u0441\u0442\u0440\u043E \u0438 ", /*#__PURE__*/React.createElement("span", {
    className: "italic"
  }, "\u044D\u0444\u0444\u0435\u043A\u0442\u0438\u0432\u043D\u043E"), ", \u043F\u043E\u0442\u043E\u043C\u0443 \u0447\u0442\u043E \u0441\u043B\u0435\u0434\u0443\u0435\u043C \u0441\u0438\u043B\u044C\u043D\u043E\u0439 \u043F\u0440\u043E\u0432\u0435\u0440\u0435\u043D\u043D\u043E\u0439 \u043C\u0435\u0442\u043E\u0434\u0438\u043A\u0435."), /*#__PURE__*/React.createElement("div", {
    className: "who"
  }, "\u0422\u0430\u0442\u044C\u044F\u043D\u0430 \u0418\u043E\u0444\u0444\u0435 \xB7 \u0433\u043B\u0430\u0432\u043D\u044B\u0439 \u043C\u0435\u0442\u043E\u0434\u0438\u0441\u0442 \xB7 \u0430\u0432\u0442\u043E\u0440 \u043A\u0443\u0440\u0441\u0430 \xB7 30 \u043B\u0435\u0442 \u0432 \u043F\u0440\u043E\u0444\u0435\u0441\u0441\u0438\u0438")));
}
function FinalCTA() {
  return /*#__PURE__*/React.createElement("div", {
    className: "ks-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "final"
  }, /*#__PURE__*/React.createElement("div", {
    className: "han"
  }, "\u542F"), /*#__PURE__*/React.createElement("h2", null, "\u0413\u043E\u0442\u043E\u0432\u044B \u043D\u0430\u0447\u0430\u0442\u044C?"), /*#__PURE__*/React.createElement("p", null, "\u0417\u0430\u043F\u0438\u0448\u0438\u0442\u0435\u0441\u044C \u043D\u0430 \u0431\u0435\u0441\u043F\u043B\u0430\u0442\u043D\u044B\u0439 \u043F\u0440\u043E\u0431\u043D\u044B\u0439 \u0443\u0440\u043E\u043A \u2014 \u0437\u0430 30 \u043C\u0438\u043D\u0443\u0442 \u043F\u0440\u043E\u0439\u0434\u0451\u043C \u0434\u0438\u0430\u0433\u043D\u043E\u0441\u0442\u0438\u043A\u0443 \u0442\u0435\u043A\u0443\u0449\u0435\u0433\u043E \u0443\u0440\u043E\u0432\u043D\u044F \u0438 \u043F\u043E\u0434\u0431\u0435\u0440\u0451\u043C \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0443 \u043F\u043E\u0434 \u0432\u0430\u0448\u0438 \u0446\u0435\u043B\u0438."), /*#__PURE__*/React.createElement("div", {
    className: "cta-row"
  }, /*#__PURE__*/React.createElement("a", {
    className: "btn btn-primary",
    href: "#"
  }, "\u0417\u0430\u043F\u0438\u0441\u0430\u0442\u044C\u0441\u044F \u043D\u0430 \u0434\u0438\u0430\u0433\u043D\u043E\u0441\u0442\u0438\u0447\u0435\u0441\u043A\u0438\u0439 \u0443\u0440\u043E\u043A \u2192"), /*#__PURE__*/React.createElement("a", {
    className: "btn btn-ghost",
    href: "#"
  }, "\u0438\u043B\u0438 \u0443\u0437\u043D\u0430\u0442\u044C \u0441\u0442\u043E\u0438\u043C\u043E\u0441\u0442\u044C")), /*#__PURE__*/React.createElement("div", {
    className: "note"
  }, "\u0411\u0435\u0437 \u043E\u0431\u044F\u0437\u0430\u0442\u0435\u043B\u044C\u0441\u0442\u0432. \u0420\u0435\u0448\u0435\u043D\u0438\u0435 \u043E \u043F\u0440\u043E\u0434\u043E\u043B\u0436\u0435\u043D\u0438\u0438 \u2014 \u043F\u043E\u0441\u043B\u0435 \u0443\u0440\u043E\u043A\u0430.")));
}
Object.assign(window, {
  Hero,
  Methodology,
  Stats,
  Formats,
  Comparison,
  Team,
  Quote,
  FinalCTA
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/Sections.jsx", error: String((e && e.message) || e) }); }

})();
