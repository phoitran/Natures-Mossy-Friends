export function activityImageUrl(id: string) {
  const revision = id === 'WIN-08' ? 'pebble-ears-1' : id === 'FAL-06' ? 'pebble-eyes-1' : ['WIN-06','WIN-07'].includes(id) ? 'winter-variety-2' : '';
  return `/assets/activities/${id}.webp${revision ? '?v='+revision : ''}`;
}
