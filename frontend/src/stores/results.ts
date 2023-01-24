import type { Filter, Laptop, SearchBoxes, SearchRanges, SearchWords } from 'src/types/types';
import { writable } from 'svelte/store';

export const laptops = writable<Laptop[]>([]);
export const fields = writable<Filter>({ checkboxes: {}, ranges: {} } as Filter);

export const searchCheckboxes = writable<SearchBoxes>({});
export const searchRanges = writable<SearchRanges>({});
export const searchWords = writable<SearchWords>('');

