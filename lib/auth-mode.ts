// Fixed at build time: an independent deployment must never trust Sites headers.
declare const __MOSSY_STANDALONE__: boolean;
export const standaloneAuth = typeof __MOSSY_STANDALONE__ !== 'undefined' && __MOSSY_STANDALONE__;
