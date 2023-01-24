import type { Laptop, SearchBoxes, SearchRanges, SearchWords } from '../types/types';

export async function getLaptops(
	checkboxes: SearchBoxes,
	ranges: SearchRanges,
	words: SearchWords
): Promise<Laptop[]> {
	const res = await fetch('http://localhost:8000/laptops', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ checkboxes, ranges, words })
	});
	if (!res.ok) {
		return [];
	}
	return res.json() as Promise<Laptop[]>;
}
