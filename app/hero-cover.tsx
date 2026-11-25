'use client';
import { useEffect, useState } from 'react';
import { Pause, Play } from 'lucide-react';
import catalogue from '../content/activities.json';
import { activityImageUrl } from '../lib/activity-image';

const active = (Array.isArray(catalogue) ? catalogue : (catalogue as any).activities).filter((activity:any) => !activity.archived);
const slides = [...active.filter((activity:any) => activity.id === 'WIN-07'), ...active.filter((activity:any) => activity.id !== 'WIN-07')];
export default function HeroCover() {
  const [current, setCurrent] = useState(0);
  const [paused, setPaused] = useState(false);
  const [reduced, setReduced] = useState(true);
  useEffect(() => {
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    const update = () => setReduced(preference.matches);
    update(); preference.addEventListener('change', update);
    return () => preference.removeEventListener('change', update);
  }, []);
  useEffect(() => {
    if (paused || reduced) return;
    const timer = window.setInterval(() => { if (!document.hidden) setCurrent(index => (index + 1) % slides.length); }, 4000);
    return () => window.clearInterval(timer);
  }, [paused, reduced]);
  return <div className="hero-cover" role="group" aria-label="Seasonal activity inspiration">
    <div className="hero-photo">
      {slides.map((slide:any, index:number) => <div key={slide.id} className={`hero-slide${index === current ? ' active' : ''}`} aria-hidden={index !== current}>
        <div className="photo-art">{[current,(current+1)%slides.length,(current+slides.length-1)%slides.length].includes(index)&&<img src={activityImageUrl(slide.id)} alt={`Generated inspiration: ${slide.title}`} loading="eager" fetchPriority={index === 0 ? 'high' : 'low'} decoding="async" style={{ left: 0, width: `${slide.examples.length*100}%` }} />}</div>
      </div>)}
    </div>
    {!reduced && <button className="hero-pause" onClick={() => setPaused(value => !value)} aria-label={paused ? 'Play cover slideshow' : 'Pause cover slideshow'}>{paused ? <Play size={15} /> : <Pause size={15} />}<span>{paused ? 'Play' : 'Pause'}</span></button>}
  </div>;
}
