import { getCollection } from 'astro:content';

const visible = (entry: { data: { draft: boolean } }) => import.meta.env.DEV || !entry.data.draft;

export async function getPosts() {
  const posts = await getCollection('blog', visible);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

export async function getProjects() {
  const projects = await getCollection('projects', visible);
  return projects.sort((a, b) => a.data.order - b.data.order);
}

// Film-camera date stamp groups, e.g. ['26', '10', '01'] (year, month, zero-padded day).
export function stampParts(date: Date) {
  const yy = String(date.getUTCFullYear()).slice(-2);
  const dd = String(date.getUTCDate()).padStart(2, '0');
  return [yy, String(date.getUTCMonth() + 1), dd];
}

export function longDate(date: Date) {
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
}

// Prefix a path with the site's base (/My-Website).
export function url(path = '') {
  return import.meta.env.BASE_URL.replace(/\/$/, '') + '/' + path.replace(/^\//, '');
}
