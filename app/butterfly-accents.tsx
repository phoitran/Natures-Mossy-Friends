type Placement = 'hero' | 'featured' | 'signup' | 'explore' | 'projects';

export default function ButterflyAccents({ placement }: { placement: Placement }) {
  return <div className={`butterfly-accents butterflies-${placement}`} aria-hidden="true">
    {Array.from({ length: placement === 'hero' || placement === 'projects' ? 2 : 1 }, (_, index) => <span className={`butterfly butterfly-${index + 1}`} key={index}>
      <svg viewBox="0 0 64 56" fill="none" focusable="false">
        <g className="butterfly-wing left-wing" fill="currentColor">
          <path d="M31 28C24 7 8 2 5 13C2 24 17 32 31 30Z" />
          <path d="M31 30C15 26 7 35 13 44C19 53 28 41 31 30Z" opacity=".78" />
        </g>
        <g className="butterfly-wing right-wing" fill="currentColor">
          <path d="M33 28C40 7 56 2 59 13C62 24 47 32 33 30Z" />
          <path d="M33 30C49 26 57 35 51 44C45 53 36 41 33 30Z" opacity=".78" />
        </g>
        <path d="M32 23V39M32 23C31 17 28 15 26 15M32 23C33 17 36 15 38 15" stroke="#688a6c" strokeWidth="2" strokeLinecap="round" />
      </svg>
    </span>)}
  </div>;
}
