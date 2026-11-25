import MossyApp from '../mossy-app';
export default async function Page({ params }: { params: Promise<{path?:string[]}> }) {
  const p = await params;
  return <MossyApp initialPath={'/' + (p.path || []).join('/')} />;
}
