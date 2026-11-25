export default function SeasonFriend({season='spring',className=''}:{season?:string;className?:string}) {
 const index = Math.max(0,['spring','summer','fall','winter'].indexOf(season));
 return <span aria-hidden="true" className={'season-friend '+className} style={{backgroundPosition:`${index%2?100:0}% ${index<2?0:100}%`}}/>;
}
