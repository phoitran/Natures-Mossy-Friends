type Choice = {id:string;season:string;ages:string[];archived?:boolean};
export function surpriseChoices<T extends Choice>(items:T[], season:string, age:string):T[] {
 return items.filter(a => !a.archived && (season === 'all' || a.season === season) && (age === 'all' || a.ages.includes(age)));
}
export function chooseSurprise<T extends Choice>(items:T[], previousId:string, random = Math.random):T|undefined {
 const pool = items.length > 1 ? items.filter(a => a.id !== previousId) : items;
 return pool.length ? pool[Math.min(pool.length - 1, Math.floor(random() * pool.length))] : undefined;
}
