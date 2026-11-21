import { getCollection } from 'astro:content';

const visible = (entry: { data: { draft: boolean } }) => import.meta.env.DEV || !entry.data.draft;

export async function getProjects() {
  const projects = await getCollection('projects', visible);
  return projects.sort((a, b) => a.data.order - b.data.order);
}

// Prefix a path with the site's base (/My-Website).
export function url(path = '') {
  return import.meta.env.BASE_URL.replace(/\/$/, '') + '/' + path.replace(/^\//, '');
}
