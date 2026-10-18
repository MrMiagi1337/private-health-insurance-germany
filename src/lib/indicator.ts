// Sliding selection indicator for segmented controls and tab pills (Apple pass, 2026-10-17).
//
// Instead of each tab painting its own "active" background (a hard cut when the selection
// moves), one indicator element glides from the old tab to the new one. The move is a CSS
// transition on transform/width with the --spring-bounce curve, so it starts from wherever
// the indicator currently is (interruptible: click three tabs quickly and it re-targets
// without jumping) and carries a little momentum into the new position.
//
// Usage: attachIndicator(listEl, () => activeTabEl). The list gets class .has-ind, an
// .ind child, and the custom props --ind-x / --ind-w / --ind-h. Styling of the pill itself
// (colour, inset, radius) lives in the component's CSS via --ind-inset / --ind-radius.
// If JS never runs, components keep their static active styles (guarded by :not(.has-ind)).

export function attachIndicator(list: HTMLElement, active: () => HTMLElement | null | undefined, className = 'ind') {
  if (list.querySelector(`:scope > .${className}`)) return () => {};
  const ind = document.createElement('span');
  ind.className = className;
  ind.setAttribute('aria-hidden', 'true');
  list.classList.add('has-ind');
  list.prepend(ind);

  let ready = false;
  const place = () => {
    const a = active();
    if (!a) return;
    // Measure relative to the list's padding box so horizontal scrolling of the list keeps them aligned.
    const x = a.offsetLeft - list.clientLeft;
    list.style.setProperty('--ind-x', `${x}px`);
    list.style.setProperty('--ind-w', `${a.offsetWidth}px`);
    list.style.setProperty('--ind-h', `${a.offsetHeight}px`);
    if (!ready) {
      // First paint: jump into place without animating, then enable transitions.
      ind.style.transition = 'none';
      void ind.offsetWidth;
      ind.style.transition = '';
      list.style.setProperty('--ind-ready', '1');
      ready = true;
    }
  };

  place();
  const ro = new ResizeObserver(place);
  ro.observe(list);
  Array.from(list.children).forEach((c) => c !== ind && ro.observe(c));
  document.fonts?.ready.then(place);
  return place;
}
